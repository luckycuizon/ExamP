from web3 import Web3
from Web3Base import Web3Base
import requests
import json
import os

class FxBridgeContract(Web3Base):
    def __init__(self,_network,_address,_abiJson):
        super().__init__(_network,_address,_abiJson)

     # Read and returns the bridge token list
    def getBridgeTokenList(self):
        tokenList = self.contract.functions.getBridgeTokenList().call()
        return tokenList
    
    # Returns the total supply token locked in the bridge based on the address
    def get_total_supply(self, contract_address):
        base_url = "https://api.etherscan.io/api"
        payload = {
            "module": "stats",
            "action": "tokensupply",
            "contractaddress": contract_address,
            "apikey": os.getenv('ETHERSCAN_API_KEY'),
        }

        response = requests.get(base_url, params=payload)

        if response.status_code == 200:
            json_data = response.json()
            if json_data["status"] == "1":
                total_supply = int(json_data["result"])
                return total_supply
            else:
                raise Exception("Error: " + json_data["message"])
        else:
            raise Exception("Error: " + response.text)
    

    # Returns the owner of the contract
    def getOwner(self):
        ownerAddress = self.contract.functions.owner().call()
        return ownerAddress