# Project001 - CSV Business Formatter

CSVデータを業務で利用しやすいExcel形式へ変換し、日々の定型業務を効率化するためのPythonツールです。

This project is a Python-based business automation tool that converts CSV files into easy-to-use Excel reports for daily business operations.

---

## Project Overview（概要）

### 日本語

Project001はBusiness Automation Toolsシリーズの第一弾です。

CSVデータの取り込み、整形、Excel出力を自動化し、業務改善を目的としたPythonツールとして開発します。

### English

Project001 is the first project in the Business Automation Tools series.

It automates CSV processing and Excel report generation to improve business workflows.

---

## Purpose（目的）

### 日本語

CSVファイルを毎回手作業で開き、整形し、Excelへ転記・集計する作業を減らすことを目的としています。

手作業によるミスを減らし、確認作業や集計作業の時間短縮を目指します。

### English

The purpose of this project is to reduce manual work such as opening CSV files, formatting data, and creating Excel reports.

It aims to reduce human errors and shorten the time required for checking and reporting tasks.

---

## Target Users（対象ユーザー）

### 日本語

- CSVファイルを日常的に扱う方
- Excelで集計・確認作業を行う方
- 製造業、事務、営業、経理、総務などの担当者
- 手作業による転記・集計を減らしたい方
- 小規模な業務改善ツールを必要としている方

### English

- People who regularly work with CSV files
- Users who perform checking and reporting tasks in Excel
- Staff in manufacturing, administration, sales, accounting, or general affairs
- Users who want to reduce manual copy-and-paste or aggregation work
- Users who need small business automation tools

---

## Features and Implementation Status（機能・実装状況）

### CSV Processing（CSV処理）

### 日本語

- [x] CSVファイルの読み込み
- [x] UTF-8およびCP932による自動再試行
- [x] データ整形
- [x] 不要列の削除
- [x] 列名変更
- [x] 列の並び替え

### English

- [x] Import CSV files
- [x] Automatically retry with UTF-8 and CP932 encodings
- [x] Format data
- [x] Remove unnecessary columns
- [x] Rename columns
- [x] Reorder columns

### Excel Output（Excel出力）

### 日本語

- [x] Excelファイルへの出力
- [ ] 集計シートの作成
- [x] シート名の設定
- [ ] 基本的な書式設定
- [x] 出力フォルダの自動作成
- [x] 日時付き出力ファイル名での保存

### English

- [x] Export data to Excel files
- [ ] Generate summary sheets
- [x] Set sheet names
- [ ] Apply basic formatting
- [x] Automatically create the output folder
- [x] Save output files with timestamped names

### Logging（ログ出力）

### 日本語

- [x] 処理状況およびエラーを記録するログ処理
- [x] 入力ファイル名・出力ファイル名のログ記録
- [x] ターミナルへのログ出力
- [x] 日時付きログファイルへの保存

### English

- [x] Log processing status and errors
- [x] Record input and output file names in logs
- [x] Output logs to the terminal
- [x] Save logs to timestamped log files

---

## Development Status（開発状況）

### 日本語

🟢 v1.0正式リリース完了

CSV読み込み、データ整形、Excel出力、ログ出力までの基本処理を実装し、`v1.0.0`として正式公開しています。全5モジュールを対象とする単体テスト57件の作成と確認も完了しています。

### English

🟢 v1.0 Official Release Complete

The basic workflow for CSV import, data formatting, Excel export, and logging has been implemented and officially released as `v1.0.0`. Creation and verification of 57 unit tests covering all five modules are also complete.

### Current Test Result（現在のテスト結果）

- 実行日 / Run date: 2026-07-24
- 結果 / Result: **57 passed**（全57件）

---

## Development Roadmap（開発ロードマップ）

### 日本語

- [x] 要件定義
- [x] 基本設計
- [x] CSV読み込み機能
- [x] データ整形機能
- [x] Excel出力機能
- [x] ログ出力機能
- [x] 単体テスト作成
- [x] 単体テスト確認完了
- [x] v1.0 開発完了
- [x] リリース準備完了
- [x] GitHub公開・`v1.0.0`タグ作成

### English

- [x] Requirements definition
- [x] Basic design
- [x] CSV import feature
- [x] Data formatting feature
- [x] Excel export feature
- [x] Logging feature
- [x] Unit test implementation
- [x] Unit test verification completed
- [x] v1.0 development completed
- [x] Release preparation completed
- [x] GitHub publication and `v1.0.0` tag creation

### Future Improvements（今後の改善候補）

- [ ] 集計シートの実装 / Implement summary sheets
- [ ] Excel基本書式の実装 / Implement basic Excel formatting

---

## Folder Structure（フォルダ構成）

```text
Project001_CSVBusinessFormatter
├── docs
├── sample
│   └── input
├── src
├── tests
│   ├── conftest.py
│   └── test_*.py
├── logs
├── output
└── README.md
```

### 日本語

- `docs`：要件定義書、設計書などを管理
- `sample`：サンプルCSVや出力例を管理
- `src`：Pythonソースコードを管理
- `tests`：5つのソースモジュールを対象とするpytest単体テストを管理
- `logs`：処理日時、処理状況、エラーなどを記録したログファイルを管理
- `output`：生成したExcelファイルを管理

### English

- `docs`: Project documents such as requirements and design notes
- `sample`: Sample CSV files and output examples
- `src`: Python source code
- `tests`: pytest unit tests for the five source modules
- `logs`: Log files containing processing times, status, and errors
- `output`: Generated Excel files

---

## Development History（開発履歴）

### 日本語

| Version | 内容 |
| --- | --- |
| v0.1.0 | README作成・プロジェクト初期構成作成 |
| v0.2.0 | 要件定義・基本設計ドキュメントを作成 |
| v0.3.0 | CSV読み込み機能を実装 |
| v0.4.0 | データ整形・Excel出力機能を実装 |
| v0.5.0 | ターミナルおよびログファイルへのログ出力機能を実装 |
| v0.6.0 | 全5モジュールの単体テスト57件と単体テスト仕様書を追加 |

### English

| Version | Description |
| --- | --- |
| v0.1.0 | Created README and initial project structure |
| v0.2.0 | Created requirements and basic design documentation |
| v0.3.0 | Implemented the CSV import feature |
| v0.4.0 | Implemented data formatting and Excel export features |
| v0.5.0 | Implemented terminal and file logging |
| v0.6.0 | Added 57 unit tests for all five modules and the unit test specification |

---

## License（ライセンス）

### 日本語

このプロジェクトはMIT Licenseのもとで公開しています。

### English

This project is licensed under the MIT License.

## Author（作者）

Florian Seto
