import requests
from bs4 import BeautifulSoup as soupy
import urllib3

def login_elements(tag):
    """A filter to find cas login form elements"""
    return tag.has_key('name') and tag.has_key('value')

def caslogin(session, caslogin, username, password, service=None):
    if service:
        params = {'service' : service}
    else:
        params = None
        
    urllib3.contrib.pyopenssl.inject_into_urllib3()

    cas_page = session.get(caslogin, params = params)
    # Move past any redirects
    caslogin = cas_page.url
    cas_doc = soupy(cas_page.text)
    form_inputs = cas_doc.find_all(login_elements)
    login_data = dict()
    for tag in form_inputs:
        login_data[tag['name']] = tag['value']
    login_data['username'] = username
    login_data['password'] = password
    
    signin_page = session.post(caslogin, login_data, cookies=cas_page.cookies, params = params)

    if signin_page.status_code != requests.codes.ok:
        print signin_page.headers
        print signin_page.cookies
        print signin_page.text
    return  signin_page.status_code == requests.codes.ok


