# from https://www.programiz.com/python-programming/datetime/current-datetime


from datetime import datetime

# datetime object containing current date and time
now = datetime.now()


# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

