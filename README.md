# NetInsight AI

An AI-powered Network Operations Assistant that combines **Llama 3**, **Ollama**, **Streamlit**, and **Netmiko** to execute network commands on devices using natural language.

NetInsight AI allows network engineers to interact with network devices conversationally instead of manually connecting to devices and typing commands.

---

## Features

* Natural language network command execution
* Local AI inference using Llama 3 via Ollama
* Interactive web interface built with Streamlit
* Multi-device support
* SSH connectivity using Netmiko
* No cloud APIs required
* Fast and lightweight architecture
* Easily extensible for network automation workflows

---

## Example Queries

```text
Run show version on r1

Show ip interface brief on r2

Run show interfaces status on r1 and r3

Execute show ip route on all routers
```

The AI interprets the request, identifies the target devices and commands, then connects to the devices and returns the output.

---

## Architecture

```text
User
  │
  ▼
Streamlit Chat Interface
  │
  ▼
Llama 3 (Ollama)
  │
  ▼
Intent Extraction
  │
  ▼
Netmiko SSH Connection
  │
  ▼
Network Devices
  │
  ▼
Command Output
  │
  ▼
User
```

---

## Technology Stack

* Python
* Streamlit
* Ollama
* Llama 3
* Netmiko
* Requests

---

## Project Structure

```text
NetInsight-AI/
│
├── NetInsight.py
├── README.md
├── requirements.txt
└── screenshots/
```

---

## Prerequisites

Install:

* Python 3.10+
* Ollama
* Llama 3 model

---

## Install Ollama

Download and install Ollama:

https://ollama.com

Pull the Llama 3 model:

```bash
ollama pull llama3
```

Verify the model:

```bash
ollama list
```

Start the Ollama service:

```bash
ollama serve
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/NetInsight-AI.git

cd NetInsight-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

Start Streamlit:

```bash
streamlit run NetInsight.py
```

Open:

```text
http://localhost:8501
```

---

## Device Inventory

Update the device inventory section in the script with your network devices:

```python
DEVICE_INVENTORY = {
    "r1": {
        "device_type": "arista_eos",
        "host": "192.168.0.201",
        "username": "admin",
        "password": "admin"
    }
}
```

---

## Security Notice

This project is intended for lab and learning environments.

Recommended improvements for production use:

* Store credentials in environment variables
* Use encrypted secrets management
* Implement role-based access control
* Restrict command execution using allowlists
* Enable audit logging

---

## Future Enhancements

* AI-powered troubleshooting analysis
* OSPF health checks
* BGP validation
* Routing table comparison
* Network health summaries
* Configuration compliance checks
* Multi-vendor support
* RAG-based network documentation search
* Webex and Teams integration

---

## Sample Workflow

```text
User:
Show ip interface brief on r2

AI:
Identifies device = r2
Identifies command = show ip interface brief

Netmiko:
Connects to r2 via SSH

Result:
Displays command output in Streamlit
```

---

## Author

Adarsh Singh

Network Automation | AI for Networking |

---

## License

This project is licensed under the MIT License.
