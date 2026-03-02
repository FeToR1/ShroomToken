import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

PRIVATE_KEY = os.getenv('PRIVATE_KEY')
ACCOUNT_ADDRESS = os.getenv('ACCOUNT_ADDRESS')
INFURA_URL = os.getenv('INFURA_URL')

w3 = Web3(Web3.HTTPProvider(INFURA_URL))


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
    'gasPrice': w3.to_wei('10', 'gwei'),
})

signed_tx = w3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
print(f"Транзакция отправлена! hash: {w3.to_hex(tx_hash)}")

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Контракт задеплоен по адресу: {tx_receipt.contractAddress}")
