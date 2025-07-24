import requests
import json

AWS_IP_RANGES_URL = "https://ip-ranges.amazonaws.com/ip-ranges.json"
OUTPUT_FILE = "aws_ip_ranges.json"

def fetch_aws_ip_ranges():
    response = requests.get(AWS_IP_RANGES_URL)
    response.raise_for_status()
    return response.json()

def extract_ip_prefixes(data):
    ipv4 = sorted(set(entry["ip_prefix"] for entry in data.get("prefixes", []) if "ip_prefix" in entry))
    ipv6 = sorted(set(entry["ipv6_prefix"] for entry in data.get("ipv6_prefixes", []) if "ipv6_prefix" in entry))
    return ipv4, ipv6

def save_split_prefixes(ipv4, ipv6, filename):
    output = {
        "cloudName": "AWS",
        "IPv4_Prefixes": ipv4,
        "IPv6_Prefixes": ipv6
    }
    with open(filename, "w") as f:
        json.dump(output, f, separators=(",", ":"))

def main():
    data = fetch_aws_ip_ranges()
    ipv4, ipv6 = extract_ip_prefixes(data)
    save_split_prefixes(ipv4, ipv6, OUTPUT_FILE)
    print(f"[✓] Saved {len(ipv4)} IPv4 and {len(ipv6)} IPv6 prefixes to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
