from utils import get_float_input
from triangle import calculate_triangle_area


def main():
    print("Calculador de Área de un Triángulo")

    base = get_float_input("Introduce la base del triángulo: ")
    altura = get_float_input("Introduce la altura del triángulo: ")

    area = calculate_triangle_area(base, altura)

    print(f"El área del triángulo es: {area}")


if __name__ == "__main__":
    main()