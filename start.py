import subprocess
import sys
import os
import time

# Chemin vers python
py = sys.executable

# Dossier du projet
dossier = os.path.dirname(os.path.abspath(__file__))

print("=" * 45)
print("   Demarrage du systeme IoT Irrigation")
print("=" * 45)

print("\n[1/3] Demarrage du backend MQTT...")
p1 = subprocess.Popen(
    [py, "backend.py"],
    cwd=dossier,
    creationflags=subprocess.CREATE_NEW_CONSOLE  # ouvre dans une nouvelle fenetre
)
time.sleep(3)

print("[2/3] Demarrage du serveur Flask...")
p2 = subprocess.Popen(
    [py, "app.py"],
    cwd=dossier,
    creationflags=subprocess.CREATE_NEW_CONSOLE
)
time.sleep(2)

print("[3/3] Demarrage du simulateur...")
p3 = subprocess.Popen(
    [py, "simulator.py"],
    cwd=dossier,
    creationflags=subprocess.CREATE_NEW_CONSOLE
)

print("\n" + "=" * 45)
print("   Tout est demarre !")
print("   Ouvre ton navigateur sur :")
print("   http://localhost:5000")
print("=" * 45)
print("\nAppuie sur Entree pour tout arreter...")
input()

print("Arret de tous les serveurs...")
p1.terminate()
p2.terminate()
p3.terminate()
print("Arrete. Au revoir !")