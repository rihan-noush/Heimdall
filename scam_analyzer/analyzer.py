import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

message = input("Message: ")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=f"""
Check this message for scam risk.

Reply in exactly 4 lines:
Risk: LOW/MEDIUM/HIGH
Score: 0-100
Flags: max 3 short keywords
Action: max 8 words

Message: {message}
"""
)

print("\n" + response.text)