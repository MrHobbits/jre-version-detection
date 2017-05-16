#!/usr/bin/python

"""

    TODO:
    1. Create functionality to store the last version we 'knew' about
    in a file and pull it open so we can examine if it's different
    each time we run this.

    2. If the version is different, do something about it. Like launch
    a web browser or send an email, or post to slack or something.

    3. Visual studio code has been installed and will be the new editor
    for this and all future projects.

"""

from datetime import datetime
from bs4 import BeautifulSoup

import requests


def last_known_version():
    """
    Loads the variables from the save file to compare to the version we find.
    """
    dat_file = open('javainfo.dat').read()

    last_version = dat_file.split(chr(10))

    right_now = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    prev_time = datetime.strptime(last_version[1], "%Y-%m-%d %H:%M:%S")
    now_time = datetime.strptime(right_now, "%Y-%m-%d %H:%M:%S")
    time_diff = abs((now_time - prev_time).seconds)

    return (last_version[0], time_diff)

def get_version():
    """
    Attempts to grab the current version of Java from the oracle page
    """

    print(f"Old Version {last_known_version()[0]}")

    # General downloads page, which leads to the JRE 8 download page
    url = "http://www.oracle.com/technetwork/java/javase/downloads/index.html"

    # grab the webpage in its entirety (source code)
    url_source = requests.get(url).text

    # make it beautiful
    jre_version = BeautifulSoup(url_source, "lxml").find("a", {"name":"JDK8"}).text[8:]

    return jre_version

if __name__ == '__main__':
    print(f"Latest version {get_version()}")
