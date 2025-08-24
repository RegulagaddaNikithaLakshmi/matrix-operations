import numpy as np

def input_matrix(name="Matrix"):
    print(f"\nEnter {name}:")
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    print(f"Enter the elements row-wise separated by space:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        while len(row) != cols:
            print(f"Error: Enter exactly {cols} elements.")
            row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix, name="Result"):
    print(f"\n{name}:")
    print(matrix)

def matrix_operations():
    print("=== Matrix Operations Tool ===")
    while True:
        print("\nSelect Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape != B.shape:
                print("Error: Matrices must have the same dimensions for addition.")
            else:
                display_matrix(A + B, "A + B")

        elif choice == "2":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape != B.shape:
                print("Error: Matrices must have the same dimensions for subtraction.")
            else:
                display_matrix(A - B, "A - B")

        elif choice == "3":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape[1] != B.shape[0]:
                print("Error: Columns of A must match rows of B for multiplication.")
            else:
                display_matrix(np.dot(A, B), "A x B")

        elif choice == "4":
            A = input_matrix("Matrix")
            display_matrix(A.T, "Transpose")

        elif choice == "5":
            A = input_matrix("Square Matrix")
            if A.shape[0] != A.shape[1]:
                print("Error: Determinant can only be calculated for a square matrix.")
            else:
                det = np.linalg.det(A)
                print(f"\nDeterminant: {det}")

        elif choice == "6":
            print("Exiting Matrix Operations Tool. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    matrix_operations()
