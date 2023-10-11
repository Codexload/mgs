#-------------------------------------------------------Importing-----------------------------------------------------
import base64
import sys
#---------------------------------------------------------Style-------------------------------------------------------
name1st = input("Enter Your First Name==> ")
namelast = input("Enter Your Last Name==> ")
name = name1st, namelast
i = 1
while i <= 100:
    print(" ______            _ _        ")
    print("|  ____|          | (_)       ")
    print("| |__ __ _ _ __ __| |_ _ __ ")
    print("|  __/ _` | '__/ _` | | '_ \  ")
    print("| | | (_| | | | (_| | | | | |")
    print("|_|  \__,_|_|  \__,_|_|_| |_| ")
#---------------------------------------------------------Coding-------------------------------------------------------
    print("Enter Any Options \n 1. Encode Your Massage \n 2. Decode Your Massage \n 3. Update This Proggram \n 4. Exit")
    input_from_user = input("==> ")
    if input_from_user == "":
        print("You Don't Enter Any Option\nPlz Enter Any Option")
    elif input_from_user == "1":
        inp = input("Enter Your Normal Massage--> ")
        mgs = inp.encode("utf-8")
        encoded_massage = base64.b64encode(mgs).decode("utf-8")
        print("Your Encoded Massage is===>>", encoded_massage)
    elif input_from_user == "2":
        inpsec = input("Enter Your Encoded Massage--> ")
        decoded_massage = base64.b64decode(inpsec).decode("utf-8")
        print("Your Decoded Massage is===>>", decoded_massage)
    elif input_from_user == "3":
        print("Well Hello", name, "You Are Up To Date\nYou Are Using The Latest Version Of The Tool🙂❤")
    elif input_from_user == "4":
        print("You are Going To exit!!!")
        sys.exit()
    else:
        print("Please Try Again\nYou Enterd A Wrong Number")
    i += 1