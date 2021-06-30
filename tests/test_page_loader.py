"""Page_loader test."""


import tempfile
from page_loader import page_loader


def test_page_loader():
    with tempfile.TemporaryDirectory() as test_directory:
        test_file = page_loader.download(
            'https://page-loader.hexlet.repl.co/',
            str(test_directory)
        )
        with open(test_file, 'r') as opened_file:
            assert opened_file.read() == open(
                'tests/fixtures/test_page.html', 'r'
            ).read()
