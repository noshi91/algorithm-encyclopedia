# CONTRIBUTING.md

## 編集方法について

### 記事を修正するには

修正方法が明らかなものならプルリクエストを送ってください。
簡単には修正できないものなら issue を立ててください。
それぞれページの右下の「Edit this page」「Report issues」というリンクを使うと便利です。


### 記事に加筆するには

プルリクエストを送ってください。
そうすることで記事がより良くなるのであれば、記事の元々の文章を削除したり構成を変更したりしても構いません。

プルリクエストを送る際には、過去のすべての authors と reviewers にメンションを飛ばしてください。


### 記事を追加するには (概要のみ)

[トップページ](https://noshi91.github.io/algorithm-encyclopedia/) の目次にのみ項目を追加する場合は以下のようにします。

1.  [_algorithms/](https://github.com/kmyk/algorithm-encyclopedia/tree/gh-pages/_algorithms) ディレクトリの中に Markdown ファイルを追加する。
    -   [template.md](https://raw.githubusercontent.com/kmyk/algorithm-encyclopedia/gh-pages/template.md) をコピペしてくればよい
1.  追加した Markdown ファイルを編集する。
1.  プルリクエストを送る。


### 記事を追加するには (本文含む)

個別の記事ページ ([例](https://noshi91.github.io/algorithm-encyclopedia/monotone-minima)) を追加する場合は以下のようにします。

1.  対応する issue を作る。
    -   「[ページを追加する](https://github.com/online-judge-tools/verification-helper/issues/new?template=algorithm.md)」のテンプレートを使う。中身は空でよい
    -    衝突を防ぐため、ページ作成の作業をすることを宣言するのがよい
1.  上記の「記事を追加する (概要のみ)」と同様にして、トップページの目次に項目を追加する。
1.  対応する項目の Markdown ファイルに本文を追加する。
1.  プルリクエストを送る。


### authors と reviewers

記事には authors と reviewers が表示されます。
ある記事のある変更について、author とはその変更を書いた人のことであり、reviewer とはその変更をレビューした人のことです。

authors と reviewers を表示することは、その人たちがその記事への貢献をしたことを読者に伝える意味があります。
authors や reviewers として名前を乗せることは、基本的には authors や reviewers にとって利益 (つまり、読者から「あの人が書いてくれた記事は参考になるなあ」などの良い印象を持たれる) になります。
ただし、記事に重大な問題があった場合などには不利益 (つまり、読者から「あの人の書いた記事は不正確で困るなあ」などの悪い印象を持たれる) になる可能性もあることは認識しておくべきでしょう。

authors や reviewers に名前が乗っていることは、その人たちがその記事の内容全体に責任を負っていることは意味しません。
その人たちが責任を負うのは、その人たちが関与した変更のみです。
誤字や脱字などの自明な修正であれば、authors や reviewers への確認なしに勝手に記事が修正されるかもしれません。
authors や reviewers と連絡が取れない場合は、その人たちの確認なしに非自明な内容の追加や削除がされるかもしれません。
後から記事が変更されたとき、それによって発生した問題によって元々の authors や reviewers が不利益を被ることを防ぐために、表示は「その記事の authors / reviewers」ではなく「その記事ある変更の authors / reviewers」という形でなされます。

完全な編集履歴は commit log から閲覧することができます。
しかし、GitHub 上へ移動して commit log を確認するのは面倒であり、たいていの読者はこれを確認しないでしょう。
authors と reviewers の表示は、commit log を確認しない読者に対しても、誰がその記事に貢献したのかを分かりやすく伝える効果があります。


### メタデータの仕様

[front matter](http://jekyllrb-ja.github.io/docs/front-matter/) に書くべき情報は以下の通りです。

-   `layout`: 常に `entry`
-   `changelog` (辞書の配列): そのページの更新履歴
    -   `summary`: その更新の内容の概要
    -   `authors`: その更新をした人たちの名前 (AtCoder ID)
    -   `reviewers` (空欄可): その更新をレビューした人たちの名前 (AtCoder ID)
    -   `date`: その更新をした日時 ([ISO 8601](https://ja.wikipedia.org/wiki/ISO_8601) で秒まで) (例: `2020-07-09T00:00:00+09:00`)。`$ date --iso-8601=seconds` を実行するとよい。時間や分や秒は適当でも (たとえばすべて 0 でも) 構わない。
-   `algorithm` (空欄可): アルゴリズムについての概要
    -   `input` (空欄可): アルゴリズムへの入力
    -   `output` (空欄可): アルゴリズムからの出力
    -   `time_complexity` (空欄可): アルゴリズムの時間計算量
    -   `space_complexity` (空欄可): アルゴリズムの空間計算量
    -   `aliases` (空欄可): アルゴリズムの別名の列
    -   `level` (空欄可): アルゴリズムの知名度。難しさは判定しにくいので有名さ (競プロでどのくらいよく使われるか) を使う。「この色の人ならみんな知っていそうだな (主観)」という色を書く。赤でも知らなさそうなものは黒 (`black`) とする。
-   `description`: アルゴリズムの概要。「（ここにアルゴリズムの名前が入る）とは、（ここにアルゴリズムの概要が入る）というアルゴリズムである。」という形の文から初めて数文ぐらいで書くのがよい。KaTeX は使用可。HTML も使用可だがあまり推奨されない。
-   `draft` (省略可): これが `true` であるとトップページから記事ページへのリンクが貼られない。
-   `draft_urls` (省略可): 記事の本文の代わりになるリンク (複数可)


### 数式

数式には [KaTeX](https://katex.org/) が使えます。KaTeX が対応している関数の一覧は [Supported Functions](https://katex.org/docs/supported.html) にあります。

[コードブロック](https://docs.github.com/ja/github/writing-on-github/creating-and-highlighting-code-blocks)中で数式を利用したい場合は言語名に `plaintext-katex` を指定してください。


### AtCoder ID

Markdown 中に `<a class="handle">chokudai</a>` のように AtCoder ID を書くと、その AtCoder ID は highest の色で表示されます。
競技プログラマの名前を記述するときはこれを利用してください。

色の情報は [_sass/user-colors.scss](https://github.com/kmyk/algorithm-encyclopedia/blob/gh-pages/_sass/user-colors.scss) ファイルに CSS として保存されています。このファイルは [scripts/user-ratings.py](https://github.com/kmyk/algorithm-encyclopedia/blob/gh-pages/scripts/user-ratings.py) によって生成されます。定期的に `$ python3 scripts/user-ratings.py` を実行して色の情報のファイルを更新してください。


## 画像ファイル

[`assets/img/`](https://github.com/kmyk/algorithm-encyclopedia/tree/gh-pages/assets/img) に置いてください。
また、後から画像を修正する必要が発生したときのために、画像の編集方法を [`assets/img/README.md`](https://github.com/kmyk/algorithm-encyclopedia/tree/gh-pages/assets/img/README.md) に書いておいてください。

### ローカルでの記事の閲覧

ローカルで記事を閲覧するには、以下のコマンドを順に実行してください。HTTP サーバが建ち <http://127.0.0.1:4000/> から閲覧できます。

``` console
$ git clone https://github.com/noshi91/algorithm-encyclopedia
$ cd algorithm-encyclopedia
$ sudo apt install ruby-all-dev ruby-bundler
$ bundle install --path .vendor/bundle
$ bundle exec jekyll serve --incremental
```


### ローカルでのテストの実行

GitHub Actions を利用して、典型的なミスが機械的に検出されるよう設定されています。
このテストをローカルで実行するには、以下のコマンドを順に実行してください。

``` console
$ pip3 install -r scripts/requirements.txt
$ python3 scripts/lint.py
```

また `--fix` オプションを付けて実行 (`$ python3 scripts/lint.py`) すると自動で修正できるミスは自動で修正してくれます。

テスト ([`scripts/lint.py`](https://github.com/kmyk/algorithm-encyclopedia/blob/gh-pages/scripts/lint.py)) には気軽に変更を加えてしまって構いません。
このテストは記事を書く人の快適さを目的として用意されています。
記事の内容に制限をかけることはその手段でしかありません。
記事でなくテストの側が不適切であるためにテストが失敗になってしまっているときは、テストの側を修正して成功にしてください。
記事を書いている上で気付いた典型的なミス (例: `有向グラフ` を `有効グラフ` と typo してしまう) は、テストに検出処理を追加できそうなら追加しておいてください。


### 複製の公開

このリポジトリの fork を作ったあと、そのリポジトリで GitHub Pages を有効にしてください ([GitHub Pages サイトの公開元を設定する - GitHub Docs](https://docs.github.com/ja/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site))。fork では自動的には GitHub Pages が有効にならないことに注意してください。
実際に公開した例は <https://kmyk.github.io/algorithm-encyclopedia-staging/> にあります。

通常の GitHub 上では Markdown ファイル中の数式をプレビューできないという問題があるため、プルリクエストを出す際にはこのような複製を準備して完全な形のものを閲覧できるようにしておくとスムーズでしょう。

なお、GitHub Pages に公開された複製からは自動で <https://noshi91.github.io/algorithm-encyclopedia/> へのリダイレクトが発生するようになっています。
これは、本体のリポジトリの GitHub Pages とテスト用の複製の GitHub Pages との間での、どれが本体なのか分からないという混乱の発生を防ぐための措置です。
本体のリポジトリへリダイレクトされない完全な fork を作りたいときは、`_config.yml` や `CNAME` を編集することでこの挙動を修正できます。


## どのような内容についての記事が掲載されるか

### 記事が説明する対象の種類について

競技プログラミングに関連する知識であって、アルゴリズムや数学の知識を取り扱います。
そのような知識の例は以下のようになります。

-   個別のアルゴリズムやデータ構造
    -   例: Dijkstra 法
    -   例: 単体法
-   アルゴリズムやデータ構造の分類
    -   例: 動的計画法
    -   例: 線型計画法
-   アルゴリズム的な問題
    -   例: 巡回セールスマン問題
    -   例: 線型計画問題
-   個別の数学的対象
    -   例: ピーターセングラフ
-   数学的対象のクラス
    -   例: モノイド
    -   例: 単調な数列
-   数学的性質
    -   例: 線形性
    -   例: 数列の単調性
-   数学的事実
    -   例: 最小カット最大フロー定理

どれに含めればよいか分かりにくい対象もあります (たとえば「木の直径」は性質と見るべきか対象と見るべきか曖昧でしょう) が、そのような対象についての記事であってもかまいません。

データ構造については[データ構造Wiki](https://scrapbox.io/data-structures/) への寄稿も検討してみてください。

上記のものに含められないような知識については[典型テク版のページ](https://dic.kimiyuki.net/tenkei/)に隔離した形で掲載します。
そのような知識の例は以下のようになります。

-   考察テク
    -   例: 完全グラフや星グラフのような極端な場合を考えるとよい
-   典型パターン
    -   例: クエリ列を処理するときは逆から考えるとうまくいくことがある
-   実装テク
    -   例: 閉区間でなく半開区間を使うと実装が楽になる場合が多い
-   個別のプログラミング言語についての知識
    -   例: C++ の `std::cin` は何も考えずに使うと Codeforces では TLE することがある


### 記事が説明する対象の難易度や知名度について

基本的には、どんな難易度や知名度の知識についての記事であっても掲載します。
特に、実際の競プロではほとんど出現しないようなマイナーな知識についても積極的に掲載していく方針です。
最も記載したいものは「現在はほとんど知られていないが、将来的には典型となるであろう知識」です。

ただし、十分に広く知られておりかつ競プロに特有ではない知識 (例: 三角関数) についての記事は、内容次第ではメンテコストの都合から掲載を見合わせる可能性はあります。


## どのように記事を書くべきか

### 何について語っているかを明確にする

あなたが説明しようとしているものが何であるかについて、明確に説明してください。
たとえばそれが「あるひとつの具体的なアルゴリズム」であるのか「ある性質を満たすアルゴリズムの総称」であるのか「何らかの形の問題」であるのかについて自覚的に書いてください。

可能なら厳密な特徴付けを与えてください。
性質や利用方法や具体例は定義ではありません。
「条件 P を満たすものは A である」という説明では A を説明したことにはなりません。
「条件 Q を満たすものは A であり、条件 Q を満たさないものは A ではない」ということまで説明する必要があります。
すべてのアルゴリズムとデータ構造について、明確にそれが何であるかを特徴付けられるとは限りませんが、できる限り説明するようにしてください。具体例をいくつか列挙するだけにして正確なところは読者が察するのを期待するという書き方は避けてください。

たとえば「阪本さんとは誰ですか？」と聞かれたとき、どのように答えるのがよいでしょうか？
「かわいいです」とか「関西弁を話します」というのは答えになっていません。
「黒いねこです」という答えも不十分です。
黒いねこであることは坂本さんの代表的な性質のひとつかもしれませんが、黒いねこは坂本さんではありません。
「○○研究所で飼われているある黒猫です」のように個体を特定して答える必要があります。

たとえば「累積和とは何ですか？」と聞かれたときも同様です。
「配列上の区間の総和を求めることができます」というのは累積和の利用例のひとつでしかなく、累積和そのものの説明ではありません。
累積和を利用する問題をひとつ選んで例として紹介して「累積和はこのように使います」とするのでも同じです。まずは「a を数列とするとき、a に対する累積和とは、bᵢ = a₀ + a₁ + ⋯ + aᵢ₋₁ で定まるような数列 b のことである」のように説明してください。利用方法や具体例は定義ではありません。もちろん、その後に利用方法を説明する必要はありますし、具体例を挙げることは理解を助けるでしょう。


### それが何をするのかを明確にする

あなたが説明しようとしているものが何をするのかについて、明確に説明してください。
アルゴリズムについて説明する時は、そのアルゴリズムが「どのような問題を解くのか」を宣言してください。
あるいは「入力」「出力」「計算量」を明示してください。


### 他の事柄との関係を明確にする

あなたが説明しようとしているものが他のものとどのように関連しているかについて、説明を与えてください。
「関連項目」などの節を作り、その中に列挙するのでもよいでしょう。


### 意見を書くときはそれが誰の意見なのかを明確にする

事実と意見は区別してください。広く共有されているわけではない主観的な意見を書くときは、それが誰の意見なのかを明確にしてください。
特になにか過激な意見を主張したいときは、その意見はひとまず自分のブログに書き、「外部リンク」などの節の中から参照するのがよいでしょう。


### 他: 管理コストを下げる

-   他の記事に書かれた細部に直接依存することは避ける。記事同士を疎結合に保ち、ある記事の編集が他の記事に影響しないようにする。
-   リンクを張るときはリンク先の永続性に注意する。特に他人のブログ記事や競プロライブラリへのリンクを貼るときは [Internet Archive](https://archive.org/web/) によるスナップショットを取っておく ([Save Page Now - Wayback Machine](https://web.archive.org/save/))。
-   リンクを張るときはリンク先との関係が分かるようにする。例題を紹介するならば簡単な解説を書いておく。記事を紹介するならばなぜ他の記事でなくその記事が選ばれているのか分かるようにしておく。
-   ソースコードはそのままコピペして動くものを載せる。ソースコードの妥当性は簡単に検証できるようにしておく。
-   画像ファイルは後から他の人が修正しやすいような形式を選び、修正方法のドキュメントを残しておく。


## ライセンスについて

書かれたページは [Creative Commons Attribution 4.0 International License (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/) で公開されます。
