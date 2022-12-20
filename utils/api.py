import requests, json

def getCur(cur):
    res = requests.get(f"https://v6.exchangerate-api.com/v6/9a93affadb8370730ef79130/latest/{cur}").text
    data = json.loads(res)
    return data

if __name__=="__main__":
    print(getCur("USD"))