# Project001 CSV Business Formatter 単体テスト仕様書

## 1. 目的

`src` フォルダ配下の各モジュールについて、正常系および異常系の動作を確認する。

## 2. テスト方針

- テストフレームワークは `pytest` を想定する。
- ファイルを扱うテストでは、テストごとに一時フォルダを作成して使用する。
- 外部関数、現在日時、ログ設定などは、単体テストの対象に応じてモック化する。
- DataFrame の確認では、値、列名、列順、データ型、および元データが変更されていないことを確認する。
- 例外の確認では、例外型に加えて、業務上重要なメッセージも確認する。
- 「実施結果」欄はテスト実施時に「OK」または「NG」を記入する。初期値は「未実施」とする。

## 3. テストケース

### 3.1 csv_reader.py

| No | テスト項目 | 入力 | 期待結果 | 実施結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| CR-001 | 【正常系】UTF-8 CSVの読み込み | UTF-8で保存した `社員番号,氏名` のヘッダーと2行のデータを持つ `.csv` ファイル | 2行2列のDataFrameが返り、列名と各セルの値が入力CSVと一致する | 未実施 | `read_csv` |
| CR-002 | 【正常系】CP932 CSVへの再試行 | 日本語を含むCP932の `.csv` ファイル | UTF-8での読込失敗後にCP932で読み込まれ、DataFrameの内容が入力CSVと一致する | 未実施 | `read_csv`。必要に応じてログも確認 |
| CR-003 | 【正常系】列データ型の指定 | `社員番号` が `001,002` のCSV、`column_types={"社員番号": str}` | `社員番号` 列が文字列として読み込まれ、先頭ゼロが保持される | 未実施 | `read_csv` |
| CR-004 | 【正常系】列データ型指定なし | 数値列を持つCSV、`column_types=None` | pandasの型推論でCSVを読み込んだDataFrameが返る | 未実施 | `read_csv` |
| CR-005 | 【正常系】ヘッダーのみのCSV | ヘッダー行のみを持つUTF-8の `.csv` ファイル | 0行で、CSVに記載した列を持つDataFrameが返る | 未実施 | `read_csv`。空ファイルとは区別する |
| CR-006 | 【正常系】大文字拡張子 | 正常な内容を持つ `.CSV` ファイル | 拡張子が大文字でも検証を通過し、DataFrameが返る | 未実施 | `_validate_csv_file`、`read_csv` |
| CR-007 | 【異常系】存在しないファイル | 存在しない `not_found.csv` のパス | `FileNotFoundError` が発生し、メッセージに対象パスが含まれる | 未実施 | `_validate_csv_file` 経由 |
| CR-008 | 【異常系】ディレクトリを指定 | 存在する一時ディレクトリのパス | `ValueError` が発生し、「ファイルではありません」と対象パスがメッセージに含まれる | 未実施 | `_validate_csv_file` 経由 |
| CR-009 | 【異常系】CSV以外の拡張子 | 存在する `input.txt` ファイル | `ValueError` が発生し、「CSV形式ではありません」と対象パスがメッセージに含まれる | 未実施 | `_validate_csv_file` 経由 |
| CR-010 | 【異常系】空ファイル | 0バイトの `.csv` ファイル | `pandas.errors.EmptyDataError` が再送出される | 未実施 | `read_csv` |
| CR-011 | 【異常系】CSV構造不正 | 閉じていない引用符など、解析不能な `.csv` ファイル | `pandas.errors.ParserError` が再送出される | 未実施 | `read_csv` |
| CR-012 | 【異常系】未対応文字コード | UTF-8、CP932のどちらでも復号できないバイト列を持つ `.csv` ファイル | 全対応文字コードでの試行後に `ValueError` が発生し、対象パスと対応文字コードがメッセージに含まれる | 未実施 | `read_csv` |
| CR-013 | 【異常系】指定した列の型変換失敗 | 数値以外を含む列を持つCSV、対象列に整数型を指定 | pandasが発生させた型変換の例外が呼出元へ送出される | 未実施 | `read_csv` |

### 3.2 data_formatter.py

| No | テスト項目 | 入力 | 期待結果 | 実施結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| DF-001 | 【正常系】1列の削除 | 列 `A,B,C` のDataFrame、`columns_to_remove=["B"]` | 列が `A,C` のDataFrameが返り、行データが保持される | 未実施 | `remove_columns` |
| DF-002 | 【正常系】複数列の削除 | 列 `A,B,C` のDataFrame、`columns_to_remove=["A","C"]` | 列 `B` のみのDataFrameが返る | 未実施 | `remove_columns` |
| DF-003 | 【正常系】削除対象が空 | 列 `A,B` のDataFrame、`columns_to_remove=[]` | 入力と同じ内容のDataFrameが返る | 未実施 | `remove_columns` |
| DF-004 | 【正常系】削除時に元データを保持 | 列 `A,B` のDataFrame、`columns_to_remove=["B"]` | 戻り値から `B` が削除される一方、入力DataFrameの列と値は変更されない | 未実施 | `remove_columns` |
| DF-005 | 【異常系】存在しない列の削除 | 列 `A,B` のDataFrame、`columns_to_remove=["X"]` | `ValueError` が発生し、メッセージに `X` が含まれる | 未実施 | `remove_columns` |
| DF-006 | 【異常系】削除対象の一部が存在しない | 列 `A,B` のDataFrame、`columns_to_remove=["A","X"]` | `ValueError` が発生し、処理途中で入力DataFrameが変更されない | 未実施 | `remove_columns` |
| DF-007 | 【正常系】1列の名称変更 | 列 `A,B` のDataFrame、`column_name_map={"A":"X"}` | 列名が `X,B` のDataFrameが返り、値が保持される | 未実施 | `rename_columns` |
| DF-008 | 【正常系】複数列の名称変更 | 列 `A,B,C` のDataFrame、`column_name_map={"A":"X","C":"Z"}` | 列名が `X,B,Z` のDataFrameが返る | 未実施 | `rename_columns` |
| DF-009 | 【正常系】名称変更指定が空 | 列 `A,B` のDataFrame、`column_name_map={}` | 入力と同じ内容のDataFrameが返る | 未実施 | `rename_columns` |
| DF-010 | 【正常系】名称変更時に元データを保持 | 列 `A,B` のDataFrame、`column_name_map={"A":"X"}` | 戻り値の列名のみ変更され、入力DataFrameは変更されない | 未実施 | `rename_columns` |
| DF-011 | 【異常系】存在しない列の名称変更 | 列 `A,B` のDataFrame、`column_name_map={"X":"Y"}` | `ValueError` が発生し、メッセージに `X` が含まれる | 未実施 | `rename_columns` |
| DF-012 | 【正常系】列順の変更 | 列 `A,B,C` のDataFrame、`column_order=["C","A","B"]` | 列順が `C,A,B` のDataFrameが返り、各列の値が保持される | 未実施 | `reorder_columns` |
| DF-013 | 【正常系】一部列の選択と並べ替え | 列 `A,B,C` のDataFrame、`column_order=["C","A"]` | 列順が `C,A` となり、指定されていない `B` は戻り値に含まれない | 未実施 | `reorder_columns` の現行仕様 |
| DF-014 | 【正常系】空の列順指定 | 列 `A,B` のDataFrame、`column_order=[]` | 行数を保持した0列のDataFrameが返る | 未実施 | `reorder_columns` の現行仕様 |
| DF-015 | 【正常系】列順変更時に元データを保持 | 列 `A,B` のDataFrame、`column_order=["B","A"]` | 戻り値のみ列順が変わり、入力DataFrameは変更されない | 未実施 | `reorder_columns` |
| DF-016 | 【異常系】存在しない列を列順に指定 | 列 `A,B` のDataFrame、`column_order=["A","X"]` | `ValueError` が発生し、メッセージに `X` が含まれる | 未実施 | `reorder_columns` |

### 3.3 excel_writer.py

| No | テスト項目 | 入力 | 期待結果 | 実施結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| EW-001 | 【正常系】Excelファイル出力 | 2行2列のDataFrame、存在する一時フォルダ配下の `.xlsx` パス | Excelファイルが作成され、再読込した列名とセル値がDataFrameと一致する | 未実施 | `write_excel` |
| EW-002 | 【正常系】既定シート名 | DataFrame、`sheet_name` を省略 | シート名が「加工済みデータ」になる | 未実施 | `write_excel` |
| EW-003 | 【正常系】任意シート名 | DataFrame、`sheet_name="勤務実績"` | シート名が「勤務実績」になる | 未実施 | `write_excel` |
| EW-004 | 【正常系】出力先フォルダの自動作成 | DataFrame、存在しない複数階層フォルダ配下の出力パス | 親フォルダが再帰的に作成され、Excelファイルが出力される | 未実施 | `write_excel` |
| EW-005 | 【正常系】インデックスを出力しない | 独自インデックスを持つDataFrame | ExcelにDataFrameのインデックス列が出力されず、業務列だけが存在する | 未実施 | `write_excel` |
| EW-006 | 【正常系】空DataFrameの出力 | 列名のみを持つ0行のDataFrame | Excelファイルが作成され、ヘッダーのみが出力される | 未実施 | `write_excel` |
| EW-007 | 【正常系】既存ファイルの上書き | 既に存在する `.xlsx` パスと新しいDataFrame | 例外なく上書きされ、再読込結果が新しいDataFrameと一致する | 未実施 | `write_excel` の現行仕様 |
| EW-008 | 【異常系】不正なシート名 | DataFrame、Excelの制約を超える32文字以上のシート名 | Excel出力ライブラリの例外が呼出元へ送出される | 未実施 | `write_excel` |
| EW-009 | 【異常系】書き込み不能 | DataFrame、ファイルとして既に存在するパスを親フォルダとして指定 | ディレクトリ作成またはファイル書込時の例外が呼出元へ送出される | 未実施 | OS依存の権限試験を避ける |

### 3.4 logging_config.py

| No | テスト項目 | 入力 | 期待結果 | 実施結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| LC-001 | 【正常系】ログフォルダの作成 | `logs` が存在しない一時プロジェクトフォルダ | `logs` フォルダが作成される | 未実施 | `setup_logging` |
| LC-002 | 【正常系】ログファイル名 | 現在日時を `2026-01-02 03:04:05` に固定したプロジェクトフォルダ | 戻り値が `logs/csv_business_formatter_20260102_030405.log` になる | 未実施 | `datetime.now` をモック化 |
| LC-003 | 【正常系】ログファイルへのUTF-8出力 | ログ設定後に日本語のINFOログを1件出力 | 戻り値のファイルが存在し、日本語メッセージがUTF-8で記録される | 未実施 | ハンドラーをflushして確認 |
| LC-004 | 【正常系】ログレベル | 一時プロジェクトフォルダ | ルートロガーのレベルが `INFO` に設定される | 未実施 | `setup_logging` |
| LC-005 | 【正常系】既存logsフォルダ | `logs` が既に存在する一時プロジェクトフォルダ | 例外なく設定され、新しいログファイルのパスが返る | 未実施 | `setup_logging` |
| LC-006 | 【異常系】logsパスがファイル | プロジェクト直下に通常ファイルとして作成した `logs` | `FileExistsError` 等のディレクトリ作成例外が呼出元へ送出される | 未実施 | `setup_logging` |
| LC-007 | 【異常系】ログファイル作成失敗 | `logging.FileHandler` が `OSError` を発生するようモック化 | `OSError` が呼出元へ送出される | 未実施 | OS依存の権限試験を避ける |

### 3.5 main.py

| No | テスト項目 | 入力 | 期待結果 | 実施結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| MN-001 | 【正常系】一連の処理の完了 | `read_csv` がサンプル相当のDataFrameを返すようにし、外部関数をモック化 | `setup_logging`、`read_csv`、`remove_columns`、`rename_columns`、`reorder_columns`、`write_excel` が各1回、規定順序で呼ばれ、例外なく終了する | 未実施 | `main` |
| MN-002 | 【正常系】入力パスの組み立て | `Path(__file__)` を基準に実行 | `read_csv` に `<project_dir>/sample/input/sample.csv` が渡される | 未実施 | `main` |
| MN-003 | 【正常系】社員番号の型指定 | 外部関数をモック化して実行 | `read_csv` の型指定に `{"社員番号": str}` が渡される | 未実施 | `main` |
| MN-004 | 【正常系】整形条件と処理間データ連携 | 各整形関数が識別可能なDataFrameを返すようモック化 | 削除列 `不要列`、名称変更 `社員番号→従業員番号` と `勤務時間→勤務時間数`、列順 `従業員番号,氏名,部署,勤務時間数` が使用され、各戻り値が次処理へ渡る | 未実施 | `main` |
| MN-005 | 【正常系】日時付き出力パス | 現在日時を `2026-01-02 03:04:05` に固定 | `write_excel` の出力先が `<project_dir>/output/formatted_data_20260102_030405.xlsx` になる | 未実施 | `datetime.now` をモック化 |
| MN-006 | 【正常系】既定シート名での出力 | 外部関数をモック化して実行 | `write_excel` がDataFrameと出力パスの2引数で呼ばれ、既定シート名を使用する | 未実施 | `main` |
| MN-007 | 【異常系】CSV読込失敗 | `read_csv` が `FileNotFoundError` を発生 | 後続の整形関数と `write_excel` は呼ばれず、同じ `FileNotFoundError` が再送出される | 未実施 | エラーログ出力も確認 |
| MN-008 | 【異常系】不要列削除失敗 | `remove_columns` が `ValueError` を発生 | 後続の名称変更、列順変更、Excel出力は呼ばれず、同じ `ValueError` が再送出される | 未実施 | エラーログ出力も確認 |
| MN-009 | 【異常系】列名変更失敗 | `rename_columns` が `ValueError` を発生 | 後続の列順変更とExcel出力は呼ばれず、同じ `ValueError` が再送出される | 未実施 | エラーログ出力も確認 |
| MN-010 | 【異常系】列順変更失敗 | `reorder_columns` が `ValueError` を発生 | `write_excel` は呼ばれず、同じ `ValueError` が再送出される | 未実施 | エラーログ出力も確認 |
| MN-011 | 【異常系】Excel出力失敗 | `write_excel` が `OSError` を発生 | 同じ `OSError` が再送出され、処理失敗の例外ログが出力される | 未実施 | `main` |
| MN-012 | 【異常系】ログ設定失敗 | `setup_logging` が `OSError` を発生 | `read_csv` 以降の処理は呼ばれず、`OSError` が呼出元へ送出される | 未実施 | 現行実装では `try` ブロック開始前のため、main内の失敗ログ対象外 |

## 4. 合否判定基準

- 期待結果をすべて満たした場合は「OK」とする。
- 期待結果と1項目でも異なる場合は「NG」とし、備考欄に実際の結果、原因、課題番号などを記録する。
- テスト未実施の場合は「未実施」とする。

