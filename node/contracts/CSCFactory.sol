// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./CSC.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "./IFactoryERC721.sol";
import "./ContextMixin.sol";


contract CSCFactory is FactoryERC721, Ownable, ContextMixin{

    event Transfer(
        address indexed from,
        address indexed to,
        uint256 indexed tokenId
    );

    uint256 public constant MAX_COOL_SHEEPS = 10000;

    uint256 NUM_OPTIONS = 2;
    uint256 SINGLE_COOL_SHEEP_OPTION = 0;
    uint256 MULTIPLE_COOL_SHEEPS_OPTION = 1;
    uint256 NUM_COOL_SHEEPS_IN_MULTIPLE_CREATURE_OPTION = 5;

    address public nftAddress;
    address public proxyAdress;
    string public baseURI;

    constructor(address _proxyAddress, address _nftAddress) {
        proxyAdress = _proxyAddress;
        nftAddress = _nftAddress;

        fireTransferEvents(address(0), owner());
    }

    function name() override external pure returns (string memory) {
        return "Cool Sheep Club Factory";
    }

    function symbol() override external pure returns (string memory) {
        return "CSCF";
    }

    function supportsFactoryInterface() override public pure returns (bool) {
        return true;
    }

    function numOptions() override public view returns (uint256) {
        return NUM_OPTIONS;
    }

    function canMint(uint256 _optionId) override public view returns (bool) {
        if (_optionId >= NUM_OPTIONS) {
            return false;
        }

        CSC CoolSheep = CSC(nftAddress);
        uint256 CoolSheepSupply = CoolSheep.totalSupply();

        uint256 numItemsAllocated = 0;
        if (_optionId == SINGLE_COOL_SHEEP_OPTION) {
            numItemsAllocated = 1;
        } else if (_optionId == MULTIPLE_COOL_SHEEPS_OPTION) {
            numItemsAllocated = NUM_COOL_SHEEPS_IN_MULTIPLE_CREATURE_OPTION;
        }
        return CoolSheepSupply < (MAX_COOL_SHEEPS - numItemsAllocated);
    }

    function tokenURI(uint256 _optionId) override external view returns (string memory) {
        return string(abi.encodePacked(baseURI, Strings.toString(_optionId)));
    }

    function setBaseURI(string memory _baseURI) public onlyOwner{
        baseURI = _baseURI;
    }

    function mint(uint256 _optionId, address _toAddress) override public {
        assert(
            proxyAdress == _msgSender() ||
                owner() == _msgSender()
        );
        
        require(canMint(_optionId));

        CSC CoolSheep = CSC(nftAddress);
        if (_optionId == SINGLE_COOL_SHEEP_OPTION) {
            CoolSheep.mintTo(_toAddress);
        } else if (_optionId == MULTIPLE_COOL_SHEEPS_OPTION) {
            for (uint256 i = 0;
                i < NUM_COOL_SHEEPS_IN_MULTIPLE_CREATURE_OPTION;
                i++
            ) {
                CoolSheep.mintTo(_toAddress);
            }
        }
    }

    function transferOwnership(address newOwner) override public onlyOwner {
        address _prevOwner = owner();
        super.transferOwnership(newOwner);
        fireTransferEvents(_prevOwner, newOwner);
    }

    function fireTransferEvents(address _from, address _to) private {
        for (uint256 i = 0; i < NUM_OPTIONS; i++) {
            emit Transfer(_from, _to, i);
        }
    }

    function transferFrom(
        address _from,
        address _to,
        uint256 _tokenId
    ) public {
        mint(_tokenId, _to);
    }

    function isApprovedForAll(address _owner, address _operator)
        public
        view
        returns (bool)
    {
        if (owner() == _owner && _owner == _operator) {
            return true;
        }
        if (
            owner() == _owner &&
            proxyAdress == _operator
        ) {
            return true;
        }

        return false;
    }

    function ownerOf(uint256 _tokenId) public view returns (address _owner) {
        return owner();
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