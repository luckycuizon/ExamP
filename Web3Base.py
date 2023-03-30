from web3 import Web3
from datetime import datetime
import json
import os

class Web3Base:
    def __init__(self,_network,_address,_abiJson):
        # Read bridge abi 
        with open(_abiJson, 'r') as abi:
            self.contract_abi = json.load(abi)

        self.web3 = Web3(Web3.HTTPProvider(_network))
        self.contract = self.web3.eth.contract(address=_address,abi=self.contract_abi)

    def getLatestBlock(self):
        # Get the latest block number
        latest_block = self.web3.eth.block_number

        # Get the block object for the latest block
        block = self.web3.eth.get_block(latest_block)

        return block

    def getBlockHeight(self,block):
        return block.number
    
    def getBlockTimestamp(self,block):
        return datetime.fromtimestamp(block.timestamp)