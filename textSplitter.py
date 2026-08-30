import re

message = input("Enter text: ")

# Pattern matches words ending in .com, .org, .net, etc., or starting with www.
link_pattern = r'(?:https?://)?(?:www\.)?[\w\.-]+\.(?:com|org|net|edu|gov|io)\S*'

# Extract links
links = re.findall(link_pattern, message, re.IGNORECASE)

# Clean text
text_only = re.sub(link_pattern, '', message, flags=re.IGNORECASE).strip()

print("Links:", links)
print("Text:", text_only)
