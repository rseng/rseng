"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from rseng.utils.file import read_yaml
import logging
import os

here = os.path.dirname(os.path.abspath(__file__))
bot = logging.getLogger("rseng.main.taxonomy")


class Taxonomy:
    """a taxonomy holds the research software taxonomy
    """

    def __init__(self, data_file=None, version="latest"):
        """data_file, if provided, should be a custom owx (owl xml file)
           that is typically generated via export from webprotege.stanford.edu

           Arguments:
             data_file (str) : path to a data file, with ids, questions, options
             version (str)   : version string for file criteria-<version>.tsv
        """
        self.tree = None
        self.nodes = {}

        if not data_file:
            data_file = os.path.join(here, "taxonomy-%s.yaml" % version)

        if not os.path.exists(data_file):
            raise FileNotFoundError

        self.load(data_file)

    def export(self, filename=None, force=True, sep="\t"):
        """save taxonomy to human readable file
        """
        if filename is not None and os.path.exists(filename) and force is False:
            sys.exit("{filename} exists! Set force=True to override it.")

        lines = []
        for uid, criteria in self.criteria.items():
            lines.append(criteria.export(sep))
        if not filename:
            return "\n".join(lines)
        write_file(filename, "\n".join(lines))
        return filename

    def __str__(self):
        return "[Taxonomy:%s]" % len(self.nodes)

    def __repr__(self):
        return self.__str__()

    def export(self):
        """export will export a flat structure of the tree
        """
        pass

    def flatten(self):
        out = {}

        def flatten(x, name=""):
            if isinstance(x, dict):
                if "children" in x:
                    if not name:
                        flatten(x["children"], x["name"])
                    else:
                        flatten(x["children"], name + " >> " + x["name"])
                else:
                    out[name + " >> " + x["name"]] = x

            elif isinstance(x, list):
                for i, elem in enumerate(x):
                    flatten(elem, name)

        flatten(self.tree)
        return out

    def load(self, data_file):
        """Load a data file
        """
        self.tree = read_yaml(data_file)
        nodes = self.tree.copy()
        while nodes:
            node = nodes.pop(0)

            # Add node to lookup, validate as we go
            if node["uid"] not in self.nodes:
                self.nodes[node["uid"]] = node
                assert "name" in node and "uid" in node
                assert node["uid"].startswith("RSE-taxonomy")
            nodes += node.get("children", [])
