# Caesar Cipher CLI

A modern command-line tool for encrypting and decrypting text using the Caesar cipher algorithm.

## Features

- Encrypt and decrypt text using the Caesar cipher
- Beautiful CLI interface with rich text formatting
- Support for both uppercase and lowercase letters
- Preserves non-alphabetic characters
- Interactive prompts for input

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Encrypt Text
```bash
python caesar_cipher.py encrypt
```
or with options:
```bash
python caesar_cipher.py encrypt --text "Hello World" --shift 3
```

### Decrypt Text
```bash
python caesar_cipher.py decrypt
```
or with options:
```bash
python caesar_cipher.py decrypt --text "Khoor Zruog" --shift 3
```

### Get Help
```bash
python caesar_cipher.py --help
```

## Example

Encrypting "Hello World" with a shift of 3:
```bash
python caesar_cipher.py encrypt --text "Hello World" --shift 3
```
Output: "Khoor Zruog"

Decrypting "Khoor Zruog" with a shift of 3:
```bash
python caesar_cipher.py decrypt --text "Khoor Zruog" --shift 3
```
Output: "Hello World" 