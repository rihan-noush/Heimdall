from datetime import datetime
from urllib.parse import urlparse
import requests
import whois

# Common free shared hosting/cloud platforms scammers misuse
SHARED_HOSTS = [
    "web.app",
    "firebaseapp.com",
    "vercel.app",
    "netlify.app",
    "github.io",
    "glitch.me",
    "pages.dev",
]


def unshorten_url(url):
    """Resolves short links (bit.ly, tinyurl, etc.) to their target URL."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.head(
            url, allow_redirects=True, timeout=5, headers=headers
        )
        return response.url
    except Exception:
        return url


def get_domain_age_in_days(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # 1. Unshorten first
    real_url = unshorten_url(url)
    domain = urlparse(real_url).netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    # 2. Check shared hosts -> Returns integer 0
    for host in SHARED_HOSTS:
        if domain.endswith(host):
            return 0, f"Shared Host Detected ({domain})"

    # 3. WHOIS Lookup
    try:
        info = whois.whois(domain)
        created = info.creation_date

        if isinstance(created, list):
            created = created[0]

        if created:
            creation_date = (
                created.date() if hasattr(created, "date") else created
            )
            today = datetime.now().date()
            days_passed = (today - creation_date).days

            # Returns integer (e.g., 450)
            return days_passed, creation_date.strftime("%Y-%m-%d")
        else:
            # Missing date -> Returns integer -1
            return -1, "Creation date missing"

    except Exception as e:
        # Extract ONLY the first sentence of the error to stop long WHOIS text dumps
        clean_error = str(e).split("\n")[0]
        # Failure / Non-existent domain -> Returns integer -1
        return -1, f"Lookup failed: {clean_error}"


# Execution
url = input("Enter URL: ")
days, date_info = get_domain_age_in_days(url)

# `days` is strictly an int here (Check with type(days))
print(f"Age Code : {days}")
print(f"Status   : {date_info}")
