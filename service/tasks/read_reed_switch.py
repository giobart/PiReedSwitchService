import RPi.GPIO as GPIO
from timeloop import Timeloop
from datetime import timedelta
from service.config import REED_OUT, REED_1_IN
from service.config import NOTIFICATION_ENDPOINT
import requests

time_loop = Timeloop()

# Initialize GPIO with
GPIO.setmode(GPIO.BCM)
GPIO.setup(REED_OUT, GPIO.OUT)
GPIO.setup(REED_1_IN, GPIO.IN)

# Le porte GPIO vengono disattivate.
GPIO.output(16, GPIO.HIGH)

counter = 0

@time_loop.job(interval=timedelta(seconds=1))
def reed_switch_sensor():
    input = GPIO.input(REED_1_IN)

    #send 1 notification every 10 input.
    global counter

    if counter <= 0 and input == '1':
        requests.get(NOTIFICATION_ENDPOINT)
        counter = 10
    elif input == '1':
        counter -= 1
