#!/usr/bin/env python
# coding: utf-8

# ## Functions Exercise Solutions

# In[1]:


# Exercise 1
# Define a function named is_two. 
# It should accept one input and return True if 
# the passed input is either the number or the string 2, 
# False otherwise.

def is_two(n):
    return n == 2 or n == '2'


# In[2]:


is_two(2)


# In[3]:


is_two('2')


# In[4]:


is_two(2.0)


# In[5]:


is_two('banana')


# In[9]:


# Exercise 2
# Define a function named is_vowel. 
# It should return True if the passed string is a vowel, 
# False otherwise.

def is_vowel(somestring):
    if type(somestring) == str:
        result = somestring.lower() in ['a', 'e', 'i', 'o', 'u']
        return result
    else:
        return False


# In[10]:


is_vowel('aeiou')


# In[13]:


is_vowel('iou')


# In[14]:


is_vowel('ii')


# In[15]:


is_vowel('cat')


# In[11]:


is_vowel('aa')


# In[12]:


is_vowel('a')


# In[16]:


is_vowel('m')


# In[17]:


# Exercise 3
# Define a function named is_consonant.
# It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(somestring):
    if type(somestring) == str:
        only_letters = somestring.isalpha()
        return only_letters and not is_vowel(somestring)
    return False


# In[18]:


is_consonant('m')


# In[19]:


is_consonant('3')


# In[20]:


is_consonant('a')


# In[21]:


is_consonant('mm')


# In[22]:


# Exercise 4
# Define a function that accepts a string that is a word. 
# The function should capitalize the 
# first letter of the word if the word starts with a consonant.

def capitalize_starting_consonant(string):
    if type(string) != str:
        return False
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
    return string


# In[23]:


capitalize_starting_consonant('banana')


# In[24]:


capitalize_starting_consonant('apple')


# In[25]:


# Exercise 5
# Define a function named calculate_tip. 
# It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, 
# and return the amount to tip.

def calculate_tip(bill, tip_percentage=0.2):
    if type(tip_percentage) != float:
        return False
    if tip_percentage < 0 or tip_percentage > 1:
        return 'the tip percentage must be between 0 and 1'
    return tip_percentage * bill


# In[26]:


# Exercise 6
# Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

def apply_discount(price, discount_percentage):
    discount = price * discount_percentage
    return price - discount


# In[27]:


# Exercise 7
# Define a function named handle_commas. 
# It should accept a string that is a number that contains 
# commas in it as input, 
# and return a number as output.

def handle_commas(somestring):
    if type(somestring) != str:
        return 'input must be a string'
    somestring = somestring.replace(',', '')
    if somestring.isdigit():
        return float(somestring)
    else:
        return 'input must be a string that is a number'


# In[28]:


# Exercise 8
# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade 
# associated with that number (A-F).

def get_letter_grade(grade):
    if type(grade) == int or type(grade) == float:
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"
    else:
        return "Input must be a number"


# In[29]:


# Exercise 9
# Define a function named remove_vowels that accepts a 
# string and returns a string with all the vowels removed.

def remove_vowels(somestring):
    if type(somestring) != str:
        return False
    output = ''
    for letter in somestring:
        if is_consonant(letter):
            output += letter
    return output


# In[30]:


# Exercise 10
# Define a function named normalize_name. 
# It should accept a string and return a valid python identifier
# steps I want to take
# make lowercase, remove whitespace, establish valid identifier

def normalize_name(string):
    output = ''
    string = string.lower()
    for character in string:
        if character.isidentifier() or character == ' ':
            output += character
    output = output.strip()
    output = output.replace(' ', '_')
    return output


# In[32]:


# Exercise 11
# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(somenums):
    output = []
    for i, num in enumerate(somenums):
        sum_so_far = sum(somenums[:i + 1])
        output.append(sum_so_far)
    return output


# We have used this mysterious function named `enumerate`. But what does it do and why are we creating a for loop that somehow references two things (`i` and `num`)?
# 
# To begin, lets try printing out the output of `enumerate` on a simple string:

# In[37]:


# print(enumerate('apple'))


# Here we see that the output of the enumerate function is a reference to an object. Enumerate produces a pattern, or recipe, that can be used in conjunction with other functions to create human readable output. Let's try it with `list`:

# In[36]:


# print(list(enumerate('apple')))


# Now the pattern is becoming apparent. Here, `list` plus `enumerate` created a list of tuples. How many elements are in this list?

# In[39]:


len(list(enumerate('apple')))


# And what does the first element look like?

# In[40]:


list(enumerate('apple'))[0]


# Each element of this list is a tuple, that is itself made up of two elements. But what is the pattern that we can identify?

# In[41]:


list(enumerate('apple'))


# In[42]:


list(enumerate('bear'))


# In[43]:


list(enumerate('peace'))


# Enumerate is essentially breaking up our string into individual parts, and then attaching a number to those parts.
# 
# So when we ask `for i, num in enumerate(somenums)`
# 
# We are essentially asking for both parts of each element. The first part, which is the number, we call `i`. The second part, which is the piece of our original argument, we call `num`.
# 
# `enumerate` isn't limited to strings, we can also use it with any kind of iterable:

# In[44]:


list(enumerate([12, 15, 3.5]))


# So lets go back to our original code.
# 
# We say:
# 
# `for i, num in enumerate(somenums):`
# 
# This will iterate through our `somenums` object, creating tuples that store `i` the position and `num` the piece of the original object.
# 
# When we then use `i` later in our code, we do so in combination with `sum` to have python `sum` all the values in our list up to a certain position. 
# 
# Now, we also could have solved this a different way, using `range`:

# In[47]:


def cumulative_sum(somenums):
    output = []
    for i in range(len(somenums)):
        sum_so_far = sum(somenums[:i + 1])
        output.append(sum_so_far)
    return output


# In[48]:


cumulative_sum([1, 1, 1])


# In[49]:


cumulative_sum([2, 4, 6])


# Although `range` is a simpler way to approach the problem, we will see `enumerate` used several times later in the course. If its still confusing to you, don't worry. There will be more time to go over it in the future. But feel free to experiment and tinker with `enumerate`. Understanding it will give you one more tool to use later.

# In[45]:


# ### Bonus Question 1
# Create a function named twelveto24. 
# It should accept a string in the format 10:45am or 4:30pm and 
# return a string that is the representation of the time in a 24-hour format.

def twelveto24(time):
    try:
        hour = ''
        minute = ''
        colon_position = time.rindex(':')
        formatted_time = ''
        if time[-2:] == 'am':
            hour = int(time[:colon_position])
            if int(hour) <= 11:
                formatted_time = time[:-2]
                return formatted_time
            else:
                hour = '00'
                minute = time[colon_position + 1:-2]
                formatted_time = hour + ':' + minute
                return formatted_time
        elif time[-2:] == 'pm':
            hour = int(time[:colon_position]) + 12
            minute = time[colon_position + 1:-2]
            formatted_time = str(hour) + ':' + minute
            return formatted_time
        else:
            return "Please input the time in the correct format."
    except ValueError:
        return 'Please input the time in the correct format.'


# In[ ]:


# Bonus write a function that does the opposite.

def twelvefrom24(time24):
    
    colon_position = time24.rindex(':')
    hour = time24[:colon_position]
    minute = time24[colon_position + 1:]
    formatted_time = ''
    if int(hour) == 0:
        hour = '12'
        formatted_time = hour + ':' + minute + 'am'
        return formatted_time
    elif int(hour) < 12:
        formatted_time = time24 + 'am'
        return formatted_time
    elif int(hour) == 12:
        formatted_time = time24 + 'pm'
        return formatted_time
    else:
        hour = int(hour) - 12
        formatted_time = str(hour) + ':' + minute + 'pm'
        return formatted_time


# In[ ]:


# #### Bonus Question 2
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# - col_index('A') returns 1
# - col_index('B') returns 2
# - col_index('AA') returns 27

def col_index(col_name):
    letter_to_num = {
                    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
                    'H': 8, 'I': 9, 'J':10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
                    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
                    'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
                     }
    col_value = 0
    for index in range(-1, -(len(col_name)+1), -1):
        col_value += letter_to_num[(col_name[index])] * (26 ** -(index + 1))
    return col_value


# In[ ]:




