import requests
import json


def login(User_account,User_password):
    url1 = "http://www.revth.com:12300/auth/login"
    # url2 = "http://www.revth.com:12300/auth/validate"
    headers1 = {
        "Content-Type": 'application/json',
    }
    form_data = {
        "username": User_account,
        "password": User_password
    }
    response = requests.post(url=url1, headers=headers1, data=json.dumps(form_data), verify=False)
    # print(response.text)
    # print(response.json()["data"]["token"])
    re_js = response.json()
    if re_js["status"] == 0:
        return response.json()["data"]["token"]
    else:
        return re_js["status"]


def register(user_account,user_password,student_number,student_password):
    url = "http://www.revth.com:12300/auth/register2"
    form_data = {
        "username": user_account,
        "password": user_password,
        "student_number": student_number,
        "student_password": student_password
    }
    headers = {
        "Content-Type": 'application/json',
    }
    response = requests.post(url=url, headers=headers, data=json.dumps(form_data), verify=False)
    #print(response.text)
    return response.json()["status"]

'''
{
  "status": 0,
  "data": {
    "id": 1000,
    "card": "*2 *3 *4 *5 *6 *7 *8 *9 *10 *J *Q *K *A"
  }
}
'''


def begin_game(token):
    url = "http://api.revth.com/game/open"
    headers = {
        "X-Auth-Token": token,
    }
    response = requests.post(url=url, headers=headers, verify=False).json()
    #print(response)
    card = response["data"]["card"]
    id = response["data"]["id"]
    return id, card

# 出牌
def play(id, cards, token):
    """
    :param cards: list of string
    """
    url = "http://api.revth.com/game/submit"
    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json",
    }
    form_data = {
        "id": id,
        "card": cards,
    }

    #print(json.dumps(form_data))
    response = requests.post(url=url, headers=headers, data=json.dumps(form_data), verify=False)
    #print(response.text)
    if response.json()["status"] == 0:
        return 0
    print("出牌错误")



def get_detail(token, id):
    url = "http://api.revth.com/history/{}".format(id)
    header = {
        "X-Auth-Token": token,
    }
    response = requests.get(url,headers=header)
    print(response.text)
    re_js = response.json()
    if re_js["status"] == 0:
        return re_js
    else:
        return False

# todo
def get_game_list(token):
    url="http://api.revth.com/history/25/5/0"
    header = {
        "X-Auth-Token": token,
    }
    response = requests.get(url,headers=header)
    #print(response.text)
    re_js = response.json()
    if re_js["status"] == 0:
        #print(re_js)
        return re_js
    else:
        return False


def get_ranking():
    url = "http://api.revth.com/rank"
    response = requests.get(url)
    re_js = response.json()
    #for i in re_js:
        #print(i["name"])
        #print(i["score"])
        # print(i["player_id"])

    # js["name"],js["score"],js["player_id"]
    return re_js
