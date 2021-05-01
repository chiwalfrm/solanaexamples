import requests
r = requests.get(url='https://raw.githubusercontent.com/project-serum/serum-ts/master/packages/tokens/src/mainnet-beta.json')
for key in r.json():
        print(key['tokenSymbol'],key['mintAddress'])
