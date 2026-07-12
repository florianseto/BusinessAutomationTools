# Sample Data（サンプルデータ）

このフォルダでは、Project001の動作確認に使用するサンプルデータを管理します。

This folder contains sample data used to verify Project001 behavior.

## Current Sample（現在のサンプル）

- `input/sample.csv`：CSV読み込み、不要列削除、列名変更、列並び替え、Excel出力の確認に使用する入力データ

`src/main.py`を実行すると、このCSVファイルが読み込まれ、加工結果が`output`フォルダへExcel形式で保存されます。

When `src/main.py` is executed, this CSV file is processed and the result is saved in Excel format in the `output` folder.
