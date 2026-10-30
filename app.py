
import streamlit as st
import requests
import json
import os


MODEL = "gemma3:1b"

# Local development default.
# For cloud deployment, configure OLLAMA_URL in Streamlit Secrets.
OLLAMA_URL = st.secrets.get(
    "OLLAMA_URL",
    os.getenv(
        "OLLAMA_URL",
        "http://localhost:11434/api/chat"
    )
)

OLLAMA_API_KEY = st.secrets.get(
    "OLLAMA_API_KEY",
    os.getenv("OLLAMA_API_KEY", "")
)



st.set_page_config(
    page_title="Scam Message Investigator",
    page_icon="🔍",
    layout="wide"
)

st.title("Scam Message Investigator")

st.write(
    "An AI-powered application to investigate suspicious "
    "SMS messages, emails and job offers."
)

st.divider()


st.subheader("Message Investigation")

message_type = st.selectbox(
    "Select Message Type",
    ["SMS Message", "Email", "Job Offer"]
)

user_message = st.text_area(
    "Enter Your Message",
    height=200,
    placeholder="Paste your suspicious message here..."
)




def detect_scam(message, category):

    prompt = f"""
You are an AI Cybersecurity Assistant.

Analyse the following message for possible scam indicators.

Category: {category}

Message:
{message}

Return ONLY valid JSON in this format:

{{
    "risk_level": "Low / Medium / High Concern",
    "message_type": "Type of message",
    "summary": "Short explanation",
    "warning_signs": [
        "Warning sign 1",
        "Warning sign 2"
    ],
    "recommended_actions": [
        "Action 1",
        "Action 2"
    ]
}}

Instructions:
- Identify suspicious payment requests.
- Identify OTP and password requests.
- Identify fake prize announcements.
- Identify suspicious job offers.
- Identify urgent or threatening language.
- Explain the reasons clearly.
- Do not claim a message is definitely fraudulent without proof.
"""

    headers = {
        "Content-Type": "application/json"
    }

    if OLLAMA_API_KEY:
        headers["Authorization"] = (
            "Bearer " + OLLAMA_API_KEY
        )

    response = requests.post(
        OLLAMA_URL,
        headers=headers,
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False,
            "format": "json"
        },
        timeout=180
    )

    response.raise_for_status()

    result = response.json()["message"]["content"]

    return json.loads(result)




if st.button("Investigate Message", type="primary"):

    if not user_message.strip():

        st.warning("Please enter a message before investigation.")

    else:

        with st.spinner("AI is analysing your message..."):

            try:

                result = detect_scam(
                    user_message,
                    message_type
                )

                st.divider()
                st.header("Investigation Report")

              
                risk = result.get(
                    "risk_level",
                    "Unknown"
                )

                if "High" in risk:

                    st.error("Risk Level: " + risk)

                elif "Medium" in risk:

                    st.warning("Risk Level: " + risk)

                elif "Low" in risk:

                    st.success("Risk Level: " + risk)

                else:

                    st.info("Risk Level: " + risk)

            
                st.subheader("Message Type")
                st.write(
                    result.get(
                        "message_type",
                        "Not available"
                    )
                )

               
                st.subheader("Message Summary")
                st.write(
                    result.get(
                        "summary",
                        "Not available"
                    )
                )

               
                st.subheader("Warning Signs")

                warning_signs = result.get(
                    "warning_signs",
                    []
                )

                if warning_signs:

                    for sign in warning_signs:
                        st.write("- " + str(sign))

                else:

                    st.write("No warning signs provided.")

               
                st.subheader("Recommended Actions")

                actions = result.get(
                    "recommended_actions",
                    []
                )

                if actions:

                    for action in actions:
                        st.write("- " + str(action))

                else:

                    st.write("No recommendations provided.")

               
                st.divider()

                report = json.dumps(
                    result,
                    indent=4,
                    ensure_ascii=False
                )

                st.download_button(
                    label="Download Investigation Report",
                    data=report,
                    file_name="scam_investigation_report.json",
                    mime="application/json"
                )

                st.info(
                    "Safety Note: AI analysis is an estimate. "
                    "Never share OTPs, passwords or banking details. "
                    "Verify suspicious messages through official sources."
                )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to Ollama. "
                    "Check whether the Ollama server is available."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "AI response timed out. Please try again."
                )

            except requests.exceptions.RequestException as e:

                st.error(
                    "Ollama request failed: " + str(e)
                )

            except (ValueError, KeyError, json.JSONDecodeError):

                st.error(
                    "AI response format was unexpected. "
                    "Please try again."
                )

            except Exception as e:

                st.error(
                    "Something went wrong: " + str(e)
                )
