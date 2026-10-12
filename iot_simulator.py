import os
import paho.mqtt.client as mqtt
import json
import random
import time
import threading
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AWS_IOT_ENDPOINT")
port = int(os.getenv("AWS_IOT_PORT", "8883"))
topic = os.getenv("MQTT_TOPIC", "iot/sensor/data")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="sensor01")

connect_event = threading.Event()
connect_rc = {"value": None}


def on_connect(client, userdata, flags, reason_code, properties):
    rc = reason_code.value if hasattr(reason_code, "value") else int(reason_code)
    connect_rc["value"] = rc
    if rc == 0:
        print("Connected to AWS IoT Core")
    else:
        print(f"Connection failed with reason code: {rc}")
    connect_event.set()


def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
    print(f"Disconnected from AWS IoT Core. Reason: {reason_code}")


client.on_connect = on_connect
client.on_disconnect = on_disconnect

base_dir = Path(__file__).resolve().parent

ca_file = base_dir / os.getenv("CA_CERT_FILE", "AmazonRootCA1.pem")
cert_file = base_dir / os.getenv("CLIENT_CERT_FILE")
key_file = base_dir / os.getenv("CLIENT_KEY_FILE")

for tls_file in [ca_file, cert_file, key_file]:
    if not tls_file.exists():
        raise FileNotFoundError(f"Missing TLS file: {tls_file}")

client.tls_set(
    ca_certs=str(ca_file),
    certfile=str(cert_file),
    keyfile=str(key_file)
)

client.connect(endpoint, port, keepalive=60)
client.loop_start()

if not connect_event.wait(10):
    raise TimeoutError("No CONNACK from AWS IoT Core within 10 seconds.")

if connect_rc["value"] != 0:
    raise ConnectionError(f"AWS IoT Core rejected connection, rc={connect_rc['value']}")

try:
    while True:
        data = {
            "device_id": "sensor01",
            "temperature": random.randint(20, 40),
            "humidity": random.randint(40, 80)
        }

        payload = json.dumps(data)
        publish_result = client.publish(topic, payload)
        if publish_result.rc == mqtt.MQTT_ERR_SUCCESS:
            print("Sent:", payload)
        else:
            print(f"Publish failed, rc={publish_result.rc}")

        time.sleep(5)
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    client.loop_stop()
    client.disconnect()
