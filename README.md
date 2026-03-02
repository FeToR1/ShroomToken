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
python3 src/compile_contract.py
```

## Deploy contract

```
python3 src/deploy_contract.py
```
