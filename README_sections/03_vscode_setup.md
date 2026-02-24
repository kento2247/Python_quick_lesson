# 3. VSCode設定

## 3-1. なぜVSCodeを使うか / インストール方法

VSCodeを使う理由:

- 無料で使える軽量エディタ
- Python開発に必要な拡張機能が充実している
- Git/GitHub連携がしやすく、変更履歴を確認しやすい
- Windows/macOS/Linuxで同じように使える

インストール:

1. 公式サイトにアクセス: `https://code.visualstudio.com/`
2. 自分のOS向けインストーラをダウンロード
3. 画面の指示に従ってインストール
4. インストール後、VSCodeを起動して作業フォルダを開く（`File -> Open Folder`）

---

## 3-2. 拡張機能の説明とインストール方法

拡張機能のインストール手順:

1. 左サイドバーの `Extensions`（四角いアイコン）を開く
2. 検索欄で拡張機能名を検索
3. `Install` を押す

推奨拡張機能:

- Python
  - Python実行、Lint/Format連携、デバッグ機能を提供
- Pylance
  - 型チェックや補完を強化し、コードを読みやすく保つ
- GitHub Copilot
  - コード提案や定型実装の補助
- GitLens
  - `git blame` や履歴の可視化を強化
- Remote - SSH
  - リモートサーバ上の開発環境をVSCodeから直接操作

補足:

- `Command Palette`（`Ctrl/Cmd + Shift + P`）から `Extensions: Install Extensions` でも導入可能
- コマンドラインからは `code --install-extension <extension-id>` でも導入できる

---

## 3-3. 自動保存などの推奨設定

設定画面を開く:

1. `Ctrl/Cmd + ,` で設定を開く
2. 検索欄に項目名（例: `auto save`）を入力して設定

最初に有効化したい設定:

- `Files: Auto Save` -> `afterDelay`
- `Files: Auto Save Delay` -> `1000`（1秒）
- `Editor: Format On Save` -> `ON`
- `Editor: Tab Size` -> `4`
- `Editor: Insert Spaces` -> `ON`
- `Editor: Rulers` -> `88`（行長の目安）

`settings.json` で設定する例:

```json
{
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "editor.formatOnSave": true,
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "editor.rulers": [88]
}
```
