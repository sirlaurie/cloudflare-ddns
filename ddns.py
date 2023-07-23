import json
import os
import httpx


def get_ipv6() -> str:
    """
    get the ip address of whoever executes the script
    """
    url = "https://6.ipw.cn/"
    response = httpx.get(url)
    print(f"current IPv6 address: {response.text}")
    return str(response.text)

def get_ipv4() -> str:
    """
    get the ip address of whoever executes the script
    """
    url = "https://4.ipw.cn/"
    response = httpx.get(url)
    print(f"current IPv4 address: {response.text}")
    return str(response.text)


def set_ip(current_ipv4: str, current_ipv6: str):
    """
    sets the ip in via cloudflare api
    """
    zone_id = os.environ.get("ZONE_ID", "")

    api_key = os.environ.get("API_KEY", "")
    user_email = os.environ.get("USER_EMAIL", "")
    record_name = os.environ.get("RECORD_NAME", "")

    headers = {
        "X-Auth-Email": user_email,
        "X-Auth-Key": api_key,
        "Content-Type": "application/json",
    }

    aaaa_record_id = os.environ.get("AAAA_RECORD_ID")
    url = (
        "https://api.cloudflare.com/client/v4/zones/%(zone_id)s/dns_records/%(record_id)s"
        % {"zone_id": zone_id, "record_id": aaaa_record_id}
    )
    payload = {"type": "AAAA", "name": record_name, "content": current_ipv6}
    response = httpx.put(url, headers=headers, data=json.dumps(payload)) # type: ignore    print(response.status_code)

    a_record_id = os.environ.get("A_RECORD_ID")
    url = (
        "https://api.cloudflare.com/client/v4/zones/%(zone_id)s/dns_records/%(record_id)s"
        % {"zone_id": zone_id, "record_id": a_record_id}
    )
    payload = {"type": "A", "name": record_name, "content": current_ipv4}
    response = httpx.put(url, headers=headers, data=json.dumps(payload)) # type: ignore
    print(response.status_code)


def main():
    current_ipv4 = get_ipv4()
    current_ipv6 = get_ipv6()
    set_ip(current_ipv4, current_ipv6)


if __name__ == "__main__":
    main()
