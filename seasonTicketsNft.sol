pragma solidity ^0.5.5;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract seasonTicket is ERC721Full {// makes it easier and cleans the code up for me. 
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
        address initialBuyer;// who first bought the Nft
        address seller;// who is selling
    }
    mapping(uint256 => Nft) public nftCollection;

    function buyNft (
        string memory name,
         address payable initialBuyer
         ) public payable returns(string memory, address) {
            corporateBalance = address(this).balance;   // buyer sends money to the seasonTicket contract.// nftBalance confirms the money is in the seasonTicket contract
        return(name, initialBuyer);
        }
        // this calls the balance of the users account
        function balance(address owner) public view returns(uint accountBalance) {
            accountBalance = owner.balance;
                // wei_balance = w3.eth.get_balance(address);
                // ether = w3.fromWei(wei_balance, 'ether')
                // return ("ether");
            }

//the contract deployer (first account) pays the gas fees
//with the initialRegisterNft // i can set global variables = my variables in function 
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
// maybe make an event. for the flip. not a function to make the code less bc its an instant 
// one time hapening. \
    function flipNft(
        string memory name,
        address payable seller, 
        address payable Buyer,
        uint price
        )
        public payable returns (string memory, address, address, uint) {
        require(seller == Buyer || Buyer == seller, "You are not authorized to sell this");
        // require()
        return (name, seller, Buyer, price);
    }

    // function corporateWithdrawl(
    //     uint corporateBalance; 
        
    // )
/*
     function mintRandomly() public {
         uint tokenID = //randomly generate an ID that is within the totalSupply
         _safeMint(to, tokenID);}
*/

  function() external payable {}

}