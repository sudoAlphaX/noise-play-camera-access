def getLink(name, ip="192.72.1.1"):
    return "http://" + ip + name


def getLinks(medias, ip="192.72.1.1"):
    links = []

    for media in medias:
        links.append("http://" + ip + media["name"])

    return links


if __name__ == "__main__":
    link = getLink("/SD/Photo/IMG240201-132842F.JPG")
    print(link)
