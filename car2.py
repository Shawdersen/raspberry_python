#引入gpio的模块
import RPi.GPIO as GPIO
import time
#设置GPIO模式
GPIO.setmode(GPIO.BOARD)
#设置in1到in4接口
IN1 = 15
IN2 = 16
IN3 = 13
IN4 = 11
#初始化接口
def init():
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(IN3,GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)
#前进的代码
def qianjin(sleep_time):
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(sleep_time)
    GPIO.cleanup()
#后退
def cabk(sleep_time):
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
    time.sleep(sleep_time)
    GPIO.cleanup()
#左转
def left(sleep_time):
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(sleep_time)
        GPIO.cleanup()
#右转
def right(sleep_time):
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)
    time.sleep(sleep_time)
    GPIO.cleanup()
init()#调用初始化方法初始化接口
cabk(10)#调用后退方法，并且10秒后停止