# KON-ERC20-Token
Create your own ERC20 Token: `NtinosToken (KON)`

Create the Token easily with the help of <a href="https://github.com/OpenZeppelin/openzeppelin-contracts/tree/master/contracts/token/ERC20">OpenZeppelin</a>

For more help check their <a href="https://docs.openzeppelin.com/contracts/4.x/erc20">documentation</a>

## NtinosToken.sol

- A smart contract to __create__ your own ERC20 Token

## What's an ERC20 Token

``` 
An ERC-20 is the technical standard for fungible tokens created using the Ethereum blockchain. 
A fungible token is one that is interchangeable with another token. 
```

## Deploy.py
A python script to: 
 - Connect to a Blockchain `(Testnet, Mainnet)`
 - Get an account safely
   - Use the `essential_scripts.py`
 - Deploy our contract

## Essential_Scripts.py
Get an account safely:
 - From a local or a forked local blockchain environment
 - A real one which we saved in the brownie accounts list
 - A real one via the config & .env file

## Help with the project
To run the code there are some requirements. You must install: 

### pipx 
Install _pipx_ by running the following on the command line: `python -m pip install --user pipx` then `python3 -m pipx ensurepath`

For more information check: <a href="https://pypa.github.io/pipx/">Install pipx</a>

### Brownie
Install _Brownie_ by running the following on the command line: `pip install eth-brownie`

For more information check: <a href="https://pypi.org/project/eth-brownie/">Install Brownie</a>
