# 3. VSCode設定

AIと協働する実装では，エディタ設定と拡張機能の整備が作業効率と再現性を左右します．  
VSCodeは，その作業基盤を構築するための中心的なツールです．

## 3-1. なぜVSCodeを使うか / インストール方法

VSCodeを使う理由:

- 無料で使える軽量エディタ
- Python開発に必要な拡張機能が充実している
- Git/GitHub連携がしやすく，変更履歴を確認しやすい
- Windows/macOS/Linuxで同じように使える

インストール:

1. 公式サイトにアクセス: `https://code.visualstudio.com/`
2. 自分のOS向けインストーラをダウンロード
3. 画面の指示に従ってインストール
4. インストール後，VSCodeを起動して作業フォルダを開く（`File -> Open Folder`）

### `code` コマンド（VSCodeをCLIから開く）

`code` は，ターミナルからVSCodeを開くためのコマンドです．  
作業フォルダを素早く開けるため，GitやCLI作業と相性が良いです．

確認:

```bash
code --version
```

`code` が見つからない場合:

- macOS: VSCodeで `Command Palette` -> `Shell Command: Install 'code' command in PATH`
- Windows/Linux: VSCodeインストール時の「PATHに追加」設定を有効化して再起動

よく使う例:

```bash
code .                # 現在ディレクトリを開く
code README.md        # 特定ファイルを開く
code -r .             # 既存ウィンドウで開き直す
```

## 先ほどcloneしたプロジェクトをVSCodeで開いてみましょう．

```bash
cd Python_quick_lesson
code .
```

---

## 3-2. 拡張機能の説明とインストール方法

拡張機能のインストール手順:

1. 左サイドバーの `Extensions`（四角いアイコン）を開く
2. 検索欄で拡張機能名を検索
3. `Install` を押す

推奨拡張機能:

- Python
  - Python実行，Lint/Format連携，デバッグ機能を提供
- Pylance
  - 型チェックや補完を強化し，コードを読みやすく保つ
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

## 3-4. AI Coding支援の設定

### GitHub Copilot
- GitHub Copilot をインストール後，`Settings` -> `GitHub Copilot` で以下を有効化
  - `Enable GitHub Copilot`
  - `GitHub Copilot: Inline Suggestion Enabled`
  - `GitHub Copilot: Show Completions` を `Always` に設定
- これにより，コード補完や定型実装の提案が常に表示されるようになります．

### Node.js（前提）
Codex CLI / Gemini CLI は `npm` パッケージとして配布されるため，先にNode.jsを入れる:

1. `https://nodejs.org/` から LTS 版をインストール
2. ターミナルで確認:

```bash
node -v
npm -v
```

### Codex
- 利用条件は公式ドキュメントの最新案内を確認
- インストール:

```bash
npm install -g @openai/codex
```

- 使い始め:

```bash
codex
```

- 認証:
  - 初回起動時にCLIに認証URLが表示される
  - そのURLをブラウザで開いて認証すると，CLIにログイン状態が反映される

### Gemini CLI
- 対象: 一般ユーザ（手軽にCLI型AI支援を試したい人）
- インストール:

```bash
npm install -g @google/gemini-cli
```

- 使い始め:

```bash
gemini
```

- 認証:
  - 初回起動時にCLIに認証URLが表示される
  - そのURLをブラウザで開いてGoogleアカウントで認証する
