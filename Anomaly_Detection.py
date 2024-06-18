import numpy as np

def generate_sensor_data(num_samples=100, anomaly_ratio=0.1):
    """Generate random sensor data with some anomalies."""
    data = np.random.normal(0, 1, num_samples)
    num_anomalies = int(num_samples * anomaly_ratio)
    anomaly_indices = np.random.choice(num_samples, num_anomalies, replace=False)
    data[anomaly_indices] = data[anomaly_indices] * 10  # Introduce anomalies
    return data

def detect_anomalies(data, threshold=3):
    mean = np.mean(data)
    std_dev = np.std(data)
    anomalies = []

    for index, value in enumerate(data):
        z_score = (value - mean) / std_dev
        if np.abs(z_score) > threshold:
            anomalies.append((index, value, z_score))
    
    return anomalies

if __name__ == "__main__":
    data = generate_sensor_data()
    anomalies = detect_anomalies(data)
    print("Sensor Data:", data)
    print("Detected Anomalies:", anomalies)
