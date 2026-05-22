# Dashboard de Supervision d'Irrigation IoT

Système IoT complet permettant de surveiller l'humidité du sol en temps réel
via MQTT, MongoDB Atlas et un dashboard web Flask.

---

## Captures d'écran

### Capteur physique (micro:bit + capteur d'humidité)
![Capteur physique](screenshots/7_capteur_physique.jpg)

### Dashboard — humidité normale
![Dashboard normal](screenshots/1_dashboard_normal.png)

### Dashboard — alerte sol trop sec (humidité < 30%)
![Dashboard alerte](screenshots/2_dashboard_alerte.png)

### Historique des mesures
![Historique](screenshots/3_historique_mesures.png)

### Terminal simulateur — messages MQTT envoyés
![Terminal simulator](screenshots/4_terminal_simulator.png)

### MongoDB Atlas — collection soil_data
![MongoDB Atlas](screenshots/5_mongodb_atlas.png)

### Terminal Flask — requêtes API reçues
![Terminal Flask](screenshots/6_terminal_flask.png)

---

## Architecture du système

Capteur IoT (micro:bit)
│
▼  MQTT over TLS (port 8883)
HiveMQ Cloud — Broker MQTT
│
▼  Subscribe
Backend Python — Paho MQTT (backend.py)
│
▼  insert_one()
MongoDB Atlas — Collection soil_data
│
▼  API REST
Flask Web Server (app.py)
│
▼  HTTP + JavaScript (refresh 5s)
Dashboard Web — http://localhost:5000

---

## Technologies utilisées

| Composant | Technologie |
|---|---|
| Capteur physique | micro:bit + capteur humidité |
| Protocole IoT | MQTT over TLS (port 8883) |
| Broker | HiveMQ Cloud |
| Backend | Python 3 + Paho MQTT |
| Base de données | MongoDB Atlas (cloud gratuit) |
| API | Flask + Flask-CORS |
| Frontend | HTML + CSS + Chart.js |

---

## Format des messages MQTT
Humidite du sol: 54% | Date: 2026-05-22 16:12:22
Les messages sont publiés sur le topic : `irrigation/soil`

---

## Structure du projet
projetIOT/
├── config.py           # Paramètres MQTT et MongoDB
├── backend.py          # Subscriber MQTT + stockage BDD
├── app.py              # Serveur Flask + API REST
├── simulator.py        # Simulateur de capteur
├── start.py            # Lance tout en une commande
├── README.md           # Ce fichier
├── screenshots/        # Captures d'écran
│   ├── 1_dashboard_normal.png
│   ├── 2_dashboard_alerte.png
│   ├── 3_historique_mesures.png
│   ├── 4_terminal_simulator.png
│   ├── 5_mongodb_atlas.png
│   ├── 6_terminal_flask.png
│   └── 7_capteur_physique.jpg
└── templates/
└── index.html      # Dashboard web

---

## Installation et lancement

### 1. Cloner le projet
```bash
git clone https://github.com/TON_USERNAME/projetIOT.git
cd projetIOT
```

### 2. Installer les dépendances
```bash
pip install paho-mqtt pymongo flask flask-cors
```

### 3. Configurer MongoDB Atlas
Dans `config.py`, remplace l'URL :
```python
MONGO_URI = "mongodb+srv://admin:MOTDEPASSE@cluster0.9sysgue.mongodb.net/?appName=Cluster0"
```

### 4. Lancer le projet complet
```bash
python start.py
```

Ouvre ensuite le navigateur sur **http://localhost:5000**

---

## Fonctionnalités du dashboard

- Humidité actuelle affichée en temps réel
- Graphique historique (50 dernières mesures)
- Tableau des mesures avec date et état
- Alerte automatique rouge si humidité < 30%
- Rafraîchissement automatique toutes les 5 secondes
- Statut de connexion affiché

---

## Paramètres MQTT HiveMQ Cloud
Serveur  : 1ce520eab52a4627914aef266aff8647.s1.eu.hivemq.cloud
Port     : 8883 (TLS sécurisé)
Topic    : irrigation/soil

---

## Exemple de document MongoDB

```json
{
  "_id": "ObjectId('6a106d9e3a630b6216c334f9')",
  "humidity": 82,
  "timestamp": "2026-05-22 16:13:14"
}
```

---

*Projet réalisé dans le cadre du cours IoT — EMSI 2026*
"# projet-IoT" 
