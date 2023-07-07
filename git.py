word = str(input('Введите ваше слово: '))
if word == word[::-1]:
  print("True")
else:
  print("False")