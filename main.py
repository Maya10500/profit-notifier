import requests
import json

URLBASE="https://api.guildwars2.com/v2/"


def main():
#
    conf=""
    with open("conf.json","r") as conf_file:
        conf=json.load(conf_file)
    resp = requests.get(URLBASE+"commerce/transactions/history/buys?access_token="+conf["apikey"])
    items = resp.json()
    for item in items:
        resp_obj = requests.get(URLBASE + "items/" + str(item["item_id"])+"?lang=fr")
        print(resp_obj.json()["name"] + " a été acheté au prix EXHORBITANT de "+str(item["price"])+ "et y en avait "+ str(item["quantity"])+".")










if __name__ == '__main__':
    main()
