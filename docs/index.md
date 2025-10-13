# Welcome

A place for my future self to quickly get back up to speed (and hopefully be useful to others).

## Recently Updated

{% set sorted_pages = pages | sort(attribute='meta.git_revision_date_localized', reverse=True) %}
{% for page in sorted_pages[:10] %}
{% if page.title != "Home" and not page.is_index %}
- **[{{ page.title }}]({{ page.url }})** - {{ page.meta.git_revision_date_localized if page.meta.git_revision_date_localized else "Recently" }}
{% endif %}
{% endfor %}
