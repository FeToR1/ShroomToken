import json, os, sys
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()
w3 = Web3(Web3.HTTPProvider(os.getenv('INFURA_URL')))
contract = w3.eth.contract(
    address=os.getenv('CONTRACT_ADDRESS'),
    abi=json.load(open('ShroomToken.abi.json'))
)

def balance(addr=None):
    addr = addr or os.getenv('ACCOUNT_ADDRESS')
    addr = w3.to_checksum_address(addr)
    bal = contract.functions.balanceOf(addr).call()
    print(f"Balance: {w3.from_wei(bal, 'ether')} SHRM")

def transfer(to, amount):
    tx = contract.functions.transfer(
        w3.to_checksum_address(to),
        w3.to_wei(float(amount), 'ether')
    ).build_transaction({
        'from': os.getenv('ACCOUNT_ADDRESS'),
        'nonce': w3.eth.get_transaction_count(os.getenv('ACCOUNT_ADDRESS')),
        'gas': 100000,
        'gasPrice': w3.eth.gas_price,
        'chainId': int(os.getenv('CHAIN_ID'))
    })
    signed = w3.eth.account.sign_transaction(tx, os.getenv('PRIVATE_KEY'))
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    print(f"Sent! Hash: {tx_hash.hex()}")
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Confirmed!")

def mint(amount):
    tx = contract.functions.mint(
        w3.to_checksum_address(os.getenv('ACCOUNT_ADDRESS')),
        w3.to_wei(float(amount), 'ether')
    ).build_transaction({
        'from': os.getenv('ACCOUNT_ADDRESS'),
        'nonce': w3.eth.get_transaction_count(os.getenv('ACCOUNT_ADDRESS')),
        'gas': 150000,
        'gasPrice': w3.eth.gas_price,
        'chainId': int(os.getenv('CHAIN_ID'))
    })
    signed = w3.eth.account.sign_transaction(tx, os.getenv('PRIVATE_KEY'))
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    print(f"Minted! Hash: {tx_hash.hex()}")
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Confirmed!")

def burn(amount):
    tx = contract.functions.burn(
        w3.to_wei(float(amount), 'ether')
    ).build_transaction({
        'from': os.getenv('ACCOUNT_ADDRESS'),
        'nonce': w3.eth.get_transaction_count(os.getenv('ACCOUNT_ADDRESS')),
        'gas': 100000,
        'gasPrice': w3.eth.gas_price,
        'chainId': int(os.getenv('CHAIN_ID'))
    })
    signed = w3.eth.account.sign_transaction(tx, os.getenv('PRIVATE_KEY'))
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    print(f"Burned! Hash: {tx_hash.hex()}")
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Confirmed!")

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'help'
    if cmd == 'balance': balance(sys.argv[2] if len(sys.argv) > 2 else None)
    elif cmd == 'transfer': transfer(sys.argv[2], sys.argv[3])
    elif cmd == 'mint': mint(sys.argv[2])
    elif cmd == 'burn': burn(sys.argv[2])
    else: print("Usage:\n  balance [addr] - check balance (default: your account)\n  transfer <to> <amount> - send tokens\n  mint <amount> - mint tokens to your account\n  burn <amount> - burn your tokens")
