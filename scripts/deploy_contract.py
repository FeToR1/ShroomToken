import json
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

PRIVATE_KEY = os.getenv('PRIVATE_KEY')
ACCOUNT_ADDRESS = os.getenv('ACCOUNT_ADDRESS')
INFURA_URL = os.getenv('INFURA_URL')
CHAIN_ID = int(os.getenv('CHAIN_ID'))

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

print(w3.from_wei(w3.eth.get_balance(ACCOUNT_ADDRESS), 'ether'))
with open('ShroomToken.abi.json') as f:
    abi = json.load(f)
with open('ShroomToken.bin-runtime') as f:
    bytecode = f.read()

ShroomToken = w3.eth.contract(abi=abi, bytecode=bytecode)

nonce = w3.eth.get_transaction_count(ACCOUNT_ADDRESS)

transaction = ShroomToken.constructor().build_transaction({
    'from': ACCOUNT_ADDRESS,
    'nonce': nonce,
    'gas': 2_500_000,
    'gasPrice': w3.to_wei('5', 'gwei'),
    'chainId': CHAIN_ID,
})

signed_tx = w3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
print(f"Transaction sent! hash: {tx_hash.hex()}")

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Contract deployed: {tx_receipt.contractAddress}")
