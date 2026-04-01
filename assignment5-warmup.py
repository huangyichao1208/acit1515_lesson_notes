"""
Key Skills for Assignment 5:
    1. Creating and adding values to a list
    2. Outputting values from a list
    3. Editing values in a list
    4. Searching for values in a list
    5. Using a for loop to output values in a list
    6. Copying values from one list to another
"""



"""
1. Creating and adding values to a list
"""
# a. Create a variable named 'provinces' that is initially empty
provinces = []


# b. Append the following values into the list: BC, AB, SK, MB, ON, QC, PE
provinces.append('BC')
provinces.append('AB')
provinces.append('SK')
provinces.append('MB')
provinces.append('ON')
provinces.append('QC')
provinces.append('PE')

"""
2. Outputting values from a list
"""
# a. Output 'BC' from the provinces variable using square bracket notation
print (provinces [0])


# b. Output 'ON' from the provinces variable using square bracket notation and a negative index
print (provinces [-3])


# c. Output 'AB', 'SK', and 'MB' from the provinces variable using square bracket *slice* notation
print (provinces [1:4])


"""
3. Editing values in a list
"""
# a. Change 'PE' to 'NS' and output the list
provinces [-1] = 'NS'
print (provinces)


"""
4. Searching for values in a list
"""
# a. Write any statements necessary to check if 'BC' exists in the list of provinces. If 'BC' exists
# in the list, output 'BC is a province'
if 'BC' in provinces:
    print ('BC is a province')


"""
5. Using a for loop to output values in a list
"""
# a. Write any statements necessary to output all the values from the provinces list, one value per line
for values_p in provinces:
    print (values_p)


# b. Write any statements necessary to output all the values from the provinces list using the range() function
i = 0
for i in range(len(provinces)):
    print (provinces[i])
    i = i+1


"""
5. Copying values from one list to another
"""
# a. Create a list called 'numbers' that contains the numbers 1 through 20. Create a second list called 'large_even' that is initially empty. Use a for loop to loop through the numbers list and copy all the even numbered values from the 'numbers' list into the 'large_even' list. When completed, the 'large_even' list should contain the numbers [10, 12, 14, 16, 18, 20]
numbers = [1,2,3,4,5,6,7,8,9,10,
           11,12,13,14,15,16,17,18,19,20]
large_even = []
for i in range (9,len(numbers),2):
    large_even.append(numbers[i])