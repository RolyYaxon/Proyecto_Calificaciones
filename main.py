import tkinter as tk
from application.train_perceptron import train_perceptron
from controller.perceptron_controller import PerceptronController
from ui.perceptron_gui import PerceptronGUI

if __name__ == "__main__":
    perceptron, history = train_perceptron(input_size=2, learning_rate=0.1, epochs=10)
    controller = PerceptronController(perceptron)
    root = tk.Tk()
    app = PerceptronGUI(root, controller)
    root.mainloop()
