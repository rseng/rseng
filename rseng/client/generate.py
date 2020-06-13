"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from rseng.main import ResearchSoftware
import logging
import os

bot = logging.getLogger("rse.client")


def main(args, extra):

    # Create a client to interact with
    client = ResearchSoftware(version=args.ver)

    if args.type == "taxonomy":
        files = client.export_taxonomy_markdown(args.path)
        print("\n".join(files))
    else:
        files = client.export_criteria_markdown(args.path)
        print("\n".join(files))