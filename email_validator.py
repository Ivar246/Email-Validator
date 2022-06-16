import re

statement = 'hello, i am ravi shrestaha. i am studying bachelorin in computer science and information technology.'

pattern = re.compile(r'technology.$')
matches= pattern.finditer(statement)

for match in matches:
    print(match)