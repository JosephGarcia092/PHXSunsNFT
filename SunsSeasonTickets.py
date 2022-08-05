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

st.title('Phoenix Suns 2023 Season Tickets')

st.header('Welcome to the Future! Introducing NFT Season Tickets!')

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Standard Package")
    st.write("")
    st.image("https://www.gannett-cdn.com/presto/2021/05/20/PPHX/ef2c47f9-7893-49b8-b6dd-28be395930df-Playoffs_Round_1_Matchup_Announcement_Graphics_Social_4x5.jpg")

with col2:
    st.header("Ultra Package")
    st.write("")
    st.image("https://www.gannett-cdn.com/presto/2021/05/20/PPHX/ef2c47f9-7893-49b8-b6dd-28be395930df-Playoffs_Round_1_Matchup_Announcement_Graphics_Social_4x5.jpg")

with col3:
    st.header("VIP Package")
    st.write("")
    st.image("https://www.gannett-cdn.com/presto/2021/05/20/PPHX/ef2c47f9-7893-49b8-b6dd-28be395930df-Playoffs_Round_1_Matchup_Announcement_Graphics_Social_4x5.jpg")

Standard = col1
Ultra = col2
VIP = col3

options = [Standard, Ultra, VIP]

