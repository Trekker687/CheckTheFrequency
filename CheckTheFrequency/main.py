dictionary = {'Manvir': 9, 'Is':6, 'Cool':10}
print("The original dictionary : " + str(dictionary))

value = int(input("Enter a value"))
res = 0
for key in dictionary:
    if dictionary[key] == value:
        res = res + 1

print("Frequency of the value is : " + str(res))
