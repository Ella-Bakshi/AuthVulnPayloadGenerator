# AuthVulnPayloadGenerator

## Introduction

The code in this repository is designed to generate payload lists for authentication vulnerability testing. It helps simulate scenarios where, for example, an attacker might evade IP-blocking mechanisms by logging into their own account periodically, thus preventing failed login attempt limitations from being reached. This Python script allows users to create customized lists of usernames and passwords for such testing.

## Usage

The script allows the creation of either usernames or passwords lists, with the option to repeat them a specified number of times. The lists are saved into two separate files: `output_user.txt` for usernames and `output_password.txt` for passwords.

## How It Works

1. **Selection of Type**: The user chooses between generating a list of usernames (enter `0`) or passwords (enter `1`).
2. **Validation of Input**: The user is prompted for the number of unique items in the list, and input is validated to ensure it is a number.
3. **Item Input**: The user enters the required usernames or passwords.
4. **Repetition**: The list is repeated in the output file as many times as specified.
5. **File Output**: The repeated list is written to a text file.

## Installation

1. Clone the repository: `git clone https://github.com/Ella-Bakshi/AuthVulnPayloadGenerator.git`
2. Navigate to the cloned directory.
3. Run the script using Python 3: `python auth_list_creator.py`

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
