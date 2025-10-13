# Welcome

A place for my future self to quickly get back up to speed (and hopefully be useful to others).

## All Pages

{% for nav_item in nav %}
{% if nav_item.title and nav_item.title != "Home" %}
- [{{ nav_item.title }}]({{ nav_item.url }})
{% endif %}
{% endfor %}
