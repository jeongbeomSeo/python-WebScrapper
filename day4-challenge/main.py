import requests
import os


def asking():
    answer = input("Do you want to start over? y/n ")
    if(answer != "y" and answer != "n"):
        print("That's not a vaild answer")
        asking()
    elif(answer == "y"):
        main()
    else:
        print("ok. bye!!")


def main():
    os.system("clear")

    print("Welcome to IsItDown.py!")

    urls = input("Please wrtie a URL or URLs you want to check. (separated by comma) \n")

    url_list = urls.split(',')

    for url in url_list:
        url = url.strip()
        if "." not in url:
            print(f"{url} is not a vaild URL")
            continue
        elif "http://" not in url:
            url = "http://" + url
        try:
            request = requests.get(url)
            status_num = request.status_code
            if(status_num == 200):
                print(f"{url} is up!")
            else:
                print(f"{url} is down!")
        except:
            print(f"{url} is down!")
    asking()

main()

