import streamlit as st 
from mnemonic import Mnemonic 
from bip44 import Wallet
from web3 import Account
import os
from dotenv import load_dotenv
load_dotenv()

####################
# import functions
from Mnemonic import generate_mnemonic

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

@st.cache(allow_output_mutation=True)
def load_contract():

    #### THIS NEEDS TO BE UPDATED
    # Load the contract ABI
    with open(Path('./contracts/compiled/artwork_abi.json')) as f:
        artwork_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=artwork_abi
    )

    return contract

contract = load_contract()
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

@st.cache(allow_output_mutation=True)
def load_contract():

    #### THIS NEEDS TO BE UPDATED
    # Load the contract ABI
    with open(Path('./contracts/compiled/artwork_abi.json')) as f:
        artwork_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=artwork_abi
    )

    return contract

st.title('Phoenix Suns 2023 Season Tickets')

st.header('Welcome to the Future! Introducing NFT Season Tickets!')

col4, col5 = st.columns(2)
col4.metric("Wins", "64", "1.2 °F")
col5.metric("Losses", "18", "-8%")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Standard Package")
    st.write("Tickets and NFT, and 5% off Merchandise for the Season")
    st.image("https://cdn.dribbble.com/users/412468/screenshots/16900443/fdcce1cf-9f49-45d2-a67d-4909891cbe6c.png")

with col2:
    st.header("Ultra Package")
    st.write("Game tickets, $40 F&B Package, NFT, and 10% off Merchandise for the Season")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRmQVCFrB94NgfBTfUmDLRG8zxxvpKol4In3e744IS31p3M_DRHH4LPMqTSvqNOrdO1Qc&usqp=CAU")

with col3:
    st.header("VIP Package")
    st.write("Game tickets, $$100 F&B Package, Photo with Mascot, Raffle for $10k, NFT, and 15% off Merchandise for the Season")
    st.image("https://assets.simpleviewinc.com/simpleview/image/fetch/c_fill,h_690,q_70,w_1040/https://assets.simpleviewinc.com/simpleview/image/upload/crm/chandler/Phoenix-Suns-Logo_A84287DC-5056-A36A-0B2C90380AD9B0DC-a842865c5056a36_a8428fc1-5056-a36a-0be758710200bec8.jpg")

standard_image = "https://cdn.dribbble.com/users/412468/screenshots/16900443/fdcce1cf-9f49-45d2-a67d-4909891cbe6c.png"
ultra_image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRmQVCFrB94NgfBTfUmDLRG8zxxvpKol4In3e744IS31p3M_DRHH4LPMqTSvqNOrdO1Qc&usqp=CAU"
vip_image = "https://assets.simpleviewinc.com/simpleview/image/fetch/c_fill,h_690,q_70,w_1040/https://assets.simpleviewinc.com/simpleview/image/upload/crm/chandler/Phoenix-Suns-Logo_A84287DC-5056-A36A-0B2C90380AD9B0DC-a842865c5056a36_a8428fc1-5056-a36a-0be758710200bec8.jpg"

packages_database = {
    "Standard Package": ["Standard Package", .05, standard_image, "Tickets and NFT, and 5% off Merchandise for the Season"],
    "Ultra Package": ["Ultra Package", .08, ultra_image, "Game tickets, $40 F&B Package, NFT, and 10% off Merchandise for the Season"],
    "VIP Package": ["VIP Package", .09, vip_image, "Game tickets, $$100 F&B Package, Photo with Mascot, Raffle for $10k, NFT, and 15% off Merchandise for the Season"]}

packages = ["Standard Package", "Ultra Package", "VIP Package"]

def package():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(packages_database.values())

    for number in range(len(packages)):
        st.image(db_list[number][2], width=200)
        st.write("Package Type: ", db_list[number][0])
        st.write("Cost in Ethereum: ", db_list[number][1])
        st.write("What's included: ", db_list[number][2])
        st.text(" \n")
        
# Create a select box to choose a package
st.sidebar.markdown("## Select a Package")
select_package = st.sidebar.selectbox("Select a Package", packages)

st.sidebar.markdown("## What's Included")

included = packages_database[select_package][3]
st.sidebar.write(included)

st.sidebar.markdown("## Cost in Ether")
cost = packages_database[select_package][1]
st.sidebar.write(cost)