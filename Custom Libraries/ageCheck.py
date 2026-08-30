from datetime import datetime
from urllib.parse import urlparse
import whois

SHARED_HOSTS = ["github.io", "wordpress.com", "blogspot.com"]


def unshorten_url(url):
    return url


def get_domain_age_in_days(*urls):
    if len(urls) == 1 and isinstance(urls[0], (list, tuple)):
        urls = urls[0]

    results = {}

    for original_url in urls:
        url = original_url.strip()
        if not url:
            continue

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        real_url = unshorten_url(url)
        domain = urlparse(real_url).netloc.lower()

        if domain.startswith("www."):
            domain = domain[4:]

        is_shared = False
        for host in SHARED_HOSTS:
            if domain.endswith(host):
                results[original_url] = (0, f"Shared Host Detected ({domain})")
                is_shared = True
                break

        if is_shared:
            continue

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

                results[original_url] = (
                    days_passed,
                    creation_date.strftime("%Y-%m-%d"),
                )
            else:
                results[original_url] = (-1, "Creation date missing")

        except Exception as e:
            clean_error = str(e).split("\n")[0]
            results[original_url] = (-1, f"Lookup failed: {clean_error}")

    return results


# --- Dynamic User Input ---
raw_input = input("Enter or paste all links (separated by spaces or commas): ")

# Split user input by commas or spaces into a list of URLs
urls_list = [
    url.strip()
    for url in raw_input.replace(",", " ").split()
    if url.strip()
]

# Run function on user input
ages = get_domain_age_in_days(urls_list)

# Print results one by one
print("\n--- Results ---")
for url, result in ages.items():
    print(f"URL: {url} -> Days: {result[0]}, Details: {result[1]}")
