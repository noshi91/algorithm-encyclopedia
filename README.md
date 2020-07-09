# Kyopro Encyclopedia of Algorithms

## これなに

競プロ用のアルゴリズムの解説を集めた百科辞典を目指しているサイトです。

### 内容の方針

-   想定読者: AtCoder 黄色以上
-   具体例を列挙して察してもらうだけは避ける。数学的な証明を書いていきたい
-   できるだけ他のページには依存しない

### なぜ GitHub Pages なのか

コンテンツを GitHub 上で管理する半 wiki 形式です。このため、

-   プルリクエスト経由で、誰でも自由に記事の追加や修正を提案できるが、
-   プルリクエストのマージには承認が必要であり、記事の内容が保証される。
-   また、修正やレビューの過程がコミットログやレビューコメントなどの形で残る。

などのメリットがあります。
デメリットとしては、GitHub の制約により、レビュー時の数式の表示がしんどいことが挙げられます。

他の形式の場合、ブログのような個人的なメディアで記事を書くと古い記事が時代遅れになったまま残りがちであり、編集がまったく自由な共有 wiki で管理すると著者や内容の質が曖昧になりがちです。これらの間を選ぶことでそれぞれの持つ問題を解決することを目標としています。

## Contribution

### 手元でのテスト

``` console
$ sudo apt install ruby-all-dev ruby-bundler
$ bundle install --path .vendor/bundle
$ bundle exec jekyll serve --incremental
# open http://127.0.0.1:4000
```

### 記事の追加

他の記事を見ながら適当にしてください。

[front matter](http://jekyllrb-ja.github.io/docs/front-matter/) に書くべき情報は以下の通りです。

-   `layout`: 常に `entry`
-   `author`: その記事を書いた人の名前 (AtCoder ID)
-   `reviewers` (空欄可): その記事をレビューした人たちの名前 (AtCoder ID)
-   `date`: その記事を初めて書いた日時 ([ISO 8691](https://ja.wikipedia.org/wiki/ISO_8601) で秒まで)。`$ date --iso-8601=seconds` を実行するとよい。例: `2020-07-09T00:00:00+09:00`
-   `updated_at` (空欄可): その記事を最後に修正した日時 ([ISO 8691](https://ja.wikipedia.org/wiki/ISO_8601) で秒まで)
-   `tags` (空欄可): タグの列
-   `algorithm` (空欄可): アルゴリズムについての概要
    -   `input` (空欄可): アルゴリズムへの入力
    -   `output` (空欄可): アルゴリズムからの出力
    -   `time_complexity` (空欄可): アルゴリズムの時間計算量
    -   `space_complexity` (空欄可): アルゴリズムの空間計算量
    -   `aliases` (空欄可): アルゴリズムの別名の列
-   `description`: アルゴリズムの概要。「（ここにアルゴリズムの名前が入る）とは、（ここにアルゴリズムの概要が入る）というアルゴリズムである。」という形の文から初めて数文ぐらいで書く感じで
-   `draft` (省略可): これが存在するとトップページからのリンクが貼られません。
