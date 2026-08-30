import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

message = input("Message: ")

prompt = f"""
Check this message for scam risk in the following criteria (0 - No, 1 - Yes):
urgency, threat, reward temptation, request of sensitive information, impersonation, language style anomaly, and the message intent.

Reply with just the numbers separated by commas.

Message: {message}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\n" + response.text)
