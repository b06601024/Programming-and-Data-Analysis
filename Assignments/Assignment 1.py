#!/usr/bin/env python
# coding: utf-8

# # Programming and Data Analysis
# 
# > Assignment 1
# 
# Kuo, Yao-Jen <yaojenkuo@ntu.edu.tw> from [DATAINPOINT](https://www.datainpoint.com)

# ## Instructions
# 
# - The assignment will be disconnected if idling over 10 minutes, we can reactivate a new session by clicking the assignment link again.
# - We've imported necessary modules at the top of each assignment.
# - We've put necessary files(if any) in the working directory.
# - We've defined the names of functions/inputs/parameters for you.
# - Write down your solution between the comments `### BEGIN SOLUTION` and `### END SOLUTION`.
# - It is NECESSARY to `return` the answer, tests will fail by just printing out the answer.
# - You can run tests after each question or after finishing all questions.
# - Running tests to see if your solutions are right:
#     - File -> Save Notebook to save exercises.ipynb.
#     - File -> New -> Terminal to open a Terminal.
#     - Use command `python test_runner.py` to run test.
# - When you are ready to submit, click File -> Export Notebook As -> Executable Script.
# - Rename the exported Python script with your student ID(e.g. `b01234567.py`) and upload to the Assignment session on NTU COOL/NTNU Moodle.

# ## 01. Define a function named `calculate_movie_minutes(hours, mins)` which returns the time of a movie in minutes from hours and minutes.
# 
# - Expected inputs: 2 numerics `hours` and `mins`.
# - Expected outputs: a numeric.

# In[ ]:


def calculate_movie_minutes(hours, mins):
    """
    >>> calculate_movie_minutes(2, 22) # The Shawshank Redemption
    142
    >>> calculate_movie_minutes(2, 55) # The Godfather
    175
    >>> calculate_movie_minutes(2, 32) # The Dark Knight
    152
    """
    ### BEGIN SOLUTION
    answer = hours*60+mins
    return answer
    ### END SOLUTION


# ## 02. Define a function named `convert_kilometer_to_mile(km)` which converts kilometers to miles of a given distance in kilometers.
# 
# \begin{equation}
# 1 \; \text{km} = 0.621371192 \; \text{mile}
# \end{equation}
# 
# - Expected inputs: a numerics `km`.
# - Expected outputs: a numeric.

# In[ ]:


def convert_kilometer_to_mile(km):
    """
    >>> convert_kilometer_to_mile(42.195) # a full marathon
    26.21875744644
    >>> convert_kilometer_to_mile(21.095) # a half marathon
    13.10782529524
    """
    ### BEGIN SOLUTION
    mile = km*0.621371192
    return mile
    ### END SOLUTION


# ## 03. Define a function named `convert_fahrenheit_to_celsius(x)` which converts Fahrenheit degrees to Celsius degrees.
# 
# \begin{equation}
# Celsius^{\circ} C = (Fahrenheit^{\circ} F - 32) \times \frac{5}{9}
# \end{equation}
# 
# - Expected inputs: a numeric `x`.
# - Expected outputs: a numeric.

# In[ ]:


def convert_fahrenheit_to_celsius(x):
    """
    >>> convert_fahrenheit_to_celsius(212)
    100.0
    >>> convert_fahrenheit_to_celsius(32)
    0.0
    """
    ### BEGIN SOLUTION
    answer = (x-32)*(5/9)
    return answer
    ### END SOLUTION


# ## 04. Define a function named `calculate_bmi(height, weight)` which calculates BMI according to heights in centimeters and weights in kilograms.
# 
# \begin{equation}
# BMI = \frac{weight_{kg}}{height_{m}^2}
# \end{equation}
# 
# - Expected inputs: 2 numerics `height` and `weight`.
# - Expected outputs: a numeric.

# In[ ]:


def calculate_bmi(height, weight):
    """
    >>> calculate_bmi(216, 147) # Shaquille O'Neal in his prime
    31.507201646090532
    >>> calculate_bmi(206, 113) # LeBron James
    26.628334433028563
    >>> calculate_bmi(211, 110) # Giannis Antetokounmpo
    24.70744143213315
    """
    ### BEGIN SOLUTION
    bmi = weight/((height/100)**2)
    return bmi
    ### END SOLUTION


# ## 05. Define a function named `show_integer_with_commas(x)` which returns an integer in comma format. 
# 
# - Expected inputs: a numeric `x`.
# - Expected outputs: a string.

# In[ ]:


def show_integer_with_commas(x):
    """
    >>> show_integer_with_commas(1000)
    '1,000'
    >>> show_integer_with_commas(1000000)
    '1,000,000'
    >>> show_integer_with_commas(1000000000)
    '1,000,000,000'
    """
    ### BEGIN SOLUTION
    return f"{x:,}"
    
    ### END SOLUTION


# ## 06. Define a function named `show_big_mac_index(country, currency, price)` which returns the Big Mac Index given a country, its currency, and the price of a Big Mac. 
# 
# - Expected inputs: 2 strings and a numeric.
# - Expected outputs: a string.

# In[ ]:


def show_big_mac_index(country, currency, price):
    """
    >>> show_big_mac_index('US', 'USD', 5.65)
    A Big Mac costs 5.65 USD in US.
    >>> show_big_mac_index('South Korea', 'Won', 6520)
    A Big Mac costs 6,520.00 Won in South Korea.
    >>> show_big_mac_index('Taiwan', 'NTD', 72)
    A Big Mac costs 72.00 NTD in Taiwan.
    """
    ### BEGIN SOLUTION
    return f"A Big Mac costs {price:,.2f} {currency} in {country}."
    ### END SOLUTION


# ## 07. Define a function named `is_positive(x)` which returns whether `x` is positive or not.
# 
# - Expected inputs: a numeric.
# - Expected outputs: a boolean.

# In[ ]:


def is_positive(x):
    """
    >>> is_positive(-1)
    False
    >>> is_positive(0)
    True
    >>> is_positive(1)
    True
    """
    ### BEGIN SOLUTION
    return x == True or x == False
    ### END SOLUTION


# ## 08. Define a function named `is_a_divisor(x, y)` which returns whether `x` is a divisor of `y` or not.
# 
# - Expected inputs: 2 integers.
# - Expected outputs: a boolean.

# In[ ]:


def is_a_divisor(x, y):
    """
    >>> is_a_divisor(1, 3)
    True
    >>> is_a_divisor(2, 3)
    False
    >>> is_a_divisor(3, 3)
    True
    >>> is_a_divisor(1, 4)
    True
    >>> is_a_divisor(2, 4)
    True
    >>> is_a_divisor(3, 4)
    False
    >>> is_a_divisor(4, 4)
    True
    """
    ### BEGIN SOLUTION
    return y%x == 0
    ### END SOLUTION


# ## 09. Define a function named `are_vowels_contained(x)` which returns whether x contains one of the vowels: a, e, i, o, u.
# 
# - Expected inputs: a string.
# - Expected outputs: a boolean.

# In[ ]:


def are_vowels_contained(x):
    """
    >>> are_vowels_contained('pythn')
    False
    >>> are_vowels_contained('ncnd')
    False
    >>> are_vowels_contained('rtclt')
    False
    >>> are_vowels_contained('python')
    True
    >>> are_vowels_contained('anaconda')
    True
    >>> are_vowels_contained('reticulate')
    True
    """
    ### BEGIN SOLUTION
    return "a" in x or "e" in x or "i" in x or "o" in x or "u" in x
    ### END SOLUTION


# ## 10. Define a function named `are_all_vowels_contained(x)` which returns whether x contains all of the vowels: a, e, i, o, u.
# 
# - Expected inputs: a string.
# - Expected outputs: a boolean.

# In[ ]:


def are_all_vowels_contained(x):
    """
    >>> are_all_vowels_contained('python')
    False
    >>> are_all_vowels_contained('anaconda')
    False
    >>> are_all_vowels_contained('reticulate')
    False
    >>> are_all_vowels_contained('anaconda and reticulate')
    True
    """
    ### BEGIN SOLUTION
    return "a" in x and "e" in x and "i" in x and "o" in x and "u" in x
    ### END SOLUTION

