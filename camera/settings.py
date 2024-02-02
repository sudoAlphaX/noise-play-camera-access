import requests
import datetime


def setTime(time=datetime.datetime.now(), ip="192.72.1.1"):
    data = requests.get(
        "http://{}/cgi-bin/Config.cgi?action=set&property=TimeSettings&value={}".format(
            ip, time.strftime("%Y$%m$%d$%H$%M$%S$")
        )
    )

    if data.text == "0\nOK\n":
        return True

    else:
        return False


def setResolution(res, ip="192.72.1.1"):
    data = requests.get(
        "http://{}/cgi-bin/Config.cgi?action=set&property=Videores&value={}".format(
            ip, res
        )
    )

    if data.text == "0\nOK\n":
        return True

    else:
        return False


def setWhiteBalance(wb, ip="192.72.1.1"):
    data = requests.get(
        "http://{}/cgi-bin/Config.cgi?action=set&property=AWB&value={}".format(ip, wb)
    )

    if data.text == "0\nOK\n":
        return True

    else:
        return False


def setFrequency(fq, ip="192.72.1.1"):
    data = requests.get(
        "http://{}/cgi-bin/Config.cgi?action=set&property=Flicker&value={}Hz".format(
            ip, fq
        )
    )

    if data.text == "0\nOK\n":
        return True

    else:
        return False


def setExposure(exp, ip="192.72.1.1"):
    if int(exp) == 0:
        expval = "0"

    elif int(exp) > 0:
        expval = "P" + str(int(exp)).zfill(3)

    elif int(exp) < 0:
        expval = "N" + str(abs(int(exp))).zfill(3)

    else:
        return False

    data = requests.get(
        "http://{}/cgi-bin/Config.cgi?action=set&property=Exposure&value=EV{}".format(
            ip, expval
        )
    )

    if data.text == "0\nOK\n":
        return True

    else:
        return False


if __name__ == "__main__":
    data = setResolution("2.7K15")
    print(data)
