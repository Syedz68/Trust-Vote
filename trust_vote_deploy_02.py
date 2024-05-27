import json
from web3 import Web3
from solcx import compile_standard, install_solc
from trust_vote_deploy_01 import abi, byteCode, chain_id, myAddress, privateKey, w3

tx_receipt = None
nonce = None
election = None
contract_address = None
flag = True


def DEPLOY():
    Election = w3.eth.contract(abi=abi, bytecode=byteCode)
    global nonce
    nonce = w3.eth.get_transaction_count(myAddress)
    transaction = Election.constructor().build_transaction(
        {
            "chainId": chain_id,
            "gasPrice": w3.eth.gas_price,
            "from": myAddress,
            "nonce": nonce,
        }
    )
    nonce += 1
    signed_tx = w3.eth.account.sign_transaction(transaction, private_key=privateKey)
    print("Deploying the contract!!!")
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Waiting for the transaction to finish...")
    global tx_receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Done! Contract deployed to {tx_receipt.contractAddress}")
    global contract_address
    contract_address = tx_receipt.contractAddress
    print("------------------------------------------------")
    print(tx_receipt)
    print(type(tx_receipt))
    global flag
    flag = False


def PLACEVOTE(vote):
    global tx_receipt
    global contract_address
    global nonce
    Election = w3.eth.contract(address=contract_address, abi=abi)
    create_transaction = Election.functions.placeVote(vote).build_transaction(
        {
            "chainId": chain_id,
            "gasPrice": w3.eth.gas_price,
            "from": myAddress,
            "nonce": nonce,
        }
    )
    nonce += 1
    signed_tx = w3.eth.account.sign_transaction(create_transaction, private_key=privateKey)
    tx_signed_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Making the transaction now............")
    tx_receipt = w3.eth.get_transaction_receipt(tx_signed_hash)
    print(tx_receipt)
    print("The transaction has been completed..........")


def VIEWVOTESTATUS():
    global tx_receipt
    global election
    Election = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    votestatus = Election.functions.viewVoteStatus().call(
        {
            "chainId": chain_id,
            "gasPrice": w3.eth.gas_price,
            "from": myAddress,
            "nonce": nonce,
            "to": contract_address
        }
    )
    print("This is the current vote status: ")
    print(votestatus)
    return votestatus


def deployContractOnce():
    global flag
    while flag:
        DEPLOY()