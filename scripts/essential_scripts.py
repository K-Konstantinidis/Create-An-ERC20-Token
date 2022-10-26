from brownie import accounts, network, config

FORKED_LOCAL_ENVIRONMENTS = [
    "mainnet-fork",
    "mainnet-fork-development",
    "mainnet-fork-dev",
]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["ganache-local", "development"]

# Return:
# if 1: A brownie account we chose from the array
# if 2: A brownie account
# if 3: A personal account from the brownie accounts list
# General: A personal account from the .env file
def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    if id:
        return accounts.load(id)

    return accounts.add(config["wallets"]["from_key"])
