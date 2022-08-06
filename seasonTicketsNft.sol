pragma solidity ^0.5.5;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract seasonTicket is ERC721Full {
    constructor() public ERC721Full("Suns", "PHX") {}

    function buyNft(address owner, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 nftId = totalSupply();
        _mint(owner, nftId);
        _setTokenURI(nftId, tokenURI);

        return nftId;
    }
}
