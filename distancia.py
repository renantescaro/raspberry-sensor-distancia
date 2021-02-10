import sys
import time
import signal
import RPi.GPIO as GPIO
from threading import Thread

class Distancia(Thread):
    def __init__(self, **kwargs):
        super(Distancia, self).__init__(**kwargs)
        self.TRIG = 33
        self.ECHO = 37
        self.distancia = 0
        self.sampling_rate  = 20.0
        self.velocidade_som = 349.10
        self.max_distance   = 4.0
        GPIO.setmode(GPIO.BOARD)
        signal.signal(signal.SIGINT, self._sigint_handler)
        self.max_delta_t = self.max_distance / self.velocidade_som
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        GPIO.output(self.TRIG, False)


    def _clean(self):
        GPIO.cleanup()


    def _sigint_handler(self ,signum, instant):
        self._clean()
        sys.exit()


    def run(self):
        while True:
            GPIO.output(self.TRIG, True)
            time.sleep(0.00001)
            GPIO.output(self.TRIG, False)

            while GPIO.input(self.ECHO) == 0:
                start_t = time.time()

            while GPIO.input(self.ECHO) == 1 and time.time() - start_t < self.max_delta_t:
                end_t = time.time()

            if end_t - start_t < self.max_delta_t:
                delta_t = end_t - start_t
                distance = 100*(0.5 * delta_t * self.velocidade_som)
            else:
                distance = -1

            time.sleep(1/self.sampling_rate)
            self.distancia = round(distance, 2)