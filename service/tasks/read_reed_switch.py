import RPi.GPIO as GPIO
from timeloop import Timeloop
from datetime import timedelta
from service.config import REED_1_IN
from service.config import NOTIFICATION_ENDPOINT, LIGHT_ENDPOINT
import requests
import logging

time_loop = Timeloop()
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='reed_switch.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# GPIO REED_1_IN == 0 IF CIRCUIT CLOSED, 1 OTW
GPIO.setmode(GPIO.BCM)
GPIO.setup(REED_1_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0


@time_loop.job(interval=timedelta(seconds=1))
def reed_switch_sensor():
    reed_input = str(GPIO.input(REED_1_IN))

    # used to send 1 notification every 10 input.
    global counter

    if counter <= 0 and reed_input == '1':

        try:
            # send notification to telegram application
            requests.get(NOTIFICATION_ENDPOINT)
            logging.info('DOOR SEEMS OPEN - NOTIFICATION SENT')

            # turn on the light on the room
            requests.get(LIGHT_ENDPOINT)
            logging.info('DOOR SEEMS OPEN - LIGHT ON')

            counter = 10
        except Exception as e:
            logging.error(str(e.__cause__))

    elif reed_input == '1':
        counter -= 1
    else:
        counter = 0


@time_loop.job(interval=timedelta(seconds=3))
def reed_switch_log():
    reed_input = GPIO.input(REED_1_IN)
    logging.info('Reed Switch Status: ' + str(reed_input))
