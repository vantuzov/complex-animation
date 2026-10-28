import tkinter as tk

if __package__:
    from src.app import create_window
    from src.animation import get_shape_points
else:
    from app import create_window
    from animation import get_shape_points

root, canvas = create_window()

progress = 0
direction = 1

def animate():
    global progress, direction

    width = canvas.winfo_width()
    height = canvas.winfo_height()
    points = get_shape_points(width, height, progress)

    canvas.delete("shape")
    canvas.create_polygon(*points, fill="#dddddd", outline="black",
                          width=5, tags="shape")

    progress += direction * 0.01
    if progress >= 1 or progress <= 0:
        direction *= -1
    root.after(20, animate)

animate()
root.mainloop()
