import numpy as np
from scipy.optimize import minimize

class MPC:
    def __init__(self, horizon, dt):
        self.horizon = horizon
        self.dt = dt

    def objective(self, u, *args):
        x0, target = args
        cost = 0
        x = x0.copy()

        for i in range(self.horizon):
            x = self.dynamics(x, u[i])
            cost += np.linalg.norm(x - target)**2

        return cost

    def dynamics(self, x, u):
        return x + self.dt * u

    def solve(self, x0, target):
        u0 = np.zeros(self.horizon)  # Flatten to one-dimensional array
        result = minimize(self.objective, u0, args=(x0, target), method='SLSQP')
        return result.x

# Running the MPC with sample initial state and target
if __name__ == "__main__":
    mpc = MPC(horizon=10, dt=0.1)
    x0 = np.array([0, 0])
    target = np.array([1, 1])

    u_opt = mpc.solve(x0, target)
    print("Optimal Control Inputs:", u_opt)
