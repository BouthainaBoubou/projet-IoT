import paho.mqtt.client as mqtt
import ssl, re
from pymongo import MongoClient
from config import *

# Connexion MongoDB
mongo      = MongoClient(MONGO_URI)
collection = mongo[DB_NAME][COLLECTION]
print("Connecté à MongoDB Atlas")

def parse_message(texte):
    """
    Transforme 'Humidite du sol: 54% | Date: 2000-01-01 00:06:43'
    en dictionnaire Python {'humidity': 54, 'timestamp': '2000-01-01 00:06:43'}
    """
    resultat = re.search(r"Humidite du sol:\s*(\d+)%\s*\|\s*Date:\s*(.+)", texte)
    if resultat:
        return {
            "humidity":  int(resultat.group(1)),
            "timestamp": resultat.group(2).strip()
        }
    return None

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connecté au broker MQTT HiveMQ")
        client.subscribe(MQTT_TOPIC)
        print(f"En écoute sur : {MQTT_TOPIC}")
    else:
        print(f"Erreur connexion MQTT, code : {rc}")

def on_message(client, userdata, msg):
    texte = msg.payload.decode("utf-8")
    print(f"Message recu : {texte}")
    data = parse_message(texte)
    if data:
        collection.insert_one(data)
        print(f"Sauvegarde en BDD : {data}")
    else:
        print("Format de message non reconnu")

# Démarrage
client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.tls_set(tls_version=ssl.PROTOCOL_TLS)
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT)
client.loop_forever()