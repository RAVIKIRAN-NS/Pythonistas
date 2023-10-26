# numbers = [1,2,3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "ANGELA"
# letter_list = [letter for letter in name]
# print(letter_list)

# new_range = [n * 2 for n in range(1,5)]
# print(new_range)

# names= ['alex','beth','caroline','dave','eleanor','freddie']
# short_name = [nam for nam in names if len(nam) < 5]
# print(short_name)

names= ['alex','beth','caroline','dave','eleanor','freddie']
long_name = [nam.upper() for nam in names if len(nam) > 5]
print(long_name)
