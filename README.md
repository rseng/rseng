# Research Software Engineering

[![PyPI version](https://badge.fury.io/py/rseng.svg)](https://badge.fury.io/py/rseng)

Criteria and taxonomy for research software engineering (rseng).

## Overview

This repository serves a taxonomy and criteria for research software,
intended to be used with the [research software encyclopedia](https://github.com/rseng/rse).
The two are maintained separately for development, and because it might
be the case that the criteria and taxonomy would want to be used separately
from the encyclopedia.

## Usage

Usage of the library includes programmatic (within Python or command line) 
interaction with criteria or taxonomy.

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

And further interact with the CriteriaSet:

```python
print(cset.export()) # You can also define a "filename" and/or "sep" here.
RSE-research-intention	Is the software intended for research?	yes,no
RSE-domain-intention	Is the software intended for a particular domain?	yes,no
RSE-question-intention	Was the software created with intention to solve a research question?	yes,no
RSE-citation	Has the software been cited?	yes,no
RSE-usage	Has the software been used by researchers?	yes,no
RSE-absence	Would taking away the software be a detriment to research?	yes,no
```

**under development**

## License

 * Free software: MPL 2.0 License
