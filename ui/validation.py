from tkinter import messagebox

def validate_puntos(puntos):
    if not puntos.isdigit() or not (0 <= int(puntos) <= 100):
        messagebox.showerror("Entrada inválida", "Por favor ingrese un valor numérico entre 0 y 100 para los puntos.")
        return False
    return True

def validate_ausencias(ausencias):
    if not ausencias.isdigit() or not (0 <= int(ausencias) <= 12):
        messagebox.showerror("Entrada inválida", "Por favor ingrese un valor numérico entre 0 y 12 para las ausencias.")
        return False
    return True
