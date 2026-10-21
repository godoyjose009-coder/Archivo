def calcular_area(base: float, altura: float) -> float:
    """Calcula el area de un rectangulo"""
    if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("La base y la altura deben ser valores numericos (int o float)")

    if base < 0 or altura < 0:
        raise ValueError("Dimensiones no pueden ser negativos")

    return float(base * altura)