from brownie import network, config, accounts, MockV3Aggregator, FundMe
from web3 import Web3

FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 20000000000


def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active in FORKED_LOCAL_ENVIRONMENT):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
    #We have to pay attention to what variables the MockV3Aggregator.sol file takes as inputs.
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE,"ether"),{"from": get_account()})
    print("Mocks Deployed!")