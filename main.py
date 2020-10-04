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
    dict_buys = {}

    for item in items:
        if item["item_id"] in dict_buys :
            if item["price"] in dict_buys[item["item_id"]]:
                dict_buys[item["item_id"]][item["price"]] =dict_buys[item["item_id"]][item["price"]]+ item["quantity"]
            else :
                dict_buys[item["item_id"]][item["price"]] = item["quantity"]
        else :
            dict_buys[item["item_id"]] = {item["price"]:item["quantity"]}
    ids=""
    dict_price = {}
    resp_price_actu = requests.get(URLBASE + "commerce/prices?ids=" + ids[:-1]).json()

    for key, value in dict_buys.items():
        resp_obj = requests.get(URLBASE + "items/" + str(key) + "?lang=fr")
        resp_price_actu = requests.get(URLBASE + "commerce/prices/" + str(key)).json()
        ids=ids+str(key)+","
        for key2,value2 in value.items():
            print(resp_obj.json()["name"] + " a été acheté au prix EXHORBITANT de "+str(key2)+ " et y en avait "+ str(value2)+".")
            print("L'objet est à présent au prix de "+ str(resp_price_actu["buys"]["unit_price"]))
            if resp_price_actu["buys"]["unit_price"]*0.85-key2>0:
                print("Tu peux vendre "+resp_obj.json()["name"])
            else:
                print("Ne vends pas " + resp_obj.json()["name"])















if __name__ == '__main__':
    main()
