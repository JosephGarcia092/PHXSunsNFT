pragma solidity ^0.5.5;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

/* general structer of the website
KEY NOTE:
 *Initial Buyer* 
step one : 
buy the Nft. using ganache well have the 10 address or people that are buying the Nft. 
first account in ganache will be the "company" who deploys the contract so we have to do an initialBuyNft
to get the first person who will buy from the "company"
the nft needs to have a name, price in eth, who is selling it, and buyer
once the sale has been completed, the buyer of the Nft should then register the Nft and have a mapping of Nft

step two:
once we have gone over the buy of the Nft we want to make sure that we can get the _mintrandomly
to pick one of the 10 wallets to give the ULT Nft. 

step three:
input the royalty function to allow the "inital owner" of the Nft to be able to collect royalties on post buy

*/
contract seasonTicket is ERC721Full {
    constructor() public ERC721Full("Suns", "PHX") {}
// struct of the NFT (name of nft, how much, who is selling)

    struct Nft {
        string name;// of the NFT
        uint256 price;// listing price 
        address payable initialBuyer;// who first bought the Nft
        address payable seller;// who is selling
    }
    mapping(uint256 => Nft) public nftCollection;
    
    function initialBuyNft(
        string memory name, 
        uint256  price, 
        address payable initialBuyer, 
        address payable seller) public view returns (string memory, uint256, address, address) {
        return (name, price, initialBuyer, seller);
    }

    function InitialRegisterNft (
        address payable initialBuyer,
        address payable seller,
        string memory name,
        uint256 price,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();
        _mint(initialBuyer, tokenId);
        _setTokenURI(tokenId, tokenURI);
        nftCollection[tokenId] = Nft(name, price, initialBuyer, seller);
        return tokenId;
    }

    function secondBuyNft(
        string memory name, a
        ddress payable seller, 
        address payable initialBuyer, 
        uint price) public {
        require(initialBuyer == seller, "You are not authorized to sell this");
        require(address(this).balance >= price, "You dont have funds for this");
    }
/*
     function mintRandomly() public {
         uint tokenID = //randomly generate an ID that is within the totalSupply
         _safeMint(to, tokenID);}
*/

  function() external payable {}

}