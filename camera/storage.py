import requests
import xmltodict


def getVideos(start=0, count=10, ip="192.72.1.1"):
    data = requests.get(
        "http://{}/cgi-bin/Config.cgi?action=dir&format=all&property=Normal&from={}&count={}".format(
            ip, start, count
        )
    )

    jsondata = xmltodict.parse(data.text)
    return jsondata["Normal"]['file']


def getPhotos(start=0, count=10, ip="192.72.1.1"):
    data = requests.get(
        "http://{}/cgi-bin/Config.cgi?action=dir&format=all&property=Photo&from={}&count={}".format(
            ip, start, count
        )
    )

    jsondata = xmltodict.parse(data.text)
    return jsondata["Photo"]['file']


if __name__ == "__main__":
    data = getPhotos()
    print(data)
