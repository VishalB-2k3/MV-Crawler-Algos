import numpy as np
from sklearn.neighbors import NearestNeighbors

def icp(a, b, max_iterations=20, tolerance=1e-6):
    src = np.copy(a)
    dst = np.copy(b)

    for i in range(max_iterations):
        neighbors = NearestNeighbors(n_neighbors=1).fit(dst)
        distances, indices = neighbors.kneighbors(src)

        try:
            T = np.eye(4)
            T[0:3, 0:3] = np.dot(np.linalg.inv(src.T @ src), src.T @ dst[indices[:, 0]])

            src = np.dot(src, T[0:3, 0:3].T) + T[0:3, 3]

            mean_error = np.mean(distances)
            if mean_error < tolerance:
                break
        except np.linalg.LinAlgError as e:
            print(f"Error in ICP iteration {i}: {e}")
            break

    return T, mean_error

# Example point clouds
if __name__ == "__main__":
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[1, 2.1, 3], [4.1, 5, 6], [7, 8, 9.1]])

    T, error = icp(a, b)
    print("Transformation Matrix:", T)
    print("Mean Error:", error)
