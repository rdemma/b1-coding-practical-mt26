class Controller:
    def __init__(self, K_P: float = 0.15, K_D: float = 0.60):
        self.K_P = K_P
        self.K_D = K_D
        self.previous_error = None

    def reset(self):
        self.previous_error = None

    def __call__(self, reference: float, observation: float) -> float:
        if self.previous_error is None:
            self.previous_error = 0

        error = reference - observation
        action = self.K_P * (error) + self.K_D * (error - self.previous_error)
        self.previous_error = error
        return action