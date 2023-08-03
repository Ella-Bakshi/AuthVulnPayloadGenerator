# AuthVulnPayloadGenerator

## Introduction

The code in this repository is designed to generate payload lists for authentication vulnerability testing. It helps simulate scenarios where, for example, an attacker might evade IP-blocking mechanisms by logging into their own account periodically, thus preventing failed login attempt limitations from being reached. This Python script allows users to create customized lists of usernames and passwords for such testing, including an alternating username list option to simulate controlled periodic logins by an attacker.

## Usage

The script allows the creation of usernames or passwords lists, or an alternating username list with an attacker-controlled username at specified intervals. The lists are saved into separate files depending on the chosen type.

## How It Works

1. **Selection of Type**: The user chooses between generating a list of usernames (enter `0`), passwords (enter `1`), or an alternating username list with attacker-controlled username (enter `2`).
2. **Frequency Input**: If option `2` is selected, the user must enter the frequency of the attacker-controlled username in the list.
3. **Validation of Input**: The user is prompted for the number of unique items in the list, and input is validated to ensure it is a number.
4. **Item Input**: The user enters the required usernames, passwords, or alternating usernames with an attacker-controlled username.
5. **Repetition**: The list is repeated in the output file as many times as specified.
6. **File Output**: The repeated list is written to a text file, with the filename dependent on the type selected.

## Installation

1. Clone the repository: `git clone https://github.com/Ella-Bakshi/AuthVulnPayloadGenerator.git`
2. Navigate to the cloned directory.
3. Run the script using Python 3: `python3 auth_list_creator.py`

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
