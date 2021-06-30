# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import socket
import json
import requests
from pprint import pprint 
from config import USERNAME, TOKEN, REPO_OWNER, REPO_NAME

def make_github_issue(title, body=None, assignee=USERNAME, closed=False, labels=[]):
    # Create an issue on github.com using the given parameters
    # Url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)

    # Headers
    headers = {
        "Authorization": "token %s" % TOKEN,
        "Accept": "application/vnd.github.v3+json"
    }

    # Create issue
    message = f"[bot] issue registered by: **{USERNAME}** from **{socket.gethostname()}**"
    message += "\n\n"
    message += f"{body}"
    data = {
        'title': title,
        'body': message,
        'assignee': assignee,
        'closed': closed,
        'labels': labels
    }
    data = json.dumps(data)
    response = requests.request("POST", url, data=data, headers=headers)
    
    if response.status_code == 201:
        print ('Successfully created Issue "%s"' % title)
    else:
        print ('Could not create Issue "%s"' % title)
        print ('Response:', response.json())

if __name__ == '__main__':
    title = 'this is test'
    body = 'this is test'
    assignee = USERNAME
    closed = False
    make_github_issue(title, body, assignee, closed)
