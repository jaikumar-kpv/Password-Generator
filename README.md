# Python Password Generator

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A versatile and secure command-line password generator written in Python. This script allows for the creation of strong, randomized passwords tailored to specific security requirements.

---

## Table of Contents

- [Description](#description)
- [Key Features](#key-features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [As a Standalone Script](#as-a-standalone-script)
  - [As an Imported Module](#as-an-imported-module)
- [Code Documentation](#code-documentation)
  - [`generate_password()` Function](#generate_password-function)
- [Contributing](#contributing)
- [License](#license)

---

## Description

In an era where digital security is paramount, using strong and unique passwords for different services is crucial. This Python Password Generator provides a simple yet powerful tool to create such passwords directly from your terminal. It is built with security and usability in mind, ensuring that passwords are not only random but also meet common complexity requirements by guaranteeing the inclusion of selected character types. The script is self-contained and relies only on Python's standard libraries, making it highly portable and easy to run anywhere.

---

## Key Features

-   **Customizable Length**: Define any password length (minimum of 4 characters).
-   **Character Set Control**: Granular control over the character sets to be used:
    -   Lowercase letters (`a-z`)
    -   Uppercase letters (`A-Z`)
    -   Numeric digits (`0-9`)
    -   Special characters (e.g., `!@#$%^&*()`)
-   **Guaranteed Complexity**: The generated password is guaranteed to contain at least one character from each of the selected types.
-   **Securely Randomized**: Uses Python's `random` module for cryptographic-quality randomness where available (`random.choice` is suitable for this use case). The final password is shuffled to prevent predictable patterns.
-   **Interactive CLI**: An easy-to-use command-line interface guides the user through the password generation process.
-   **Zero Dependencies**: No external libraries are needed. It runs out-of-the-box with a standard Python 3 installation.
-   **Modular Design**: The core logic is encapsulated in a function that can be easily imported and used in other Python applications.

---

## Requirements

-   **Python 3.6** or newer.

---

## Installation

No installation is required. Simply download the `password_generator.py` script to your local machine.

1.  Clone the repository or download the script:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
    Or simply save the Python code into a file named `password_generator.py`.

---

## Usage

You can use this tool in two ways: directly from the command line or by importing it into your own Python scripts.

### As a Standalone Script

Run the script from your terminal and follow the interactive prompts.

```bash
python password_generator.py
