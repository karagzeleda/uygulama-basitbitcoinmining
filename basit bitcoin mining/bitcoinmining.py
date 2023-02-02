from hashlib import sha256
#Ne kadar uzunlukta bir veri gönderilirse gönderilsin 64 karakterden oluşan bir değer gönderen sha256'nın tanımlanması.  
import time

def _SHA256(value):
    return sha256(value.encode()).hexdigest()

def mine(transactions,previous_hash,difficulty):
    prefix_zeros = '0'*difficulty
    nonce = 0
    while True:
        nonce += 1
        value = transactions + previous_hash + str(nonce)
        hash = _SHA256(value)
        if(hash.startswith(prefix_zeros)):
            print(f"Nonce Bulundu : {nonce}")
            return hash



def main():
    difficulty = 2
    transactions = 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb'
    previous_hash = '00000000000000000000a82abd8de7154563caaa537ebcca145334c24c6403a7b'
    start_time = time.time()
    print("Mining işlemi başladı..")
    hash = mine(transactions,previous_hash,difficulty)
    total_time = str(time.time() - start_time)
    print(f"Mining  {total_time} sürede bulundu..")
    print(f"Hash: {hash}")

main () 