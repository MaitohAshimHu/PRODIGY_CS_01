Caesar Cipher CLI
A modern command-line tool for encrypting and decrypting text using the Caesar cipher algorithm.
Features
- Encrypt and decrypt text using the Caesar cipher
- Clean and intuitive CLI interface
- Supports both uppercase and lowercase letters
- Preserves non-alphabetic characters
- Interactive prompts for user-friendly input
  
Installation
Using a Virtual Environment (Recommended)
- Clone the repository:
- 
git clone https://github.com/your-repo-url.git
cd your-repo-folder

- Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows

- Install dependencies:
pip install -r requirements.txt


Usage
Encrypt Text
python caesar_cipher.py encrypt


or with options:
python caesar_cipher.py encrypt --text "Hello World" --shift 3


Deactivate Virtual Environment
To exit the virtual environment after use, simply run:
deactivate




