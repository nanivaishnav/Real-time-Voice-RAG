import streamlit as st
import requests
import sseclient
import json

st.title("🎙️ Real-Time Voice RAG")

query = st.text_input("Ask something")

if query:
    response = requests.post(
        "http://localhost:8000/stream",
        json={"query": query},
        stream=True
    )

    client = sseclient.SSEClient(response)

    output = ""
    placeholder = st.empty()

    for event in client.events():
        data = json.loads(event.data)

        if "token" in data:
            output += data["token"]
            placeholder.markdown(output)

        if "audio" in data:
            audio_bytes = bytes.fromhex(data["audio"])
            st.audio(audio_bytes)