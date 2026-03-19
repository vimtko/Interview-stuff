#Code challenge
#Take a string an reverse it

def stringreversed(text):
    return text[::-1] #slicing text[start:end:step] by using step -1 starts from the end of the text

print(stringreversed("helloworld")) #output: dlrowolleh


def stringreversed2(text):
    reversed_string=""
    for char in text: #iteration of every character of the text given
        reversed_string = char + reversed_string #adds that character to the list in a inversed order
    return reversed_string

stringreversed2("helloworld 2") #output: dlrowolleh


def stringreversed3(text):
    return "".join(reversed(text)) #adds in reverse order using a pre-built function

stringreversed3("helloworld 3") #output: dlrowolleh



