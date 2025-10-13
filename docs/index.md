# Welcome

A place for my future self to quickly get back up to speed (and hopefully be useful to others).

## All Pages

{% for nav_item in navigation.pages %}
{% if nav_item.title != "Home" %}
- [{{ nav_item.title }}]({{ nav_item.url }})
{% endif %}
{% endfor %}
