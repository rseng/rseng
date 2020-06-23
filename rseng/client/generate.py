"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from rseng.main import ResearchSoftware
import logging

bot = logging.getLogger("rseng.client")


def main(args, extra):

    # Create a client to interact with
    client = ResearchSoftware(version=args.ver)

    if args.type == "taxonomy":
        files = client.export_taxonomy_markdown(args.path, force=args.force)
        print("\n".join(files))
    elif args.type == "taxonomy-json":
        filename = client.export_taxonomy_json(args.path, force=args.force)
        print(filename)
    elif args.type == "criteria":
        files = client.export_criteria_markdown(args.path, force=args.force)
        print("\n".join(files))
    elif args.type == "criteria-annotation-template":
        filename = client.export_criteria_annotation_template(
            args.path or "annotate-criteria-template.md", force=args.force
        )
        print(filename)
    elif args.type == "taxonomy-annotation-template":
        filename = client.export_taxonomy_annotation_template(
            args.path or "annotate-taxonomy-template.md", force=args.force
        )
        print(filename)
    else:
        print("Please specify an export type as the first argument.")
