import requests
import os
import re
from urllib.parse import urlparse


def download(page_url, save_path=os.getcwd()):
    r = requests.get(page_url)
    if not r:
        print('Wrong URL!')
    parsed = urlparse(page_url)
    scheme = "%s://" % parsed.scheme
    url = parsed.geturl().replace(scheme, '', 1)
    file_name = re.sub(r'[\W_]+', '-', url)[0:20] + '.html'
    completename = os.path.join(save_path, file_name)
    download_file = open(completename, 'w')
    download_file.write(r.text)
    download_file.close()
    return completename
