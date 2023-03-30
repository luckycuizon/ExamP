import json
import os
from web3 import Web3
from dotenv import load_dotenv
import threading
import datetime
import csv
from FxBridgeContract import FxBridgeContract
from TokenBridgeLocked import TokenBridgeLocked

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

# Create a list to hold the token supply data
token_supply_data = []

for crypto in tokenList:
    address, name, symbol, decimals = crypto

    # Read the total supply of that token locked in the bridge
    tokenLocked = TokenBridgeLocked(address)
    totalSupply = tokenLocked.getTotalSupply()

    # Gets the latest block
    latestBlock = tokenLocked.getLatestBlock()
    # Gets the block height based on the latest block
    blockHeight = tokenLocked.getBlockHeight(latestBlock)
    # Gets the block timestamp based on the latest block
    blockTimestamp = tokenLocked.getBlockTimestamp(latestBlock)
    

    print(f"Address: {address}")
    print(f"Name: {name}")
    print(f"Symbol: {symbol}")
    print(f"Total Supply: {totalSupply} ")
    print(f"Decimals: {decimals}")
    print(f"Block Height: {blockHeight}")
    print(f"Block Timestamp: {blockTimestamp}")
    print("----" * 10)

    # Append the token supply data to the list
    token_supply_data.append([address, name, symbol, totalSupply, decimals, blockHeight, blockTimestamp])

# Write the token supply data to a CSV file
with open('fx-bridge token supply.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Address', 'Name', 'Symbol', 'Total Supply', 'Decimals', 'Block Height', 'Block Timestamp'])
    writer.writerows(token_supply_data)