"""csv_reader.py の単体テスト（T001～T013）。"""

from unittest.mock import Mock

import pandas as pd
import pytest

import csv_reader


def test_t001_read_utf8_csv(tmp_path):
    csv_file = tmp_path / "input.csv"
    csv_file.write_text("社員番号,氏名\n001,山田太郎\n002,佐藤花子\n", encoding="utf-8")

    actual = csv_reader.read_csv(str(csv_file), {"社員番号": str})

    expected = pd.DataFrame({"社員番号": ["001", "002"], "氏名": ["山田太郎", "佐藤花子"]})
    pd.testing.assert_frame_equal(actual, expected)


def test_t002_retry_with_cp932(tmp_path, caplog):
    csv_file = tmp_path / "input.csv"
    csv_file.write_bytes("社員番号,氏名\n001,髙橋太郎\n".encode("cp932"))
    caplog.set_level("DEBUG", logger=csv_reader.__name__)

    actual = csv_reader.read_csv(str(csv_file), {"社員番号": str})

    assert actual.loc[0, "氏名"] == "髙橋太郎"
    assert "文字コードが一致しないため再試行します" in caplog.text


def test_t003_preserve_leading_zero_with_dtype(tmp_path):
    csv_file = tmp_path / "input.csv"
    csv_file.write_text("社員番号\n001\n002\n", encoding="utf-8")

    actual = csv_reader.read_csv(str(csv_file), {"社員番号": str})

    assert actual["社員番号"].tolist() == ["001", "002"]
    assert actual["社員番号"].dtype == object


def test_t004_read_without_dtype(tmp_path):
    csv_file = tmp_path / "input.csv"
    csv_file.write_text("数量\n10\n20\n", encoding="utf-8")

    actual = csv_reader.read_csv(str(csv_file))

    assert actual["数量"].tolist() == [10, 20]
    assert pd.api.types.is_integer_dtype(actual["数量"])


def test_t005_header_only_csv(tmp_path):
    csv_file = tmp_path / "input.csv"
    csv_file.write_text("社員番号,氏名\n", encoding="utf-8")

    actual = csv_reader.read_csv(str(csv_file))

    assert actual.empty
    assert actual.columns.tolist() == ["社員番号", "氏名"]


def test_t006_uppercase_csv_extension(tmp_path):
    csv_file = tmp_path / "input.CSV"
    csv_file.write_text("A\n1\n", encoding="utf-8")

    actual = csv_reader.read_csv(str(csv_file))

    assert actual["A"].tolist() == [1]


def test_t007_nonexistent_file(tmp_path):
    csv_file = tmp_path / "not_found.csv"

    with pytest.raises(FileNotFoundError, match="指定されたファイルが存在しません") as exc_info:
        csv_reader.read_csv(str(csv_file))

    assert str(csv_file) in str(exc_info.value)


def test_t008_directory_path(tmp_path):
    with pytest.raises(ValueError, match="指定されたパスはファイルではありません") as exc_info:
        csv_reader.read_csv(str(tmp_path))

    assert str(tmp_path) in str(exc_info.value)


def test_t009_non_csv_extension(tmp_path):
    text_file = tmp_path / "input.txt"
    text_file.write_text("A\n1\n", encoding="utf-8")

    with pytest.raises(ValueError, match="指定されたファイルはCSV形式ではありません") as exc_info:
        csv_reader.read_csv(str(text_file))

    assert str(text_file) in str(exc_info.value)


def test_t010_empty_file(tmp_path):
    csv_file = tmp_path / "empty.csv"
    csv_file.touch()

    with pytest.raises(pd.errors.EmptyDataError):
        csv_reader.read_csv(str(csv_file))


def test_t011_malformed_csv(tmp_path):
    csv_file = tmp_path / "invalid.csv"
    csv_file.write_text('A,B\n1,"引用符が閉じていない\n', encoding="utf-8")

    with pytest.raises(pd.errors.ParserError):
        csv_reader.read_csv(str(csv_file))


def test_t012_unsupported_encoding(tmp_path, monkeypatch):
    csv_file = tmp_path / "unsupported.csv"
    csv_file.write_bytes(b"dummy")
    read_mock = Mock(side_effect=UnicodeDecodeError("codec", b"x", 0, 1, "invalid"))
    monkeypatch.setattr(csv_reader.pd, "read_csv", read_mock)

    with pytest.raises(ValueError, match="CSVファイルの読み込みに失敗しました") as exc_info:
        csv_reader.read_csv(str(csv_file))

    assert str(csv_file) in str(exc_info.value)
    assert str(csv_reader.SUPPORTED_ENCODINGS) in str(exc_info.value)
    assert read_mock.call_count == len(csv_reader.SUPPORTED_ENCODINGS)


def test_t013_dtype_conversion_error(tmp_path):
    csv_file = tmp_path / "input.csv"
    csv_file.write_text("数量\n数値以外\n", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_reader.read_csv(str(csv_file), {"数量": int})
