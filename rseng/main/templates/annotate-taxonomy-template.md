---
name: Annotate Taxonomy
about: Select this template to annotate software with taxonomy categories
title: "[TAXONOMY]"
labels: 'taxonomy'
assignees: ''
---

## Repository

<!-- write the name of the repository here-->

## Taxonomy

<!-- check one or more boxes for categories to indicate "yes" -->

{% for item in items %}
 - [ ] {{ item }}{% endfor %}

