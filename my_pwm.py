#first commit 14th Jan 2016
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
led=11
GPIO.setup(led,GPIO.OUT)
my_pwm = GPIO.PWM(led,100)
my_pwm.start(0)
try:
  while(True):
     brightness=input("How bright? (1-67) ")
     print (str(2**brightness))
     my_pwm.ChangeDutyCycle(2**brightness)
except KeyboardInterrupt:
  print("InteruptedOK")
  my_pwm.stop()
  GPIO.cleanup()
   
