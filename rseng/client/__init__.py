#!/usr/bin/env python

"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from rseng.logger import RSENG_LOG_LEVELS, RSENG_LOG_LEVEL
import rseng
import argparse
import sys
import logging


def get_parser():
    parser = argparse.ArgumentParser(
        description="Research software engineering taxonomy and criteria."
    )

    parser.add_argument(
        "--version",
        dest="version",
        help="suppress additional output.",
        default=False,
        action="store_true",
    )

    parser.add_argument(
        "--log_level",
        dest="log_level",
        choices=RSENG_LOG_LEVELS,
        default=RSENG_LOG_LEVEL,
        help="Customize logging level for rse inspector.",
    )

    description = "actions for rseng"
    subparsers = parser.add_subparsers(
        help="rseng actions", title="actions", description=description, dest="command",
    )

    # print version and exit
    subparsers.add_parser("version", help="show software version")

    # Generate a key for the interface
    generate = subparsers.add_parser(
        "generate", help="generate output files for taxonomy and criteria",
    )

    generate.add_argument(
        "type",
        help="Type to generate",
        choices=[
            "taxonomy",
            "criteria",
            "taxonomy-json",
            "criteria-annotation-template",
            "taxonomy-annotation-template",
        ],
        nargs="?",
    )

    generate.add_argument(
        "path",
        help="Path (directory) to generate files into (should not exist)",
        nargs="?",
        default=None,
    )

    generate.add_argument(
        "ver",
        help="Version of criteria and taxonomy to use",
        nargs="?",
        default="latest",
    )

    generate.add_argument(
        "--force",
        dest="force",
        help="force generation of folder if already exists.",
        default=False,
        action="store_true",
    )

    return parser


def main():
    """main entrypoint for rse
    """

    parser = get_parser()

    def help(return_code=0):
        """print help, including the software version and active client 
           and exit with return code.
        """
        version = rseng.__version__

        print("\nResearch Software Engineering taxonomy and criteria v%s" % version)
        parser.print_help()
        sys.exit(return_code)

    # If the user didn't provide any arguments, show the full help
    if len(sys.argv) == 1:
        help()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    # Set the logging level
    logging.basicConfig(level=getattr(logging, args.log_level))
    bot = logging.getLogger("rseng.client")
    bot.setLevel(getattr(logging, args.log_level))

    # Show the version and exit
    if args.command == "version" or args.version:
        print(rseng.__version__)
        sys.exit(0)

    # Does the user want a shell?
    main = None
    if args.command == "generate":
        from .generate import main

    if main is not None:
        main(args=args, extra=extra)
    else:
        help()


if __name__ == "__main__":
    main()
