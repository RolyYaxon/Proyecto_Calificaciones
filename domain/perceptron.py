import numpy as np

def step_function(x):
    return 1 if x >= 0 else 0

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.random.rand(input_size)
        self.threshold = np.random.rand(1)
        self.learning_rate = learning_rate

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights) - self.threshold
        return step_function(summation)

    def train(self, training_data, labels, epochs=10):
        history = []
        for epoch in range(epochs):
            epoch_history = []
            for inputs, label in zip(training_data, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights += self.learning_rate * error * np.array(inputs)
                self.threshold -= self.learning_rate * error
                epoch_history.append((inputs, prediction, label, error, self.weights.copy(), self.threshold.copy()))
            history.append(epoch_history)
        return history
