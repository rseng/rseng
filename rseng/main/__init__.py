"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from rseng.main.taxonomy import Taxonomy
from rseng.main.criteria import CriteriaSet
from rseng.main.templates import get_template
from rseng.utils.file import write_file

from datetime import datetime
from jinja2 import Template
import logging
import os
import re
import sys

bot = logging.getLogger("rse.main")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class ResearchSoftware:
    """The Research Engineering client will load current taxonomy and criteria
       for research software, and generate documentation files for them.
    """

    def __init__(self, version=None):
        """create a software repository. We take a config file, which should
           sit at the root of the repository, and then parse the subfolders
           accordingly.
        """
        self.taxonomy = Taxonomy(version=version)
        self.criteria = CriteriaSet(version=version)

    def export_taxonomy_markdown(
        self, outdir=None, template="taxonomy-metadata-template.md", force=False
    ):
        """Given an output directory and a template name, export a set of
           markdown files for the entire taxonomy
        """
        # If output folder not provided, assume _taxonomy in $PWD
        outdir = outdir or "_taxonomy"
        template = get_template(template)

        # If the output file exists and force is false, exit early
        if not force and os.path.exists(outdir):
            sys.exit(f"{outdir} exists, use --force to overwrite.")
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        # Flatten the tree, print each node to file
        files = []
        for path, node in self.taxonomy.flatten().items():
            instance = Template(template)
            result = instance.render(
                name=node.get("name", ""),
                updated_at=now,
                uid=node.get("uid", ""),
                example=node.get("example"),
                content=path,
            )
            output = os.path.join(outdir, "%s.md" % node.get("uid"))
            write_file(output, result)
            files.append(output)

        return files

    def export_criteria_markdown(
        self, outdir, template="criteria-metadata-template.md", force=False
    ):
        """Given an output directory and a template name, export a set of
           markdown files for each criteria
        """
        # If output folder not provided, assume _taxonomy in $PWD
        outdir = outdir or "_criteria"
        template = get_template(template)

        # If the output file exists and force is false, exit early
        if not force and os.path.exists(outdir):
            sys.exit(f"{outdir} exists, use --force to overwrite.")
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        files = []
        for criteria in self.criteria:
            instance = Template(template)
            result = instance.render(
                name=criteria.question,
                updated_at=now,
                uid=criteria.uid,
                options=criteria.options,
            )
            output = os.path.join(outdir, "%s.md" % criteria.uid)
            write_file(output, result)
            files.append(output)

        return files