
"""
Task 14: NumPy Matrix Operations

Operations:
1. Matrix addition
2. Matrix subtraction
3. Matrix multiplication
4. Matrix transpose
"""

import numpy as np


def display_matrix(title, matrix):
    """Print a matrix with a descriptive title."""
    print(f"\n{title}")
    print("-" * 40)
    print(matrix)


def main():
    # Create two manually defined matrices.
    matrix_a = np.array([
        [1, 2],
        [3, 4]
    ])

    matrix_b = np.array([
        [5, 6],
        [7, 8]
    ])

    # Validate that the matrices have compatible dimensions.
    if matrix_a.shape != matrix_b.shape:
        print("Error: Addition and subtraction require equal shapes.")
        return

    print("=" * 50)
    print("          NUMPY MATRIX OPERATIONS")
    print("=" * 50)

    display_matrix("Matrix A:", matrix_a)
    display_matrix("Matrix B:", matrix_b)

    print(f"\nShape of Matrix A: {matrix_a.shape}")
    print(f"Shape of Matrix B: {matrix_b.shape}")

    # Element-wise addition and subtraction.
    addition = matrix_a + matrix_b
    subtraction = matrix_a - matrix_b

    # Matrix multiplication using the @ operator.
    if matrix_a.shape[1] == matrix_b.shape[0]:
        multiplication = matrix_a @ matrix_b
        display_matrix("Matrix Multiplication (A @ B):",
                       multiplication)
    else:
        multiplication = None
        print("\nMatrix multiplication is not possible "
              "for these dimensions.")

    # Transpose of each matrix.
    transpose_a = matrix_a.T
    transpose_b = matrix_b.T

    display_matrix("Addition (A + B):", addition)
    display_matrix("Subtraction (A - B):", subtraction)
    display_matrix("Transpose of Matrix A:", transpose_a)
    display_matrix("Transpose of Matrix B:", transpose_b)

    print("\nKEY CONCEPTS")
    print("-" * 40)
    print("Addition and subtraction operate element by element.")
    print("The @ operator performs matrix multiplication.")
    print("The .T attribute swaps rows and columns.")

    print("\nAll matrix operations completed successfully.")


if __name__ == "__main__":
    main()
