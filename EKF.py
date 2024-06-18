import numpy as np

class EKF:
    def __init__(self, state_dim, meas_dim):
        self.state_dim = state_dim
        self.meas_dim = meas_dim
        self.x = np.zeros((state_dim, 1))  # Initial state
        self.P = np.eye(state_dim)         # Initial covariance matrix
        self.F = np.eye(state_dim)         # State transition model
        self.H = np.zeros((meas_dim, state_dim))  # Measurement model
        self.Q = np.eye(state_dim)         # Process noise covariance
        self.R = np.eye(meas_dim)          # Measurement noise covariance

    def predict(self, u):
        self.x = np.dot(self.F, self.x) + u
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q

    def update(self, z):
        y = z - np.dot(self.H, self.x)
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        self.x = self.x + np.dot(K, y)
        self.P = self.P - np.dot(np.dot(K, self.H), self.P)

# Running the EKF with sample control inputs and measurements
if __name__ == "__main__":
    ekf = EKF(state_dim=4, meas_dim=2)

    # Example usage
    u = np.array([[1], [1], [0.1], [0.1]])  # Control input (e.g., from IMU)
    z = np.array([[5], [5]])                # Measurement (e.g., from UWB)

    ekf.predict(u)
    ekf.update(z)

    print("Estimated State:", ekf.x)
