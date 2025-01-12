import datetime



def display_current_datetime():
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    print("current Date and Time :",current_date)


def  calculate_future_date():
    days_to_add = int(input("Enter the number of days to add:"))

    current_date = datetime.datetime.now()

    future_date = current_date + datetime.timedelta(days=days_to_add)   

    print("future date:", future_date.strftime("%Y-%m-%d"))


display_current_datetime()
calculate_future_date()    