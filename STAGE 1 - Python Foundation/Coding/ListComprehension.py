# numbers = [1,2,3,4,5]

# squares = [n*n for n in numbers]
# # for n in numbers:
# #     squares.append(n*n)

# print(squares)

numbers = [1,2,3,4,5,6]

evens = [n for n in numbers if n%2 == 0 ]
result = ["Even" if n%2 ==0 else "Odd" for n in numbers]
print(evens)
print(result)

words = ["ai","python","ml","data","a"]

long_words = [w for w in words if len(w) > 2]
print(long_words)