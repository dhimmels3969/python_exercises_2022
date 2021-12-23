import time
import datetime
from datetime import date
import os
import fileinput
import glob
import re
from collections import Counter
##############################################################
from difflib import SequenceMatcher
from difflib import get_close_matches
##############################################################

customer = (
    ('id','98698761'),
    ('name', 'marry'),
    ('surname', 'smith'),
    ('rented_books', 3 )
    )

def code_exrc_54():
    customer_dict={}
    new_item = {}
    for item in customer:
        new_item[item[0]] = item[1]
        customer_dict.update(new_item)
    return customer_dict
        # print(item[0])
        # print(item[1])
#######################################################################

def code_exrc_55():
    passwords = ['ccavfb', 'baaded', 'bbaa', 'aaeed', 'vbb', 'aadeba', 'aba', 'dee', 'dade', 'abc', 'aae', 'dded',
                 'abb', 'aaf', 'ffaec']
    for pswd in passwords:
        if pswd.__contains__("ba") or pswd.__contains__("ab"):
            print(pswd)

def code_exrc_76():
    list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon']
    list2 = [22, 15, 5, 11, 11, 1, 6, 27, 5, 25, 8, 6, 21, 21, 24, 19, 28, 17, 21, 21, 16, 13, 16, 3, 8, 10, 3, 16, 6, 23]
    new_list=[]
    for i in range(0, len(list2), 7):
        new_list.append(list2[i])
    print(new_list)

def code_exrc_79():
    numbers = [1, 4, 6, 8, 9, 6, 7, 8, 9, 3, 44, 55, 6, 77, 88, 997, 7, 6, 7, 7, 8, 9, 8, 8, 8, 9, 8, 8, 0, 9, 0, 9, 8,
               9, 8, 8, 8, 9, 9, 9, 9, 0, 1, 3, 5, 6, 7, 8, 7, 7, 7, 8, 7, 7, 5, 4, 5, 6, 5, 56, 4, 3, 4, 5, 6, 6, 7, 8,
               8, 9]
    new_list = []
    for x in range(0, len(numbers), 2):
        new_list.append(numbers[x])
    print(sum(new_list) / len(new_list))

##############################################################


def code_exrc_88():
    input = {'a': 5, 'b': 3, 'c': 10}
    results = {}
    return results
##############################################################


def code_exrc_87():
    input = {'a': [1, 2], 'b': [3, 4]}
    total = 0
    for value in input.values():
        total += sum(value)

    # list comprehension
    total_lc = sum([sum(value) for value in input.values()])

    # generator expression
    total_ge = sum(sum(value) for value in input.values())

    # use sum directly
    # total_asd = sum(sum(input.values()))

    print("list comprehension: %s" % total_lc)
    print("generator expression: %s" % total_ge)
    # print("calculate sum directly: %s" % total_asd)

    return total

##############################################################
def talk_90(query, vocabulary):
    return vocabulary[query]


def code_exrc_90():
    vocabulary = {
        "hello": "Hi there!",
        "what's your name": "My name is Roboto!",
        "what is your name": "My name is Roboto!",
        "bye": "Goodbye!"
    }
    print(talk_90('hello', vocabulary))
    print("...")
##############################################################

def code_exrc_88():
    input = {'a': 5, 'b': 3, 'c': 10}
    results = {}
    for key, value in input.items():
        if value > 4:
            results[key] = value
    return results

##############################################################

def talk_92(query, vocabulary):
    if query in vocabulary:
        return vocabulary[query]
    # elif query == "what time is it":
    #     current_time = time.strftime('%H:%M')
    #     return current_time
    else:
        return "I don't understand that"


def code_exrc_92():
    vocabulary = {
        "hello": "Hi there!",
        "what's your name": "My name is Roboto!",
        "what is your name": "My name is Roboto!",
        "bye": "Goodbye!",
        "what time is it": time.strftime('%H:%M')
    }
    results = talk_92("what time is it", vocabulary)
    return results



##############################################################

def talk_93(query, vocabulary):
    best_match = get_close_matches(query, vocabulary.keys(), n=3, cutoff=0.25)[0]
    if len(best_match) > 0:
        if best_match in vocabulary:
            return vocabulary[best_match]
        else:
            return "I don't understand that"
    else:
        return "I don't understand that"


def code_exrc_93():
    vocabulary = {
        "hello": "Hi there!",
        "what's your name": "My name is Roboto!",
        "what is your name": "My name is Roboto!",
        "bye": "Goodbye!",
        "what time is it": time.strftime('%H:%M')
    }
    results = talk_93("tell me the time", vocabulary)
    return results



##############################################################

def foo_94(mydate):
    # mydate.split("-")[1].rjust(2, "0")
    # holddate = mydate.split("-")
    # holddate[0] = holddate[0].rjust(4, "0")
    # holddate[1] = holddate[1].rjust(2, "0")
    # holddate[2] = holddate[2].rjust(2, "0")
    rslvddate = datetime.datetime.strptime(mydate, "%Y-%m-%d").strftime("%A")
    mydate = mydate.split("-")
    mydate[0] = mydate[0].rjust(4, "0")
    mydate[1] = mydate[1].rjust(2, "0")
    mydate[2] = mydate[2].rjust(2, "0")
    mydate = "-".join(mydate)
    results = date.fromisoformat(mydate).strftime('%A')
    return results

##############################################################

def foo_95():
    cwd = os.getcwd()
    for i in range(1,10):
        filename = os.path.join(cwd, "file" + str(i) + ".txt")
        if not os.path.exists(filename):
            f = open(os.path.join(cwd, "file" + str(i) + ".txt"), 'w').close()

    # cwd = os.getcwd()
    # for i in range(1,10):
    #     f = open(os.path.join(cwd, "day" + str(i) + ".txt"), 'x')
    #     f.close()
    return ""

##############################################################

def foo_70():
    # Function gets any Python class object (e.g. str, int, float, etc) and returns the object name as string (i.e. 'str', 'int', 'float')
    def object_to_string(obj):
        items = str(obj).split(" ")
        obj_type = items[-1].replace(">", "").replace("'", "")
        return obj_type

    vocabulary = {
        "hello": "Hi there!",
        "what's your name": "My name is Roboto!",
        "what is your name": "My name is Roboto!",
        "bye": "Goodbye!",
        "what time is it": time.strftime('%H:%M')
    }

    a = object_to_string('<built-in function max>')
    print(a)
    a = object_to_string(type(vocabulary))
    print(a)

##############################################################

def foo_97():
    with fileinput.input(files=('file2.txt', 'file3.txt')) as f:
        lines = []
        number_list = []
        for line in f:
            lines.append(line)
    # read through the list and pick out numerical items...
    for line in lines:
        # numberz= re.findall('\d*\.?\d+',line)
        numberz= re.findall("[0-9]+\.*[0-9]*",line)
        # "[0-9]+\.*[0-9]*"
        if len(numberz) > 0:
            for values in numberz:
                try:
                    converted_value = float(values)
                    number_list.append(converted_value)
                except:
                    pass
            #     if values.isdecimal() or values.isnumeric():
            #         number_list.append(float(values))
    print(number_list)
    avg = sum(values for values in number_list) / len(number_list)
    return avg
##############################################################

def foo_97c():
    text_files = glob.glob("*.txt")
    lists = []
    for text_file in text_files:
        with open(text_file) as file:
            lists.append(file.readlines())

    all_lines = sum(lists, [])

    matches = [re.compile("[0-9]+\.*[0-9]*").search(line) for line in all_lines]

    numbers = [float(match.group(0)) for match in matches if match]
    # print(sum(numbers) / len(numbers))
    avg = sum(numbers) / len(numbers)
    return avg

    # lines = []
    # number_list = []
    # with fileinput.input(files=('file2.txt', 'file3.txt')) as f:
    #     lines.append(f.readlines())
    # all_lines = sum(lines, [])
    #     # for line in f:
    #     #     lines.append(line)
    # # read through the list and pick out numerical items...
    # for line in lines:
    #     # numberz= re.findall('\d*\.?\d+',line)
    #     numberz= re.findall("[0-9]+\.*[0-9]*",line)
    #     # "[0-9]+\.*[0-9]*"
    #     if len(numberz) > 0:
    #         for values in numberz:
    #             try:
    #                 converted_value = float(values)
    #                 number_list.append(converted_value)
    #             except:
    #                 pass
    #         #     if values.isdecimal() or values.isnumeric():
    #         #         number_list.append(float(values))
    # print(number_list)

##############################################################

def foo_99():
    cwd = os.getcwd()
    for i in range(1,51):
        directory = str(i)
        newpath = os.path.join(cwd, directory)
        if not os.path.exists(newpath):
            os.mkdir(newpath)
    return ""
##############################################################

def foo_100():
    cwd = os.getcwd()
    day_folders = ['mon', 'tue', 'wed', 'thu', 'fri']
    for i in range(1, 51):
        directory = str(i)
        newpath = os.path.join(cwd, directory)
        if not os.path.exists(newpath):
            os.mkdir(newpath)
            os.chdir(newpath)
            for folder in day_folders:
                subfolder = os.path.join(newpath, folder)
                if not os.path.exists(subfolder):
                    os.mkdir(subfolder)
    return ""
##############################################################


def foo_116():
    mystring = "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient python, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus."
    mystring_len = len(mystring)
    occurences = Counter(mystring)
    length_without_dots = mystring_len - occurences['.']
    return length_without_dots
##############################################################

