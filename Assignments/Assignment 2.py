#!/usr/bin/env python
# coding: utf-8

# # Programming and Data Analysis
# 
# > Assignment 2
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
# - `SyntaxError` breaks our `test_runner.py` and results in a zero point grade. It is highly recommended testing your solution by calling functions/methods in notebook or running tests before submission.
# - Running tests to see if your solutions are right:
#     - File -> Save Notebook to save exercises.ipynb.
#     - File -> New -> Terminal to open a Terminal.
#     - Use command `python test_runner.py` to run test.
# - When you are ready to submit, click File -> Export Notebook As -> Executable Script.
# - Rename the exported Python script with your student ID(e.g. `b01234567.py`) and upload to the Assignment session on NTU COOL/NTNU Moodle.

# ## 01. Define a function named `find_bmi_category(bmi)` which returns the category of BMI according to BMI.
# 
# Source: <https://en.wikipedia.org/wiki/Body_mass_index#Categories>
# 
# - Expected inputs: `float`.
# - Expected outputs: `str`.

# In[ ]:


def find_bmi_category(bmi: float) -> str:
    """
    >>> find_bmi_category(32.90) # Zion Williamson, professional basketball player
    'Class I Obese'
    >>> find_bmi_category(26.63) # LeBron James, professional basketball player
    'Pre-obese'
    >>> find_bmi_category(24.83) # Roger Federer, professional tennis player
    'Normal range'
    >>> find_bmi_category(17.58) # Suguru Osako, professional marathon runner 
    'Mild thinness'
    """
    ### BEGIN SOLUTION
    if bmi < 16.0:
        msg = "Severe thinness"
        return msg
    elif bmi >= 16.0 and bmi <= 16.9:
        msg = "Moderate thinness"
        return msg
    elif bmi >= 17.0 and bmi <= 18.4:
        msg = "Mild thinness"
        return msg
    elif bmi >= 18.5 and bmi <= 24.9:
        msg = "Normal range"
        return msg
    elif bmi >= 25.0 and bmi <= 29.9:
        msg = "Pre-obese"
        return msg
    elif bmi >= 30.0 and bmi <= 34.9:
        msg = "Class I Obese"
        return msg
    elif bmi >= 35.0 and bmi <= 39.9:
        msg = "Class II Obese"
        return msg
    elif bmi >= 40.0:
        msg = "Class III Obese"
        return msg    
    ### END SOLUTION


# ## 02. Define a function named `convert_temperature_degrees_to_different_scales(x, from_scale, to_scale)` which converts temperature degrees between 3 different scales.
# 
# \begin{equation}
# \text{Fahrenheit}(^{\circ} F) = \text{Celsius}(^{\circ} C) \times \frac{9}{5} + 32 \\
# \text{Celsius}(^{\circ} C) = (\text{Fahrenheit}(^{\circ} F) - 32) \times \frac{5}{9} \\
# \text{Kelvin}(K) = Celsius(^{\circ} C) + 273.15
# \end{equation}
# 
# - Expected inputs: `float`/`str`/`str`.
# - Expected outputs: `float`.

# In[ ]:


def convert_temperature_degrees_to_different_scales(x: float, from_scale: str, to_scale: str) -> float:
    """
    >>> convert_temperature_degrees_to_different_scales(0, "Celsius", "Fahrenheit")
    32.0
    >>> convert_temperature_degrees_to_different_scales(100, "Celsius", "Fahrenheit")
    212.0
    >>> convert_temperature_degrees_to_different_scales(32, "Fahrenheit", "Celsius")
    0.0
    >>> convert_temperature_degrees_to_different_scales(212, "Fahrenheit", "Celsius")
    100.0
    >>> convert_temperature_degrees_to_different_scales(0, "Celsius", "Kelvin")
    273.15
    >>> convert_temperature_degrees_to_different_scales(100, "Celsius", "Kelvin")
    373.15
    >>> convert_temperature_degrees_to_different_scales(32, "Fahrenheit", "Kelvin")
    273.15
    >>> convert_temperature_degrees_to_different_scales(212, "Fahrenheit", "Kelvin")
    373.15
    """
    ### BEGIN SOLUTION
    if from_scale == "Celsius" and to_scale == "Fahrenheit":
        x1 = x*(9/5)+32 
    elif from_scale == "Fahrenheit" and to_scale == "Celsius":
        x1 = (x-32)*(5/9)
    elif from_scale == "Celsius" and to_scale == "Kelvin":
        x1 = x+273.15  
    elif from_scale == "Fahrenheit" and to_scale == "Kelvin":
        x1 = (x-32)*(5/9)+273.15    
    elif from_scale == "Kelvin" and to_scale == "Celsius":
        x1 = x-273.15
    elif from_scale == "Kelvin" and to_scale == "Fahrenheit":
        x1 = x-273.15/(5/9)+32
    return x1    
    ### END SOLUTION


# ## 03. Define a function named `check_types(x)` which returns the type of `x` in a string format.
# 
# - Expected inputs: an unknown type of `x`.
# - Expected outputs: `str`.

# In[ ]:


def check_types(x) -> str:
    """
    >>> check_types(1)
    'int'
    >>> check_types(1.0)
    'float'
    >>> check_types(False)
    'bool'
    >>> check_types(True)
    'bool'
    >>> check_types('5566')
    'str'
    >>> check_types(None)
    'NoneType'
    """
    ### BEGIN SOLUTION
    if type(x) == int:
        return "int"
    elif type(x) == float:
        return "float"
    elif type(x) == bool:
        return "bool"
    elif type(x) == str:
        return "str"
    elif type(x) == type(None):
        return "NoneType"   
    ### END SOLUTION


# ## 04. Define a function named `fizz_buzz(x)` which returns `'Fizz'` when `x` can be divided by 3, returns `'Buzz'` when `x` can be divided by 5, returns `'Fizz Buzz'` when `x` can be divided by both 3 and 5. Otherwise, the function returns `x` itself.
# 
# - Expected inputs: `int`.
# - Expected outputs: `int`/`str`.

# In[ ]:


from typing import Union

def fizz_buzz(x: int) -> Union[int, str]:
    """
    >>> fizz_buzz(0)
    'Fizz Buzz'
    >>> fizz_buzz(3)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(15)
    'Fizz Buzz'
    >>> fizz_buzz(16)
    16
    """
    ### BEGIN SOLUTION
    if x % 3 == 0:
        ans = "Fizz"
    if x % 5 == 0:
        ans = "Buzz"
    if x % 3 == 0 and x % 5 == 0:
        ans = "Fizz Buzz"
    if (x % 3 != 0) and (x % 5 != 0):
        ans = x
    return ans
    ### END SOLUTION


# ## 05. Define a function named `first_n_fizz_buzz(n)` which returns the first `n` FizzBuzz numbers as a `list`.
# 
# - Expected inputs: `int`.
# - Expected outputs: `list`.

# In[ ]:


def first_n_fizz_buzz(n: int) -> list:
    """
    >>> first_n_fizz_buzz(4)
    ['Fizz Buzz', 1, 2, 'Fizz']
    >>> first_n_fizz_buzz(6)
    ['Fizz Buzz', 1, 2, 'Fizz', 4, 'Buzz']
    >>> first_n_fizz_buzz(16)
    ['Fizz Buzz', 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz']
    """
    ### BEGIN SOLUTION
    result = []
    for x in range(0, n):
        if x % 3 == 0 and x % 5 == 0:
            result.append("Fizz Buzz")
        elif x % 3 == 0:
            result.append('Fizz')
        elif x % 5 == 0:
            result.append('Buzz')
        else:
            result.append(int(x))
    return result
    ### END SOLUTION


# ## 06. Define a function named `retrieve_the_middle_elements(x)` which returns the middle elements of a given `list`. 
# 
# - Expected inputs: `list`.
# - Expected outputs: `int`/`tuple`.

# In[ ]:


from typing import Union

def retrieve_the_middle_elements(x: list) -> Union[int, tuple]:
    """
    >>> retrieve_the_middle_elements([2, 3, 5])
    3
    >>> retrieve_the_middle_elements([2, 3, 5, 7])
    (3, 5)
    >>> retrieve_the_middle_elements([2, 3, 5, 7, 11])
    5
    >>> retrieve_the_middle_elements([2, 3, 5, 7, 11, 13])
    (5, 7)
    """
    ### BEGIN SOLUTION
    half_len = int((len(x) / 2))
    if len(x) % 2 == 0:
        return (x[half_len -1] ,x[half_len]) 
    else:
        return x[half_len]
    ### END SOLUTION


# ## 07. Define a function named `median(x)` which returns the median value of a given list.
# 
# Source: <https://en.wikipedia.org/wiki/Median>
# 
# - Expected inputs: `list`
# - Expected outputs: `int`/`float`

# In[ ]:


from typing import Union

def median(x: list) -> Union[int, float]:
    """
    >>> median([2, 3, 5, 7, 11])
    5
    >>> median([2, 3, 5, 7, 11, 13])
    6.0
    >>> median([11, 13, 17, 2, 3, 5, 7])
    7
    >>> median([7, 11, 13, 17, 19, 2, 3, 5])
    9.0
    """
    ### BEGIN SOLUTION
    sorted_x = sorted(x)
    half_len = int(len(sorted_x) / 2)
    if len(sorted_x) % 2 == 0:
        return (sorted_x[half_len -1] + sorted_x[half_len]) / 2
    else:
        return sorted_x[half_len]
    ### END SOLUTION


# ## 08. Define a function named `collect_divisors(x)` which returns all positive divisors of a given `int`.
# 
# Source: <https://en.wikipedia.org/wiki/Divisor>
# 
# - Expected inputs: `int`.
# - Expected outputs: `list`.

# In[ ]:


def collect_divisors(x: int) -> list:
    """
    >>> collect_divisors(1)
    [1]
    >>> collect_divisors(2)
    [1, 2]
    >>> collect_divisors(3)
    [1, 3]
    >>> collect_divisors(4)
    [1, 2, 4]
    >>> collect_divisors(5)
    [1, 5]
    """
    ### BEGIN SOLUTION
    out = []
    for i in range(1,x+1):
        if x % i == 0:
            out.append(i)
    return out

    ### END SOLUTION


# ## 09. Define a function named `is_prime(x)` which returns whether `x` is a prime number or not. You may extend the previous `collect_divisors()` function to solve this problem.
# 
# Source: <https://en.wikipedia.org/wiki/Prime_number>
# 
# - Expected inputs: `int`
# - Expected outputs: `bool`

# In[ ]:


def is_prime(x: int) -> bool:
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    """
    ### BEGIN SOLUTION
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
                return False
        return True      
    ### END SOLUTION


# ## 10. Define a function named `reverse_vowels(x)` converts the vowels in a word from upper-cased to lower-cased, and from lower-cased to upper-cased.
# 
# - Expected inputs: `str`
# - Expected outputs: `str`

# In[ ]:


def reverse_vowels(x: str) -> str:
    """
    >>> reverse_vowels('Luke Skywalker')
    'LUkE SkywAlkEr'
    >>> reverse_vowels('Darth Vadar')
    'DArth VAdAr'
    >>> reverse_vowels('The Avengers')
    'ThE avEngErs'
    """
    ### BEGIN SOLUTION
    new_phrase = ""
    for letter in x:
        if letter in ['a', 'e', 'i', 'o', 'u'] or letter in ['A', 'E', 'I', 'O', 'U']:
            new_phrase += letter.swapcase()
        else:
            new_phrase += letter
    return new_phrase   
    ### END SOLUTION

