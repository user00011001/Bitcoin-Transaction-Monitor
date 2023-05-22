import json
import datetime
from websocket._app import WebSocketApp


def on_message(ws, message):
    """
    Function called when a message is received. The message contains information about a bitcoin transaction.
    """
    msg_json = json.loads(message)
    print("\nNew Bitcoin Transaction Received:")
    print("------------------------------")

    print("Transaction ID: ", msg_json.get('x', {}).get('hash'))

    timestamp = msg_json.get('x', {}).get('time')
    print("Received at: ", datetime.datetime.fromtimestamp(
        int(timestamp)).strftime('%Y-%m-%d %H:%M:%S'))

    print("\nInputs:")
    for inp in msg_json.get('x', {}).get('inputs', []):
        print(" - From Address: ", inp.get('prev_out', {}).get('addr'))
        print(" - Amount: ", inp.get('prev_out', {}).get('value', 0) / 1e8, " BTC")

    print("\nOutputs:")
    for out in msg_json.get('x', {}).get('out', []):
        print(" - To Address: ", out.get('addr'))
        print(" - Amount: ", out.get('value', 0) / 1e8, " BTC")

    print("------------------------------")


def on_error(ws, error):
    """
    Function called when an error occurs.
    """
    print("Error occurred: ", error)


def on_close(ws):
    """
    Function called when the WebSocket connection is closed.
    """
    print("\nConnection closed")


def on_open(ws):
    """
    Function called when the WebSocket connection is opened.
    """
    # Subscribe to unconfirmed transactions
    ws.send(json.dumps({"op": "unconfirmed_sub"}))


if __name__ == "__main__":
    ws = WebSocketApp("wss://ws.blockchain.info/inv",
                      on_message=on_message,
                      on_error=on_error,
                      on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
