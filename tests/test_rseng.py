#!/usr/bin/env python
"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

import os
import sys
import pytest


def test_criteria(tmp_path):
    """test criteria sets
    """
    print("Testing Criteria Sets")
    from rseng.main.criteria import CriteriaSet

    cset = CriteriaSet()
    assert cset.count >= 6
    assert len(cset.criteria) >= 6
    assert cset.count == len(cset.criteria)
    for name, criteria in cset.criteria.items():
        assert name.startswith("RSE-")
        assert criteria.question
        assert criteria.uid == name
        assert criteria.export()
    assert cset.export()
    list(cset)
    for criteria in cset:
        print(criteria)


def test_taxonomy(tmp_path):
    """test taxonomy items
    """
    print("Testing Taxonomy items")
    from rseng.main.taxonomy import Taxonomy

    tax = Taxonomy()
    assert tax.count >= 24
    for name in tax.flatten():
        print(name)
    for name, item in tax.flatten().items():
        for key in ["uid", "name"]:
            assert key in item
