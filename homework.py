#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Juft raqamlar:", even_numbers)
print("Toq raqamlar:", odd_numbers)
#2
raqamlar = [1, 2, 3, 4, 5]
yigindi = 0
indeks = 0

while indeks < len(raqamlar):
    yigindi += raqamlar[indeks]
    indeks += 1
print("Raqamlar yig'indisi:", yigindi)
#3
def aylantirish(royxat):
    return royxat[1:] + [royxat[0]]
print(aylantirish([1, 2, 3, 4]))
#4
def min_max_topish(royxat):
    eng_kichik = min(royxat)
    eng_katta = max(royxat)
    return eng_kichik, eng_katta
print(min_max_topish([3, 1, 4, 1, 5, 9]))
#5
def elementni_qidirish(royxat, qiymat):
    for element in royxat:
        if element == qiymat:
            return True
    return False
print(elementni_qidirish([1, 2, 3, 4], 3))
print(elementni_qidirish([1, 2, 3, 4], 5))
#6
def unikal_elementlar(royxat):
    return list(set(royxat))
print(unikal_elementlar([1, 2, 2, 3, 4, 4, 5]))
#7
def to_lowercase(words):
    return [word.lower() for word in words]
words = ["Salom", "Dunyo", "Python"]
print(to_lowercase(words))
#8
def remove_word(words, target):
    return [word for word in words if word != target]
words = ["salom", "dunyo", "python"]
print(remove_word(words, "dunyo"))
#9
def find_capitalized_words(words):
    return [word for word in words if word[0].isupper()]
words = ['Salom', 'dunyo', 'Python', 'kod']
print(find_capitalized_words(words))
#10
def word_lengths(words):
    return [len(word) for word in words]
words = ['salom', 'dunyo']
print(word_lengths(words))
#11
def word_lengths(words):
    return [len(word) for word in words]
words = ['salom', 'dunyo']
print(word_lengths(words))
#12
def find_word(words, target):
    return target in words
words = ['salom', 'dunyo']
target = 'dunyo'
print(find_word(words, target))
#13
def to_lowercase(words):
    return [word.lower() for word in words]
words = ['Salom', 'Dunyo']
print(to_lowercase(words))
#14
def remove_word(words, target):
    return [word for word in words if word != target]
words = ['salom', 'dunyo', 'salom']
target = 'salom'
print(remove_word(words, target))
#15
def find_word_index(word_list, word):
    try:
        index = word_list.index(word)
        return index
    except ValueError:
        return -1
words = ["apple", "banana", "cherry", "date"]
word_to_find = input("Qidiriladigan so'zni kiriting: ")
index = find_word_index(words, word_to_find)
if index != -1:
    print(f"So'z ro'yxatda {index}-indeksda joylashgan.")
else:
    print("So'z ro'yxatda topilmadi.")
#16
def reverse_list(word_list):
    return word_list[::-1]

words = ["apple", "banana", "cherry", "date"]
reversed_words = reverse_list(words)
print("Teskari tartibda:", reversed_words)
#17
import re
def extract_numbers(word_list):
    return [''.join(re.findall(r'\d+', word)) for word in word_list]
words = ["apple123", "banana456", "cherry789", "date0"]
numbers = extract_numbers(words)
print("Faqat raqamlar:", numbers)
#18
def find_words_of_length(word_list, length):
    return [word for word in word_list if len(word) == length]
words = ["apple", "banana", "cherry", "date"]
length = int(input("So'z uzunligini kiriting: "))
specific_length_words = find_words_of_length(words, length)
print(f"{length} uzunlikdagi so'zlar:", specific_length_words)