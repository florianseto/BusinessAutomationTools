"""
Excelファイルの出力処理を提供するモジュール
Author:
    Florian Seto
"""

import logging
from pathlib import Path

import pandas as pd


logger = logging.getLogger(__name__)


def write_excel(dataframe: pd.DataFrame, output_file_path: str , sheet_name: str = "加工済みデータ") -> None:
    """
    DataFrameをExcelファイルへ出力します。

    Args:
        dataframe: 出力対象のDataFrame。
        output_file_path: 出力するExcelファイルのパス。
        sheet_name: Excelのシート名。
    Returns:
        None
    """

    output_path = Path(output_file_path)

    # 出力先フォルダが存在しない場合は作成する
    output_path.parent.mkdir(parents=True, exist_ok=True)

    logger.info(f"Excel出力開始: output_file={output_path}")

    # DataFrameのインデックス列は業務データではないため出力しないようにする
    dataframe.to_excel(output_path, sheet_name=sheet_name, index=False, engine="openpyxl")

    logger.info(f"Excel出力完了: output_file={output_path}, rows={len(dataframe)}, columns={len(dataframe.columns)}")
