---
name: Annotate Criteria
about: Select this template to annotate criteria for a software repository
title: "[CRITERIA]"
labels: 'criteria'
assignees: ''
---

## Repository

<!-- write the name of the repository here-->

## Criteria

<!-- check one or more boxes for criteria to indicate "yes" -->

{% for item in items %}
 - [ ] criteria-{{ item }}{% endfor %}

