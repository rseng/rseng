"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from rseng.main.taxonomy import Taxonomy
from rseng.main.criteria import CriteriaSet
from rseng.main.templates import get_template
from rseng.utils.file import write_file, write_json

from datetime import datetime
from jinja2 import Template
from copy import deepcopy
import logging
import os
import sys

bot = logging.getLogger("rseng.main")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class ResearchSoftware:
    """The Research Engineering client will load current taxonomy and criteria
       for research software, and generate documentation files for them.
    """

    def __init__(self, version="latest"):
        """create a software repository. We take a config file, which should
           sit at the root of the repository, and then parse the subfolders
           accordingly.
        """
        self.taxonomy = Taxonomy(version=version)
        self.criteria = CriteriaSet(version=version)

    # Taxonomy Export

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
                path=path,
                updated_at=now,
                uid=node.get("uid", ""),
                example=node.get("example"),
                content=path,
            )
            output = os.path.join(outdir, "%s.md" % node.get("uid"))
            write_file(output, result)
            files.append(output)

        return files

    def export_taxonomy_json(self, outfile=None, force=False, size=12):
        """Given an output json file, export the taxonomy d3 data. In the future,
           sizes could be customized based on importance, etc.
        """
        outfile = outfile or "taxonomy.json"

        # If the output file exists and force is false, exit early
        if not force and os.path.exists(outfile):
            sys.exit(f"{outfile} exists, use --force to overwrite.")

        # Make a copy of nodes before editing
        tree = deepcopy(self.taxonomy.tree)
        for uid, node in self.taxonomy.nodes.items():
            node["size"] = size

        # Generate the tree in the typical d3.js format
        root = {"name": "root", "children": self.taxonomy.tree}

        # Restore original tree (without sizes)
        self.taxonomy.tree = tree
        return write_json(root, outfile)

    def export_taxonomy_annotation_template(
        self, outfile, template="annotate-taxonomy-template.md", force=False
    ):
        """Export a markdown template for a taxonomy annotation (as GitHub issue)
        """
        items = ["%s\n%s\n" % (v["uid"], k) for k, v in self.taxonomy.flatten().items()]
        return self.export_annotation_template(
            template=template, items=items, outfile=outfile, force=force
        )

    # Annotation template

    def export_annotation_template(self, template, items, outfile=None, force=False):
        """Given an output directory and a template name, export a set of
           markdown files for each criteria or taxonomy item.
        """
        # If output folder not provided, assume _taxonomy in $PWD
        template = get_template(template)

        # If the output file exists and force is false, exit early
        if outfile and not force and os.path.exists(outfile):
            sys.exit(f"{outfile} exists, use --force to overwrite.")

        instance = Template(template)
        result = instance.render(items=items)
        if outfile:
            write_file(outfile, result)
            return outfile
        return result

    # Criteria Export

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

    def export_criteria_annotation_template(
        self, outfile, template="annotate-criteria-template.md", force=False
    ):
        """Given an output directory and a template name, export a set of
           markdown files for each criteria
        """
        items = ["%s\n%s\n" % (c.uid, c.question) for c in self.criteria]
        return self.export_annotation_template(
            template=template, items=items, outfile=outfile, force=force
        )
