import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt

water_value = 0.0

def on_connect(client, userdata, flags, rc):
    print("Connecté MQTT avec code", rc)
    client.subscribe("wokwi/water")

def on_message(client, userdata, msg):
    global water_value
    try:
        water_value = float(msg.payload.decode())
        update_gui()
    except:
        pass

def update_gui():
    water_label.config(text=f"{water_value:.1f} cm")
    if water_value < 100:
        status_label.config(text="Niveau bas ⚠️", foreground="red")
    elif 100 <= water_value < 300:
        status_label.config(text="Niveau moyen ✅", foreground="orange")
    else:
        status_label.config(text="Niveau haut 💧", foreground="blue")

# === Tkinter ===
root = tk.Tk()
root.title("Surveillance Niveau d'Eau")
root.geometry("400x250")
root.configure(bg="#2c3e50")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 14), background="#2c3e50", foreground="white")

title_label = ttk.Label(root, text="Système de Gestion d'Eau", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

water_label = ttk.Label(root, text="--- cm", font=("Arial", 24, "bold"))
water_label.pack(pady=20)

status_label = ttk.Label(root, text="En attente...", font=("Arial", 16))
status_label.pack(pady=10)

# === MQTT ===
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.loop_start()

root.mainloop()
