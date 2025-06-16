import click
from rich.console import Console
from rich.panel import Panel
from rich import print as rprint

console = Console()

def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    """
    Encrypt or decrypt text using Caesar cipher.
    
    Args:
        text (str): The text to encrypt/decrypt
        shift (int): The shift value
        decrypt (bool): If True, decrypt the text; if False, encrypt it
    
    Returns:
        str: The encrypted/decrypted text
    """
    if decrypt:
        shift = -shift
    
    result = []
    for char in text:
        if char.isalpha():
            # Determine the base ASCII value (a=97, A=65)
            base = ord('a') if char.islower() else ord('A')
            # Apply the shift and wrap around using modulo 26
            shifted = (ord(char) - base + shift) % 26
            # Convert back to character
            result.append(chr(base + shifted))
        else:
            # Keep non-alphabetic characters unchanged
            result.append(char)
    
    return ''.join(result)

@click.group()
def cli():
    """Caesar Cipher CLI - Encrypt and decrypt text using the Caesar cipher algorithm."""
    pass

@cli.command()
@click.option('--text', '-t', prompt='Enter text to encrypt', help='Text to encrypt')
@click.option('--shift', '-s', prompt='Enter shift value', type=int, help='Shift value for encryption')
def encrypt(text: str, shift: int):
    """Encrypt text using Caesar cipher."""
    encrypted = caesar_cipher(text, shift)
    console.print(Panel(
        f"[green]Original text:[/green] {text}\n[blue]Encrypted text:[/blue] {encrypted}",
        title="Encryption Result",
        border_style="blue"
    ))

@cli.command()
@click.option('--text', '-t', prompt='Enter text to decrypt', help='Text to decrypt')
@click.option('--shift', '-s', prompt='Enter shift value', type=int, help='Shift value for decryption')
def decrypt(text: str, shift: int):
    """Decrypt text using Caesar cipher."""
    decrypted = caesar_cipher(text, shift, decrypt=True)
    console.print(Panel(
        f"[green]Encrypted text:[/green] {text}\n[blue]Decrypted text:[/blue] {decrypted}",
        title="Decryption Result",
        border_style="blue"
    ))

if __name__ == '__main__':
    cli() 