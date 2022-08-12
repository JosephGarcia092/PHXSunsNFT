tx_hash = contract.functions.buyNft(
    token_id,
    int(new_appraisal_value),
    report_uri).transact({"from": w3.eth.accounts[0]})
receipt = w3.eth.waitForTransactionReceipt(tx_hash)st.write(receipt)