import subprocess
import RPi.GPIO as GPIO
import time

string = str(subprocess.check_output(['vcgencmd', 'measure_temp']))

print("Initial temp:", string.replace("b\"temp=", "").replace("'C\\n\"", ""))

currentTemp = float(string.replace("b\"temp=", "").replace("'C\\n\"", ""))

fan = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(fan, GPIO.OUT)

# for i in range(10):
#     GPIO.output(fan, GPIO.HIGH)
#     time.sleep(2)
#     GPIO.output(fan, GPIO.LOW)
#     time.sleep(2)

threshold = 40.0

GPIO.output(fan, GPIO.LOW)

while (currentTemp > threshold):

    if GPIO.input(fan) == False:

        GPIO.output(fan, GPIO.HIGH)

    time.sleep(30)

    string = str(subprocess.check_output(['vcgencmd', 'measure_temp']))
    currentTemp = float(string.replace("b\"temp=", "").replace("'C\\n\"", ""))

    print("Current temp:", currentTemp)

print("Successfully cooled below threshold!")

GPIO.cleanup()
