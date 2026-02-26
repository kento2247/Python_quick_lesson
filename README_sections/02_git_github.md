# 2. Git / GitHub

AIと協働して開発を進めるには，変更履歴を安全に管理し，他者と共有できることが前提になります．  
Git/GitHubは，そのための基盤となるツールです．

## 2-1. なぜ重要か

Git/GitHubは，開発でよく起きる次の問題を解決します．

1. 「どの変更で壊れたかわからない」
   - 解決: コミット履歴で変更点を時系列で追跡できる．
2. 「前の状態に戻したいが戻せない」
   - 解決: 特定コミットへ戻す・比較することができる．
3. 「複数人編集で上書き事故が起きる」
   - 解決: ブランチとPRで変更を分離し，レビュー後に統合できる．
4. 「実験や分析の再現ができない」
   - 解決: コードと設定の履歴を残し，いつでも同じ状態を再現できる．
5. 「誰が何を変更したか不明」
   - 解決: 変更者・変更理由（コミットメッセージ）が記録される．

要するに，Gitは「ローカルの履歴管理」，GitHubは「共有・レビュー・安全な統合」を担当し，開発ミスと手戻りを大幅に減らします．

---

## 2-2. Gitインストール

Ubuntu / WSL:

```bash
sudo apt update
sudo apt install git
```

macOS（Homebrew）:

```bash
brew install git
```

※ macOSにはGitが標準で入っている場合もありますが，古い版のことがあるため `git --version` で確認します．

確認:

```bash
git --version
```

初期設定（最初に1回だけ）:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## 2-3. 基本操作と `.gitignore`

```bash
git init
touch sample.txt
git add .
git commit -m "initial commit"
```

`.gitignore` は「Gitで追跡しないファイル」を指定する設定ファイルです．  
容量の大きいファイルや，バージョン管理をする必要のないファイルを指定します．
例: 仮想環境，ログ，キャッシュ，秘密情報（`.env` など）．

```gitignore
# Python
__pycache__/
*.pyc

# Virtual environment
.venv/
venv/

# Secrets
.env
```

ポイント:

- 一度コミット済みのファイルは `.gitignore` だけでは追跡停止されない
- その場合は `git rm --cached <file>` を使って追跡対象から外す

---

## 2-4. GitHubへの接続とGit/GitHubの関係，SSH Key設定

関係の整理:

- `Git`: ローカルで履歴管理するツール
- `GitHub`: Gitリポジトリを共有・レビューするクラウドサービス

`git clone` とは:

- GitHub上の既存リポジトリを，ローカルPCに丸ごと複製するコマンド
- 初めて他者リポジトリを触るときの起点になる
- `clone` 後は，履歴・ブランチ情報も含めてローカルで作業できる

例（SSH）:

```bash
git clone git@github.com:kento2247/Python_quick_lesson.git
cd Python_quick_lesson
```

ローカルリポジトリをGitHubに接続する基本:

```bash
git remote add origin git@github.com:USER/REPO.git
git branch -M main
git push -u origin main
```

SSH Keyとは:

- パスワードの代わりに使う認証鍵
- 公開鍵（GitHubに登録）と秘密鍵（手元で厳重管理）のペアで認証する

SSH Keyの作成と登録（Linux/macOS）:

```bash
ssh-keygen -t ed25519
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

1. `cat ~/.ssh/id_ed25519.pub` の出力をコピー
2. GitHub: `Settings` -> `SSH and GPG keys` -> `New SSH key`
3. 接続確認:

```bash
ssh -T git@github.com
```

---

## 2-5. `git merge`, `git stash`, `git status`, `git checkout`

### `git status`

現在の変更状態（未追跡，ステージ済み，ブランチ状況）を確認する．

```bash
git status
```

### `git checkout`

ブランチ切り替えや，特定コミット/ファイルの状態に移動する．  
（新しめの運用ではブランチ切替は `git switch` も推奨）

```bash
git checkout feature/login
```

### `git stash`

コミットしたくない作業途中の変更を一時退避する．

```bash
git stash
git stash list
git stash pop
```

### `git merge`

別ブランチの変更を現在ブランチへ統合する．

```bash
git checkout main
git merge feature/login
```

競合（conflict）が出た場合は，対象ファイルを修正後にコミットする．

---

## 2-6. GitHub上での操作（PR, Merge, Organization, Private/Public）

### PR（Pull Request）

- 「この変更を取り込んでください」というレビュー依頼
- 差分確認，コメント，CI結果確認，承認を行う場所

### Merge

- PRが承認された変更をベースブランチ（例: `main`）へ統合
- 代表的な方法: `Create a merge commit`, `Squash and merge`, `Rebase and merge`

### Organization

- チーム/研究室/企業単位でリポジトリと権限を管理する仕組み
- メンバー管理，チームごとのアクセス制御，監査がしやすい

### Private / Public

- `Public`: 誰でも閲覧可能（OSS・公開教材向け）
- `Private`: 許可ユーザーのみ閲覧可能（社内/研究データ向け）

---

## 2-7. ブランチ命名規則とGitHub Pages

### ブランチ命名規則（例）

可読性のため，用途をプレフィックスで明示する．

- `feature/add-login-page`
- `fix/resolve-import-error`
- `docs/update-readme`
- `refactor/split-trainer-module`

ポイント:

- 英小文字 + ハイフン区切り
- 何をするブランチか1行でわかる名前にする
- issue番号と連携する場合は `feature/123-add-login` のようにする

### GitHub Pages

GitHubリポジトリから静的サイトを公開する機能．  
ドキュメント，研究紹介ページ，講義資料公開に便利．

基本設定の流れ:

1. GitHubの対象リポジトリを開く
2. `Settings` -> `Pages`
3. 公開元ブランチ（例: `main`）とフォルダ（例: `/docs`）を選択
4. 表示された公開URLにアクセスして確認
