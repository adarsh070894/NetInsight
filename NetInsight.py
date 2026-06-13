import json
import ollama
from netmiko import ConnectHandler
import requests
import streamlit as st
from rich.console import Console
from rich.markdown import Markdown

OLLAMA_API_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3"

DEVICE_INVENTORY = {
    "r1": {
        "device_type": "arista_eos",
        "host": "192.168.0.201",
        "username": "admin",
        "password": "admin"
    },
    "r2": {
        "device_type": "arista_eos",
        "host": "192.168.0.202",
        "username": "admin",
        "password": "admin"
    },
    "r3": {
        "device_type": "arista_eos",
        "host": "192.168.0.203",
        "username": "admin",
        "password": "admin"
    }
}

SYSTEM_PROMPT = """
You are a network assistant. Extract intent from the user's natural language command and return a JSON with:
{
    "action": "run_command",
    "devices": ["r1", "r2","r3"],
    "commands": ["show ip interface brief"]
}
Only reply with JSON output. Do not add explanation.
"""


def ask_llm(user_input):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        json_response = response.json()["message"]["content"]
        parsed_intent = json.loads(json_response)
        return parsed_intent
    except Exception as e:
        return {"error": str(e)}


def run_commands(devices, commands):
    output = ""
    for device in devices:
        device_info = DEVICE_INVENTORY.get(device)
        if not device_info:
            output += f"\n[ERROR] Device {device} not found in inventory"
            continue
        try:
            with ConnectHandler(**device_info) as conn:
                for cmd in commands:
                    cmd_output = conn.send_command(cmd)
                    output += f"\n[{device}] > {cmd}\n\n{cmd_output}\n"
        except Exception as e:
            output += f"\n[ERROR] Could not connect to {device}: {e}"
    return output


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(page_title="LLaMA3 Local Chatbot", layout="wide")
st.title("LLaMA3 Local Chat (powered by Ollama)")
user_input = st.chat_input("Ask me to run a command on your network device...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("Talking to LLaMA3..."):
        intent = ask_llm(user_input)
        if "error" in intent:
            reply = f"ERROR: {intent['error']}"
        elif intent.get("action") == "run_command":
            reply = run_commands(devices=intent["devices"], commands=intent["commands"])
        else:
            reply = f"Could not understand the prompt. LLM returned {intent}"

    st.chat_message("assistant").markdown(f"{reply}")
    st.session_state.chat_history.append({"role": "assistant", "content": f"{reply}"})
