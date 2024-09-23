import numpy as np

def strassen(A, B):
    n = A.shape[0]
    
    if n == 1:
        return A * B

    # Splitting the matrices into quadrants
    mid = n // 2

    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    # Strassen's formula
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    # Computing the submatrices of the result
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combining the quadrants into a single matrix
    C = np.zeros((n, n))
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C

# Helper function to pad matrices to the nearest power of 2
def pad_matrix(matrix, size):
    padded = np.zeros((size, size))
    padded[:matrix.shape[0], :matrix.shape[1]] = matrix
    return padded

if __name__ == "__main__":
    # Example usage
    A = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

    B = np.array([[16, 15, 14, 13],
                  [12, 11, 10, 9],
                  [8, 7, 6, 5],
                  [4, 3, 2, 1]])

    # Padding matrices to the nearest power of 2 if necessary
    size = 1 << (max(A.shape + B.shape) - 1).bit_length()  # Next power of 2
    A_padded = pad_matrix(A, size)
    B_padded = pad_matrix(B, size)

    C_padded = strassen(A_padded, B_padded)
    
    # Remove padding to return original matrix size result
    C = C_padded[:A.shape[0], :A.shape[1]]

    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    print("\nResultant Matrix C (A * B):")
    print(C)
