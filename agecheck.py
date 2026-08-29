from datetime import datetime
from urllib.parse import urlparse
import whois


def get_domain_age_in_days(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    domain = urlparse(url).netloc
    if domain.startswith("www."):
        domain = domain[4:]

    try:
        info = whois.whois(domain)
        created = info.creation_date

        if isinstance(created, list):
            created = created[0]

        if created:
            # Strip time info to calculate accurate days
            creation_date = created.date() if hasattr(created, "date") else created
            today = datetime.now().date()

            days_passed = (today - creation_date).days
            return days_passed, creation_date.strftime("%Y-%m-%d")
        else:
            return None, "Creation date not found."

    except Exception as e:
        return None, f"Lookup failed: {e}"


url = input("Enter URL: ")
days, date_info = get_domain_age_in_days(url)

if days is not None:
    print(f"Creation Date: {date_info}")
    print(f"Age: {days} days old")
else:
    print(date_info)
