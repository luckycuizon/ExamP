# Fx Bridge

A brief description of your project.

## Installation

pip install -r requirements.txt

## Usage

Execute the command below to return the first 20 validator addresses.

`curl -X POST http://127.0.0.1:26657 -d "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"validators\",\"params\":{\"height\":\"1\", \"page\":\"1\", \"per_page\":\"20\"}}" > genesis_validators.json`

To check the csv file, open the fx-bridge token supply.csv

## Contributing

Explain how others can contribute to the project.

## License

Include information about the project's license.