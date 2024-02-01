import requests
import datetime


def setTime(time=datetime.datetime.now(), ip="192.72.1.1"):
    data = requests.get(
        "http://{}/cgi-bin/Config.cgi?action=set&property=TimeSettings&value={}".format(
            ip, time.strftime("%Y$%m$%d$%H$%M$%S$")
        )
    )

    if data.status_code == 200:
        return True

    else:
        return False
