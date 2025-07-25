import requests
import json

AWS_IP_RANGES_URL = "https://ip-ranges.amazonaws.com/ip-ranges.json"
OUTPUT_FILE = "aws_ip_ranges.json"

def fetch_aws_ip_ranges():
    response = requests.get(AWS_IP_RANGES_URL)
    response.raise_for_status()
    return response.json()

def extract_ip_prefixes(data):
    ipv4 = [entry["ip_prefix"] for entry in data.get("prefixes", []) if "ip_prefix" in entry]
    ipv6 = [entry["ipv6_prefix"] for entry in data.get("ipv6_prefixes", []) if "ipv6_prefix" in entry]
    return sorted(set(ipv4 + ipv6))

def save_json(ip_list, filename):
    output = {
        "cloudName": "AWS",
        "Prefixes": ip_list
    }
    with open(filename, "w") as f:
        json.dump(output, f, separators=(",", ":")) 

def main():
    data = fetch_aws_ip_ranges()
    ip_list = extract_ip_prefixes(data)
    save_json(ip_list, OUTPUT_FILE)
    print(f"[✓] Saved {len(ip_list)} prefixes to {OUTPUT_FILE}.")

if __name__ == "__main__":
    main()
