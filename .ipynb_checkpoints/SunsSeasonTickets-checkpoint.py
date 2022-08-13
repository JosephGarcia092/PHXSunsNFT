import os
import json
from web3 import Web3
from web3 import Account
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
st.set_page_config(layout="wide")
load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Cache the contract on load
@st.cache(allow_output_mutation=True)
# Define the load_contract function
def load_contract():

    # Load Art Gallery ABI
    with open(Path('./compiled/trial2.json')) as f:
        project_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=project_abi
    )
    # Return the contract from the function
    return contract


# Load the contract
contract = load_contract()



### Setting up front end
st.title('Phoenix Suns 2023 Season Tickets')

st.header('Welcome to the Future! Introducing NFT Season Tickets!')
st.subheader("Upon purchase of your package you will be able to generate your own NFT! Each NFT will be unique and individual to you, make sure you hold on to them because you will receive a discount on all future merchandise.")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Standard Package")
    st.write("")
    st.write("Game ticket, NFT, and 5% off Merchandise for the Season")
    st.write("Tickets will be available in Section 106 - 110 or 117 - 123")
    st.write("")
    st.write("")    
    st.image("https://cdn.dribbble.com/users/412468/screenshots/16900443/fdcce1cf-9f49-45d2-a67d-4909891cbe6c.png?compress=1&resize=500x400")

with col2:
    st.header("Ultra Package")
    st.write("")
    st.write("Game ticket, $40 F&B Package, NFT, and 10% off Merchandise for the Season")
    st.write("Tickets will be available in Section 101 - 105 or 111 - 116")
    st.write("")
    st.write("")    
    st.image("https://cdn.dribbble.com/users/1785078/screenshots/3644361/media/bbe8083c5426965690c4c0db01803947.png?compress=1&resize=500x400")

with col3:
    st.header("VIP Package")
    st.write("Game ticket, $$100 F&B Package, Photo with Mascot, Raffle for $10k, NFT, and 15% off Merchandise for the Season")
    st.write("Tickets will be available in Section 101 - 105 or 111 - 116 lower levels (not including courtside or rows 1-8)")
    st.image("https://cdn.dribbble.com/users/51266/screenshots/3916926/phoenix_basketball.png?compress=1&resize=500x400")
    
col4, col5 = st.columns(2)
col4.metric("Wins ('21-'22)", "64", "13")
col5.metric("Losses ('21-'22)", "18", "-3", delta_color="inverse")

standard_image = "https://cdn.dribbble.com/users/412468/screenshots/16900443/fdcce1cf-9f49-45d2-a67d-4909891cbe6c.png?compress=1&resize=500x400"
ultra_image = "https://cdn.dribbble.com/users/1785078/screenshots/3644361/media/bbe8083c5426965690c4c0db01803947.png?compress=1&resize=400x300"
vip_image = "https://cdn.dribbble.com/users/51266/screenshots/3916926/phoenix_basketball.png?compress=1&resize=500x400"

packages_database = {
    "Standard Package": ["Standard Package", 2, standard_image, "Game ticket, NFT, and 5% off Merchandise for the Season"],
    "Ultra Package": ["Ultra Package", 5, ultra_image, "Game ticket, $40 F&B Package, NFT, and 10% off Merchandise for the Season"],
    "VIP Package": ["VIP Package", 10, vip_image, "Game ticket, $$100 F&B Package, Photo with Mascot, Raffle for $10k, NFT, and 15% off Merchandise for the Season"]}

packages = ["Standard Package", "Ultra Package", "VIP Package"]

def package():
    """"""
    db_list = list(packages_database.values())

    for number in range(len(packages)):
        st.image(db_list[number][2], width=200)
        st.write("Package Type: ", db_list[number][0])
        st.write("Cost in Ethereum: ", db_list[number][1])
        st.write("What's included: ", db_list[number][2])
        st.text(" \n")
        
# Create a select box to choose a package
st.sidebar.markdown("## Select a Package")
select_package = st.sidebar.selectbox("Packages", packages)

st.sidebar.markdown("## What's Included")

included = packages_database[select_package][3]
st.sidebar.write(included)

st.sidebar.markdown("## Cost in Ether")
cost = packages_database[select_package][1]
st.sidebar.write(cost)

st.sidebar.markdown("## Choose an Account")
accounts = w3.eth.accounts
account = accounts[0]
your_count = st.selectbox("Select Account", options=accounts) ## possible steamlit issue
st.markdown("---")
## first try at attempt to get the variable to call buyNft. 
string = select_package
address = account
## i was trying to figure out the code of this. 
if st.button("Purchase Package"):
    tx_hash = contract.functions.buyNft(string, address).transact(
        {'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    st.markdown("---")
#




### Generate NFT button
transaction_id = st.number_input("Enter transaction hash id to display NFT:", step=1)

#if st.button("Generate NFT"):
    
    #nft_owner = contract.functions.ownerOf(transaction_id).call()
    #st.write(f"This NFT is awarded to {transaction_id}")
    
import random
one = "1.0.png"
two = "1.14.png"
three = "1.3.png"
image_list = [one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,one,two,two,two,two,two,two,two,two,three,three,three,three,three,three,three]
random.shuffle(image_list)

if st.button("Generate NFT"):
    st.image(image_list[0])
    