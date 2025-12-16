import math


class Vector2D:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"


def main():
    print("Демонстрация работы класса Vector2D")
    print("=" * 60)

    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, -2)

    print(f"\nv1 = Vector2D(3, 4)")
    print(f"v2 = Vector2D(1, -2)")


    print(f"\n1. Сложение:")
    result_add = v1 + v2
    print(f"   v1 + v2 = {result_add}")


    print(f"\n2. Вычитание:")
    result_sub = v1 - v2
    print(f"   v1 - v2 = {result_sub}")


    print(f"\n3. Длина вектора:")
    length_v1 = v1.length()
    print(f"   v1.length() = {length_v1}")
    length_v2 = v2.length()
    print(f"   v2.length() = {math.sqrt(5):.1f}")


    print(f"\n4. Строковое представление:")
    print(f"   print(v1) -> {v1}")
    print(f"   print(v2) -> {v2}")


if __name__ == "__main__":
    main()
