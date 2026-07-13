"""main.py の単体テスト（T046～T057）。"""

from datetime import datetime
from pathlib import Path
from unittest.mock import Mock, call

import pandas as pd
import pytest

import main as main_module


class FixedDatetime:
    @classmethod
    def now(cls):
        return datetime(2026, 1, 2, 3, 4, 5)


@pytest.fixture
def workflow(monkeypatch, tmp_path):
    source = pd.DataFrame(
        {"社員番号": ["001"], "氏名": ["山田"], "部署": ["営業"], "勤務時間": [8], "不要列": ["x"]}
    )
    removed = source.drop(columns=["不要列"])
    renamed = removed.rename(columns={"社員番号": "従業員番号", "勤務時間": "勤務時間数"})
    reordered = renamed[["従業員番号", "氏名", "部署", "勤務時間数"]]
    mocks = {
        "setup_logging": Mock(return_value=tmp_path / "test.log"),
        "read_csv": Mock(return_value=source),
        "remove_columns": Mock(return_value=removed),
        "rename_columns": Mock(return_value=renamed),
        "reorder_columns": Mock(return_value=reordered),
        "write_excel": Mock(),
    }
    for name, mock in mocks.items():
        monkeypatch.setattr(main_module, name, mock)
    return mocks, (source, removed, renamed, reordered)


def test_t046_complete_workflow_in_order(workflow):
    mocks, _ = workflow
    manager = Mock()
    for name, mock in mocks.items():
        manager.attach_mock(mock, name)

    main_module.main()

    called_names = [item[0] for item in manager.mock_calls]
    assert called_names == [
        "setup_logging", "read_csv", "remove_columns", "rename_columns", "reorder_columns", "write_excel"
    ]
    assert all(mock.call_count == 1 for mock in mocks.values())


def test_t047_input_path_is_based_on_project_directory(workflow):
    mocks, _ = workflow
    main_module.main()
    project_dir = Path(main_module.__file__).resolve().parent.parent
    assert mocks["read_csv"].call_args.args[0] == str(project_dir / "sample" / "input" / "sample.csv")


def test_t048_employee_number_dtype_is_string(workflow):
    mocks, _ = workflow
    main_module.main()
    assert mocks["read_csv"].call_args.args[1] == {"社員番号": str}


def test_t049_formatting_arguments_and_dataframe_handoff(workflow):
    mocks, frames = workflow
    source, removed, renamed, reordered = frames
    main_module.main()
    mocks["remove_columns"].assert_called_once_with(source, ["不要列"])
    mocks["rename_columns"].assert_called_once_with(
        removed, {"社員番号": "従業員番号", "勤務時間": "勤務時間数"}
    )
    mocks["reorder_columns"].assert_called_once_with(
        renamed, ["従業員番号", "氏名", "部署", "勤務時間数"]
    )
    assert mocks["write_excel"].call_args.args[0] is reordered


def test_t050_timestamped_output_path(workflow, monkeypatch):
    mocks, _ = workflow
    monkeypatch.setattr(main_module, "datetime", FixedDatetime)
    main_module.main()
    project_dir = Path(main_module.__file__).resolve().parent.parent
    assert mocks["write_excel"].call_args.args[1] == project_dir / "output" / "formatted_data_20260102_030405.xlsx"


def test_t051_write_excel_uses_default_sheet_name(workflow):
    mocks, frames = workflow
    main_module.main()
    mocks["write_excel"].assert_called_once()
    assert mocks["write_excel"].call_args == call(frames[3], mocks["write_excel"].call_args.args[1])
    assert mocks["write_excel"].call_args.kwargs == {}


@pytest.mark.parametrize(
    ("test_id", "failed_step", "error", "not_called"),
    [
        ("T052", "read_csv", FileNotFoundError("missing"),
         ["remove_columns", "rename_columns", "reorder_columns", "write_excel"]),
        ("T053", "remove_columns", ValueError("remove"),
         ["rename_columns", "reorder_columns", "write_excel"]),
        ("T054", "rename_columns", ValueError("rename"), ["reorder_columns", "write_excel"]),
        ("T055", "reorder_columns", ValueError("reorder"), ["write_excel"]),
        ("T056", "write_excel", OSError("write"), []),
    ],
)
def test_t052_to_t056_workflow_failure_stops_following_steps(
    workflow, monkeypatch, test_id, failed_step, error, not_called
):
    mocks, _ = workflow
    logger_exception = Mock()
    monkeypatch.setattr(main_module.logger, "exception", logger_exception)
    mocks[failed_step].side_effect = error

    with pytest.raises(type(error)) as exc_info:
        main_module.main()

    assert exc_info.value is error, test_id
    for name in not_called:
        mocks[name].assert_not_called()
    logger_exception.assert_called_once_with("CSV Business Formatterのメイン処理に失敗しました。")


def test_t057_logging_setup_failure_stops_workflow(workflow, monkeypatch):
    mocks, _ = workflow
    error = OSError("logging")
    mocks["setup_logging"].side_effect = error
    logger_exception = Mock()
    monkeypatch.setattr(main_module.logger, "exception", logger_exception)

    with pytest.raises(OSError) as exc_info:
        main_module.main()

    assert exc_info.value is error
    mocks["read_csv"].assert_not_called()
    mocks["remove_columns"].assert_not_called()
    mocks["rename_columns"].assert_not_called()
    mocks["reorder_columns"].assert_not_called()
    mocks["write_excel"].assert_not_called()
    logger_exception.assert_not_called()

