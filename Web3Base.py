from web3 import Web3
import json
import os

class Web3Base:
    def __init__(self,_network,_address,_abiJson):
        # Read bridge abi 
        with open(_abiJson, 'r') as abi:
            self.contract_abi = json.load(abi)

        self.web3 = Web3(Web3.HTTPProvider(_network))
        self.contract = self.web3.eth.contract(address=_address,abi=self.contract_abi)