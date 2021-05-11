import json
import urllib.request as ur

def ip_info():
    url = 'http://ipinfo.io/json'
    response = ur.urlopen(url)
    data = json.load(response)
    return data

if __name__ == "__main__":
    ip = ip_info().get('ip')
    output = "IP Address: {}".format(ip)
    print(output)



