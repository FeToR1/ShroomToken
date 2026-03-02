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
    output_values=["abi", "bin-runtime"],
    solc_version=solc_version,
    import_remappings=[f"@openzeppelin={OPENZEPPELIN_DIR}"]
)

my_contract_id = None
for key in compiled.keys():
    if key.endswith(f"ShroomToken"):
        my_contract_id = key
        break

abi = compiled[my_contract_id]['abi']
bin_runtime = compiled[my_contract_id]['bin-runtime']


with open("ShroomToken.abi.json", "w") as f:
    json.dump(abi, f, indent=2)

with open("ShroomToken.bin-runtime", "w") as f:
    f.write(bin_runtime)

