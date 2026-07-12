# Source Code（ソースコード）

このフォルダでは、Project001のPythonソースコードを管理します。

This folder contains the Python source code for Project001.

## Modules（モジュール）

- `main.py`：CSV読み込みからExcel出力までのメイン処理
- `csv_reader.py`：CSVファイルの検証、UTF-8／CP932での読み込み
- `data_formatter.py`：不要列削除、列名変更、列並び替え
- `excel_writer.py`：Excelファイルの出力および出力フォルダの作成
- `logging_config.py`：ターミナルおよび日時付きログファイルへの出力設定

## Development Status（開発状況）

CSV読み込み、データ整形、Excel出力、ログ出力の基本機能は実装済みです。自動テスト、集計シートおよび書式設定は今後対応予定です。

The core CSV import, data formatting, Excel export, and logging features are implemented. Automated tests, summary sheets, and formatting are planned.
