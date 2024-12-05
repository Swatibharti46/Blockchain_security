from solcx import compile_standard

# Sample contract to check
contract_code = """
pragma solidity ^0.8.0;

contract Reentrancy {
    mapping(address => uint) public balances;

    // Vulnerable function
    function withdraw(uint amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // Reentrancy vulnerability
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        balances[msg.sender] -= amount;
    }

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }
}
"""

# Compile the contract to check for errors
compiled_contract = compile_standard({
    'language': 'Solidity',
    'sources': {'Reentrancy.sol': {'content': contract_code}},
    'settings': {'outputSelection': {'*': {'*': ['abi', 'evm.bytecode']}}}
})

# Check for potential reentrancy vulnerability patterns
def check_reentrancy_vulnerability(contract_code):
    if '.call{' in contract_code:
        print("Warning: Possible reentrancy vulnerability detected (use of .call).")
    else:
        print("No obvious reentrancy vulnerability detected.")
    
    if 'require(success' in contract_code:
        print("Warning: Reentrancy vulnerability might be present (failure handling of external calls).")
    
    if 'balances[msg.sender] -= amount;' not in contract_code:
        print("Warning: Effects should be applied after external calls (checks-effects-interactions pattern).")

check_reentrancy_vulnerability(contract_code)
