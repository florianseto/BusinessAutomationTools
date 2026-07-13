"""logging_config.py の単体テスト（T039～T045）。"""

import logging
from datetime import datetime

import pytest

import logging_config


class FixedDatetime:
    @classmethod
    def now(cls):
        return datetime(2026, 1, 2, 3, 4, 5)


@pytest.fixture(autouse=True)
def restore_root_logging():
    root = logging.getLogger()
    old_handlers = root.handlers[:]
    old_level = root.level
    yield
    for handler in root.handlers[:]:
        if handler not in old_handlers:
            handler.close()
    root.handlers = old_handlers
    root.setLevel(old_level)


def test_t039_create_log_directory(tmp_path):
    logging_config.setup_logging(tmp_path)
    assert (tmp_path / "logs").is_dir()


def test_t040_timestamped_log_filename(tmp_path, monkeypatch):
    monkeypatch.setattr(logging_config, "datetime", FixedDatetime)
    actual = logging_config.setup_logging(tmp_path)
    assert actual == tmp_path / "logs" / "csv_business_formatter_20260102_030405.log"


def test_t041_write_utf8_log_message(tmp_path):
    log_file = logging_config.setup_logging(tmp_path)
    logging.getLogger("unit-test").info("日本語ログメッセージ")
    for handler in logging.getLogger().handlers:
        handler.flush()
    assert "日本語ログメッセージ" in log_file.read_text(encoding="utf-8")


def test_t042_root_log_level_is_info(tmp_path):
    logging_config.setup_logging(tmp_path)
    assert logging.getLogger().level == logging.INFO


def test_t043_existing_log_directory(tmp_path):
    (tmp_path / "logs").mkdir()
    actual = logging_config.setup_logging(tmp_path)
    assert actual.is_file()


def test_t044_logs_path_is_a_file(tmp_path):
    (tmp_path / "logs").write_text("file", encoding="utf-8")
    with pytest.raises(FileExistsError):
        logging_config.setup_logging(tmp_path)


def test_t045_file_handler_creation_failure(tmp_path, monkeypatch):
    def raise_os_error(*args, **kwargs):
        raise OSError("ログファイルを作成できません")

    monkeypatch.setattr(logging_config.logging, "FileHandler", raise_os_error)
    with pytest.raises(OSError, match="ログファイルを作成できません"):
        logging_config.setup_logging(tmp_path)

