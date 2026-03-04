# Install dependencies

```
git submodule update --init --recursive
```

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Compile contract

```
python3 compile_contract.py
```

## Deploy contract

```
python3 deploy_contract.py
```

## Test contract

```
python3 interact_contract.py
```

# Description 

Kutergin Fedor (0x9d3478c1deA23064a72d5405FAB5d5955c9f72f0)
Ioffe Alexander (0x53Cb4c128B7dc3CD1F763aC011dE34817a23f244),
Chernyaev Maxim (0x6f597922E1225e3ac3Ab802c5aa9056ed9672201)

CHAIN_ID=11155111 - sepolia testnet

1. Got ETH from faucet https://cloud.google.com/application/web3/faucet/ethereum/sepoliaх

[fetor_wallet]

2. Compiled contract
3. Deployed contract

```
Transaction sent! hash: d663f0f292a48ab2185cc0edb52ae3dacda775004cc3f19db46c3b8420eea8d3
Contract deployed: 0x0D6620D7176B6EC1b047EBf22668c66D538D7EB0
```

https://sepolia.etherscan.io/address/0x0D6620D7176B6EC1b047EBf22668c66D538D7EB0


[contract_deployed]

4. Tested contract

