from datetime import datetime
from pytz import timezone
from kamerscraper import finddebates

def getnow():
    now = datetime.now(tz=timezone('Europe/Amsterdam'))
    date = now.strftime("%d-%m-%Y")
    hour = now.hour
    minute = now.minute

    return date, hour, minute

def indebate(time, verbose=True):
    date, hour, minute = time
    debates = finddebates(date, verbose=verbose)
    for sh, sm, eh, em in debates:
        if int(sh) * 60 + int(sm) <= hour * 60 + minute <= int(eh) * 60 + int(em):
            return True
    return False

print(indebate(getnow()))
