import requests

def main():
    print("Coucou")
    resp = requests.get("https://google.com")
    print(resp.text)







if __name__ == '__main__':
    main()
