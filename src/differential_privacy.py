import syft as sy
import numpy as np

def add_noise(data, epsilon):
    noise = np.random.laplace(0, 1/epsilon, size=data.shape)
    return data + noise

if __name__ == "__main__":
    data = np.array([1.0, 2.0, 3.0, 4.0])
    epsilon = 0.1
    noisy_data = add_noise(data, epsilon)
    print(f"Original data: {data}")
    print(f"Noisy data: {noisy_data}")
