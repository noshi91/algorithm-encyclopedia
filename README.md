# Kyopro Encyclopedia of Algorithms and Data Structures

## これなに

競プロ用のアルゴリズムの解説を集めた百科辞典を目指します。
Stanford Encyclopedia of Philosophy リスペクトです。

### なにがうれしいのか

GitHub 上で管理する半 wiki 形式である。このため、

-   プルリクエスト経由で、誰でも自由に記事の追加や修正を提案できるが、
-   プルリクエストのマージには承認が必要であり、記事の内容が保証される。
-   また、修正やレビューの過程がコミットログやレビューコメントなどの形で残る。

ブログ記事として書くと古い記事が時代遅れになったまま残りがちだったり、あまり丁寧でない共有 wiki だと誰が書いたのかが曖昧になりがちという問題があるが、これらを解決したい。

## ローカルでのテスト

``` console
$ sudo apt install ruby-all-dev ruby-bundler
$ bundle install --path .vendor/bundle
$ bundle exec jekyll serve --incremental
# open http://127.0.0.1:4000
```

## 記事の追加

他の記事を見ながら適当にしましょう。

[front matter](http://jekyllrb-ja.github.io/docs/front-matter/) に書くべき情報は以下の通りです。

-   `layout`: 常に `entry`
-   `author`: その記事を書いた人の名前 (AtCoder ID)
-   `reviewers` (省略可): その記事をレビューした人たちの名前 (AtCoder ID)
-   `date`: その記事を初めて書いた日時 ([ISO 8691](https://ja.wikipedia.org/wiki/ISO_8601) で秒まで)。`$ date --iso-8601=seconds` を実行するとよい。例: `2020-07-09T00:00:00+09:00`
-   `updated_at` (省略可): その記事を最後に修正した日時 ([ISO 8691](https://ja.wikipedia.org/wiki/ISO_8601) で秒まで)
-   `tags` (省略可): タグの列
-   `algorithm` (省略可): アルゴリズムについての概要
    -   `input` (省略可): アルゴリズムへの入力
    -   `output` (省略可): アルゴリズムからの出力
    -   `time_complexity` (省略可): アルゴリズムの時間計算量
    -   `space_complexity` (省略可): アルゴリズムの空間計算量
    -   `aliases` (省略可): アルゴリズムの別名の列
-   `description`: アルゴリズムの概要。「（ここにアルゴリズムの名前が入る）とは、（ここにアルゴリズムの概要が入る）というアルゴリズムである。」という形の一文ぐらいでよい
