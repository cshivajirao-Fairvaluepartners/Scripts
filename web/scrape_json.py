# Script to scrape a JSON endpoint

import argparse
import json
import pprint
from urllib.request import urlopen

# Scrapes URL and returns JSON
def scrape_json(url):
    j = None
    try:
        r = urlopen(url).read()
    except:
        print("Could not scrape URL")
    else:
        try:
            j = json.loads(r.decode('utf-8'))
        except:
            print("Could not load JSON content from URL")
    finally:
        return j

# Main
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="JSON scraper")
    parser.add_argument("-t", required=True, help="target URL: (format is http://somedomain.com)")
    args = parser.parse_args()

    if not args.t.startswith("http"):
        print("Invalid URL format, URLs must begin with 'http://', or 'https://'")
    else:
        result = scrape_json(args.t)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(result)
