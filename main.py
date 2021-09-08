phoneBook = {'1111111111': 'Amal',
             '2222222222': 'Mohammed',
             '3333333333': 'Khadijah',
             '4444444444': 'Abdullah',
             '5555555555': 'Rawan',
             '6666666666': 'Faisal',
             '7777777777': 'Layla'}


def searchByPhoneNumber(phoneNum):
    phoneNumStr=str(phoneNum)
    if not(len(phoneNumStr) == 10) or not(phoneNumStr.isdigit()):
        print("This is invalid number!")
        return

    for key in phoneBook:
        if(phoneNumStr==key):
            print("This is "+phoneBook[key]+"'s"+" phone number")
            return
    print("Sorry, the number is not found!")
    return



def searchByName(personName):

    if not type(personName) == str:
        print("Please, Enter valid name!")
        return

    for key in phoneBook:
        if personName == phoneBook[key]:
            print("The phone number of "+personName+" is : "+key)
            return
    print("Sorry, the number is not found!")
    return


def insertNewContact(newName, newPhone):
    newPhoneStr=str(newPhone)
    newNameStr=str(newName)
    phoneBook.update({newPhoneStr: newNameStr})
    return



def start():
 userInput=None

 while (userInput != 4):
   print("\n\n Hi There, How can I help you? "
       "\n 1. Enter 1 to search for the owner's name by the phone number "
       "\n 2. Enter 2 to search for a phone number by person's name "
       "\n 3. Enter 3 to insert new contact "
       "\n 4. Enter 4 to exit \n")

   userInput=int(input("Please, Enter your Choice"))

   if userInput==1:
    phoneInput = input("Enter the phone number: ")
    searchByPhoneNumber(phoneInput)


   elif userInput==2:
       personName = str(input("Enter person name: "))
       searchByName(personName)

   elif userInput==3:
       newName = input("Enter new contact name:")
       newPhone = input("Enter new phone number: ")
       insertNewContact(newName, newPhone)
       print("New contact Added Successfully!")

   elif userInput==4:
       exit()

   else:
       print("Please, Make sure you are entering valid choice!")



start()