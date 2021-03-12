def reverse_text(string):
    for letter in string[::-1]:
        yield letter

for char in reverse_text("step"):
    print(char, end='')
