# 4-mypage

`README_sections/01-03` の内容（CLI / Git / VSCode）を使って，最小Webページを作るサンプルです．

## ファイル構成

- `index.html`: ページ本体
- `style.css`: 見た目
- `script.js`: テーマ切替と更新時刻表示

## ローカル確認

```bash
cd sample_projects/4-mypage
python3 -m http.server 8000
```

ブラウザで `http://localhost:8000` を開いて確認します．

## Git運用例

```bash
git add .
git commit -m "add mypage sample"
```

必要に応じてGitHub Pagesで公開できます．
