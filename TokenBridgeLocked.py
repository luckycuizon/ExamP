from web3 import Web3
from Web3Base import Web3Base
import requests
import json
import os
from dotenv import load_dotenv

# Load global settings from .env
load_dotenv()

class TokenBridgeLocked(Web3Base):
    def __init__(self,_address):
        super().__init__(os.getenv('MAINNET_ETH_URL'),_address,'erc20_abi_.json')

    def getTotalSupply(self):
        totalSupply = self.contract.functions.totalSupply().call()
        return totalSupply