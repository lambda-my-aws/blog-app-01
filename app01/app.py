#!/usr/bin/env python

import argparse


from werkzeug.contrib.fixers import ProxyFix
from app01 import App


def start_app():
    parser = argparse.ArgumentParser(description="Starts the App")
    parser.add_argument(
        "--debug",
        default=False,
        action="store_true",
        help="define the section to be updated",
        required=False,
    )
    args = parser.parse_args()
    debug = args.debug

    App.wsgi_app = ProxyFix(App.wsgi_app)
    App.run(debug=debug)


if __name__ == "__main__":
    start_app()
