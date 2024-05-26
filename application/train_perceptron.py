from domain.perceptron import Perceptron
from infrastructure.training_data import get_training_data

def train_perceptron(input_size, learning_rate, epochs):
    training_data, labels = get_training_data()
    perceptron = Perceptron(input_size=input_size, learning_rate=learning_rate)
    history = perceptron.train(training_data, labels, epochs)
    return perceptron, history
