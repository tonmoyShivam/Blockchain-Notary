// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DocumentNotary {
    // Structure to store document information
    struct Document {
        bytes32 documentHash;
        uint256 timestamp;
        address owner;
        string description;
        bool exists;
    }
    
    // Mapping from document hash to Document
    mapping(bytes32 => Document) public documents;
    
    // Mapping to track documents by owner
    mapping(address => bytes32[]) public ownerDocuments;
    
    // Events
    event DocumentNotarized(
        bytes32 indexed documentHash,
        address indexed owner,
        uint256 timestamp,
        string description
    );
    
    event DocumentVerified(
        bytes32 indexed documentHash,
        bool exists,
        uint256 timestamp,
        address owner
    );
    
    // Notarize a document
    function notarizeDocument(bytes32 _documentHash, string memory _description) public {
        require(!documents[_documentHash].exists, "Document already notarized");
        
        documents[_documentHash] = Document({
            documentHash: _documentHash,
            timestamp: block.timestamp,
            owner: msg.sender,
            description: _description,
            exists: true
        });
        
        ownerDocuments[msg.sender].push(_documentHash);
        
        emit DocumentNotarized(_documentHash, msg.sender, block.timestamp, _description);
    }
    
    // Verify a document
    function verifyDocument(bytes32 _documentHash) public view returns (
        bool exists,
        uint256 timestamp,
        address owner,
        string memory description
    ) {
        Document memory doc = documents[_documentHash];
        return (doc.exists, doc.timestamp, doc.owner, doc.description);
    }
    
    // Get all documents for an owner
    function getOwnerDocuments(address _owner) public view returns (bytes32[] memory) {
        return ownerDocuments[_owner];
    }
    
    // Get document count for an owner
    function getOwnerDocumentCount(address _owner) public view returns (uint256) {
        return ownerDocuments[_owner].length;
    }
    
    // Check if document exists
    function documentExists(bytes32 _documentHash) public view returns (bool) {
        return documents[_documentHash].exists;
    }
}