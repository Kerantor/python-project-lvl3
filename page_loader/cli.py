"""CLI parser of the 'Page loader'."""


import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(
        description='Load page'
    )
    parser.add_argument(
        '--output',
        choices=['plain', 'json', 'stylish'],
        metavar='Path to download file',
        help='set path to download file',
        nargs=1,
        default=os.getcwd())
    parser.add_argument('page_url')
    return parser.parse_args()
