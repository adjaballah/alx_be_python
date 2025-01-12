from datetime import datetime, timedelta

def display_current_datetime():
    
    current_datetime = datetime.now()

    current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    print("Current date and time:",current_date)


def  calculate_future_date():

    days_to_add = int(input("Enter the number of days to add to the current date:"))

    current_date = datetime.now()

    future_date = current_date + timedelta(days=days_to_add)   

    print("Future date:", future_date.strftime("%Y-%m-%d"))


display_current_datetime()
calculate_future_date()    