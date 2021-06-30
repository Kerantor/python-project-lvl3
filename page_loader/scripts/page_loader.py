#!/usr/bin/env python


"""Script of the 'Page loader'."""


from page_loader import page_loader
from page_loader import cli


def main():
    args = cli.parse_args()
    print(
        page_loader.download(
            args.page_url,
            args.output
        )
    )


if __name__ == '__main__':
    main()
