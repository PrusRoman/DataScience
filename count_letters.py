#Определите функцию count_letters(sentence, average), которая считает количество букв в строке без учёта пробелов.
#У функции должен быть необязательный булевый аргумент average, который по умолчанию равен False.
#Если он равен True, то функция должна возвращать количество букв в среднем на слово.
#count_letters("Beep boop") # => 8
#count_letters("Beep boop", average=True) # => 4
#count_letters("I will build my own theme park") # => 24
#count_letters("I will build my own theme park", average=True) # => 3.429
#Словом считается любая последовательность символов, отделённая пробелами или границами предложения.
#Cреднюю длину слова можно не округлять


def count_letters(sentence, average = False):
  if average == False:
    str = len(sentence.replace(' ',''))
    return(str)
  if average == True:
    str_list = sentence.split(' ')
    avg = 0
    for word in str_list:
      avg += len(word)
    avg = avg/len(str_list)
    return(avg)
print(count_letters('I will build my own theme park', True))
