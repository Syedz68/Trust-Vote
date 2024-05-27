import json
from web3 import Web3
from solcx import install_solc, compile_standard

# Install the specific Solidity compiler version
install_solc('0.8.0')

# Read the Solidity file
with open("./Election.sol", "r") as file:
    electionList = file.read()

# Compile the Solidity code
compiledSol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"Election.sol": {"content": electionList}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0"
)

# Save the compiled contract to a JSON file
with open("compiled_code_election.json", "w") as file:
    json.dump(compiledSol, file)

# Extract the bytecode and ABI
byteCode = compiledSol["contracts"]["Election.sol"]["Election"]["evm"]["bytecode"]["object"]
abi = json.loads(compiledSol["contracts"]["Election.sol"]["Election"]["metadata"])["output"]["abi"]

# Set up the web3 instance and deploy the contract
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337

myAddress = "0x703a45eE52E11C7F42EAaE2b7e34cdC161ecbf48"
privateKey = "0xcf66743aeb7c3c01440ebee53a5a2be345154e80393be06e621988db1b5750f7"

print(byteCode)
print(abi)
