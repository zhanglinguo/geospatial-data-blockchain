import hashlib
from web3 import Web3
from config import WEB3_PROVIDER, CONTRACT_ADDRESS, PRIVATE_KEY

w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))
assert w3.is_connected(), "连接区块链失败"

CONTRACT_ABI = [
    {
        "inputs": [{"internalType": "string", "name": "_hash", "type": "string"}],
        "name": "storeHash",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "string", "name": "_hash", "type": "string"}],
        "name": "exists",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def get_file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def upload_hash(filepath):
    file_hash = get_file_hash(filepath)
    print(f"文件哈希: {file_hash}")

    if contract.functions.exists(file_hash).call():
        print("该哈希已存在，无需重复上链")
        return

    account = w3.eth.account.from_key(PRIVATE_KEY)
    nonce = w3.eth.get_transaction_count(account.address)

    tx = contract.functions.storeHash(file_hash).build_transaction({
        'from': account.address,
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': w3.eth.gas_price
    })

    signed_tx = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"交易已发送: {tx_hash.hex()}")
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"上链成功，区块号: {receipt.blockNumber}")

if __name__ == "__main__":
    upload_hash("data/elevation_sample.csv")