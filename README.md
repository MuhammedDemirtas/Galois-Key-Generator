
# Galois Key Generator (Irreducible)

This project is a Python-based cryptographic key generator that leverages Galois Field (GF) mathematics. The tool generates secure keys based on a user-provided input sequence and an irreducible polynomial of user-defined degree.

## Features

- **Irreducible Polynomial Generation**:
  - Automatically generates irreducible polynomials over a Galois Field (GF) with a specified degree.
  
- **Input Flexibility**:
  - Supports both string and numeric input sequences.
  - Dynamically normalizes input sequences to match the desired key length.

- **Customizable Key Length**:
  - Users can define the desired length (`x`) of the generated cryptographic key.

- **Hexadecimal Key Output**:
  - Outputs the generated cryptographic key in an easy-to-use hexadecimal format.

- **Reproducible Results**:
  - Ensures the same input produces the same key using a fixed random seed.

## Installation

To use the Galois Key Generator, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/MuhammedDemirtas/Galois-Key-Generator.git
    cd Galois-Key-Generator
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:
    ```bash
    python Galois_Hash_Generator.py
    ```

## Usage

1. Edit the input parameters in the script:
    - **Input Sequence (`input_sequence`)**: A string or integer sequence.
    - **Field Size (`field_size`)**: Size of the Galois Field (must be a prime number).
    - **Degree (`degree`)**: Degree of the irreducible polynomial.
    - **Target Length (`target_length`)**: Desired length of the cryptographic key.

2. Run the script to generate a key. Example:
    ```bash
    python Galois_Hash_Generator.py
    ```

3. The output will include:
    - The generated irreducible polynomial.
    - The hexadecimal representation of the cryptographic key.

## Example

Input parameters:
```python
input_sequence = "123456789"
field_size = 7
degree = 3
target_length = 32
```

Output:
```
Generated irreducible polynomial: Poly(-x**3 - x**2 - 2*x + 1, x, modulus=7)
Input Sequence: 123456789
Generated Key (Hexadecimal): 23320404214600641460064146006455
```

## Code Overview

- **`generate_irreducible_polynomial()`**:
  Generates an irreducible polynomial over a Galois Field (GF).

- **`normalize_sequence()`**:
  Normalizes input sequences to match the target length.

- **`galois_key_generation()`**:
  Produces cryptographic keys by combining the input sequence with the polynomial.

- **Main Script**:
  Handles user inputs, calls the required functions, and displays the results.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Author

Developed by **M. Demirtas**. Contributions and feedback are welcome!
