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

#### 日本語

- [x] CSVファイルの読み込み
- [x] UTF-8およびCP932による自動再試行
- [x] データ整形
- [x] 不要列の削除
- [x] 列名変更
- [x] 列の並び替え

#### English

- [x] Import CSV files
- [x] Automatically retry with UTF-8 and CP932 encodings
- [x] Format data
- [x] Remove unnecessary columns
- [x] Rename columns
- [x] Reorder columns

### Excel Output（Excel出力）

#### 日本語

- [x] Excelファイルへの出力
- [ ] 集計シートの作成
- [x] シート名の設定
- [ ] 基本的な書式設定
- [x] 出力フォルダの自動作成
- [x] 日時付き出力ファイル名での保存

#### English

- [x] Export data to Excel files
- [ ] Generate summary sheets
- [x] Set sheet names
- [ ] Apply basic formatting
- [x] Automatically create the output folder
- [x] Save output files with timestamped names

### Logging（ログ出力）

#### 日本語

- [x] 処理状況およびエラーを記録するログ処理
- [x] 入力ファイル名・出力ファイル名のログ記録
- [x] ターミナルへのログ出力
- [x] 日時付きログファイルへの保存

#### English

- [x] Log processing status and errors
- [x] Record input and output file names in logs
- [x] Output logs to the terminal
- [x] Save logs to timestamped log files

---

## Development Status（開発状況）

### 日本語

🟡 基本機能実装済み・テスト準備フェーズ

CSV読み込み、データ整形、Excel出力、ログ出力までの基本処理を実装済みです。現在は自動テストと出力機能の拡充を予定しています。

### English

🟡 Core Features Implemented / Preparing for Testing

The basic workflow for CSV import, data formatting, Excel export, and logging has been implemented. Automated testing and output enhancements are planned next.

---

## Development Roadmap（開発ロードマップ）

### 日本語

- [x] 要求定義
- [x] 基本設計
- [x] CSV読み込み機能
- [x] データ整形機能
- [x] Excel出力機能
- [x] ログ出力機能
- [ ] テスト
- [ ] v1.0 リリース

### English

- [x] Requirements definition
- [x] Basic design
- [x] CSV import feature
- [x] Data formatting feature
- [x] Excel export feature
- [x] Logging feature
- [ ] Testing
- [ ] v1.0 release

---

## Folder Structure（フォルダ構成）

```text
Project001_CSVBusinessFormatter
├── docs
├── sample
│   └── input
├── src
├── tests
├── logs
├── output
└── README.md
```

### 日本語

- `docs`：要求定義書、設計書などを管理
- `sample`：サンプルCSVや出力例を管理
- `src`：Pythonソースコードを管理
- `tests`：今後追加するテストコードを管理
- `logs`：処理日時、処理状況、エラーなどを記録したログファイルを管理
- `output`：生成したExcelファイルを管理

### English

- `docs`: Project documents such as requirements and design notes
- `sample`: Sample CSV files and output examples
- `src`: Python source code
- `tests`: Test code to be added
- `logs`: Log files containing processing times, status, and errors
- `output`: Generated Excel files

---

## Development History（開発履歴）

### 日本語

| Version | 内容 |
| --- | --- |
| v0.1.0 | README作成・プロジェクト初期構成作成 |
| v0.2.0 | 要求定義・基本設計ドキュメントを作成 |
| v0.3.0 | CSV読み込み機能を実装 |
| v0.4.0 | データ整形・Excel出力機能を実装 |
| v0.5.0 | ターミナルおよびログファイルへのログ出力機能を実装 |

### English

| Version | Description |
| --- | --- |
| v0.1.0 | Created README and initial project structure |
| v0.2.0 | Created requirements and basic design documentation |
| v0.3.0 | Implemented the CSV import feature |
| v0.4.0 | Implemented data formatting and Excel export features |
| v0.5.0 | Implemented terminal and file logging |

---

## License（ライセンス）

### 日本語

このプロジェクトは MIT License を予定しています。

### English

This project is planned to use the MIT License.

## Author（作者）

Florian Seto
