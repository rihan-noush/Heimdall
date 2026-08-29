import requests
import json

url = input("Enter URL: ")

def test_scam_link(url_to_check, api_key):
    endpoint = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"
    
    # Configure the payload parameters
    payload = {
        "client": {
            "clientId": "python-scam-checker",
            "clientVersion": "1.0.0"
        },
        "threatInfo": {
            "threatTypes": [
                "MALWARE", 
                "SOCIAL_ENGINEERING", 
                "UNWANTED_SOFTWARE", 
                "POTENTIALLY_HARMFUL_APPLICATION"
            ],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url_to_check}]
        }
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(endpoint, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        result = response.json()
        
        # If the result dictionary is empty, Google has not flagged the URL.
        if not result:
            print(f"✅ Safe: '{url_to_check}' passed Google Safe Browsing checks.")
            return {"status": "safe", "details": None}
        
        # If threat info exists, extract the matching details
        match_info = result["matches"][0]
        threat_type = match_info.get("threatType")
        platform = match_info.get("platformType")
        
        print(f"❌ WARNING: '{url_to_check}' is unsafe!")
        print(f"   Threat Type Identified: {threat_type}")
        print(f"   Targeted Platform: {platform}")
        
        return {"status": "unsafe", "threat": threat_type, "platform": platform}
        
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error connecting to Google API: {e}")
        return {"status": "error", "message": str(e)}

# --- Example Usage ---
API_KEY = "AIzaSyCbHwJqBmzxY14bnE65qjxYfuuzgfWNT2s"

test_scam_link(url, API_KEY)
