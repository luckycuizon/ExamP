import json
import os
from web3 import Web3
from dotenv import load_dotenv
import threading
import datetime
import csv
from FxBridgeContract import FxBridgeContract

# Load global settings from .env
load_dotenv()

# Create an instance of the FxBridge Contract
fxBridge = FxBridgeContract(os.getenv('MAINNET_ETH_URL'),os.getenv('BRIDGE_PROXY_ADDRESS'),'bridge_abi.json')


# Pundix Exam Instruction
#  Write a script to query info on the fx-bridge (50 points)
# 	•	For each type of ERC20 token registered on this bridge (the ethereum side)
# 	•	The total supply of that token locked in the bridge


# 	•	For each type of ERC20 token registered on this bridge (the ethereum side)
# Read the bridge token list
tokenList = fxBridge.getBridgeTokenList()

for crypto in tokenList:
    address, name, symbol, decimals = crypto

# 	•	The total supply of that token locked in the bridge
    # Get the total supply of that token locked in the bridge
    totalSupply = fxBridge.get_total_supply(address)

    print(f"Address: {address}")
    print(f"Name: {name}")
    print(f"Symbol: {symbol}")
    print(f"Total Supply: {totalSupply} ")
    print(f"Decimals: {decimals}")
    print("----" * 10)