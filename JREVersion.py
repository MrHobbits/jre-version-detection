from bs4 import BeautifulSoup

import requests

# General downloads page, which leads to the JRE 8 download page
url = "http://www.oracle.com/technetwork/java/javase/downloads/index.html"

# grab the webpage in its entirety (source code)
url_source = requests.get(url).text

# make it beautiful
jre_version = BeautifulSoup(url_source,"lxml").find("a",{"name":"JDK8"}).text[8:]

print('Current Java Release is: {}'.format(jre_version))

"""
    TODO:
    1. Create functionality to store the last version we 'knew' about
    in a file and pull it open so we can examine if it's different
    each time we run this.

    2. If the version is different, do something about it. Like launch
    a web browser or send an email, or post to slack or something.

    3. Get this working with GIT.

    4. Maybe get it working in PyCharm too for that added Git integration?

    5. I dont like PyCharm as much as I thought I would (I dont like the colors)
    and it looks funny. what about Atom.io? Lets see if it works with GIT.
"""
