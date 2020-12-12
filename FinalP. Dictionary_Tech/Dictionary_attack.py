#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
print("Can your password survive a dictionary attack?")
counter = 0
#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
while True:
    test_password = input("Type in a trial password: ")
    counter +=1
    if counter == 3:
        break
    for text in f:
        if test_password.strip() == text.strip():
            print("Weak Password, try again!")
            print(test_password)
if test_password.strip() != text.strip():
        print("Strong Password")


f.close()




#dictionarylist = []

#dictionaryList.append(test_password)






#Write logic to see if the password is in the dictionary file below here:
