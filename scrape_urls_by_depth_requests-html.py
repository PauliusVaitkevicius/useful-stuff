from requests_html import HTMLSession
import validators as va
import time
from threading import Thread
import sys

PAGE = "http://www.mii.lt"

all_urls = set()


def write_set_to_file(fset):
    with open("links.txt", "w") as f:
        for val in fset:
            f.write(val + "\n")


def get_links(url, depth):
    urls_todo = set()
    urls_todo.add(url)

    session = HTMLSession()

    for d in range(1, depth + 1):
        links = set()

        print(f"{d} URLS DONE: ", len(all_urls))
        print(f"{d} URLS TODO: ", len(urls_todo))

        for url in urls_todo:
            urls_todo_cycle = set()
            try:
                request = session.get(url)
                urls_todo_cycle.update(request.html.absolute_links)
            except Exception:
                print("UPS! :)")
                continue

        for url in urls_todo_cycle:
            if va.url(url):
                links.add(url)
                # print(url)

        all_urls.update(links)
        write_set_to_file(all_urls)

        urls_todo = links
        del links


if __name__ == "__main__":
    get_links(PAGE, 4)
    print(len(all_urls))
