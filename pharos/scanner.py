from mac_vendor_lookup import MacLookup
from scapy.all import ARP, Ether, srp

from pharos.classifier import classify_asset


def scan_network(ip_range: str, timeout: int = 2) -> list[dict]:
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    answered, _ = srp(packet, timeout=timeout, verbose=False)

    mac_lookup = MacLookup()
    results = []

    for _, received in answered:
        ip = received.psrc
        mac = received.hwsrc

        try:
            vendor = mac_lookup.lookup(mac)
        except Exception:
            vendor = "Unknown"

        asset_type, risk_hint = classify_asset(vendor)

        results.append({
            "ip": ip,
            "mac": mac,
            "vendor": vendor,
            "asset_type": asset_type,
            "risk_hint": risk_hint,
        })

    return results
