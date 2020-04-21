from timeloop import Timeloop
from datetime import timedelta
from datetime import datetime
from service.config import NOTIFICATION_ENDPOINT, WEB_PAGE
import requests
import logging
import codecs

time_loop = Timeloop()
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='page_refresher.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

counter = 0


@time_loop.job(interval=timedelta(deploy0))
def page_update_notify():
    # get page
    webpage = requests.get(WEB_PAGE).text

    page_file = codecs.open("pages/lastpage.html", "r", "utf-8")
    webpage_old = page_file.read()
    page_file.close()

    if webpage_old != webpage:
        print("fuck off")
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")

        page_file = codecs.open("pages/lastpage.html", "w", "utf-8")
        page_file.write(webpage)
        page_file.close()

        backup = codecs.open("pages/" + dt_string + ".html", "w+", "utf-8")
        backup.write(webpage_old)
        backup.close()

        requests.get(NOTIFICATION_ENDPOINT)

    # check if equal

    #
    #
    # if counter <= 0 and reed_input == '1':
    #
    #     try:
    #         # send notification to telegram application
    #         requests.get(NOTIFICATION_ENDPOINT)
    #         logging.info('DOOR SEEMS OPEN - NOTIFICATION SENT')
    #
    #         # turn on the light on the room
    #         requests.get(LIGHT_ENDPOINT)
    #         logging.info('DOOR SEEMS OPEN - LIGHT ON')
    #
    #         counter = 10
    #     except Exception as e:
    #         logging.error(str(e.__cause__))
    #
    # elif reed_input == '1':
    #     counter -= 1
    # else:
    #     counter = 0
