import calendar,time
def localTime():
    localtime = time.asctime(time.localtime(time.time()))
    print(f"Current local time is {localtime}")

def displayCalendar():
    c = calendar.month(int(input("Enter year: ")),int(input("Enter month: ")))
    print("The calendar is:\n",c)
while(1):
    choice = int(input("Menu\n1)Show current local time\n2)Show calendar for a month\n3)Exit\nEnter your choice: "))
    if choice ==1:  localTime()
    elif choice == 2: displayCalendar()
    elif choice == 3: exit(1)
    else: print("Wrong choice")

