import json
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

import paho.mqtt.client as mqtt

# Konfigurasi MQTT sesuai proyek REST-API-IOT
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/sensor"

# File database dibuat di folder yang sama dengan script ini
DB_PATH = Path(__file__).resolve().parent / "sensor.db"


def siapkan_database():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sensor_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                suhu REAL NOT NULL,
                kelembaban REAL NOT NULL,
                timestamp TEXT,
                received TEXT NOT NULL,
                payload TEXT
            )
        """)
        conn.commit()


def saat_terhubung(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"Terhubung ke MQTT broker {MQTT_HOST}:{MQTT_PORT}")
        client.subscribe(MQTT_TOPIC)
        print(f"Berlangganan topik: {MQTT_TOPIC}")
    else:
        print(f"Gagal terhubung ke MQTT. Kode: {reason_code}")


def saat_pesan(client, userdata, message):
    try:
        data = json.loads(message.payload.decode("utf-8"))

        suhu = float(data["suhu"])
        kelembaban = float(data["kelembaban"])
        timestamp = data.get("timestamp")
        received = datetime.now(timezone.utc).isoformat()
        payload_asli = json.dumps(data, ensure_ascii=False)

        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("""
                INSERT INTO sensor_history
                (suhu, kelembaban, timestamp, received, payload)
                VALUES (?, ?, ?, ?, ?)
            """, (suhu, kelembaban, timestamp, received, payload_asli))
            conn.commit()

        print(f"Tersimpan: suhu={suhu}°C, kelembapan={kelembaban}%")
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Pesan sensor tidak valid, tidak disimpan: {error}")


if __name__ == "__main__":
    siapkan_database()

    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
        client_id="sqlite_sensor_logger"
    )
    client.on_connect = saat_terhubung
    client.on_message = saat_pesan

    print(f"Database: {DB_PATH}")
    print("Menunggu data sensor. Tekan Ctrl+C untuk berhenti.")
    try:
        client.connect(MQTT_HOST, MQTT_PORT, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nPenyimpanan sensor dihentikan.")
    except Exception as error:
        print(f"Tidak dapat menjalankan penyimpanan sensor: {error}")
    finally:
        client.disconnect()
