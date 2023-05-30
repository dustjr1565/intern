class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Division by zero.")
            return None


def run(opt: str, num1: int, num2: int):
    calculator = Calculator()
    if opt == "add":
        result = calculator.add(num1, num2)
    elif opt == "subtract":
        result = calculator.subtract(num1, num2)
    elif opt == "multiply":
        result = calculator.multiply(num1, num2)
    elif opt == "divide":
        result = calculator.divide(num1, num2)
    else:
        print("Invalid option")
        return
    print(result)


if __name__ == "__main__":
    run("subtract", 1, 3)
