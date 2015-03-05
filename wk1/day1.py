# print 'hello'


# # if, if/else

# grade = 60
# message = 'you really effed it up!'
# if grade > 89:
#     message = "A"
# elif grade > 79:
#     message = 'B'
# elif grade > 69:
#     message = 'C'
#
# print message


# # if, if/else
#
# name = 'bob'
#
# if(name == 'bob'):
#     print 'your name is bob'
# elif(name == 'joe'):
#     print 'your name is bob'
# else:
#     print "you're a nobody"


# # simple iterative loop
#
# for i in range(10):
#     print i


# # iterative loop with a starting point, end point and a metric
#
# for i in range(2,11,2):
#     print i




# # iterate over a list (array)
#
# grades = [70, 80, 90]
# grades.append(100)

# grades.splice(1,1) javaScript for removing an index
# grades.pop() - get rid of the last element
# grades.pop(0) - get rid of an element at a specific index

# print grades

# # functions
#
# an empty function
# def greetings():
#     pass
#
# def add(a, b):
#     total = a + b
#     return total
#
# print add(2, 2)


# calculate avg function
#
# test = [70, 80, 90, 90] # test is our variable
# def avg(n): # n is a generic variable representing a numerical value
#     total = 0
#     for i in n:
#         total += i
#     average = total/len(n)
#     return average
# pass in the variable test which will be represented in the function by n
# print avg(test)


# sum of all odd numbers in a list
#
# nums = [1,2,3,4,5,6,7,8,9]
# def odd_sum(n):
#     odd_total = 0
#     for i in n:
#         if i %2 != 0:
#             odd_total += i
#     return odd_total
# print odd_sum(nums)


# verify vowels in a string
#
word = raw_input("Type a word: ")
def vowels(w):
    vowel_container = []
    for i in w:
        if i == 'a':
            vowel_container.append(i)
        elif i == 'e':
            vowel_container.append(i)
        elif i == 'i':
            vowel_container.append(i)
        elif i == 'o':
            vowel_container.append(i)
        elif i == 'u':
            vowel_container.append(i)

    if len(vowel_container) == 0:
        return 'There are no vowels in this word'
    else:
        return vowel_container


print vowels(word)

# extra credit:
# no duplicate values
