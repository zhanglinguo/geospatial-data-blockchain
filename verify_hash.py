import hashlib
from web3 import Web3
from config import WEB3_PROVIDER, CONTRACT_ADDRESS

w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))
CONTRACT_ABI = [
    {
        "inputs": [{"internalType": "string", "name": "_hash", "type": "string"}],
        "name": "exists",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def verify_file(filepath):
    file_hash = hashlib.sha256(open(filepath, 'rb').read()).hexdigest()
    exists = contract.functions.exists(file_hash).call()
    if exists:
        print("✅ 文件哈希已在链上，未被篡改")
    else:
        print("❌ 文件哈希未在链上，可能是新文件或已被篡改")

if __name__ == "__main__":
    verify_file("data/elevation_sample.csv")