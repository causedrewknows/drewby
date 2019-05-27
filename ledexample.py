import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13,GPIO.OUT)


GPIO.output(4, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)
GPIO.output(9,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)
GPIO.output(13,GPIO.HIGH)

time.sleep(5)

GPIO.output(4,GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(9,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(13,GPIO.LOW)

GPIO.cleanup()


