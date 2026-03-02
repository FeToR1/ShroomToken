import solcx
import json

solc_version = '0.8.34'

solcx.install_solc(solc_version)

compiled = solcx.compile_files(
    ['contracts/ShroomCoin.sol'],
    output_values=["abi", "bin-runtime"],
    solc_version=solc_version,
    import_remappings=["@openzeppelin=contracts/@openzeppelin"]
)


my_contract_id = 'contracts/ShroomCoin.sol:ShroomCoin'
abi = compiled[my_contract_id]['abi']
bin_runtime = compiled[my_contract_id]['bin-runtime']


with open("ShroomCoin.abi.json", "w") as f:
    json.dump(abi, f, indent=2)

with open("ShroomCoin.bin-runtime", "w") as f:
    f.write(bin_runtime)