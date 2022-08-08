pragma solidity ^0.5.5;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
/*import "./utils/introspection/IERC165.sol";
interface IERC2981 is IERC165 {
    /**
     * @dev Returns how much royalty is owed and to whom, based on a sale price that may be denominated in any unit of
     * exchange. The royalty amount is denominated and should be paid in that same unit of exchange.
     
    function royaltyInfo(uint256 tokenId, uint256 salePrice)
        external
        view
        returns (address receiver, uint256 royaltyAmount);
*/
contract seasonTicket is ERC721Full {
    constructor() public ERC721Full("Suns", "PHX") {}
// struct of the NFT (name of nft, how much, who is selling)

    struct Nft {
        string name;// of the NFT
        uint256 price;// listing price 
        address payable seller;// who is selling
        address payable buyer;// who is buying 

    }
    mapping(uint256 => Nft) public nftCollection;

    function registerNft (
        address owner,
        string memory name,
        uint256 price,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();
        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);
        nftCollection[tokenId] = Nft(name, price, seller);

        return tokenId;
    }

    function buyNft(string name, address payable seller, address payable buyer, unit256 price) public {
        require(recipient == buyer || recipient == seler, "You are not authorized to sell this");
        require(address(this).balance >= price, "You dont have funds for this");
        return msg.sender.transfer(price)
    

    }
}
/*
 function mintRandomly() public{
  uint tokenID = /*randomly generate an ID that is within the totalSupply
 _safeMint(to, tokenID)

}*/