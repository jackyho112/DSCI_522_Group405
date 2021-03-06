# author: Ofer Mansour, Jacky Ho, Anand Vemparala
# date: 2020-01-23

'''
Download and save a csv file to a target location

Usage: data_download.py --url=<url> --file_location=<file_location>
 
'''

import requests
from docopt import docopt
import os.path

opt = docopt(__doc__)

def is_download_successful(filename):
        
    if os.path.isfile(filename):
        return True
    else:
        return False
        
def test_file_downloaded():
    filename = opt['--file_location']
    assert is_download_successful(filename) == True, "File failed to download, please try again"
        

def main(url, file_location):
    # download data from url and save to file_location
    r = requests.get(url)
    with open(file_location, "wb") as f:
        f.write(r.content) 
        


if __name__ == "__main__":
    main(opt["--url"], opt["--file_location"])
    test_file_downloaded()
