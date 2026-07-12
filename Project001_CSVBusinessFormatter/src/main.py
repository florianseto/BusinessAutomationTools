"""
CSV Business Formatterのメイン処理を提供するモジュール
Author:
    Florian Seto
"""

import logging
from datetime import datetime
from pathlib import Path

from csv_reader import read_csv
from data_formatter import remove_columns, rename_columns, reorder_columns
from excel_writer import write_excel
from logging_config import setup_logging

logger = logging.getLogger(__name__)

def main() -> None:
    """
    CSV Business Formatterのメイン処理を実行します。
    """

    # main.pyの位置を基準にプロジェクトフォルダを取得する
    project_dir = Path(__file__).resolve().parent.parent

    # ターミナルおよびログファイルへのログ出力を設定する
    log_file_path = setup_logging(project_dir)

    # 読み込み対象のサンプルCSVファイルパスを指定する
    input_file_path = project_dir / "sample" / "input" / "sample.csv"

    # 既存ファイルを上書きしないように日時付きの出力パスを作成する
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_path = (project_dir / "output" / f"formatted_data_{timestamp}.xlsx")

    # 社員番号の先頭ゼロを保持するため、文字列型として読み込む
    column_types = {
        "社員番号": str
    }

    # 業務上不要な列を出力対象から除外する
    columns_to_remove = [
        "不要列"
    ]

    # 業務で利用しやすい名称へ列名を変更する
    column_name_map = {
        "社員番号": "従業員番号",
        "勤務時間": "勤務時間数"
    }

    # Excelへ出力する列を業務上必要な順番に並べる
    column_order = [
        "従業員番号",
        "氏名",
        "部署",
        "勤務時間数"
    ]

    logger.info(
        f"CSV Business Formatterのメイン処理を開始します: "
        f"input_file={input_file_path}, output_file={output_file_path}, "
        f"log_file={log_file_path}"
    )

    try:
        # CSVファイルを読み込む
        dataframe = read_csv(str(input_file_path), column_types)

        # 読み込んだCSVデータを表示する
        logger.info(f"CSV読み込み結果: rows={len(dataframe)}, columns={len(dataframe.columns)}")

        # 不要列を削除する
        formatted_dataframe = remove_columns(dataframe, columns_to_remove)

        # 列名を変更する
        formatted_dataframe = rename_columns(formatted_dataframe, column_name_map)

        # 列を指定された順番に並べ替える
        formatted_dataframe = reorder_columns(formatted_dataframe, column_order)

        # 整形結果を確認する
        logger.info(f"データ整形結果: rows={len(formatted_dataframe)}, columns={len(formatted_dataframe.columns)}")

        # 整形したデータをExcelファイルへ出力する
        write_excel(formatted_dataframe, output_file_path)

        logger.info("CSV Business Formatterのメイン処理が正常に完了しました。")

    except Exception:
        logger.exception("CSV Business Formatterのメイン処理に失敗しました。")
        raise



if __name__ == "__main__":
    main()
