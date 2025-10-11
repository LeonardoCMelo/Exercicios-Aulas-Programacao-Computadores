def exercicio_7(a: float, b: float, c: float):
    if (a+b)<=c or (a+c)<=b or (b+c)<=a:
        return "nao eh triangulo"
    
    triangleType = ""
    
    if a == b and b == c:
        triangleType += "equilatero, "
    if a == b or c == a or b == c:
        triangleType += "isosceles, "
    if a != b and a != c and b != c:
        triangleType += "escaleno, "
    return triangleType[:-2]