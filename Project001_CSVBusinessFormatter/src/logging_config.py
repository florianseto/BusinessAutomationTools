"""
CSV Business Formatterのログ設定を提供するモジュール
Author:
    Florian Seto
"""

import logging
from datetime import datetime
from pathlib import Path


def setup_logging(project_dir: Path) -> Path:
    """
    ターミナルおよびログファイルへの出力を設定します。

    Args:
        project_dir: プロジェクトフォルダのパス。
    Returns:
        作成したログファイルのパス。
    """

    log_dir = project_dir / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = log_dir / f"csv_business_formatter_{timestamp}.log"

    log_format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler(log_file_path, encoding="utf-8"),
            logging.StreamHandler(),
        ],
        force=True,
    )

    return log_file_path
