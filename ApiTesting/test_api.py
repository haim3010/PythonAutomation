import requests
import json


def test_get_auth():

  SERVER = 'http://localhost:8000/api/auth'
  db = open('PolyData.json', 'r')
  response_auth = requests.post(SERVER,json = db)
  token = response_auth['access_token']
  return token


header = {
"Content-Type": "application/json",
"Authorization": f"Bearer f'{test_get_auth()}"
}


def test_get_list():
  URL = "http://localhost:8000/api/poly"
  PolyD = open('PolyData.json','r')
  response_poly = requests.get(URL,json =PolyD , headers = header)
  json_poly = json.loads(response_poly.text)
  assert json_poly.status_code == 200

def test_post_poly():
  URL = "http://localhost:8000/api/poly"
  PolyD = open('PolyData.json','r')
  response_poly_create = requests.post(URL,json =PolyD , headers = header)
  json_post_poly = json.loads(response_poly_create.content)
  assert json_post_poly.content == "OK"

def test_get_object():
  URL = "http://localhost:8000/api/poly/65656"
  PolyD = open('PolyData.json','r')
  response_poly_obj = requests.get(URL,json =PolyD , headers = header)
  json_get_obj = json.loads(response_poly_obj.text)
  assert json_get_obj['object_id'] == 65656
  assert json_get_obj['data']['key'] == "key1"

def test_del_object():
  URL = "http://localhost:8000/api/poly/65656"
  PolyD = open('PolyData.json','r')
  response_poly_del = requests.delete(URL,json =PolyD , headers = header)
  assert response_poly_del.status_code == 204

