def calculator(op):
    def sum(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mult(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    match op:       # python's switch case
        case "+":
            return sum
        case "-":
            return sub
        case "*":
            return mult
        case "/":
            return div
print(calculator("+")(3, 2))
op = calculator("-")    # its possible to assign it to a variable too
print(op(9,2))