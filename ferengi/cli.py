#! /usr/bin/env python3
"""Greedy data acquisition."""

from argparse import ArgumentParser, Namespace
from logging import DEBUG, INFO, basicConfig, getLogger

from ferengi.api import roa
from ferengi.openligadb import Team
from ferengi.openweathermap import update as update_openweathermap
from ferengi.spiegelnews import update as update_spiegel_news
from ferengi.weltnews import update as update_welt_news


__all__ = ['main']


LOGGER = getLogger(__file__)


def get_args() -> Namespace:
    """Returns the command line arguments."""

    parser = ArgumentParser(description='Greedy data acquisition.')
    parser.add_argument(
        '-v', '--verbose', action='store_true', help='enable verbose logging')
    parser.add_argument(
        '-f', '--force', action='store_true', help='force data import')
    parser.add_argument(
        '--rules-of-acquisition', action='store_true',
        help='print the rules of acquisition')
    subparsers = parser.add_subparsers(dest='module')
    subparsers.add_parser('openligadb', help='import soccer league tables')
    subparsers.add_parser('openweathermap', help='import weather information')
    subparsers.add_parser('spiegelnews', help='import news from spiegel.de')
    subparsers.add_parser('weltnews', help='import news from welt.de')
    return parser.parse_args()


def main():
    """Runs the FERENGI client."""

    args = get_args()
    basicConfig(level=DEBUG if args.verbose else INFO)

    if args.rules_of_acquisition:
        roa()
    elif args.module == 'openligadb':
        Team.update_from_api()
    elif args.module == 'openweathermap':
        update_openweathermap(force=args.force)
    elif args.module == 'spiegelnews':
        update_spiegel_news()
    elif args.module == 'weltnews':
        update_welt_news()
