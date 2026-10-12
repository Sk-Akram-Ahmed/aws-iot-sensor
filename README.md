# AWS IoT Sensor Dashboard

Real-time IoT sensor data simulator and Streamlit dashboard using AWS IoT Core, S3, Lambda, and DynamoDB.

## Architecture

- **`iot_simulator.py`** — Publishes simulated sensor data (temperature & humidity) to AWS IoT Core via MQTT
- **`dashboard.py`** — Streamlit dashboard that subscribes to the MQTT topic and visualizes sensor data in real-time
- **`ok.py`** — AWS Lambda function that logs S3 events to DynamoDB

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/ccv-cep.git
cd ccv-cep
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
cp .env.example .env
```
Edit `.env` and fill in your actual values:
- AWS IoT endpoint
- Certificate and key file paths
- S3 bucket name
- DynamoDB table name

### 4. Add your AWS IoT certificates
Place your certificate files in the project root:
- `AmazonRootCA1.pem`
- `your-certificate.pem.crt`
- `your-private.pem.key`

> **⚠️ These files are gitignored and must NOT be committed.**

### 5. Run

**Simulator:**
```bash
python iot_simulator.py
```

**Dashboard:**
```bash
streamlit run dashboard.py
```

## Security

All sensitive configuration is loaded from environment variables (`.env` file). Certificates and keys are excluded from version control via `.gitignore`.
