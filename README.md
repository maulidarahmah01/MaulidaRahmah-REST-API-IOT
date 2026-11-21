# MaulidaRahmah-REST-API-IOT

Project REST API IoT menggunakan Python, MQTT, Node-RED, WebSocket, dan SQLite.

## Deskripsi Proyek

Proyek ini merupakan simulasi sistem Internet of Things (IoT) untuk membaca data suhu dan kelembapan, mengirimkan data melalui protokol MQTT, mengolah data menggunakan Node-RED, dan menampilkan hasilnya pada dashboard berbasis web.

## Teknologi yang Digunakan

- Python
- MQTT (Mosquitto)
- Node-RED
- REST API
- WebSocket
- SQLite
- HTML, CSS, JavaScript
- Chart.js

## Fitur Proyek

1. Simulasi ESP32 menggunakan Python.
2. Pengiriman data sensor menggunakan MQTT.
3. REST API untuk mengambil data suhu.
4. REST API untuk mengambil riwayat data sensor.
5. Kontrol perangkat melalui REST API.
6. Dashboard untuk menampilkan suhu dan kelembapan secara real-time.
7. Grafik suhu dan kelembapan menggunakan Chart.js.
8. Pengaturan batas suhu (threshold) dan peringatan.
9. Pengamanan API menggunakan API Key.
10. Komunikasi data secara real-time menggunakan WebSocket.
11. Penyimpanan data sensor menggunakan SQLite.

## Struktur Folder

```text
REST-API-IOT/
├── simulator/
│   └── simulasi_esp32.py
├── database/
│   └── simpan_sqlite.py
├── node-red/
│   └── flows.json
├── dashboard.html
├── websocket-test.html
└── README.md
```

## Cara Menjalankan

1. Jalankan Mosquitto MQTT Broker.
2. Jalankan Node-RED.
3. Import file `flows.json` ke Node-RED jika flow belum tersedia.
4. Jalankan simulator:

```bash
python simulator/simulasi_esp32.py
```

5. Jalankan program penyimpanan SQLite:

```bash
python database/simpan_sqlite.py
```

6. Jalankan server dashboard dari folder utama proyek:

```bash
python -m http.server 8000
```

7. Buka dashboard melalui browser:

```text
http://localhost:8000/dashboard.html
```

8. Untuk menguji WebSocket, buka:

```text
http://localhost:8000/websocket-test.html
```

## Endpoint REST API

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/api/suhu` | Mengambil data sensor terbaru |
| GET | `/api/history` | Mengambil riwayat data sensor |
| POST | `/api/kontrol` | Mengirim perintah kontrol perangkat |
| PUT | `/api/threshold` | Mengatur batas suhu |

## Database

Data sensor disimpan menggunakan SQLite pada file `sensor.db`.

## Pengembang

**Maulida Rahmah**

Project REST API IoT — 2026
