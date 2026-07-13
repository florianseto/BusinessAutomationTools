"""data_formatter.py の単体テスト（T014～T029）。"""

import pandas as pd
import pytest

from data_formatter import remove_columns, rename_columns, reorder_columns


def frame_abc():
    return pd.DataFrame({"A": [1, 2], "B": [3, 4], "C": [5, 6]})


def test_t014_remove_one_column():
    actual = remove_columns(frame_abc(), ["B"])
    pd.testing.assert_frame_equal(actual, pd.DataFrame({"A": [1, 2], "C": [5, 6]}))


def test_t015_remove_multiple_columns():
    actual = remove_columns(frame_abc(), ["A", "C"])
    pd.testing.assert_frame_equal(actual, pd.DataFrame({"B": [3, 4]}))


def test_t016_remove_no_columns():
    source = frame_abc()[["A", "B"]]
    pd.testing.assert_frame_equal(remove_columns(source, []), source)


def test_t017_remove_does_not_mutate_source():
    source = frame_abc()[["A", "B"]]
    original = source.copy(deep=True)
    result = remove_columns(source, ["B"])
    assert result.columns.tolist() == ["A"]
    pd.testing.assert_frame_equal(source, original)


def test_t018_remove_missing_column():
    with pytest.raises(ValueError, match="X"):
        remove_columns(frame_abc()[["A", "B"]], ["X"])


def test_t019_remove_partly_missing_column_does_not_mutate_source():
    source = frame_abc()[["A", "B"]]
    original = source.copy(deep=True)
    with pytest.raises(ValueError, match="X"):
        remove_columns(source, ["A", "X"])
    pd.testing.assert_frame_equal(source, original)


def test_t020_rename_one_column():
    actual = rename_columns(frame_abc()[["A", "B"]], {"A": "X"})
    pd.testing.assert_frame_equal(actual, pd.DataFrame({"X": [1, 2], "B": [3, 4]}))


def test_t021_rename_multiple_columns():
    actual = rename_columns(frame_abc(), {"A": "X", "C": "Z"})
    assert actual.columns.tolist() == ["X", "B", "Z"]
    assert actual.values.tolist() == [[1, 3, 5], [2, 4, 6]]


def test_t022_rename_no_columns():
    source = frame_abc()[["A", "B"]]
    pd.testing.assert_frame_equal(rename_columns(source, {}), source)


def test_t023_rename_does_not_mutate_source():
    source = frame_abc()[["A", "B"]]
    original = source.copy(deep=True)
    result = rename_columns(source, {"A": "X"})
    assert result.columns.tolist() == ["X", "B"]
    pd.testing.assert_frame_equal(source, original)


def test_t024_rename_missing_column():
    with pytest.raises(ValueError, match="X"):
        rename_columns(frame_abc()[["A", "B"]], {"X": "Y"})


def test_t025_reorder_columns():
    source = frame_abc()
    actual = reorder_columns(source, ["C", "A", "B"])
    pd.testing.assert_frame_equal(actual, source[["C", "A", "B"]])


def test_t026_select_and_reorder_columns():
    source = frame_abc()
    actual = reorder_columns(source, ["C", "A"])
    pd.testing.assert_frame_equal(actual, source[["C", "A"]])


def test_t027_empty_column_order():
    actual = reorder_columns(frame_abc()[["A", "B"]], [])
    assert actual.shape == (2, 0)


def test_t028_reorder_does_not_mutate_source():
    source = frame_abc()[["A", "B"]]
    original = source.copy(deep=True)
    result = reorder_columns(source, ["B", "A"])
    assert result.columns.tolist() == ["B", "A"]
    pd.testing.assert_frame_equal(source, original)


def test_t029_reorder_missing_column():
    with pytest.raises(ValueError, match="X"):
        reorder_columns(frame_abc()[["A", "B"]], ["A", "X"])

