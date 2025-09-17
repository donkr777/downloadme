import asyncio
import time
from bitcoinlib.wallets import Wallet
from bit import PrivateKeyTestnet
import threading

my_key = PrivateKeyTestnet()

# Create a new wallet (if you don't have one)



''' # one method for creating transaction using bit
tx_hash = my_key.send([('mkH41dfD4S8DEoSfcVSvEfpyZ9siogWWtr', 1, 'usd')])

print(tx_hash)


'''

#1)BTC 2)USDT|TETHER||Multi chain|  3)SOLANA

# Load an existing wallet
w = Wallet('fjdslkfajsdklfjaklsdfasd') 
# You might need to provide a password if the wallet is encrypted
w.scan()

#add logic : first is to send a bunch of requests at the same time using threading to see if one goes through

def flash_btc1(address,amount:int): # continue working on this method - not complete
    try:
        transaction_id = w.send_to(address, amount, offline=False)
        print(f"Transaction sent! Transaction ID: {transaction_id}")
    except Exception as e:
        print(f"Error sending transaction: {e}")
        
def flash_btc2(address, amount: int):
    tx_hashes = []
    errors = 0
    
    def send_transaction():
        nonlocal errors
        try:
            tx_hash = my_key.send([(address, amount, "usd")])
            tx_hashes.append(tx_hash)
        except Exception as e:
            errors += 1
            print(f"Error occurred: {e}")
    
    # Create and start 100 threads
    threads = []
    for i in range(100):
        thread = threading.Thread(target=send_transaction)
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print(f"Completed: {len(tx_hashes)} successful, {errors} failed")
    return tx_hashes

test_hash=flash_btc2("18J15F8fenmh4AhrnsLQ52E3FHBTAxodCZ",340)