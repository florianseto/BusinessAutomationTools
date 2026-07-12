"""
CSVファイルの読み込み処理を提供するモジュール
Author:
    Florian Seto
"""

import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)

SUPPORTED_ENCODINGS = ("utf-8", "cp932")

def read_csv(file_path: str, column_types: dict | None = None) -> pd.DataFrame:
    """
    指定されたCSVファイル読み込み
    (UTF-8系で読み込めない場合、Windowsで一般的に使用される。Shift-JIS系の文字コードで再試行する。)
    
    Args:
        file_path (str): 読み込み対象のCSVファイルパス。
        column_types (dict | None): 列のデータ型を指定する辞書。
    Returns:
        CSVデータを格納したDataFrame。
    """

    # CSVファイルの事前チェック
    _validate_csv_file(file_path)
                       
    logger.info(f"CSV読み込み開始: file={file_path}")

    # CSVファイルを読み込む
    for encoding in SUPPORTED_ENCODINGS:
        try:
            dataframe = pd.read_csv(file_path, encoding=encoding, dtype=column_types)

            logger.info(f"CSV読込完了: file={file_path}, "
                f"encoding={encoding}, "
                f"rows={len(dataframe)}, "
                f"columns={len(dataframe.columns)}"
            )

            return dataframe

        except UnicodeDecodeError:
            # 文字コードが一致しない場合、次の文字コードで再試行する
            logger.debug(f"文字コードが一致しないため再試行します： file={file_path}, encoding={encoding}")
        
        except pd.errors.EmptyDataError:
            # CSVファイルが空の場合
            logger.exception(f"CSVファイルが空です: file={file_path}")
            raise

        except pd.errors.ParserError:
            logger.exception(f"CSVファイルの構造が不正です: file={file_path}")
            raise

    message = f"CSVファイルの読み込みに失敗しました: file={file_path}, 対応文字コード={SUPPORTED_ENCODINGS}"
    logger.error(message)
    # 指定されたファイルがCSV形式でない場合、または対応文字コードで読み込めなかった場合
    raise ValueError(message)




def _validate_csv_file(file_path: str) -> None:
    """
    CSVファイルの事前検証を行います。

    Args:
        file_path (str): 検証対象のCSVファイルパス。
    Returns:
        None
    """

    path = Path(file_path)
    # ファイルパスが存在しない場合
    if not path.exists():
        raise FileNotFoundError(f"指定されたファイルが存在しません: {file_path}")
    # ファイルパスがディレクトリの場合
    if not path.is_file():
        raise ValueError(f"指定されたパスはファイルではありません: {file_path}")
    # ファイルパスがCSV形式でない場合
    if path.suffix.lower() != ".csv":
        raise ValueError(f"指定されたファイルはCSV形式ではありません: {file_path}")

