import pandas as pd

student1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})
student2 = pd.Series({'수학': 80, '국어': 90, '영어': 80})

# print(student1)
# print(student2)

add = student1 + student2
sub = student1 - student2
mul = student1 * student2
div = student1 / student2

# print(type(div))

result = pd.DataFrame([add, sub, mul, div], index=['+', '-', '*', '/'])
print(result.T)