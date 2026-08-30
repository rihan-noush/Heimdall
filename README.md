# Heimdall - Personal Digital Safety & Scam Prevention Assistant

Heimdall is a 4-layered defense system designed to shield users from advanced financial scams, brand spoofing, phishing links, and deceptive QR codes. Built for the Smart India Hackathon 2026 by team CodeFellas, it features a combination of various scam detection techniques to ensure fast and efficient prevention.

## Features ##
Got a link, message, screenshot, or a QR code? Just type or upload those into the input box and watch Heimdall work its magic to provide  a verdict with explanations and reasons that can educate YOU in recognizing more scams in the future.

## Security ##

### Layer 1 & 2: Brand Whitelist & Malicious DB Lookup ###
Instantly matches incoming keyword logs with safe corporate domain certificates (e.g., SBI, HDFC) & queries local/global blacklists via quick key-value validation caches to intercept known ongoing campaigns.

### Layer 3 & 4: Urgency NLP Analysis & Domain Age & Verification ###
Assesses sentence context for fear tactics, false award traps, or fake UPI constraints to catch scams that contain zero hyperlinks & dynamically checks registrar metadata. Newly registered platforms (<15-30 days) or anonymous hosts trigger immediate threat indicators.

## Setup ## 
### Clone the project repository ###
``` git clone https://github.com ``` <br>
``` cd sih-codefellas ```

### Launch the backend server ###
Heimdall relies on main.py to process validation strings and serve web elements. <br>
``` python main.py ```

### Access the application dashboard ###
Open your browser and navigate to the local host address provided in your terminal output.
