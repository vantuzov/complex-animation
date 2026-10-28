import tkinter as tk


def create_window() -> tuple[tk.Tk, tk.Canvas]:
    root = tk.Tk()
    root.title("Превращение круга в треугольник")
    root.geometry("700x700")

    canvas = tk.Canvas(root, bg="#dddddd", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    return root, canvas
