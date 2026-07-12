"""
CSV Business Formatterのメイン処理を提供するモジュール
Author:
    Florian Seto
"""

import logging
from pathlib import Path

from csv_reader import read_csv

logger = logging.getLogger(__name__)

def main() -> None:
    """
    CSV Business Formatterのメイン処理を実行します。
    """

    # main.pyの位置を基準にプロジェクトフォルダを取得する
    project_dir = Path(__file__).resolve().parent.parent

    # 読み込み対象のサンプルCSVファイルパスを指定する
    input_file_path = project_dir / "sample" / "input" / "sample.csv"

    # 社員番号の先頭ゼロを保持するため、文字列型として読み込む
    column_types = {
        "社員番号": str
    }

    logger.info(f"CSV Business Formatterのメイン処理を開始します: input_file={input_file_path}")

    try:
        # CSVファイルを読み込む
        dataframe = read_csv(str(input_file_path), column_types)

        # 読み込み結果を確認する
        print(f"読み込んだCSVデータ:\n{dataframe}")

        # 読み込んだCSVデータを表示する
        logger.info(f"CSV読み込み結果: rows={len(dataframe)}, columns={len(dataframe.columns)}")

        logger.info("CSV Business Formatterのメイン処理が正常に完了しました。")

    except Exception:
        logger.exception("CSV Business Formatterのメイン処理に失敗しました。")
        raise



if __name__ == "__main__":
    main()