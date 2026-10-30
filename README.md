# Scam Message Investigator

## Project Overview

Scam Message Investigator is an AI-powered application designed to analyse suspicious SMS messages, emails, and job offers.

The application uses Artificial Intelligence to identify possible scam indicators, classify risk levels, explain warning signs, and provide safety recommendations.

It helps users understand suspicious messages and stay aware of online fraud.

## Features

- SMS Message Scam Detection
- Fraud Email Analysis
- Fake Job Offer Detection
- Risk Level Classification
- Warning Signs Identification
- Safety Recommendations
- Investigation Report Generation
- Downloadable JSON Report

## Technologies Used

- Python
- Streamlit
- Ollama
- Gemma 3:1B
- Requests
- JSON

## Project Structure

```text
Scam-Message-Investigator/
│
├── app.py
├── requirements.txt
└── README.md
```

## System Requirements

- Windows 10 or later
- Python 3.10 or later
- Visual Studio Code
- Ollama
- Gemma 3:1B Model
- Internet connection for initial setup

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd Scam-Message-Investigator
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Install Ollama Model

```bash
ollama pull gemma3:1b
```

### Step 7: Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## How the Application Works

1. Open the Scam Message Investigator application.
2. Select the message category.
3. Enter the suspicious SMS, email, or job offer.
4. Click the Investigate Message button.
5. The AI model analyses the entered text.
6. The application displays the risk level.
7. Warning signs and safety recommendations are generated.
8. Download the investigation report in JSON format.

## Risk Level Classification

| Risk Level | Description |
|---|---|
| Low | No major suspicious indicators identified |
| Medium | Some suspicious indicators identified |
| High Concern | Multiple suspicious indicators identified |

## Sample Test Cases

### Test Case 1: Suspicious SMS

Input:
"Congratulations! You won Rs. 5,00,000. Pay Rs. 500 to claim your prize."

Expected Result: High Concern

### Test Case 2: Fraud Email

Input:
"Your account will be blocked. Share your password and OTP immediately."

Expected Result: High Concern

### Test Case 3: Fake Job Offer

Input:
"Earn Rs. 5,000 per day from home. Pay a registration fee to confirm your job."

Expected Result: High Concern

### Test Case 4: Normal Message

Input:
"Your order has been shipped and will be delivered tomorrow."

Expected Result: Low

## Safety and Limitations

- AI-generated results are estimates, not guaranteed scam confirmations.
- The application analyses the text entered by the user.
- It does not independently verify sender identity or website authenticity.
- Users should never share passwords, OTPs, or banking details.
- Suspicious messages should be verified through official sources.

## Future Enhancements

- Multilingual Scam Detection
- Advanced Phishing URL Analysis
- Scam Detection History
- PDF Investigation Reports
- Improved Machine Learning Classification

## Conclusion

Scam Message Investigator uses AI technology to analyse suspicious messages and provide useful safety recommendations. It aims to improve awareness of digital scams and help users make safer decisions online.
