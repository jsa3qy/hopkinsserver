import sys
import datetime
import pytz

# date objects
tz_NY = pytz.timezone('America/New_York')
today = datetime.date.today()

# macros
DATE = datetime.datetime.now(tz_NY)
DAY = today.day
MONTH = today.month
YEAR = today.year
WEEKDAY = today.weekday() #monday is 0 and sunday is 6


def main(emails):

    func_list = [
        sendRentReminder,
        sendTrashReminder
    ]

    output_list = []
    for func in func_list:
        output_list = appendOrNot(output_list, func())
    print("To: " + emails)
    print("From: jessealloy@gmail.com")
    print("Subject: Daily Reminders")
    if len(output_list):
        for reminder in output_list:
            print(reminder + "\n")
    else:
        print("No Daily Reminders!")

# helpers
def appendOrNot(curList, func_output):
    if func_output:
        curList.append(func_output)
    return curList

# reminder functions -- return falsey val if not time, return string if it's time to remind
def sendRentReminder():
    if DAY == 25:
        return "Hello boys -- this is your automated rent reminder!"
    return False

def sendTrashReminder():
    if WEEKDAY == 1:
        return "Yo yo throw that trash out to the curb!"
    elif WEEKDAY == 3:
        return "ayeee we got trash ~and~ recycling to put out"
    return False



if __name__ == "__main__":
    emails = sys.argv[1]
    main(emails)
