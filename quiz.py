


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