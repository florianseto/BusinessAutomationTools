# Python Coding Rules

Business Automation Tools Series

Version：1.0

## 日本語

本ドキュメントは Business Automation Tools シリーズで利用するPythonコーディング規約のテンプレートです。
必要に応じて各プロジェクトで追加・変更してください。

## English

This document is the standard Python coding rules template for the Business Automation Tools series.
Project-specific rules may be added or modified when necessary.

---

## 1. Purpose（目的）

### 日本語

本規約は Business Automation Tools シリーズで開発するPythonプログラムの品質を統一することを目的とします。
可読性・保守性・再利用性を重視し、第三者が見ても理解しやすいコードを書くことを基本方針とします。

### English

This document defines the coding standards for the Business Automation Tools series.
The primary goals are readability, maintainability, and reusability.

---

## 2. Scope(適用範囲)

### 日本語

本規約は Business Automation Tools シリーズで開発するすべてのPythonプロジェクトに適用します。
プロジェクト固有のルールが必要な場合は、本規約をベースとして各プロジェクトで追加・変更を行います。

### English

These coding rules apply to all Python projects in the Business Automation Tools series.
Project-specific rules may be added or modified when necessary.

---

## 3. Development Policy（開発方針）

### 日本語

- 可読性を最優先する
- シンプルな実装を心掛ける
- 責務を分離する
- コメントは処理の目的を書く
- ログを残すことを前提とする
- 設計書と実装を一致させる
- 小さく実装・小さくコミットする

### English

- Prioritize readability.
- Keep implementations simple.
- Separate responsibilities.
- Write comments explaining the purpose.
- Assume logging is required.
- Keep implementation consistent with design documents.
- Implement and commit in small units.

---

## 4. Naming Rules（命名規則）

### Base Rules(基本ルール)

### 日本語

|対象|ルール|例|
|--------|--------|--------|
|ファイル|snake_case|csv_reader.py|
|関数|snake_case|read_csv()|
|変数|snake_case|input_file_path|
|クラス|PascalCase|CsvReader|
|定数|UPPER_CASE|DEFAULT_PATH|

### English

|Target|Rule|Example|
|--------|--------|--------|
|File|snake_case|csv_reader.py|
|Function|snake_case|read_csv()|
|Variable|snake_case|input_file_path|
|Class|PascalCase|CsvReader|
|Constant|UPPER_CASE|DEFAULT_PATH|

---

## Additional Information(補足事項)

### 日本語

Pythonでは型ヒントを利用するため、C#のようなハンガリアン記法(sNameなど)は使用しません。
変数名は意味が分かる名前を付けます。

### English

Python uses type hints, so Hungarian notation (for example, sName in C#) is not used.
Variable names should clearly describe their purpose.

### Good Example(良い例)

```
input_file_path
output_file_path
employee_dataframe
sales_list
```

### Bad Example(悪い例)

```
sName
nCount
tmp
val
abc
```

---

## 5. File Rules（ファイル構成）

### 日本語

1ファイル500行以内を目安とします。
ただし、以下のケースの場合は500行未満でも分割します。

- 責務が増えた場合
- 可読性が低下した場合

### English

The guideline is to keep each file to 500 lines or less.
However,in the following cases we will split the file even if it is less than 500 lines.

- If the responsibilities increase
- If readability decreases

### Example(例)

```
src

main.py
csv_reader.py
data_formatter.py
excel_writer.py
log_manager.py
```

---

## 6. Import Rules（インポートルール）

### 日本語

以下の順番で記載します。

① Python標準ライブラリ
② 外部ライブラリ
③ 自作モジュール

### English

The following items are listed in this order:

① Python standard library
② Third-party libraries
③ Custom modules


### 例(Example)

```python
from pathlib import Path
import logging

import pandas as pd

from csv_reader import read_csv
```

---

## 7. Comments（コメント）

### Basic Policy(基本方針)

### 日本語

コメントは(**「何をしているか」**)ではなく
(**「なぜ行うのか」**)を書くことを基本とします。

### English

Comments should explain "why" rather than "what".

### Good Example(良い例)

### 日本語

```python
# 社員番号の先頭0を保持するため文字列として読み込む
```

### English

```python
# Read the employee number as a string to preserve the leading zeros.
```

### Not Very Good Example(あまり良くない例)

### 日本語

```python
# CSVを読み込む
```

### English

```python
# Load CSV
```

---

### Comment Position(コメント位置)

### 日本語

処理の直前に記載します。

```python
# CSVファイルを読み込む
df = read_csv(...)
```

### English

```python
# Load CSV File
df = read_csv(...)
```

---

## 8. Docstrings（関数コメント）

### 日本語

以下には必ずdocstringを記載します。

モジュール
クラス
関数

### English

The following must always include a docstring.

Module
Class
Function

### Example(例)

### 日本語

```python
def read_csv(file_path: Path) -> pd.DataFrame:
    """
    CSVファイルを読み込みます。

    Args:
        file_path:
            読み込むCSVファイル

    Returns:
        DataFrame

    Raises:
        FileNotFoundError:
            ファイルが存在しない場合
    """
```

### English

```python
def read_csv(file_path: Path) -> pd.DataFrame:
    """
    Reads a CSV file.

    Args:
        file_path:
            Target CSV file

    Returns:
        DataFrame

    Raises:
        FileNotFoundError:
            If the file does not exist
    """
```

---

## 9. Type Hints（型ヒント）

### 日本語

以下には原則型ヒントを記載します。

- 引数
- 戻り値

### English

Type hints should generally be provided for the following:

- Function arguments
- Return values

### Example(例)

```python
def main() -> None:
```

```python
def read_csv(file_path: Path) -> pd.DataFrame:
```

---

## 10. Function Rules（関数設計）

### 日本語

関数は(**1つの責務**)だけを持つことを基本とします。

### English

A function should fundamentally have only one responsibility.

### NG Example(NG例)

### 日本語

```
CSV読込

↓

データ加工

↓

Excel出力

↓

ログ出力
```

### English

```
Import CSV file

↓
Data processing

↓
Excel output

↓
Log output
```

### OK Example(OK例)

```
read_csv()

↓

format_data()

↓

write_excel()

↓

write_log()
```


---

## 11. Logging Rules（ログ）

### 日本語

loggingモジュールを使用します。

### English

Use the logging module.

### Record Content(記録内容)

### 日本語

- 処理開始
- 処理終了
- 入力ファイル
- 出力ファイル
- 入力件数
- 出力件数
- 処理時間
- 警告
- エラー
- 例外
  
### English

- Processing Start
- Processing End
- Input File
- Output File
- Number of Input Items
- Number of Output Items
- Processing Time
- Warning
- Error
- Exception

---

### Log Level(ログレベル)

### 日本語

| レベル | 用途 |
|--------|--------|
| DEBUG | 詳細調査 |
| INFO | 通常処理 |
| WARNING | 警告 |
| ERROR | エラー |
| CRITICAL | 重大障害 |

### English

| Level | Purpose |
|--------|--------|
| DEBUG | Detailed Investigation Info |
| INFO | Normal Processing Info |
| WARNING | Warning Info |
| ERROR | Error Info |
| CRITICAL | Critical Info |

---

### Log Example(ログ例)

### 日本語

```
CSV読込開始

CSV読込完了

Excel出力開始

Excel出力完了

処理終了
```

### English

```
CSV Import Started

CSV Import Completed

Excel Output Started

Excel Output Completed

Processing Finished
```

---

## 12. Exception Rules（例外処理）

### 日本語

例外を握りつぶしません。

### English

Exceptions should never be silently ignored.

### NG Example(NG例)

```python
try:
    ...
except:
    pass
```

### OK Example(OK例)

```python
try:
    ...
except Exception as ex:
    logger.exception(ex)
    raise
```

---

## 13. Language Policy（言語ルール）

### 日本語

Business Automation Toolsシリーズでは、可読性と保守性を考慮し、以下の言語ルールを基本とします。
以下はプログラムの構成要素となるため、英語で記載します。

- ファイル名
- クラス名
- 関数名
- 変数名
- 定数

以下は日本国内向けの開発・運用を想定し、日本語で記載します。

- コメント
- docstring
- ログメッセージ
- ユーザー向けメッセージ

### 英語

Business Automation Tools follows the language policy below to improve readability and maintainability.
The following items should always be written in English because they are part of the source code.

- File names
- Class names
- Function names
- Variable names
- Constants

The following items are written in Japanese because this series is primarily intended for development in Japan.

- Comments
- Docstrings
- Log messages
- User messages

### Notes(備考)

### 日本語

海外向けプロジェクトでは、コメント・docstring・ログメッセージ・ユーザー向けメッセージも英語へ変更します。

### English

For overseas projects, comments, docstrings, log messages, and user messages may be written in English.

---

## 14. Development Flow（開発フロー）

### 日本語

Business Automation Toolsシリーズでは以下の順で開発を行います。

1. 要件定義
2. 基本設計
3. コーディング
4. 単体テスト
5. 結合テスト
6. GitHubへPush
7. README更新
8. リリース
9. 保守（メンテナンス）

### English

Development in the Business Automation Tools series follows this order:

1. Requirements Definition
2. Basic Design
3. Coding
4. Unit Testing
5. Integration Testing
6. Push to GitHub
7. README Update
8. Release
9. Maintenance

---

## 15. Version History（変更履歴）

### 日本語

| バージョン | 内容 |
|--------|--------|
| 1.0 | 初版作成 |

### English

| Version | Description |
|--------|--------|
| 1.0 | First edition created |
