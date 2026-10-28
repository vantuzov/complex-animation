import math

# Вычисляет координаты точек фигуры.
def get_shape_points(width: int, height: int, progress: float) -> list[float]:
    center_x = width / 2  # горизонтальный центр холста.
    center_y = height / 2  # вертикальный центр холста.
    size = min(width, height) * 0.35  # размер фигуры относительно холста.
    points = []

    for i in range(120):
        angle = 2 * math.pi * i / 120  # Вычисляем текущий угол в радианах.
        delta = (angle + math.pi / 2) % (2 * math.pi / 3) - math.pi / 3   # угол относительно ближайшей стороны треугольника.
        triangle_radius = size * math.cos(math.pi / 3) / math.cos(delta)   # расстояние от центра до стороны треугольника под этим углом.

        # смешивание
        radius = size + (triangle_radius - size) * progress
        points.extend(
            (
                center_x + radius * math.cos(angle),
                center_y + radius * math.sin(angle),
            )
        )

    return points
