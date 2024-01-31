text = "abcdefg"
print(dir(text))
help(text.isidentifier)
print(text.isidentifier()) # is abcdefg a valid identifier?
print("1234".isidentifier()) # is 1234 a valid identifier?
print("ananananananananananan".count("ana"))
print("ananananananananananan".replace("ana", "banana"))
print("ananananananananananan".find("ana", 1))
print("bbbbbabbbbbbabbbbbbbbabbbabb".split("a"))
print("this is a sentence and I want the words".split(" "))
sentence = "Hello, kind-sir; how many! I be of service today?"
punctuation = ".,;!?-"
# sanitize the sentence
for p in punctuation:
    sentence = sentence.replace(p, " ") # replace the punctuation with nothing
print(sentence)
sentence = sentence.replace("  ", " ") # replace double spaces with single spaces
# split the sentence into words
words = sentence.split(" ")
print(words)

text = "cat"
print(text.upper())
print(text)

name = "John"
second_name = "Bob"
print(f"Hi, {name} how are you? My name is {second_name}")
name = "Jane"
second_name = "Mary"
print(f"Hi, {name} how are you? My name is {second_name}")
