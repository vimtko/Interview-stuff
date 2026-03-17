#Codetraining
#3/16/2026

#Implement a method that, given a number, calculates the factorial of that number
#the metod implementation must use a astack data structure
#(factorial: every number before needs to be multiplied by, represented by variable!)
#(ej: 5!= 1*2*3*4*5 = 120)

class Factorial:
    def __init__(self):
        self.numero = None
        self.historial = []  # To track steps, e.g., each multiplication

    def calculate(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            self.historial.append(f"Factorial of {n} is 1")
            return 1
        
        stack = []
        result = 1
        # Push numbers 1 to n onto the stack
        for i in range(1, n + 1):
            stack.append(i)
        
        # Pop from stack and multiply
        while stack:
            num = stack.pop()
            result *= num
            self.historial.append(f"Multiplied by {num}, current result: {result}")
        
        return result

