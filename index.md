# Kyopro Encyclopedia of Algorithms and Data Structures

<dl>
{% for entry in site.entries %}
<dt><a href="{{ site.baseurl }}{{ entry.url }}">{{ entry.title }}</a></dt>
<dd>{{ entry.description }}</dd>
{% endfor %}
</dl>
