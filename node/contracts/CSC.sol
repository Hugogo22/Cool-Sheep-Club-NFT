// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "./ContextMixin.sol";

contract CSC is ERC721, ERC721Enumerable, Ownable, ContextMixin {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIds;

    uint256 public constant MAX_COOL_SHEEPS = 10000;

    address public proxyAdress;
    string private CSCBaseURI;

    constructor(address _proxyAddress) ERC721("Cool Sheep Club", "CSC") {
        proxyAdress = _proxyAddress;
    }

    function mintTo(address recipient)
        public onlyOwner
        returns (uint256)
    {
        require(
            _tokenIds.current() < MAX_COOL_SHEEPS
        );
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _safeMint(recipient, newItemId);

        return newItemId;
    }

    function batchMintTo(uint256 _amount, address _toAddress) public onlyOwner{
        require((_tokenIds.current() + _amount) <= MAX_COOL_SHEEPS);

        for (uint256 i = 0;
            i < _amount;
            i++
        ) {
            mintTo(_toAddress);
        }
    }

    function _baseURI() internal view override returns (string memory) {
        return CSCBaseURI;
    }

    function setBaseURI(string memory baseURI_) public onlyOwner{
        CSCBaseURI = baseURI_;
    }

    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    function isApprovedForAll(
        address _owner,
        address _operator
    ) public override view returns (bool isOperator) {
        // if OpenSea's ERC721 Proxy Address is detected, auto-return true
        if (_operator == proxyAdress) {
            return true;
        }
        
        // otherwise, use the default ERC721.isApprovedForAll()
        return ERC721.isApprovedForAll(_owner, _operator);
    }

    function _msgSender()
        internal
        override
        view
        returns (address sender)
    {
        return ContextMixin.msgSender();
    }
}