from onlinesimru import GetFree, GetRent, GetProxy, GetUser, GetNumbers


def main():
    client = GetNumbers('00f23a93807a731ee3f2f93031cf7313')
    a = client.tariffsOne(371)
    print(a)


main()
