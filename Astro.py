import time
from datetime import datetime
print("Processing please wait...")
time.sleep(3)
print("Processing complete!")
time.sleep(1)
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Hello, the time is currently:", current_time)
time.sleep(1)
#input x if = this
a = input("How are you today?--Choose from, Good, Bad and I am fine--: ")
if ((a)=='Good'):
 print("I am also very good.")

if ((a)=='Bad'):
  print("Oh, I am sorry to here that but, I am in a good mood today.")

if ((a)=='I am fine'):
  print("Ok, I have a very good mood today.")

b = input("Please chose a number between 1 and 50.")
if ((b)>='33'):
  print("Access denied!")
  
if ((b)<='33'):
  print("Access denied!")

if ((b)>='50'):
  print("Access denied")

if ((b)=='33'):
  print("You may continue,")
