def CALL_MENU():
    print("""
           __  _      _ __      
 ___ _____/ /_(_)  __(_) /___ __
/ _ `/ __/ __/ / |/ / / __/ // /
\_,_/\__/\__/_/|___/_/\__/\_, / 
                         /___/  
              Tool Developed By- Vinay Jangam
  
""")
CALL_MENU()

ui = str(input("Enter Weather Status[good/bad]: "))

def GOOD_WEATHER_CALL():
    print("The Weather is Good~!")
    print("going for a walk~!")

def BAD_WEATHER_CALL():
    print("The Weather is Bad~!")
    print("Staying at home~!")


# ACTIVITIES BELOW DEFS
def GO_MOVIE():
    print("gone to watch movie~!")
    print("Enjoying wathcing the movie~!")

def HAVE_LUNCH():
    print("Eating lunch~!")

    
if ui == "good":
    GOOD_WEATHER_CALL()
    GO_MOVIE()
    HAVE_LUNCH()
else:
    ui == "bad"
    BAD_WEATHER_CALL()