import os
from requests import get, post, put, delete

WEB_HOST = os.environ['WEB_HOST']
WEB_PORT = int(os.environ['WEB_PORT'])
BASEURL = 'http://{}:{}'.format(WEB_HOST, WEB_PORT)

################
## index.html ##
################

def test_index1():
  r = get(f'{BASEURL}/')
  assert r.status_code == 200

def test_index2():
  r = get(f'{BASEURL}/index.html')
  assert r.status_code == 200


#############
## favicon ##
#############

def test_favicon():
  r = get(f'{BASEURL}/static/favicon.png')
  assert r.status_code == 200


#########
## css ##
#########

def test_css_bootstrap():
  r = get(f'{BASEURL}/static/css/bootstrap.min.css')
  assert r.status_code == 200


#########
## js ##
#########

def test_js_jquery():
  r = get(f'{BASEURL}/static/js/jquery-3.5.1.slim.min.js')
  assert r.status_code == 200

def test_js_bootstrap_bundle():
  r = get(f'{BASEURL}/static/js/bootstrap.bundle.min.js')
  assert r.status_code == 200

def test_js_bootstrap():
  r = get(f'{BASEURL}/static/js/bootstrap.min.js')
  assert r.status_code == 200

def test_js_mykvs():
  r = get(f'{BASEURL}/static/js/kvs.js')
  assert r.status_code == 200

