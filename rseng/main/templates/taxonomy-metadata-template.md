---
name:  "{{ name }}"
date: "{{ updated_at }}"
uid: "{{ uid }}"
level: "{{ path }}"
{% if example %}example: "{{ example }}" {% endif %}
---

{{ content }}
