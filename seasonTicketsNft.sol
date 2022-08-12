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
    uint public nftBalance;
    constructor() public ERC721Full("Suns", "PHX") {}
// struct of the NFT (name of nft, how much, who is selling)

    struct Nft {
        string name;// of the NFT
        uint256 price;// listing price 
        address payable initialBuyer;// who first bought the Nft
        address payable seller;// who is selling
    }
    mapping(uint256 => Nft) public nftCollection;
    // mapping(string =>)

    function buyNft (string memory name, address initialBuyer) public payable returns(string memory, address) {
        // make a require ### here ###
         nftBalance = address(this).balance;
        // buyer sends money to the seasonTicket contract. 
        // nftBalance confirms the money is in the seasonTicket contract
        return(name, initialBuyer);
    }
// the contract deployer (first account) pays the gas fees
// with the initialRegisterNft 
    function InitialRegisterNft (
        address payable initialBuyer,
        address payable seller,
        string memory name,
        uint256 price
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();
        _mint(initialBuyer, tokenId);
        nftCollection[tokenId] = Nft(name, price, initialBuyer, seller);
        return tokenId;
    }
// maybe make an event. for the flip. not a function to make the code less bc its an instant 
// one time hapening. \
    function flipNft(
        string memory name,
        address payable seller, 
        address payable initialBuyer, 
        uint price) public payable returns (string memory, address, address, uint) {
        require(seller == initialBuyer, "You are not authorized to sell this");
        require(address(this).balance >= price, "You dont have funds for this");
        flipBalance = address(this).balance;
        return (name, seller, initialBuyer, price);
    }

    // function corporateWithdrawl(
    //     address payable seller,
    // )
/*
     function mintRandomly() public {
         uint tokenID = //randomly generate an ID that is within the totalSupply
         _safeMint(to, tokenID);}
*/

  function() external payable {}

}