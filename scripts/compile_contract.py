import solcx
import json
import os

CUR_PATH = os.path.dirname(os.path.abspath(__file__))
CONTRACT_FILE = os.path.join(CUR_PATH, "..", "contracts", "ShroomToken.sol")
OPENZEPPELIN_DIR = os.path.join(CUR_PATH, "..", "contracts", "@openzeppelin")

solc_version = '0.8.34'

solcx.install_solc(solc_version)

compiled = solcx.compile_files(
    [CONTRACT_FILE],
    output_values=["abi", "bin", "bin-runtime"],
    solc_version=solc_version,
    import_remappings=[f"@openzeppelin={OPENZEPPELIN_DIR}"],
    optimize=True,
    optimize_runs=200,
    evm_version="shanghai"
)

my_contract_id = None
for key in compiled.keys():
    if key.endswith(f"ShroomToken"):
        my_contract_id = key
        break

abi = compiled[my_contract_id]['abi']
bytecode = compiled[my_contract_id]['bin']
bin_runtime = compiled[my_contract_id]['bin-runtime']


with open("ShroomToken.abi.json", "w") as f:
    json.dump(abi, f, indent=2)

with open("ShroomToken.bin", "w") as f:
    f.write(bytecode)


contract_paths = set()
for k in compiled.keys():
    file_path = k.rsplit(':', 1)[0]
    contract_paths.add(file_path)
print(contract_paths)

sources = {}
for p in contract_paths:
    abs_path = os.path.abspath(p)
    abs_oz_path = os.path.abspath(OPENZEPPELIN_DIR)
    
    with open(abs_path, encoding='utf-8') as f:
        if abs_path.endswith('ShroomToken.sol'):
            key = os.path.basename(abs_path)
        elif abs_path.startswith(abs_oz_path):
            key = "@openzeppelin/" + os.path.relpath(abs_path, abs_oz_path)
        else:
            key = os.path.basename(abs_path)
        
        sources[key] = {
            "content": f.read()
        }

input_json = {
    "language": "Solidity",
    "sources": sources,
    "settings": {
        "optimizer": {"enabled": True, "runs": 200},
        "evmVersion": "shanghai"
    }
}

with open("input.json", "w") as f:
    json.dump(input_json, f, indent=2)