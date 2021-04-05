# Kyopro Encyclopedia of Algorithms (ア辞典)

これは競プロの知見を収集するための査読付きの半共有 wiki である。
アルゴリズムについての説明が中心となっている。なお、データ構造については [scrapbox.io/data-structures](https://scrapbox.io/data-structures/) (通称: デ wiki) を利用するのがよいだろう。

個人ブログの記事として情報を書くと属人性が高すぎ、古い記事のメンテのコストが高く、記事が不正確なまま残りやすいという問題があった。一方で誰でも自由に編集できる共有 wiki であると属人性が低すぎ、誰が書いたのかが分かりにくいため適切なクレジットが行なわれず、また記事の正確性も担保されないという問題があった。
そこでこの半共有 wiki は、GitHub 上のプルリクエストとレビュープロセスという管理形態を用いて、これらの問題の解決を目指している。
もし興味があれば [kmyk/algorithm-encyclopedia](https://github.com/kmyk/algorithm-encyclopedia) から編集に参加してほしい。

<hr>

<dl>
{% assign sorted_algorithms = site.algorithms | sort: "title" %}
{% for entry in sorted_algorithms %}
    {% unless entry.tenkei %}
        {% assign entry_id = entry.url | split: "/" | last | split: "." | first %}
        <dt id="{{ entry_id }}">
            {% if entry.algorithm.level %}
                <span style="font-style: normal;" class="rating-color-{{ entry.algorithm.level }}">&#x25C9;</span>
            {% endif %}
            {% if entry.draft %}
                {{ entry.title }}
            {% else %}
                <a href="{{ entry.url | relative_url }}">{{ entry.title }}</a>
            {% endif %}
            {% assign aliases_size = entry.algorithm.aliases | size %}
            {% if aliases_size != 0 %}
                <small>({{ entry.algorithm.aliases | join: "; " }})</small>
            {% endif %}

            {% if entry.draft %}
                <a href="#{{ entry_id }}" class="draft-link">{% octicon link height:16 %}</a>
                {% for url in entry.draft_urls %} <a href="{{ url }}" class="draft-link-external">{% octicon link-external height:16 %}</a>{% endfor %}
            {% endif %}
        </dt>
        <dd>
            {% capture algorithm_data %}
                {% if entry.algorithm.input %}<dt>input</dt><dd>{{ entry.algorithm.input }}</dd>{% endif %}
                {% if entry.algorithm.pre_condition %}<dt>pre-condition</dt><dd>{{ entry.algorithm.pre_condition }}</dd>{% endif %}
                {% if entry.algorithm.output %}<dt>output</dt><dd>{{ entry.algorithm.output }}</dd>{% endif %}
                {% if entry.algorithm.post_condition %}<dt>post-condition</dt><dd>{{ entry.algorithm.post_condition }}</dd>{% endif %}
                {% if entry.algorithm.condition %}<dt>condition</dt><dd>{{ entry.algorithm.condition }}</dd>{% endif %}
                {% if entry.algorithm.time_complexity %}<dt>time complexity</dt><dd>{{ entry.algorithm.time_complexity }}</dd>{% endif %}
                {% if entry.algorithm.space_complexity %}<dt>space complexity</dt><dd>{{ entry.algorithm.space_complexity }}</dd>{% endif %}
            {% endcapture %}
            {% assign stripped_algorithm_data = algorithm_data | strip %}
            {% if entry.draft and stripped_algorithm_data != "" %}
                <details class="algorithm-index-details">
                    <summary>
                        {{ entry.description }}
                    </summary>
                    <div class="algorithm-data">
                        <dl>
                            {{ algorithm_data }}
                        </dl>
                    </div>
                </details>
            {% else %}
                {{ entry.description }}
            {% endif %}
        </dd>
    {% endunless %}
{% endfor %}
</dl>

<div class="footer-links">
    <a href="{{ "/tenkei" | relative_url }}">典型テク版</a> /
    <a href="{{ site.github.repository_url }}">GitHub repository</a>
</div>
