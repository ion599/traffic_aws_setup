__author__ = 'lei'

import urllib
import requests

#testfile = urllib.URLopener()
#testfile.retrieve("https://megacell.s3.amazonaws.com/test.py", "~/test.py")

with open('experiment_matrices.7z', 'wb') as handle:
    response = requests.get('https://megacell.s3.amazonaws.com/experiment_matrices.7z', stream=True)

    if not response.ok:
        pass
        # Something went wrong

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)