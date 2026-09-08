# string operations
def function1():
    data = "this Is My DaTa"

    # convert the text case
    print(f"convert to lower case = {data.lower()}")
    print(f"convert to upper case = {data.upper()}")

# function1()

def function2():
    data = "The SBI furnished details of the purchase and redemption of electoral bonds to the Election Commission on the Supreme Court’s directions. The unique alphanumeric code on the bonds can be used to match each donation to the political party that received it."

    # convert the data to lowercase
    data.lower()

    # split the data into multiple sentences
    # group of words that ends at .
    # to find a sentence split the data on .
    # sentence tokenization
    sentences = data.split('.')
    # print(sentences)

    # split the data into words
    all_words = []
    for sentence in sentences:
        # find the words
        words = sentence.split(' ')
        # all_words.extend(words)
        for word in words:
            if len(word) > 0:
                all_words.append(word)
        # all_words.extend([word for word in words if len(word) > 0])

    # print(all_words)   
    word_count = {}
    for word in all_words:
        # check if the word in word_count dict
        # print(word)
        count = word_count.get(word)
        # print(count)
        if count is None:
            # the word is not yet added to dictionary
            word_count[word] = 1
        else:
            word_count[word] += 1

    print(word_count)        

# function2()

def function3():
    persons = [
        {"name": "steve", "address": "USA", "age": 58, "email": "steve@apple.com"},
        {"name": "Bill Gates", "address": "India", "age": 60, "email": "bill@microsoft.com"},
        {"name": "Bill Joy", "address": "USA", "age": 70, "email": "bill.joy@sunbeaminfo.com"}
    ]

    for person in persons:
        # < ==> left align 
        # ^ ==> center align
        # > ==> right align
        print(f"{person['email']:<25} | {person['name']:<10} | {person['age']:^4} | {person['address']:>6}")

# function3()        

def function4():
    number = 30234324
    print(f"number in decimal = {number}")
    print(f"number in binary = {number:b}")

function4()