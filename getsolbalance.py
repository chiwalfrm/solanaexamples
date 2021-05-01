import sys
from os import path
from solana.rpc.api import Client
from solana.rpc.types import TokenAccountOpts
if len(sys.argv) < 2:
        print("ERROR: Must specify file containing api configuration.")
        print("Optional arguments: 'tokens', 'getalltokenaddresses'")
        exit()
if not path.exists(sys.argv[1]):
        print('ERROR: File', sys.argv[1], 'does not exist.')
        exit()
exec(open(sys.argv[1]).read())
print('INFO: File', sys.argv[1], 'Loaded', file=sys.stderr)
print('INFO: my_address =', my_address, file=sys.stderr)
print('INFO: my_staking_address =', my_staking_address, file=sys.stderr)
print('INFO: my_tokens =', my_tokens, file=sys.stderr)
solana_client = Client("https://api.mainnet-beta.solana.com")
if len(sys.argv) > 2 and sys.argv[2] == 'tokens':
        for coin, value in my_tokens.items():
                amount = solana_client.get_token_account_balance(value, 'max')['result']['value'].get('uiAmount')
                if amount > 0:
                        print(coin.ljust(16), '{:.18f}'.format(amount).rjust(37).rstrip('0').rstrip('.'))
elif len(sys.argv) > 2 and sys.argv[2] == 'getalltokenaddresses':
        for item in solana_client.get_token_accounts_by_owner(my_address, TokenAccountOpts(program_id='TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'), 'max')['result']['value']:
                print(item['pubkey'])
else:
        print('SOL             ', '{:.18f}'.format(solana_client.get_balance(my_address, 'max')['result']['value']/1000000000).rjust(37).rstrip('0').rstrip('.'))
        for value2 in my_staking_address:
                print('sSOL            ', '{:.18f}'.format(solana_client.get_balance(value2, 'max')['result']['value']/1000000000).rjust(37).rstrip('0').rstrip('.'))
