def convert(number):
  result = ""
  if number % 3 == 0:
    result += "Pling"
  if number % 5 == 0:
    result += "Plang"
  if number % 7 == 0:
    result += "Plong"
  return result or str(number)


print(convert(6))
print(convert(10))
print(convert(14))
print(convert(35))
print(convert(15))
print(convert(21))
print(convert(105))
