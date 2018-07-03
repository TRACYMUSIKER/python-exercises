import phonebookfunctions
names_phone_dict = {
    'tracy': '518-461-7278'
}


def phonebook(phone_dict):
    user_inputted_number = raw_input("Electronic Phone Book\n=====================\n1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit\nWhat do you want to do (1-5)? ")
    if user_inputted_number == '1':
        phonebookfunctions.phonebooklookup(phone_dict)     
    elif user_inputted_number == '2':
        user_inputted_name = raw_input("What is the name of the person you'd like to add? ")
        user_inputted_phnumber = raw_input("What is the phone number of the person you'd like to add? ")
        phone_dict[user_inputted_name] = user_inputted_phnumber
        print "Entry stored for %s" % user_inputted_name
    elif user_inputted_number == '3':
        user_name_delete = raw_input("What is the name of the person you'd like to delete? ")
        del phone_dict[user_name_delete]
        print "Deleted entry for %s" % user_name_delete
    elif user_inputted_number == '4':
        str(phone_dict)
    elif user_inputted_number == '5':
        print "Bye."
        return False
    return True


def isrunning(names_phone_dict):
    shouldrun = True
    while shouldrun:
        shouldrun = phonebook(names_phone_dict)
    
isrunning(names_phone_dict)

# def phonebook(phone_dict):
#     user_inputted_number = ""
#     while user_inputted_number != str(5):
#         user_inputted_number = raw_input("Electronic Phone Book\n=====================\n1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit\nWhat do you want to do (1-5)? ")
#         phonebookfunctions.phonebooklookup(user_inputted_number)
#         phonebookfunctions.phonebookadd(user_inputted_number)
#         phonebookfunctions.phonebookdelete(user_inputted_number)
#         phonebookfunctions.phonebooklistall(user_inputted_number)
#         phonebookfunctions.phonebookquit(user_inputted_number)

