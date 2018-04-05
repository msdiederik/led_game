import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT) # LED 1
GPIO.setup(3,GPIO.OUT) # Klok
GPIO.setup(4, GPIO.IN) # Knop
GPIO.setup(17, GPIO.IN) # Knop + juiste LED


def cycle():
    for i in range(7):
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)

        start_time = time.time()
        while time.time() < start_time + 0.06:
            if GPIO.input(4):
                if GPIO.input(17):
                    # Win
                    time.sleep(1)
                    GPIO.output(2, GPIO.HIGH)
                    for _ in range(15):
                        GPIO.output(3, GPIO.HIGH)
                        GPIO.output(3, GPIO.LOW)
                        time.sleep(0.08)
                    GPIO.output(2, GPIO.LOW)
                    for _ in range(5):
                        GPIO.output(3, GPIO.HIGH)
                        GPIO.output(3, GPIO.LOW)
                        time.sleep(0.08)
                else:
                    # Lose
                    time.sleep(1)
                    for _ in range(7):
                        GPIO.output(3, GPIO.HIGH)
                        GPIO.output(3, GPIO.LOW)
                        time.sleep(0.01)


def start():
    GPIO.output(2, GPIO.HIGH)


def start_loop():
    cycle()
    time.sleep(0.5)
    while True:
        start()
        cycle()
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.5)

start_loop()
