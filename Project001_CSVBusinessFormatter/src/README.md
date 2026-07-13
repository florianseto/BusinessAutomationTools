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

CSV読み込み、データ整形、Excel出力、ログ出力の基本機能は実装済みです。各モジュールに対する単体テストも追加し、現在の開発フェーズは完了しています。2026年7月13日時点の結果は全57件中56件成功、1件はライブラリとの仕様差異です。

The core CSV import, data formatting, Excel export, and logging features are implemented, and unit tests have been added for every module. The current development phase is complete. As of July 13, 2026, 56 of 57 tests pass, with one specification difference involving the library behavior.

## Remaining Work（今後の対応）

- 必要に応じて、32文字以上のExcelシート名に関する仕様を次回改善時に見直す
- 集計シートを実装する
- Excelの基本書式を実装する

- Review the specification for Excel sheet names longer than 31 characters during a future improvement if needed
- Implement summary sheets
- Implement basic Excel formatting
