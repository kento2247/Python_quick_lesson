# 1. OSの設定

## 1-1. なぜLinuxを使うのか

システム開発・AI開発では **Linux** が標準環境です．

- サーバーの大半がLinux
- 開発ツールの互換性が高い
- Docker・AI系ライブラリとの相性が良い
- 無料で利用可能

MacはUnix系OSでありLinuxと思想・構造が近いため開発用途でよく使われます．  
一方でWindowsはLinuxと差異が大きく，環境差によるトラブルが増えがちです（例：パス構造，パッケージ管理，シェル仕様）．

そのため本講義では **Linux環境前提** で進めます．

目的：

- 環境差異によるトラブル削減
- AIツール活用の最大化
- 開発コスト低下

---

## 1-2. Windowsの方：WSLの導入

WSL（Windows Subsystem for Linux）を利用します．

1. PowerShellを管理者で起動
2. 実行:

```powershell
wsl --install
```

3. 再起動後，Ubuntu初期設定

確認:

```bash
uname -a
```

---

## 1-3. 基本的なCLI操作（Linux）

CLI（Command Line Interface）は，ターミナル上で文字で操作する方法です．  
開発現場ではGUIよりも高速・再現性が高いため，まずは基本コマンドを押さえます．

### 現在地と一覧の確認

```bash
pwd
ls
ls -la
```

- `pwd`: 現在いるディレクトリを表示
- `ls`: ファイル/フォルダ一覧を表示
- `ls -la`: 隠しファイルも含めて詳細表示

### ディレクトリ移動

```bash
cd /path/to/dir
cd ..
cd ~
```

- `cd`: ディレクトリ移動
- `cd ..`: 1つ上の階層へ
- `cd ~`: ホームディレクトリへ

### ファイル/フォルダ操作

```bash
mkdir practice
touch memo.txt
cp memo.txt memo_backup.txt
mv memo_backup.txt archive.txt
rm archive.txt
```

- `mkdir`: フォルダ作成
- `touch`: 空ファイル作成
- `cp`: コピー
- `mv`: 移動/名前変更
- `rm`: 削除（元に戻せないので注意）

### 中身の確認

```bash
cat memo.txt
head -n 5 memo.txt
tail -n 5 memo.txt
```

- `cat`: 全文表示
- `head`: 先頭だけ表示
- `tail`: 末尾だけ表示

### 便利な補助操作

- `Tab` キー: ファイル名・コマンド補完
- `↑ / ↓` キー: コマンド履歴
- `Ctrl + C`: 実行中コマンドの停止

---

## 1-4. 練習問題

以下をターミナルで実行してください（`~/cli_practice` を作業場所にする）．

1. `~/cli_practice` ディレクトリを作成し，そこへ移動する．
2. `note1.txt` と `note2.txt` を作成する．
3. `note1.txt` を `backup_note1.txt` としてコピーする．
4. `note2.txt` を `renamed_note2.txt` にリネームする．
5. `ls -la` でファイル一覧を表示し，結果を確認する．
6. `backup_note1.txt` を削除する．
7. 最後に `pwd` と `ls` を実行して，現在地と残っているファイルを確認する．

発展課題:

1. `cat` / `head` / `tail` の違いを，自分の言葉で説明する．
2. `rm` を安全に使うためのルールを3つ考える．

### 模範解答

1. `~/cli_practice` ディレクトリを作成し，そこへ移動する．

```bash
mkdir ~/cli_practice
cd ~/cli_practice
```

2. `note1.txt` と `note2.txt` を作成する．

```bash
touch note1.txt note2.txt
```

3. `note1.txt` を `backup_note1.txt` としてコピーする．

```bash
cp note1.txt backup_note1.txt
```

4. `note2.txt` を `renamed_note2.txt` にリネームする．

```bash
mv note2.txt renamed_note2.txt
```

5. `ls -la` でファイル一覧を表示し，結果を確認する．

```bash
ls -la
```

6. `backup_note1.txt` を削除する．

```bash
rm backup_note1.txt
```

7. 最後に `pwd` と `ls` を実行して，現在地と残っているファイルを確認する．

```bash
pwd
ls
```

発展課題 1 の解答例:

- `cat`: ファイル全体を表示する．
- `head`: ファイル先頭（デフォルト10行）だけを表示する．
- `tail`: ファイル末尾（デフォルト10行）だけを表示する．

発展課題 2 の解答例:

1. `rm` 実行前に `pwd` と `ls` で場所と対象ファイルを確認する．
2. ワイルドカード（`*`）を使うときは対象が想定通りか先に `ls` で確認する．
3. 管理者権限の `sudo rm` は原則使わず，本当に必要なときだけ使う．

---

## 1-5. よく使う実践コマンド（Optional）

### `rsync`（高速・差分コピー）

`rsync` は，ファイルを差分で同期できるコマンドです．  
バックアップや，ローカル-リモート間の転送でよく使います．

```bash
rsync -avh ./data/ ./backup/data/
```

- `-a`: 属性を保って再帰コピー
- `-v`: 詳細表示
- `-h`: 人が読みやすい単位で表示

IPアドレス指定でマシン間転送する例（SSH経由）:

```bash
# このマシン -> リモートマシン
rsync -avh ./data/ user@192.168.1.10:/home/user/data/

# リモートマシン -> このマシン
rsync -avh user@192.168.1.10:/home/user/data/ ./data_from_remote/
```

- `user@192.168.1.10`: リモートのユーザー名とIPアドレス
- `:` の右側がリモート側パス

### `aria2c -x10 -s10 -k1M`（高速ダウンロード）

`aria2c` は分割ダウンロード対応のCLIツールです．

```bash
aria2c -x10 -s10 -k1M "https://example.com/large_file.zip"
```

- `-x10`: 1サーバーあたり最大10接続
- `-s10`: 10分割で取得
- `-k1M`: 1MB単位で分割

大きいファイルを安定して速く落としたいときに有効です．

### `tmux`（ターミナル多重化）

`tmux` を使うと，1つのSSH/ターミナル接続内で複数セッションを管理できます．  
接続が切れても作業を継続しやすく，長時間ジョブに向いています．

```bash
tmux new -s work
```

- `new -s work`: `work` という名前で新規セッション開始
- ctrl + b, d: セッションをデタッチ（切り離す）
- ctrl + b, w: セッション一覧を表示，↑/↓で選択してEnterでアタッチ（再接続）

### `sudo`（管理者権限で実行）

`sudo` は管理者権限が必要なコマンドを一時的に実行するために使います．

```bash
sudo apt update
sudo apt install git
```

注意:

- 必要なときだけ使う
- コマンド内容を理解してから実行する
- コピーしたコマンドをそのまま `sudo` で実行しない

### `df`（ディスク使用量の確認）

`df` はファイルシステム全体の空き容量を確認するコマンドです．

```bash
df -h
```

- `-h`: GB/MBなど読みやすい単位で表示
- 容量不足のトラブル切り分けで最初に確認すると良い

---

## 1-6. シェル設定ファイル（`~/.zshrc` / `~/.bashrc`）（Optional）

シェル起動時に読み込まれるユーザー設定ファイルです．  
エイリアス，環境変数，PATH追加などをここに書くと，毎回自動で反映されます．

使い分け:

- macOS標準（zsh）: `~/.zshrc`
- Ubuntu/WSL標準（bash）: `~/.bashrc`

基本操作:

```bash
# 内容確認
cat ~/.zshrc   # bashの場合は ~/.bashrc

# 編集（好きなエディタでOK）
code ~/.zshrc  # bashの場合は ~/.bashrc

# 変更を現在のシェルへ反映
source ~/.zshrc  # bashの場合は ~/.bashrc
```

よく使う設定例:

```bash
# エイリアス
alias ll='ls -la'
alias gs='git status'

# PATH追加（例: ローカルbin）
export PATH="$HOME/.local/bin:$PATH"
```

ポイント:

- 設定を保存しただけでは現在のターミナルには反映されない
- `source` で即時反映するか，ターミナルを再起動する
- 文法ミスがあるとシェル起動時にエラーになるため，少しずつ追記して確認する
