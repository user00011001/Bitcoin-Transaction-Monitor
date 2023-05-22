# Bitcoin Transaction Monitor

This script uses WebSocket to connect to Blockchain's API and subscribes to all unconfirmed Bitcoin transactions. It prints each transaction's hash, time received, input addresses, output addresses, and transaction amounts in real-time.

## Dependencies

This script requires Python 3.6 or above, and the following Python packages:

- `websocket-client` (for WebSocket support)

You can install the dependency using pip:

```
pip install websocket-client
```

## Running the Script

Simply run the Python script from your command line:

```
python btc_transaction_monitor.py
```

## Output

The script will output the real-time Bitcoin transactions in the following format:

```bash
New Bitcoin Transaction Received:
------------------------------
Transaction ID:  [Transaction Hash]
Received at:  [Timestamp]

Inputs:
 - From Address:  [Input Address]
 - Amount:  [Amount in BTC]

Outputs:
 - To Address:  [Output Address]
 - Amount:  [Amount in BTC]
------------------------------
```

## Error Handling

The script includes basic error handling for issues with the WebSocket connection. In case of connection errors or closures, corresponding messages will be displayed in the console.

## Notes

Please note that this script is for educational purposes only. Do not use this script for illegal activities. Also, the Blockchain API, like any other external service, can have downtime or changes in its interface that might require updating the script.
