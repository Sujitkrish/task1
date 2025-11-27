word = input("Enter")
vowels=["a","e","i","o","u"]
def count(a):
    output = 0
    for i in word.lower():
        if i in vowels:
            output = output+1
    return output

print(count(word))







