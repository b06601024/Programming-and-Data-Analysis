#!/usr/bin/env python
# coding: utf-8

# # Programming and Data Analysis
# 
# > Midterm
# 
# Kuo, Yao-Jen <yaojenkuo@ntu.edu.tw> from [DATAINPOINT](https://www.datainpoint.com)

# In[ ]:


import json


# ## Instructions
# 
# - The assignment will be disconnected if idling over 10 minutes, we can reactivate a new session by clicking the assignment link again.
# - We've imported necessary modules at the top of each assignment.
# - We've put necessary files(if any) in the working directory.
# - We've defined the names of functions/inputs/parameters for you.
# - Write down your solution between the comments `### BEGIN SOLUTION` and `### END SOLUTION`.
# - It is NECESSARY to `return` the answer, tests will fail by just printing out the answer.
# - It is known that `SyntaxError` and `IndentationError` might break our `test_runner.py` and results in a zero point grade. It is highly recommended testing your solution by calling functions/methods in notebook or running tests before submission.
# - Running tests to see if your solutions are right:
#     - File -> Save Notebook to save exercises.ipynb.
#     - File -> New -> Terminal to open a Terminal.
#     - Use command `python test_runner.py` to run test.
# - When you are ready to submit, click File -> Export Notebook As -> Executable Script.
# - Double check your executable script is truly an executable Python script.
# - Rename the exported Python script with your student ID(e.g. `b01234567.py`) and upload to the Assignment session on NTU COOL/NTNU Moodle.

# ## 01. Define a function named `flip_dict_key_value_pairs` which flips a given dictionary's key-value pairs.
# 
# - Expected inputs: `dict`.
# - Expected outputs: `dict`.

# In[ ]:


def flip_dict_key_value_pairs(x: dict) -> dict:
    """
    >>> flip_dict_key_value_pairs({'TWN': 'Taiwan'})
    {'Taiwan': 'TWN'}
    >>> flip_dict_key_value_pairs({'TWN': 'Taiwan', 'JPN': 'Japan', 'LTU': 'Lithuania', 'SVN': 'Slovenia'})
    {'Taiwan': 'TWN', 'Japan': 'JPN', 'Lithuania': 'LTU', 'Slovenia': 'SVN'}
    """
    ### BEGIN SOLUTION
    x = {value:key for key, value in x.items()}
    return x
    ### END SOLUTION


# ## 02. Define a class named `RangePrime` which instantiates objects with an attribute `range_list` and a method `filter_primes()`.
# 
# - Expected inputs: `int`.
# - Expected outputs: `list`.

# In[ ]:


class RangePrime:
    """
    >>> range_prime = RangePrime(1, 5)
    >>> range_prime.range_list
    [1, 2, 3, 4, 5]
    >>> range_prime.filter_primes()
    [2, 3, 5]
    >>> range_prime = RangePrime(6, 15)
    >>> range_prime.range_list
    [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    >>> range_prime.filter_primes()
    [7, 11, 13]
    """
    ### BEGIN SOLUTION
    def __init__(self, start_number: int, end_number: int):
        self.start_number = start_number
        self.end_number = end_number
        self.range_list = list(range(start_number, end_number+1))
    def filter_primes(self) -> list:
        def fil_(num):
            fil = True
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        fil = False
            else:
                fil = False
            if fil:
                return num
        return list(filter(fil_, self.range_list))    
    ### END SOLUTION


# ## 03. Define a class named `MinMaxFinder` which instantiates objects with 4 methods `get_min()`, `get_max()`, `get_idxmin()`, and `get_idxmax()` that is able to find the minimum and maximum values/indexes given a `list`. 
# 
# - Expected inputs: `list`.
# - Expected outputs: `int` | `list`.

# In[ ]:


class MinMaxFinder:
    """
    >>> min_max_finder = MinMaxFinder([2, 3, 5, 7, 11])
    >>> min_max_finder.get_min()
    2
    >>> min_max_finder.get_max()
    11
    >>> min_max_finder.get_idxmin()
    [0]
    >>> min_max_finder.get_idxmax()
    [4]
    >>> min_max_finder = MinMaxFinder([2, 2, 3, 5, 7, 11, 11])
    >>> min_max_finder.get_min()
    2
    >>> min_max_finder.get_max()
    11
    >>> min_max_finder.get_idxmin()
    [0, 1]
    >>> min_max_finder.get_idxmax()
    [5, 6]
    """
    ### BEGIN SOLUTION
    def __init__(self, list_: list):
        self.list_ = list_
    def get_min(self):
        return min(self.list_)
    def get_max(self):
        return max(self.list_)  
    def get_idxmin(self):
        tmp = min(self.list_)
        return [i for i, x in enumerate(self.list_) if x == tmp]
    def get_idxmax(self):
        tmp = max(self.list_)
        return [i for i, x in enumerate(self.list_) if x == tmp]    
    ### END SOLUTION


# ## 04. Define a class named `PigLatin` which instantiates objects performing the Pig Latin language game with 1 attribute `original_word` and 1 method `alter()`.
# 
# - For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the word sequence. Then, "ay" is added. e.g. "pig" -> "igpay". When words begin with consonant clusters (multiple consonants that form one sound), the whole sound is added to the end. e.g. "smile" -> "ilesmay"
# - For words that begin with vowel sounds, the vowel is left alone, and "yay" is added to the end. e.g. "eat" -> "eatyay"
# 
# Source: <https://en.wikipedia.org/wiki/Pig_Latin>
# 
# - Expected inputs: `str`.
# - Expected outputs: `str`.

# In[ ]:


class PigLatin:
    """
    >>> pig_latin = PigLatin("pig")
    >>> pig_latin.original_word
    'pig'
    >>> pig_latin.alter()
    'igpay'
    >>> pig_latin = PigLatin("smile")
    >>> pig_latin.original_word
    'smile'
    >>> pig_latin.alter()
    'ilesmay'
    >>> pig_latin = PigLatin("eat")
    >>> pig_latin.original_word
    'eat'
    >>> pig_latin.alter()
    'eatyay'
    """
    ### BEGIN SOLUTION
    def __init__(self, input_str: str):
        self.vowel = {'a','e','i','o','u'}
        self.original_word = input_str
    def alter(self):
        output = ''
        for i, s in enumerate(self.original_word.lower()):
            if (s in self.vowel) & (i == 0):
                return self.original_word+'yay'
            elif s in self.vowel:
                output = self.original_word[i:]+output+'ay'
                return output
            elif s not in self.vowel:
                output+=s    
    ### END SOLUTION


# ## 05. Define a class named `RotThirteen` which instantiates objects performing the ROT13 cipher with 2 methods `rotate_char()` and `rotate_sentence()`.
# 
# Source: <https://en.wikipedia.org/wiki/ROT13>
# 
# - Expected inputs: `str`.
# - Expected outputs: `str`.

# In[ ]:


class RotThirteen:
    """
    >>> rot_13 = RotThirteen()
    >>> rot_13.rotate_char("A")
    'N'
    >>> rot_13.rotate_char("B")
    'O'
    >>> rot_13.rotate_char("Y")
    'L'
    >>> rot_13.rotate_char("Z")
    'M'
    >>> rot_13.rotate_char("a")
    'n'
    >>> rot_13.rotate_char("b")
    'o'
    >>> rot_13.rotate_char("y")
    'l'
    >>> rot_13.rotate_char("z")
    'm'
    >>> rot_13.rotate_sentence("Ornhgvshy vf orggre guna htyl.")
    'Beautiful is better than ugly.'
    >>> rot_13.rotate_sentence("Abj vf orggre guna arire.")
    'Now is better than never.'
    """
    ### BEGIN SOLUTION
    def __init__(self):
        self.chars_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.chars_small = "abcdefghijklmnopqrstuvwxyz"
    def rotate_char(self, input_str: str) -> str:
        if (input_str not in self.chars_big) & (input_str not in self.chars_small):
            return input_str
        index = self.chars_small.index(input_str.lower())+13
        if index>25:
            index = index % 26
        if input_str in self.chars_big:
            return self.chars_big[index]
        else:
            return self.chars_small[index]
    def rotate_sentence(self, input_str: str) -> str:
        return ''.join([self.rotate_char(s) for s in input_str])    
    ### END SOLUTION


# ## 06. Define a function named `lookup_zip_codes` which returns the 3-digit zip code given the name of county and town, based on `zip_codes.json` in working directory.
# 
# - Expected inputs: `str`.
# - Expected outputs: `str`.

# In[ ]:


def lookup_zip_codes(county: str, town: str) -> str:
    """
    >>> lookup_zip_codes("臺北市", "中正區")
    '100'
    >>> lookup_zip_codes("基隆市", "中正區")
    '202'
    >>> lookup_zip_codes("臺北市", "中山區")
    '104'
    >>> lookup_zip_codes("基隆市", "中山區")
    '203'
    >>> lookup_zip_codes("臺北市", "大安區")
    '106'
    >>> lookup_zip_codes("臺中市", "大安區")
    '439'
    """
    ### BEGIN SOLUTION
    zip_code_file = json.load(open('zip_codes.json', 'r'))
    return [l['zipCode'] for l in zip_code_file if ((l['county'] == county) & (l['town'] == town))][0]       
    ### END SOLUTION


# ## 07. Define a function named `lookup_country_iso_codes` which returns the 2-digit and 3-digit ISO country code given the name of country, based on `countries.json` in working directory.
# 
# - Expected inputs: `str`.
# - Expected outputs: `tuple`.

# In[ ]:


def lookup_country_iso_codes(country: str) -> tuple:
    """
    >>> lookup_country_iso_codes("Taiwan")
    ('TW', 'TWN')
    >>> lookup_country_iso_codes("Japan")
    ('JP', 'JPN')
    >>> lookup_country_iso_codes("Lithuania")
    ('LT', 'LTU')
    >>> lookup_country_iso_codes("Slovenia")
    ('SI', 'SVN')
    """
    ### BEGIN SOLUTION
    countries_file = json.load(open('countries.json', 'r'))
    select = [l for l in countries_file if l['name'] == country]
    return (select[0]['iso2'], select[0]['iso3'])    
    ### END SOLUTION


# ## 08. Define a class named `CoachRoster` instantiates objects with 2 methods `get_head_coach()` and `get_assistant_coaches()` returns the coach roster of NBA's standard league given a team's tricode based on `coaches.json` in working directory.
# 
# - Expected inputs: `str`.
# - Expected outputs: `str` | `list`.

# In[ ]:


class CoachRoster:
    """
    >>> cr = CoachRoster("coaches.json")
    >>> cr.get_head_coach("ATL")
    'Nate McMillan'
    >>> cr.get_assistant_coaches("ATL")
    ['Chris Jent',
     'Joe Prunty',
     'Jamelle McMillan',
     'Matt Hill',
     'Nick Van Exel',
     'Scottie Parker']
    >>> cr.get_head_coach("BKN")
    'Steve Nash'
    >>> cr.get_assistant_coaches("BKN")
    ['Jacque Vaughn',
     'David Vanterpool',
     'Brian Keefe',
     'Adam Harrington',
     'Jordan Ott',
     'Tiago Splitter',
     'Royal Ivey',
     'Ryan Forehan-Kelly',
     'Sebastien Poirier']
    """
    ### BEGIN SOLUTION
    def __init__(self, file_name):
        self.coach_file = json.load(open(file_name, 'r'))
    def get_head_coach(self, team_name):
        return [l['firstName']+' '+l['lastName'] for l in self.coach_file['league']['standard'] if (l['teamSitesOnly']['teamTricode'] == team_name) & (l['isAssistant'] == False)][0]
    def get_assistant_coaches(self, team_name):
        return [l['firstName']+' '+l['lastName'] for l in self.coach_file['league']['standard'] if (l['teamSitesOnly']['teamTricode'] == team_name) & (l['isAssistant'] == True)]    
    ### END SOLUTION


# ## 09. Define a function named `find_tallest_shortest_players` which returns the tallest and the shortest NBA standard league players based on `players.json` in working directory.
# 
# PS. Skip those players whose `heightMeters` is an empty string.
# 
# - Expected inputs: `str`.
# - Expected outputs: `dict`.

# In[ ]:


def find_tallest_shortest_players(x: str) -> dict:
    """
    >>> find_tallest_shortest_players('tallest')
    {'heightMeters': 2.29, 'players': ['Tacko Fall']}
    >>> find_tallest_shortest_players('shortest')
    {'heightMeters': 1.78, 'players': ['Facundo Campazzo', 'Markus Howard']}
    """
    ### BEGIN SOLUTION
    player_file = json.load(open('players.json', 'r'))
    d = {'heightMeters': 0, 'players':[]}
    if x == 'tallest':
        max_ = 0
        for l in player_file['league']['standard']:
            if (l['heightMeters'] != ''):
                if (float(l['heightMeters']) == max_):
                    d['players'].append(l['firstName']+' '+l['lastName'])
                if (float(l['heightMeters']) > max_):
                    max_ = float(l['heightMeters'])
                    d = {'heightMeters': float(l['heightMeters']), 'players':[l['firstName']+' '+l['lastName']]}
    if x == 'shortest':
        min_ = float('inf')
        for l in player_file['league']['standard']:
            if (l['heightMeters'] != ''):
                if (float(l['heightMeters']) == min_):
                    d['players'].append(l['firstName']+' '+l['lastName'])
                if (float(l['heightMeters']) < min_):
                    min_ = float(l['heightMeters'])
                    d = {'heightMeters': float(l['heightMeters']), 'players':[l['firstName']+' '+l['lastName']]}
    return d    
    ### END SOLUTION


# ## 10. Define a function named `get_current_team_roster` which returns the current roster of 2021-2022 season for every NBA standard league team based on the `teamId` attribute from `players.json` and `teams.json` in working directory.
# 
# - Expected inputs: `str`.
# - Expected outputs: `list`.

# In[ ]:


def get_current_team_roster(team_tricode: str) -> list:
    """
    >>> get_current_team_roster("BKN")
    ['LaMarcus Aldridge',
     "DeAndre' Bembry",
     'Bruce Brown',
     'Jevon Carter',
     'Nic Claxton',
     'David Duke Jr.',
     'Kevin Durant',
     'Kessler Edwards',
     'Blake Griffin',
     'James Harden',
     'Joe Harris',
     'Kyrie Irving',
     'James Johnson',
     'Patty Mills',
     'Paul Millsap',
     "Day'Ron Sharpe",
     'Cam Thomas']
    >>> get_current_team_roster("MIA")
    ['Bam Adebayo',
     'Jimmy Butler',
     'Dewayne Dedmon',
     'Marcus Garrett',
     'Udonis Haslem',
     'Tyler Herro',
     'Kyle Lowry',
     'Caleb Martin',
     'Markieff Morris',
     'KZ Okpala',
     'Victor Oladipo',
     'Duncan Robinson',
     'Max Strus',
     'P.J. Tucker',
     'Gabe Vincent',
     'Omer Yurtseven']
    """
    ### BEGIN SOLUTION
    teams = json.load(open('teams.json', 'r'))
    players = json.load(open('players.json', 'r'))
    team_id = [l['teamId'] for l in teams['league']['standard'] if l['tricode']== team_tricode][0]
    return [l['firstName']+' '+ l['lastName'] for l in players['league']['standard'] if l['teamId'] == team_id]
    ### END SOLUTION

