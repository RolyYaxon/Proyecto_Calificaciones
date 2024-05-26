from ui.validation import validate_puntos, validate_ausencias

class PerceptronController:
    def __init__(self, perceptron):
        self.perceptron = perceptron

    def verificar_paso(self, puntos, ausencias):
        if not (validate_puntos(puntos) and validate_ausencias(ausencias)):
            return None

        puntos = int(puntos)
        ausencias = int(ausencias)
        x1 = 1 if puntos >= 61 else 0
        x2 = 1 if ausencias < 2 else 0
        prediction = self.perceptron.predict([x1, x2])
        resultado = "Aprobado" if prediction == 1 else "No aprobado"
        return puntos, ausencias, resultado
