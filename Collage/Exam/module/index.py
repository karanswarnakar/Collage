import Collage.Exam.module.calculator as calculator
a = int(input("Enter a first: "))
b = int(input("Enter a secound: "))
opration = "1. add 2. sub 3. mul 4. divide"
print()

c = int(input(f"Chose any {opration }: " ))

calculator.calculator(a,b,c)        
