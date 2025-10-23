"""
Blockchain Notary System - Simple Python Script
Connect to Ganache and interact with smart contract
"""

import hashlib
from web3 import Web3
from datetime import datetime

# ============================================
# CONFIGURATION - UPDATE THESE VALUES!
# ============================================

CONFIG = {
    'RPC_URL': 'http://127.0.0.1:7545',
    'CONTRACT_ADDRESS': '0xd9145CCE52D386f254917e481eB44e9943F39138',  # Paste from Remix
    'PRIVATE_KEY': '0x237fd0697293f49bc75de3cdf19023cdc887bd2472d9b541893abc7af2425ec2',  # Paste from Ganache
    'WALLET_ADDRESS': '0x95A7C0B4C4196e4D30c2F8C0B2063b10A4A62E13'
}

# Contract ABI
CONTRACT_ABI = [
    {
        "inputs": [
            {"internalType": "bytes32", "name": "_documentHash", "type": "bytes32"},
            {"internalType": "string", "name": "_description", "type": "string"}
        ],
        "name": "notarizeDocument",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "_documentHash", "type": "bytes32"}
        ],
        "name": "verifyDocument",
        "outputs": [
            {"internalType": "bool", "name": "exists", "type": "bool"},
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
            {"internalType": "address", "name": "owner", "type": "address"},
            {"internalType": "string", "name": "description", "type": "string"}
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "_documentHash", "type": "bytes32"}
        ],
        "name": "documentExists",
        "outputs": [
            {"internalType": "bool", "name": "", "type": "bool"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# ============================================
# BLOCKCHAIN NOTARY CLASS
# ============================================

class BlockchainNotary:
    def __init__(self, config):
        print("Initializing Blockchain Notary System...")
        self.config = config
        self.w3 = Web3(Web3.HTTPProvider(config['RPC_URL']))
        
        if self.w3.is_connected():
            print("✓ Connected to blockchain!")
        else:
            raise Exception("✗ Failed to connect to blockchain. Is Ganache running?")
        
        self.contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(config['CONTRACT_ADDRESS']),
            abi=CONTRACT_ABI
        )
        
        self.account = config['WALLET_ADDRESS']
        self.private_key = config['PRIVATE_KEY']
        
        print(f"✓ Contract loaded at: {config['CONTRACT_ADDRESS']}")
        print(f"✓ Using account: {self.account}")
        print()
    
    def calculate_hash(self, content):
        """Calculate SHA-256 hash of content"""
        if isinstance(content, str):
            content = content.encode('utf-8')
        return hashlib.sha256(content).hexdigest()
    
    def notarize_document(self, content, description):
        """Notarize a document on the blockchain"""
        print(f"\n{'='*60}")
        print("NOTARIZING DOCUMENT")
        print(f"{'='*60}")
        
        try:
            # Calculate hash
            doc_hash = self.calculate_hash(content)
            print(f"📄 Document Hash: {doc_hash}")
            doc_hash_bytes = Web3.to_bytes(hexstr=doc_hash)
            
            # Build transaction
            print("⏳ Building transaction...")
            nonce = self.w3.eth.get_transaction_count(self.account)
            
            transaction = self.contract.functions.notarizeDocument(
                doc_hash_bytes,
                description
            ).build_transaction({
                'from': self.account,
                'nonce': nonce,
                'gas': 300000,
                'gasPrice': self.w3.eth.gas_price
            })
            
            # Sign transaction
            print("✍️  Signing transaction...")
            signed_txn = self.w3.eth.account.sign_transaction(
                transaction, 
                private_key=self.private_key
            )
            
            # Send transaction
            print("📤 Sending transaction...")
            tx_hash = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
            
            # Wait for receipt
            print("⏳ Waiting for confirmation...")
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            
            print(f"\n{'='*60}")
            print("✅ DOCUMENT NOTARIZED SUCCESSFULLY!")
            print(f"{'='*60}")
            print(f"📄 Document Hash: {doc_hash}")
            print(f"🔗 Transaction Hash: {receipt['transactionHash'].hex()}")
            print(f"📦 Block Number: {receipt['blockNumber']}")
            print(f"⛽ Gas Used: {receipt['gasUsed']}")
            print(f"📝 Description: {description}")
            print(f"{'='*60}\n")
            
            return True
            
        except Exception as e:
            print(f"\n❌ ERROR: {str(e)}\n")
            return False
    
    def verify_document(self, content):
        """Verify a document exists on blockchain"""
        print(f"\n{'='*60}")
        print("VERIFYING DOCUMENT")
        print(f"{'='*60}")
        
        try:
            doc_hash = self.calculate_hash(content)
            print(f"📄 Document Hash: {doc_hash}")
            doc_hash_bytes = Web3.to_bytes(hexstr=doc_hash)
            
            print("🔍 Searching blockchain...")
            result = self.contract.functions.verifyDocument(doc_hash_bytes).call()
            
            if result[0]:  # exists
                timestamp = datetime.fromtimestamp(result[1]).strftime('%Y-%m-%d %H:%M:%S')
                print(f"\n{'='*60}")
                print("✅ DOCUMENT FOUND ON BLOCKCHAIN!")
                print(f"{'='*60}")
                print(f"📄 Document Hash: {doc_hash}")
                print(f"📅 Timestamp: {timestamp}")
                print(f"👤 Owner: {result[2]}")
                print(f"📝 Description: {result[3]}")
                print(f"{'='*60}\n")
                return True
            else:
                print(f"\n{'='*60}")
                print("❌ DOCUMENT NOT FOUND ON BLOCKCHAIN")
                print(f"{'='*60}")
                print(f"📄 Calculated Hash: {doc_hash}")
                print("This document has not been notarized.")
                print(f"{'='*60}\n")
                return False
                
        except Exception as e:
            print(f"\n❌ ERROR: {str(e)}\n")
            return False

# ============================================
# MAIN PROGRAM
# ============================================

def main():
    print("\n" + "="*60)
    print("🔐 BLOCKCHAIN NOTARY SYSTEM")
    print("="*60 + "\n")
    
    # Initialize notary
    try:
        notary = BlockchainNotary(CONFIG)
    except Exception as e:
        print(f"Failed to initialize: {e}")
        print("\n⚠️  Make sure:")
        print("1. Ganache is running")
        print("2. Contract address is correct")
        print("3. Private key is correct")
        return
    
    # Main menu loop
    while True:
        print("\n" + "="*60)
        print("MAIN MENU")
        print("="*60)
        print("1. Notarize a Document")
        print("2. Verify a Document")
        print("3. Exit")
        print("="*60)
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            print("\n--- NOTARIZE DOCUMENT ---")
            content = input("Enter document content: ").strip()
            if not content:
                print("❌ Content cannot be empty!")
                continue
            description = input("Enter description: ").strip()
            if not description:
                description = "No description"
            
            notary.notarize_document(content, description)
            
        elif choice == '2':
            print("\n--- VERIFY DOCUMENT ---")
            content = input("Enter document content to verify: ").strip()
            if not content:
                print("❌ Content cannot be empty!")
                continue
            
            notary.verify_document(content)
            
        elif choice == '3':
            print("\n👋 Thank you for using Blockchain Notary System!")
            print("="*60 + "\n")
            break
        else:
            print("\n❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()