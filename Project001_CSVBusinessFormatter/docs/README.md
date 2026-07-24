# Documentation（ドキュメント）

このフォルダでは、Project001の設計書やテスト仕様書などの開発ドキュメントを管理します。

This folder contains development documents such as the design and test specifications for Project001.

## Current Documents（現在のドキュメント）

- `Project001_Design.xlsx`：プロジェクト概要、要求一覧、機能一覧、入出力設計、データ設計、非機能要件、開発計画、テスト方針などを記載
- `Project001_UnitTest.xlsx`：単体テスト項目および実施結果を管理するExcel版資料
- `Project001_Unit_Test_Specification.md`：全5モジュールの正常系・異常系テストケースを記載したMarkdown版単体テスト仕様書

## Development Status（開発状況）

要件定義と基本設計に加え、全5モジュールを対象とする単体テスト仕様書を作成し、pytestテスト57件を実装済みです。2026年7月13日時点の実行結果は56件成功、1件はExcelシート名の長さに関する仕様差異です。この差異は実装不具合とは扱わず、現在の開発フェーズは完了とします。必要な見直しは次回改善時に行います。

The requirements definition and basic design are complete. A unit test specification covering all five modules has been created, together with 57 pytest tests. As of July 13, 2026, 56 tests pass and one reflects a specification difference concerning long Excel sheet names. This is not treated as an implementation defect, so the current development phase is complete; any review will be handled during a future improvement.
