# UnitTests

This repository provides a collection of Python unit tests for core banking operations. The main focus is on testing the `BankAccount` class and its behaviors, ensuring reliability and correctness for typical account management tasks.

## Features

- **Initial Balance Verification**: Ensures accounts start with the correct balance.
- **Deposit and Withdrawal**: Tests basic deposit and withdrawal logic, including insufficient funds handling.
- **Overdraft Protection**: Validates overdraft limits and correct error raising when limits are exceeded.
- **Transfers**: Checks successful and failed transfers between accounts, including edge cases like overdraft and invalid amounts.

## Example Test Scenarios

- Depositing funds and verifying updated balances.
- Withdrawing with and without sufficient funds, including overdraft scenarios.
- Transferring funds between accounts with standard and overdraft-enabled logic.

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/basinx/UnitTests.git
    cd UnitTests
    ```
2. Run tests with Python's unittest:
    ```sh
    python -m unittest test_bank_account.py
    ```

## Structure

- `test_bank_account.py` — Contains the test cases for the `BankAccount` class.

## Requirements

- Python 3.x

## License

This repository currently does not specify a license. Please contact the repository owner for usage details.

---

For more details, see [test_bank_account.py](https://github.com/basinx/UnitTests/blob/main/test_bank_account.py).
