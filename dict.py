# num = [1, 2, 3, 4]
# squares = {}
# for n in num:
#     squares[n] = n ** 2
# print(squares)


# nums = [1, 2, 3, 4]
# squared_nums = {n: n ** 2 for n in nums}  
# print(squared_nums)


# dict1 = {
#     "Harsh":5,
#     "Jeel":4,
#     "Kavya":5
# }

# names = ["Harsh", "Jeel", "kavya"]
# len_of_names = {n: len(n) for n in names}
# print(len_of_names)

# nums = [1, 2, 3, 4]
# squared_nums = {n: n**2 for n in nums if (n**2) % 2 == 0}
# print(squared_nums)

nums = [1, 2, 3, 4]
squared_nums = {n: n**2 if (n**2) % 2 == 0 else n**3 for n in nums}
print(squared_nums)


