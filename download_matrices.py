__author__ = 'lei'

import requests
import config
import os

def get_file(file_path, s3_file_name):
    with open(file_path, 'wb') as handle:
        response = requests.get('https://megacell.s3.amazonaws.com/'+s3_file_name, stream=True)

        if not response.ok:
            pass
            # Something went wrong

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


file_path = '/home/lei/traffic/experiment_matrices.7z'
get_file(file_path, 'experiment_matrices.7z')
os.system('7za x '+file_path+' -aoa -o'+config.DATA_DIR)

