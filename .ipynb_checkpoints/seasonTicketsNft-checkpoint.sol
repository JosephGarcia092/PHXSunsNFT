pragma solidity ^0.5.5;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
contract seasonTicket is ERC721Full {
    // makes it easier and cleans the code up for me. 
    uint public corporateBalance;
    
    // address payable PHX_owner;
    // address initialBuyer;
    // address seller;
    // string name;
    // uint price;

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

    // function buyNft() public payable {
    //     uint amount = msg.value * exchange_rate;
    //     balances[msg.sender] += amount;
    //     owner.transfer(msg.value);
    // }
    function buyNft (
        string memory name,
         address initialBuyer
         ) public payable returns(string memory, address) {
            corporateBalance = address(this).balance;
        // buyer sends money to the seasonTicket contract. 
        // nftBalance confirms the money is in the seasonTicket contract
        return(name, initialBuyer);
        }
        // this calls the balance of the users account
        function balance(address owner) public view returns(uint accountBalance) {
            accountBalance = owner.balance;
            }
// the contract deployer (first account) pays the gas fees with the initialRegisterNft 
// i can set global variables = my variables in function to keep cleaner code. 
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
// this pays to the contract. everything above works as it should just the bottom stuff needs work.
// take a break the basic stuff of the project still works.
//there is no logic to keep records of the balance for the contract. (savings HW)
    function flipNft(
        string memory name, //  name of NFT 
        address payable seller, // person who owns it initially. 
        address payable initialBuyer, // the person who is buying the flip
        uint price) public payable returns (string memory, address, address, uint) {
        require(seller == initialBuyer, "You are not authorized to sell this"); // so that the seller cannot buy it to himself 
        require(address(this).balance >= price, "You dont have funds for this");// not sure if this is working or not. might delete later. lol
        corporateBalance = address(this).balance + price;
        return (name, seller, initialBuyer, price);
    }// this actually worked... the Company cannot buy back the NFTs.... (^)_(^)
    //

    // function corporateWithdrawl(\
    //     uint corporateBalance; 
        
    // )
/*
     function mintRandomly() public {
         uint tokenID = //randomly generate an ID that is within the totalSupply
         _safeMint(to, tokenID);}
*/

  function() external payable {}

}