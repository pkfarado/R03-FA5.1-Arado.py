# Version 2: Added Date Formatting
from datetime import datetime

def main():
    event_title = input("Enter event title: ")
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))

    event_date = datetime(year, month, day)

    print("\nFormatted Output:")
    print(f"Event: {event_title.upper()}")
    print(f"Date: {event_date.strftime('%B %d, %Y')}")
    print(f"Year: {year}")
    print(f"Month: {event_date.strftime('%B')}")
    print(f"Day: {day}")
    print(f"Weekday: {event_date.strftime('%A')}")

if __name__ == "__main__":
    main()