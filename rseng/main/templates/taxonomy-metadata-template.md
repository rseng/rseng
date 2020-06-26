---
name:  "{{ name }}"
date: "{{ updated_at }}"
uid: "{{ uid }}"
level: "{{ path }}"
color: "{{ color }}"
{% if example %}example: "{{ example }}" {% endif %}
---

{{ content }}
