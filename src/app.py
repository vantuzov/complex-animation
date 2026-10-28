import tkinter as tk


def create_window() -> tuple[tk.Tk, tk.Canvas]:
    #   Создание главного окна приложения и холст для анимации.
    root = tk.Tk()
    root.title("Превращение круга в треугольник")
    root.geometry("700x700")

    # Холст занимает всю доступную область окна.
    canvas = tk.Canvas(root, bg="#dddddd", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    return root, canvas
