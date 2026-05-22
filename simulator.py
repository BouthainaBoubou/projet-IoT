import paho.mqtt.client as mqtt
import ssl, time, random
from datetime import datetime
from config import *

client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.tls_set(tls_version=ssl.PROTOCOL_TLS)
client.connect(MQTT_SERVER, MQTT_PORT)

print("Simulateur démarré. Envoi toutes les 5 secondes...")
while True:
    humidite = random.randint(10, 85)
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message  = f"Humidite du sol: {humidite}% | Date: {date_str}"
    client.publish(MQTT_TOPIC, message)
    print(f"Envoyé : {message}")
    time.sleep(5)