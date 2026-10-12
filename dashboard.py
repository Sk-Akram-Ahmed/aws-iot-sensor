import json
import os
import queue
import time
from pathlib import Path

import pandas as pd
import paho.mqtt.client as mqtt
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AWS_IOT_ENDPOINT")
port = int(os.getenv("AWS_IOT_PORT", "8883"))
topic = os.getenv("MQTT_TOPIC", "iot/sensor/data")
max_points = 500

base_dir = Path(__file__).resolve().parent

ca_file = base_dir / os.getenv("CA_CERT_FILE", "AmazonRootCA1.pem")
cert_file = base_dir / os.getenv("CLIENT_CERT_FILE")
key_file = base_dir / os.getenv("CLIENT_KEY_FILE")

st.title("IoT Sensor Dashboard")

if "message_queue" not in st.session_state:
    st.session_state.message_queue = queue.Queue()
if "sensor_data" not in st.session_state:
    st.session_state.sensor_data = pd.DataFrame(columns=["temperature", "humidity"])
if "mqtt_started" not in st.session_state:
    st.session_state.mqtt_started = False

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to AWS IoT Core")
    client.subscribe(topic)
    print("Subscribed to:", topic)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        new_data = {
            "temperature": payload.get("temperature"),
            "humidity": payload.get("humidity"),
        }
        userdata["queue"].put(new_data)
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"Skipping invalid payload: {exc}")

if not st.session_state.mqtt_started:
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2, userdata={"queue": st.session_state.message_queue}
    )
    client.tls_set(
        ca_certs=str(ca_file),
        certfile=str(cert_file),
        keyfile=str(key_file),
    )
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(endpoint, port)
    client.loop_start()
    st.session_state.mqtt_client = client
    st.session_state.mqtt_started = True

rows = []
while True:
    try:
        rows.append(st.session_state.message_queue.get_nowait())
    except queue.Empty:
        break

if rows:
    new_df = pd.DataFrame(rows)
    st.session_state.sensor_data = pd.concat(
        [st.session_state.sensor_data, new_df], ignore_index=True
    ).tail(max_points).reset_index(drop=True)

if st.session_state.sensor_data.empty:
    chart_df = pd.DataFrame({"temperature": [0], "humidity": [0]})
else:
    chart_df = st.session_state.sensor_data

st.line_chart(chart_df)
st.write(f"Waiting for sensor data... Total samples: {len(st.session_state.sensor_data)}")

time.sleep(1)
st.rerun()
