from requests_html import HTMLSession
import validators as va
import time
from threading import Thread
import sys

PAGE = "http://www.15min.lt"
TIME_TO_RUN = 5

time_to_stop = False


def start_timer(time_to_run=TIME_TO_RUN):
    global time_to_stop
    time.sleep(time_to_run)
    time_to_stop = True
    print("Timer stopped")


def write_set_to_file(fset):
    with open("links.txt", "w") as f:
        for val in fset:
            f.write(val + "\n")


def get_links(urls):
    global time_to_stop
    links = set()
    if urls and len(urls) > 0:
        for url in urls:
            if time_to_stop is True:
                sys.exit()
            elif va.url(url):
                links.add(url)
                print(url)

    all_urls.update(links)
    print(len(all_urls))
    write_set_to_file(all_urls)

    try:
        for link in links:
            sess = HTMLSession()
            r = sess.get(link)
            r.html.render()
            urls = r.html.absolute_links
            fset = urls.difference(all_urls)
            get_links(fset)
    except Exception:
        print("UPS!")


if __name__ == "__main__":
    all_urls = set()
    print(PAGE)

    all_urls.add(PAGE)
    session = HTMLSession()
    request = session.get(PAGE)
    request.html.render()

    timer_thread = Thread(target=start_timer)
    timer_thread.start()

    get_links(request.html.absolute_links)

    # print(all_urls)
    # print(len(all_urls))
