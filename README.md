# Research Software Engineering

[![PyPI version](https://badge.fury.io/py/rseng.svg)](https://badge.fury.io/py/rseng)
[![https://img.shields.io/badge/rseng-project-purple](https://img.shields.io/badge/rseng-project-purple)](https://rseng.github.io/) [![https://good-labs.github.io/greater-good-affirmation/assets/images/badge.svg](https://good-labs.github.io/greater-good-affirmation/assets/images/badge.svg)](https://good-labs.github.io/greater-good-affirmation)

Criteria and taxonomy for research software engineering (rseng).

![docs/assets/img/taxonomy/taxonomy-circle.png](docs/assets/img/taxonomy/taxonomy-circle.png)

## Overview

This repository serves a taxonomy and criteria for research software,
intended to be used with the [research software encyclopedia](https://github.com/rseng/rse).
The two are maintained separately for development, and because it might
be the case that the criteria and taxonomy would want to be used separately
from the encyclopedia.

## Usage

Usage of the library includes programmatic (within Python or command line) 
interaction with criteria or taxonomy, and generation of output files.

 - [Criteria](#criteria)
 - [Taxonomy](#taxonomy)
 - [Generate](#generate)

### Criteria

For usage within Python, you will first want to instantiate a `CriteriaSet`. If you
don't provide a default file, the library default will be used.

```python
from rseng.main.criteria import CriteriaSet
cset = CriteriaSet()
# [CriteriaSet:6]
```

You can then see questions loaded. Each has a unique id that gives a sense of
what is being asked:

```python
cset.criteria                                                                       
{'RSE-research-intention': <rseng.main.criteria.base.Criteria at 0x7f3d2e85d410>,
 'RSE-domain-intention': <rseng.main.criteria.base.Criteria at 0x7f3d2dab8490>,
 'RSE-question-intention': <rseng.main.criteria.base.Criteria at 0x7f3d2dab8910>,
 'RSE-citation': <rseng.main.criteria.base.Criteria at 0x7f3d2db34810>,
 'RSE-usage': <rseng.main.criteria.base.Criteria at 0x7f3d2db340d0>,
 'RSE-absence': <rseng.main.criteria.base.Criteria at 0x7f3d2db34850>}
```

You can inspect any particular criteria:

```python
cset.criteria['RSE-usage']
<rseng.main.criteria.base.Criteria at 0x7f3d2db340d0>

cset.criteria['RSE-usage'].uid
# 'RSE-usage'

cset.criteria['RSE-usage'].question
# 'Has the software been used by researchers?'

cset.criteria['RSE-usage'].options
# ['yes', 'no']
```

And further interact with the CriteriaSet, for example export to a tabular file:

```python
print(cset.export()) # You can also define a "filename" and/or "sep" here.
RSE-research-intention	Is the software intended for research?	yes,no
RSE-domain-intention	Is the software intended for a particular domain?	yes,no
RSE-question-intention	Was the software created with intention to solve a research question?	yes,no
RSE-citation	Has the software been cited?	yes,no
RSE-usage	Has the software been used by researchers?	yes,no
RSE-absence	Would taking away the software be a detriment to research?	yes,no
```

or iterate through the criteria, or get a list of all of them.

```python
> list(cset)
[[Criteria:RSE-research-intention,Is the software intended for research?],
 [Criteria:RSE-domain-intention,Is the software intended for a particular domain?],
 [Criteria:RSE-question-intention,Was the software created with intention to solve a research question?],
 [Criteria:RSE-citation,Has the software been cited?],
 [Criteria:RSE-usage,Has the software been used by researchers?],
 [Criteria:RSE-absence,Would taking away the software be a detriment to research?]]

for criteria in cset:
    print(criteria)

[Criteria:RSE-research-intention,Is the software intended for research?]
[Criteria:RSE-domain-intention,Is the software intended for a particular domain?]
[Criteria:RSE-question-intention,Was the software created with intention to solve a research question?]
[Criteria:RSE-citation,Has the software been cited?]
[Criteria:RSE-usage,Has the software been used by researchers?]
[Criteria:RSE-absence,Would taking away the software be a detriment to research?]
```

### Taxonomy

The taxonomy is interacted with in a similar fashion.

```python
from rseng.main.taxonomy import Taxonomy
tax = Taxonomy()
```

It will show you the total number of nodes (nested too):


```python
from rseng.main.taxonomy import Taxonomy
tax = Taxonomy()
#  [Taxonomy:24]
```

Validation happens as the default file is loaded. Akin to criteria, the files
are located in [rseng/main/taxonomy](rseng/main/taxonomy) in yaml format, and
are dated. You can quickly print an easily viewable, human understandable
version of the tree:

```python
for name in tax.flatten(): 
   ...:     print(name) 
   ...:                                                                                                                                                                                                                      
Software to directly conduct research >> Domain-specific software >> Domain-specific hardware
Software to directly conduct research >> Domain-specific software >> Domain-specific optimized software
Software to directly conduct research >> Domain-specific software >> Domain-specific analysis software
Software to directly conduct research >> General software >> Numerical libraries
Software to directly conduct research >> General software >> Data collection
Software to directly conduct research >> General software >> Visualization
Software to support research >> Explicitly for research >> Workflow managers
Software to support research >> Explicitly for research >> Interactive development environments for research
Software to support research >> Explicitly for research >> Provenance and metadata collection tools
Software to support research >> Used for research but not explicitly for it >> Databases
Software to support research >> Used for research but not explicitly for it >> Application Programming Interfaces
Software to support research >> Used for research but not explicitly for it >> Frameworks
Software to support research >> Incidentally used for research >> Operating systems
Software to support research >> Incidentally used for research >> Personal scheduling and task management
Software to support research >> Incidentally used for research >> Version control
Software to support research >> Incidentally used for research >> Text editors and integrated development environments
Software to support research >> Incidentally used for research >> Communication tools or platforms
```

### Generate

After you install rseng, the `rseng` executable should be in your path.
You can generate output files for the taxonomy or critiera to a folder
oath that doesn't exist yet. For example, to generate the markdown
files for the static documentation for each of the taxonomy and criteria
we do:

#### Markdown Jekyll Pages

```bash
# rseng generate <type>   <path>          <version>
$ rseng generate taxonomy docs/_taxonomy
docs/_taxonomy/RSE-taxonomy-domain-hardware.md
docs/_taxonomy/RSE-taxonomy-optimized.md
docs/_taxonomy/RSE-taxonomy-analysis.md
docs/_taxonomy/RSE-taxonomy-numerical libraries.md
docs/_taxonomy/RSE-taxonomy-data-collection.md
docs/_taxonomy/RSE-taxonomy-visualization.md
docs/_taxonomy/RSE-taxonomy-workflow-managers.md
docs/_taxonomy/RSE-taxonomy-ide-research.md
docs/_taxonomy/RSE-taxonomy-provenance-metadata-tools.md
docs/_taxonomy/RSE-taxonomy-databases.md
docs/_taxonomy/RSE-taxonomy-application-programming-interfaces.md
docs/_taxonomy/RSE-taxonomy-frameworks.md
docs/_taxonomy/RSE-taxonomy-operating-systems.md
docs/_taxonomy/RSE-taxonomy-personal-scheduling-task-management.md
docs/_taxonomy/RSE-taxonomy-version-control.md
docs/_taxonomy/RSE-taxonomy-text-editors-ides.md
docs/_taxonomy/RSE-taxonomy-communication-tools.md
```

The default version generated for each is "latest" but you can add another
version as the last argument to change that. Here is generation
of the criteria, showing using latest:

```bash
# rseng generate <type>   <path>          <version>
$ rseng generate criteria docs/_criteria
docs/_criteria/RSE-research-intention.md
docs/_criteria/RSE-domain-intention.md
docs/_criteria/RSE-question-intention.md
docs/_criteria/RSE-citation.md
docs/_criteria/RSE-usage.md
docs/_criteria/RSE-absence.md
```

#### Intended for Visualization (json)

You can also generate a (non flat) version of the taxonomy, specifically a json
file that plugs easily into the d3 hierarchy plots.

```
# rseng generate taxonomy-json <filename>
$ rseng generate taxonomy-json taxonomy.json
```


#### GitHub Issue Templates

If you want an issue template that can work with a GitHub workflow
(both in your software repository) to items via GitHub, both can be produced
with updated criteria or taxonomy items via:

```bash
$ rseng generate criteria-annotation-template 
```

And the template will be generated (with default filename) in the present working
directory:

```markdown
---
name: Annotate Criteria
about: Select this template to annotate criteria for a software repository
title: "[CRITERIA]"
labels: ''
assignees: ''
---

## Repository

<!-- write the name of the repository here-->

## Criteria

<!-- check boxes for criteria to indicate "yes" -->


 - [ ] criteria-RSE-research-intention
 - [ ] criteria-RSE-domain-intention
 - [ ] criteria-RSE-question-intention
 - [ ] criteria-RSE-citation
 - [ ] criteria-RSE-usage
 - [ ] criteria-RSE-absence
```

You can do the same for a GitHub issues taxonomy annotation template:

```bash
$ rseng generate taxonomy-annotation-template 
```
```
---
name: Annotate Taxonomy
about: Select this template to annotate software with taxonomy categories
title: "[TAXONOMY]"
labels: ''
assignees: ''
---

## Repository

<!-- write the name of the repository here-->

## Taxonomy

<!-- check one or more boxes for categories to indicate "yes" -->


 - [ ] RSE-taxonomy-domain-hardware
Software to directly conduct research >> Domain-specific software >> Domain-specific hardware

 - [ ] RSE-taxonomy-optimized
Software to directly conduct research >> Domain-specific software >> Domain-specific optimized software

 - [ ] RSE-taxonomy-analysis
Software to directly conduct research >> Domain-specific software >> Domain-specific analysis software

 - [ ] RSE-taxonomy-numerical libraries
Software to directly conduct research >> General software >> Numerical libraries

 - [ ] RSE-taxonomy-data-collection
Software to directly conduct research >> General software >> Data collection

 - [ ] RSE-taxonomy-visualization
Software to directly conduct research >> General software >> Visualization

 - [ ] RSE-taxonomy-workflow-managers
Software to support research >> Explicitly for research >> Workflow managers

 - [ ] RSE-taxonomy-ide-research
Software to support research >> Explicitly for research >> Interactive development environments for research

 - [ ] RSE-taxonomy-provenance-metadata-tools
Software to support research >> Explicitly for research >> Provenance and metadata collection tools

 - [ ] RSE-taxonomy-databases
Software to support research >> Used for research but not explicitly for it >> Databases

 - [ ] RSE-taxonomy-application-programming-interfaces
Software to support research >> Used for research but not explicitly for it >> Application Programming Interfaces

 - [ ] RSE-taxonomy-frameworks
Software to support research >> Used for research but not explicitly for it >> Frameworks

 - [ ] RSE-taxonomy-operating-systems
Software to support research >> Incidentally used for research >> Operating systems

 - [ ] RSE-taxonomy-personal-scheduling-task-management
Software to support research >> Incidentally used for research >> Personal scheduling and task management

 - [ ] RSE-taxonomy-version-control
Software to support research >> Incidentally used for research >> Version control

 - [ ] RSE-taxonomy-text-editors-ides
Software to support research >> Incidentally used for research >> Text editors and integrated development environments

 - [ ] RSE-taxonomy-communication-tools
Software to support research >> Incidentally used for research >> Communication tools or platforms
```

Example in the wild include [this one for criteria](https://github.com/rseng/software/blob/master/.github/ISSUE_TEMPLATE/annotate-criteria.md) and [this one for the taxonomy](https://github.com/rseng/software/blob/master/.github/ISSUE_TEMPLATE/annotate-taxonomy.md).


## License

 * Free software: MPL 2.0 License
