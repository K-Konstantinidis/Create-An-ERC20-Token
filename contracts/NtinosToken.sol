// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract NtinosToken is ERC20 {
    string name = "NtinosToken"; // Token name
    string symbol = "KON"; // Token symbol

    // initialSupply in wei
    constructor(uint256 initialSupply) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }
}
