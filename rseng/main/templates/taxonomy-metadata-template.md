---
name:  "{{ name }}"
date: "{{ updated_at }}"
uid: "{{ uid }}"
{% if example %}example: "{{ example }}" {% endif %}
---

{{ content }}
