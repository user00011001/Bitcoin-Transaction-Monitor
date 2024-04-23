import json
import datetime
from websocket._app import WebSocketApp 

class BitcoinTransactionListener:
    def __init__(self, url="wss://ws.blockchain.info/inv"):
        self.ws = WebSocketApp(url, 
                               on_message=self.on_message, 
                               on_error=self.on_error, 
                               on_close=self.on_close)

        self.ws.on_open = self.on_open

    def on_message(self, ws, message):
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

    def on_error(self, ws, error):
        print("Error occurred: ", error)

    def on_close(self, ws):
        print("\nConnection closed")

    def on_open(self, ws):
        ws.send(json.dumps({"op": "unconfirmed_sub"}))

    def run(self):
        self.ws.run_forever()


if __name__ == "__main__":
    listener = BitcoinTransactionListener()
    listener.run()

