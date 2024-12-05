# Blockchain Security: Reentrancy Vulnerability Detection

## Overview

This repository contains a Python script that detects **reentrancy vulnerabilities** in Ethereum smart contracts written in Solidity. Reentrancy is a common security flaw in smart contracts that can lead to unexpected behavior, such as draining funds from the contract.

The script analyzes Solidity code for patterns that could potentially lead to reentrancy attacks, such as:
- Use of `.call{}` for transferring Ether without proper safety checks.
- Violation of the **checks-effects-interactions pattern**, which increases the risk of reentrancy attacks.

## Features

- **Reentrancy Detection**: The script checks for the use of vulnerable functions like `.call` or `.transfer`.
- **Checks-Effects-Interactions Check**: Ensures that state changes occur after external calls, reducing the risk of reentrancy.
- **Simple Solidity Analysis**: A straightforward Python-based tool to scan smart contract code.

## Prerequisites

- Python 3.x
- `py-solc-x` library for compiling Solidity code

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Swatibharti46/Blockchain-Security.git
   cd Blockchain-Security

     pip install solcx bash
   ```
 
The script will analyze the contract and print warnings if potential reentrancy vulnerabilities are detected.


Contributing
  Feel free to fork the repository and submit pull requests if you have suggestions for improvements, bug fixes, or additional features!

License
This project is open-source and available under the MIT License.

This README provides a clear overview of your project, its installation, and usage instructions.

