# Sample Data（サンプルデータ）

このフォルダでは、Project001の動作確認に使用するサンプルデータを管理します。

This folder contains sample data used to verify Project001 behavior.

## Current Sample（現在のサンプル）

- `input/sample.csv`：社員番号、氏名、部署、勤務時間、不要列を含むUTF-8の入力データ

`src/main.py`を実行すると、社員番号を文字列として読み込み、不要列の削除、列名変更、列並び替えを行います。加工結果は`output/formatted_data_YYYYMMDD_HHMMSS.xlsx`、処理ログは`logs/csv_business_formatter_YYYYMMDD_HHMMSS.log`として保存されます。

When `src/main.py` is executed, employee numbers are read as strings, the unnecessary column is removed, columns are renamed, and their order is adjusted. The result is saved as `output/formatted_data_YYYYMMDD_HHMMSS.xlsx`, and the process log is saved as `logs/csv_business_formatter_YYYYMMDD_HHMMSS.log`.

## Output Columns（出力列）

1. `従業員番号`
2. `氏名`
3. `部署`
4. `勤務時間数`
