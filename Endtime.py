import datetime

info = datetime.datetime.now()
def dataprint():
    info = datetime.datetime.now()
    day = info.strftime("%A")
    time = info.strftime("%I:%M %p")
    daynum = info.strftime("%d")
    month = info.strftime("%b")
    year = info.strftime("%Y")
    

    print(daynum,month,year,end=" ")
    print(day,end=" ")
    print(time)
    
def time():
    """
    This func prints the time
    """
    time = info.strftime("%I:%M:%S %p")
    print(time)

