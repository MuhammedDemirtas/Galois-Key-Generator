# Galois Key Generation
# Developed by: M.Demirtas
# Description: This script generates cryptographic keys using Galois Field arithmetic.
#              The generated keys are based on an input sequence and a degree-specific irreducible polynomial.
#              It supports both string and numeric inputs.

from sympy import symbols, GF, Poly
import random

def generate_irreducible_polynomial(degree, field_size):
    """
    Generates an irreducible polynomial over a Galois Field (GF).

    Args:
        degree (int): Degree of the polynomial.
        field_size (int): Size of the Galois Field (prime number).

    Returns:
        Poly: An irreducible polynomial in GF(field_size).
    """
    x = symbols('x')
    while True:
        coeffs = [random.randint(1, field_size - 1) for _ in range(degree)] + [1]
        poly = Poly(coeffs, x, modulus=field_size)
        if poly.is_irreducible:
            return poly

def normalize_sequence(input_sequence, target_length):
    """
    Normalizes the input sequence to a target length by padding if necessary.

    Args:
        input_sequence (list): Input sequence to normalize.
        target_length (int): Desired length of the sequence.

    Returns:
        list: Normalized sequence.
    """
    length_diff = target_length - len(input_sequence)
    if length_diff > 0:
        padding = [(input_sequence[-1] + i) % 7 for i in range(length_diff)]
        input_sequence += padding
    return input_sequence

def galois_key_generation(input_sequence, field_size, degree, target_length):
    """
    Generates a cryptographic key in a Galois Field based on the input sequence.

    Args:
        input_sequence (str|int): Input sequence as a string or integer.
        field_size (int): Size of the Galois Field (prime number).
        degree (int): Degree of the irreducible polynomial.
        target_length (int): Desired length of the output key (x: user-defined length).

    Returns:
        list: Generated cryptographic key.
    """
    # Generate an irreducible polynomial over GF
    poly = generate_irreducible_polynomial(degree, field_size)
    print(f"Generated irreducible polynomial: {poly}")

    # Convert input sequence to integers
    if isinstance(input_sequence, str):
        input_sequence = [ord(ch) for ch in input_sequence]  # Convert string to ASCII values
    elif isinstance(input_sequence, int):
        input_sequence = [int(digit) for digit in str(input_sequence)]  # Split number into digits

    # Ensure sequence elements are within the Galois Field
    gf_sequence = [int(ch) % field_size for ch in input_sequence]

    # Normalize the sequence to the target length
    gf_sequence = normalize_sequence(gf_sequence, target_length)

    # Generate the key by mixing the sequence with the polynomial
    key = []
    for i in range(target_length):
        element = sum(poly.coeffs()[j] * gf_sequence[(i + j) % len(gf_sequence)] for j in range(degree))
        element = (element * (i + 1)) % field_size
        key.append(element)

    return key

# Main script execution
if __name__ == "__main__":
    # Input parameters
    input_sequence = "123456789"  # Example input sequence
    field_size = 7  # Galois Field size (must be a prime number)
    degree = 3  # Degree of the irreducible polynomial
    target_length = 32  # Desired length of the key (x: user-defined length)

    # Seed the random generator for reproducibility
    random.seed(42)

    # Generate the cryptographic key
    key = galois_key_generation(input_sequence, field_size, degree, target_length)

    # Convert the key to hexadecimal format
    hex_key = [hex(k)[2:] for k in key]

    # Display the results
    print(f"Input Sequence: {input_sequence}")
    print(f"Generated Key (Hexadecimal): {''.join(hex_key)}")
