#!/usr/bin/env python3
import requests
import argparse

if __name__ == "__main__":
    Parser = argparse.ArgumentParser(description='Burp Pro Fast Crawler')
    Parser.add_argument('-f', '--file', help='List of domains/subdoamins', required=True)
    Parser.add_argument('-i', '--ip', help='IP addr of Burp API', default='127.0.0.1')
    Parser.add_argument('-p', '--port', help='Port of Burp API', default=1337)
    Parser.add_argument('-k', '--key', help='Burp API Key', required=True)
    Args = Parser.parse_args()

    BurpAPIURL = 'http://' + Args.ip + ':' + str(Args.port) + '/' + Args.key + '/v0.1/scan'

    with open (Args.file, 'r') as URLFile:
        for URLs in URLFile.read().splitlines():
            Data = '{"scan_configurations":[{"name":"Crawl strategy - fastest","type":"NamedConfiguration"}],"scope":{"include":[{"protocol":"any"}],"type":"AdvancedScope"},"urls":["+++"]}'
            #print('URL: {}\nCutted: {}'.format(URLs,CuttedURL))
            #print(Data.replace('~~',CuttedURL).replace('++',URLs))
            Resp = requests.post(BurpAPIURL,data=Data.replace('+++',URLs))
            if Resp.status_code == 201:
                print('* Scan created | URL: {}'.format(URLs))
            else:
                print('* Error: {}\n'.format(Resp.text))
