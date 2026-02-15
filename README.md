🔐 Blockchain Notary System

A decentralized document notarization system built on Ethereum blockchain using Solidity smart contracts.



📋 Project Description

This project allows users to notarize documents on the blockchain, creating immutable proof of existence with timestamps. Users can later verify any document to check if it was previously notarized.



✨ Features

Document Notarization: Store document hashes on blockchain

Timestamp Proof: Immutable timestamp for each document

Document Verification: Verify any document against blockchain records

Owner Tracking: Track document ownership

Web Interface: User-friendly HTML interface

Ganache Integration: Works with local Ganache blockchain

🛠️ Technologies Used

Smart Contract: Solidity ^0.8.0

Blockchain: Ethereum (Ganache for local development)

Frontend: HTML, CSS, JavaScript

Web3: Web3.js for blockchain interaction

Development Tool: Remix IDE

Hash Algorithm: SHA-256

📁 Project Structure

BlockchainNotary/

├── DocumentNotary.sol          # Smart contract

├── blockchain\_notary.html      # Web interface

├── README.md                   # Project documentation

└── Config.txt                  # Configuration (not uploaded)

🚀 Setup Instructions

Prerequisites

Ganache (local blockchain)

Web browser (Chrome, Firefox, Edge)

Remix IDE (for deploying contract)

Step 1: Install Ganache

Download Ganache from: https://trufflesuite.com/ganache/

Install and start Ganache

Note the RPC Server URL (usually http://127.0.0.1:7545)

Step 2: Deploy Smart Contract

Open Remix IDE: https://remix.ethereum.org

Create new file: DocumentNotary.sol

Copy and paste the smart contract code

Compile the contract (Solidity Compiler tab)

Connect Remix to Ganache:

Select "External Http Provider" in Environment

Enter: http://127.0.0.1:7545

Deploy the contract

Copy the deployed contract address

Step 3: Setup Web Interface

Open blockchain\_notary.html in your browser

Enter configuration:

RPC URL: http://127.0.0.1:7545

Contract Address: (from Remix)

Wallet Address: (from Ganache)

Private Key: (from Ganache)

Click "Connect to Blockchain"

Step 4: Test the System

Notarize a Document:



Go to "Notarize Document" tab

Enter document content

Enter description

Click "Notarize Document"

Wait for blockchain confirmation

Verify a Document:



Go to "Verify Document" tab

Enter the same document content

Click "Verify Document"

See the notarization details

📝 Smart Contract Functions

notarizeDocument(bytes32 \_documentHash, string \_description)

Notarizes a document by storing its hash on the blockchain.



Parameters:



\_documentHash: SHA-256 hash of the document

\_description: Description of the document

Returns: None (transaction)



verifyDocument(bytes32 \_documentHash)

Verifies if a document exists on the blockchain.



Parameters:



\_documentHash: SHA-256 hash of the document to verify

Returns:



exists: Boolean indicating if document exists

timestamp: Unix timestamp of notarization

owner: Address of the notarizer

description: Description of the document

documentExists(bytes32 \_documentHash)

Checks if a document hash exists.



Returns: Boolean



getOwnerDocuments(address \_owner)

Gets all document hashes for an owner.



Returns: Array of document hashes



🔒 Security Considerations

Private keys are only used locally and not transmitted

Document content is never stored on blockchain (only hashes)

Immutable records prevent tampering

Owner verification ensures authenticity

🎯 Use Cases

Legal document timestamping

Proof of authorship

Contract agreement verification

Certificate authenticity

Intellectual property protection

Academic credential verification

📊 Demo

Notarizing a Document

Input: "This is my important contract"

Description: "Employment Contract 2024"

Result: ✅ Document notarized

Transaction Hash: 0x123...

Block Number: 5

Verifying a Document

Input: "This is my important contract"

Result: ✅ Document found!

Timestamp: 2024-01-15 10:30:45

Owner: 0x95A7C0B4C4196e4D30c2F8C0B2063b10A4A62E13

🐛 Troubleshooting

Cannot connect to blockchain

Ensure Ganache is running

Check RPC URL is correct (http://127.0.0.1:7545)

Verify contract address is correct

Transaction failed

Check wallet has sufficient ETH

Verify private key is correct

Ensure contract is deployed

Document verification fails

Enter exact same content as notarized

Check for extra spaces or characters

Verify document was successfully notarized

🔄 Future Enhancements

&nbsp;File upload functionality

&nbsp;Batch document processing

&nbsp;Document expiration dates

&nbsp;Access control and permissions

&nbsp;Mobile responsive interface

&nbsp;Integration with IPFS for document storage

&nbsp;Multi-signature support

&nbsp;Email notifications


Made with ❤️ using Blockchain Technology






