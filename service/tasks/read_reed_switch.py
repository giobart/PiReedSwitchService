import RPi.GPIO as GPIO
from timeloop import Timeloop
from datetime import timedelta
from service.config import REED_1_IN
from service.config import NOTIFICATION_ENDPOINT
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
        requests.get(NOTIFICATION_ENDPOINT)
        logging.info('DOOR SEEMS OPEN - NOTIFICATION SENT')
        counter = 10
    elif reed_input == '1':
        counter -= 1
    else:
        counter = 0


@time_loop.job(interval=timedelta(seconds=3))
def reed_switch_log():
    reed_input = GPIO.input(REED_1_IN)
    logging.info('Reed Switch Status: ' + str(reed_input))
