import math
import tkinter as tk

root = tk.Tk()
root.title("Превращение круга в треугольник")
root.geometry("700x700")

canvas = tk.Canvas(root, bg="#dddddd", highlightthickness=0)
canvas.pack(fill="both", expand=True)

progress = 0
direction = 1

def animate():
    global progress, direction

    width = canvas.winfo_width()
    height = canvas.winfo_height()
    center_x = width / 2
    center_y = height / 2
    size = min(width, height) * 0.35
    points = []

    for i in range(120):
        angle = 2 * math.pi * i / 120
        delta = (angle + math.pi / 2) % (2 * math.pi / 3) - math.pi / 3
        triangle_radius = size * math.cos(math.pi / 3) / math.cos(delta)
        radius = size + (triangle_radius - size) * progress
        points.extend((center_x + radius * math.cos(angle),
                       center_y + radius * math.sin(angle)))

    canvas.delete("shape")
    canvas.create_polygon(*points, fill="#dddddd", outline="black",
                          width=5, tags="shape")

    progress += direction * 0.01
    if progress >= 1 or progress <= 0:
        direction *= -1
    root.after(20, animate)

animate()
root.mainloop()
