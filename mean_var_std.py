import numpy as np

def calculate(lst):
    # Check list length
    if len(lst) < 9:
        raise ValueError("List must contain nine numbers.")
    
    # Create a 3x3 matrix
    matrix = np.array(lst).reshape((3, 3))

    # Store list and float functions
    l = list
    f = float

    # Create the dict for output
    calculations = {
        "mean": [l(np.mean(matrix, axis=0)), l(np.mean(matrix, axis=1)), f(np.mean(matrix))],
        "variance": [l(np.var(matrix, axis=0)), l(np.var(matrix, axis=1)), f(np.var(matrix))],
        "standard deviation": [l(np.std(matrix, axis=0)), l(np.std(matrix, axis=1)), f(np.std(matrix))],
        "max": [l(np.max(matrix, axis=0)), l(np.max(matrix, axis=1)), f(np.max(matrix))],
        "min": [l(np.min(matrix, axis=0)), l(np.min(matrix, axis=1)), f(np.min(matrix))],
        "sum": [l(np.sum(matrix, axis=0)), l(np.sum(matrix, axis=1)), f(np.sum(matrix))],
    }

    return calculations
