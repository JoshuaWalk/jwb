word = input("Enter a word or phrase to see if it's a palindrome: ")
clean = ''
for c in word:
    if c.isalnum():
        clean = clean + c.lower()
reverse = clean[::-1]
if clean == "":
    print("no valid characters entered")
elif clean == reverse:
    print(True) 
else:
    print(False)