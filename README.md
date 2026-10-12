# 🔐 Secure IoT Data Processing and Real-Time Monitoring Using AWS

<p align="center">
  A cloud-based IoT monitoring system using AWS IoT Core, MQTT, TLS encryption, and Python.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/AWS-IoT%20Core-orange?logo=amazonaws&logoColor=white" alt="AWS IoT Core"/>
  <img src="https://img.shields.io/badge/Protocol-MQTT-purple" alt="MQTT"/>
  <img src="https://img.shields.io/badge/Security-TLS%20%2B%20X.509-green" alt="Security"/>
  <img src="https://img.shields.io/badge/Dashboard-Streamlit-red?logo=streamlit&logoColor=white" alt="Streamlit"/>
</p>

## 📌 Overview

The Internet of Things (IoT) enables connected devices to collect and exchange data. However, transmitting sensor data securely and monitoring it in real time are important challenges in IoT-based applications.

This project implements a cloud-based IoT data processing and monitoring system using **AWS IoT Core**. A Python-based IoT simulator generates temperature and humidity readings and publishes them to the cloud using the MQTT protocol. Secure communication is configured using TLS encryption and X.509 certificates.

A Streamlit dashboard receives sensor messages and visualizes the incoming data through dynamic graphs, enabling real-time monitoring of environmental parameters.

The project demonstrates how IoT communication, cloud services, and data visualization can be integrated into a single system.

## 🎯 Objectives

- Simulate an IoT device using Python.
- Generate temperature and humidity sensor readings.
- Transmit sensor data using the MQTT publish-subscribe protocol.
- Configure secure device-to-cloud communication using TLS and X.509 certificates.
- Use AWS IoT Core as the MQTT message broker.
- Visualize incoming sensor data through a Streamlit dashboard.
- Demonstrate a modular architecture that can be extended for additional devices and data storage.

## 🏗️ System Architecture

```text
┌──────────────────────────────┐
│      IoT Device Simulator    │
│          Python              │
│  Temperature & Humidity      │
└──────────────┬───────────────┘
               │
               │ MQTT over TLS
               │ X.509 Authentication
               ▼
┌──────────────────────────────┐
│         AWS IoT Core         │
│       MQTT Message Broker    │
└──────────────┬───────────────┘
               │
               │ MQTT Topic
               │ iot/sensor/data
               ▼
┌──────────────────────────────┐
│      Streamlit Dashboard     │
│       Python + Pandas        │
│                              │
│  Temperature Visualization   │
│  Humidity Visualization      │
└──────────────────────────────┘
```

### 🔄 Data Flow

1. **Data generation:** The Python simulator generates temperature and humidity values.
2. **Data formatting:** Sensor readings are structured as JSON messages.
3. **Secure communication:** The simulator publishes messages using MQTT over TLS.
4. **Cloud processing:** AWS IoT Core receives and routes messages through the configured MQTT topic.
5. **Data consumption:** The dashboard subscribes to the topic and receives sensor messages.
6. **Visualization:** Streamlit displays the incoming readings through dynamic graphs.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | IoT simulation and application logic |
| AWS IoT Core | Cloud connectivity and MQTT message routing |
| MQTT | Lightweight publish-subscribe communication |
| TLS | Encryption of network communication |
| X.509 Certificates | Device authentication |
| Paho MQTT | MQTT client communication |
| Streamlit | Interactive monitoring dashboard |
| Pandas | Sensor data processing and handling |
| JSON | Sensor message format |

## 🔒 Security Implementation

Security is an important component of this project.

- **TLS encryption:** Protects data in transit between the client and AWS IoT Core.
- **X.509 certificates:** Support certificate-based authentication of the IoT device.
- **AWS IoT policies:** Control which MQTT operations a device or client is permitted to perform.
- **Certificate-based connectivity:** Uses the AWS IoT certificate and private key configuration.
- **Secure MQTT connection:** Uses port `8883` for MQTT over TLS.

> **Security note:** Never commit private keys, AWS credentials, or secret environment files to GitHub. Use least-privilege AWS IoT policies and keep certificate files outside the public repository.

## 📂 Project Structure

```text
aws-iot-secure-data-monitoring/
│
├── src/
│   ├── iot_simulator.py
│   └── dashboard.py
│
├── screenshots/
│   ├── aws-iot-connection.png
│   └── dashboard.png
│
├── docs/
│   └── project-report.pdf
│
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

*Note: This is a suggested structure. Rename the files and directories to match your actual implementation.*

## ⚙️ Prerequisites

Before running the project, ensure you have:

- Python 3 installed.
- An AWS account with AWS IoT Core configured.
- An IoT Thing and an appropriate AWS IoT policy.
- A registered device certificate and its corresponding private key.
- The Amazon Root CA certificate required for your connection configuration.
- An MQTT topic configured for sensor communication.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/aws-iot-secure-data-monitoring.git

cd aws-iot-secure-data-monitoring
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Or on Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure AWS IoT Core

In the AWS Management Console:

1. Open AWS IoT Core.
2. Create or select your IoT Thing.
3. Register and activate its device certificate.
4. Attach an appropriate IoT policy.
5. Obtain your AWS IoT device data endpoint.
6. Configure the endpoint, certificate paths, private key path, and Root CA path in your local environment.

Keep private credentials outside the repository. Use environment variables or a local configuration file excluded by `.gitignore`.

### 5. Run the IoT simulator

Use the actual script path in your repository. For the suggested structure:

```bash
python src/iot_simulator.py
```

The simulator should connect to AWS IoT Core and publish JSON sensor readings to the configured topic.

### 6. Launch the dashboard

Open a separate terminal, activate the virtual environment, and run:

```bash
streamlit run src/dashboard.py
```

The dashboard should display the incoming sensor readings when the AWS IoT connection and MQTT subscription are configured correctly.

## 📊 Results

The project demonstrates the integration of a simulated IoT device, AWS cloud connectivity, secure MQTT communication, and real-time sensor visualization.

The implementation includes:

- Temperature and humidity data generation.
- MQTT message transmission to AWS IoT Core.
- Certificate-based secure connectivity.
- MQTT topic subscription and message reception.
- A Streamlit dashboard with dynamic sensor graphs.

Add screenshots of your actual AWS IoT Core configuration, MQTT test client, and running dashboard to the `screenshots/` directory.

## 🌍 Applications

The architecture can serve as a foundation for:

- Smart home environmental monitoring.
- Temperature and humidity monitoring.
- Industrial sensor monitoring.
- Connected-device telemetry.
- Educational IoT and cloud computing experiments.

These are potential applications of the architecture, not claims that every use case has been implemented.

## 🚧 Future Enhancements

- **Persistent storage:** Store historical sensor readings in Amazon DynamoDB or another suitable database.
- **Device expansion:** Support multiple simulated or physical IoT devices.
- **Alerting:** Generate notifications when readings cross configured thresholds.
- **Analytics:** Analyze historical sensor readings to identify trends.
- **Containerization:** Package the application using Docker.
- **CI/CD:** Introduce automated testing and build workflows using GitHub Actions.
- **Infrastructure as Code:** Provision cloud resources using AWS CloudFormation or Terraform.

## 📚 References

- [AWS IoT Core Documentation](https://docs.aws.amazon.com/iot/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Paho MQTT Documentation](https://eclipse.dev/paho/)
- [MQTT Protocol](https://mqtt.org/)

## 👨‍💻 Project Information

**Project:** IoT Data Processing and Storage Using Cloud Services

**Domain:** Cloud Computing, Internet of Things, and Secure Communication

**Institution:** Vardhaman College of Engineering, Hyderabad

**Project type:** Academic course-end project

Developed as part of the Cloud Computing and Virtualization Laboratory.

## ⭐ Acknowledgements

This project was developed as part of an academic course-end project to explore IoT communication, AWS cloud services, secure messaging, and real-time data visualization.

If you find this project useful for learning, feel free to explore the implementation and adapt the architecture for your own IoT experiments.
