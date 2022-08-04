import os
from dotenv import load_dotenv
load_dotenv()
from mnemonic import Mnemonic
from bip44 import Wallet
from web3 import Account

###########



###########

def generate_mnemonic():
    mnemonic = os.getenv("MNEMONIC")
    if mnemonic is None:
        mnemo = Mnemonic("english")
        mnemonic = mnemo.generate(strength=128)
    return mnemonic


