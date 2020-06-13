"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from rseng.utils.file import read_file

import logging
import os

here = os.path.dirname(os.path.abspath(__file__))
bot = logging.getLogger("rseng.main.criteria")


class CriteriaSet:
    """a criteria set holds and managed a group of criteria
    """

    def __init__(self, data_file=None, sep="\t", version="latest"):
        """data_file should be a delimited file that has unique ids, questions,
           and comma separated answer options. By default, we use the latest 
           version.

           Arguments:
             data_file (str) : path to a data file, with ids, questions, options
             sep (str)       : delimiter to use for the data file
             version (str)   : version string for file criteria-<version>.tsv
        """
        self.criteria = dict()
        if not data_file:
            data_file = os.path.join(here, "criteria-%s.tsv" % version)

        if not os.path.exists(data_file):
            raise FileNotFoundError

        self.load(data_file, sep)

    def export(self, filename=None, force=True, sep="\t"):
        """save criteria to a file.
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
        return "[CriteriaSet:%s]" % len(self.criteria)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        """Allow the user to iterate over criteria.
        """
        for name, criteria in self.criteria.items():
            yield criteria

    def load(self, data_file, sep="\t"):
        """Load a data file with a particular separator.
        """
        for line in read_file(data_file):
            try:
                uid, question, options = line.strip().split(sep)
                self.criteria[uid] = Criteria(uid, question, options.split(","))
            except:
                bot.warning(f"Malformed line {line}, skipping.")


class Criteria:
    """A parser base exists to extract and format repository metadata.
    """

    def __init__(self, uid, question, options="yes,no"):
        """a criteria includes a unique id, question, and options.
        """
        self.uid = uid
        self.question = question
        if isinstance(options, str):
            options = options.split(",")
        self.options = options

    def export(self, sep):
        """Given a separator, export a criteria to a line to write to file
        """
        return "{}{}{}{}{}".format(
            self.uid, sep, self.question, sep, ",".join(self.options)
        )

    def __str__(self):
        return "[Criteria:%s,%s]" % (self.uid, self.question)

    def __repr__(self):
        return self.__str__()

    def summary(self):
        return "[%s][%s]" % (self.uid, self.question)
