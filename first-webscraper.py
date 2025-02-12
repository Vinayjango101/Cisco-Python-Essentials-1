import urllib.request
def get_url():
    UNAME = input("ENTER UNAME: ")
    PASS = input("ENTER PASS: ")

    VALID_UNAME = "jhon" # [+]HARDCODED UNAME AND PASSWORD
    VALID_PASS = "jhon@2007"

    if UNAME != VALID_UNAME :
        print("INVALID PASS!, PROGRAM IS TERMINATED!!")
        exit()

    elif PASS != VALID_PASS:
        print("INVALID UNAME!, PROGRAM IS TERMINATED!! ")
        exit()

    else:
        URL = input("Enter Target URL: ")
        filename = input("Enter Filename: ")
        print("The Target URL is " + URL)
        print("The Filename is " + filename)
        urllib.request.urlretrieve(URL + filename)



get_url()
