---
name:  "{{ name }}"
date: "{{ updated_at }}"
uid: "{{ uid }}"
path: "{{ path }}"
{% if example %}example: "{{ example }}" {% endif %}
---

{{ content }}
