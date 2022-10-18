import Adafruit_DHT
import RPi.GPIO as GPIO
import time

#Setup dei componenti
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)


#test se tutto on
GPIO.output(21, GPIO.HIGH)
time.sleep(3)
GPIO.output(21, GPIO.LOW)

#chiedo input di
#Temperaura_Ottimale
Temp_Ottima = input("A che temperatura deve stare la pianta?")
Temp_Ottima = int(Temp_Ottima)
#Umidita_Ottimale
Hum_Ottima = input("A che umidita' deve stare la pianta?")

while True:
    #controllo temperatura e umidita
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        #solo temperatura
        if int(temperature) >= Temp_Ottima:
            #spengo la resisitenza ora comandata da led rosso
            GPIO.output(21, GPIO.LOW)
            print("temperatura giusta")
        if int(temperature) < Temp_Ottima:
            #accendo resistenza ora co,andata da led rosso
            GPIO.output(21, GPIO.HIGH)
            print("temperatura bassa, accendo res")
        time.sleep(3)
        
    else:
        print("Failed to retrieve data from humidity sensor")
