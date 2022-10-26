from brownie import NtinosToken, network, config
from scripts.essential_scripts import get_account
from web3 import Web3

# Choose your initial supply
# initial_supply in Wei
initial_supply = Web3.toWei(2000, "ether")

# Deploy our smart contract
def deploy_token():
    account = get_account()  # Get an account before the deployment
    token = NtinosToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(f"Deployed Token: {token.name()} ({token.symbol()})")
    print(f"With a total supply of: {token.totalSupply()}")
    return token


def main():
    deploy_token()
