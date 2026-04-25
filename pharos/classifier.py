from __future__ import annotations


def classify_asset(vendor: str) -> tuple[str, str]:
    """Classify an observed asset using vendor/OUI information.

    The function is intentionally conservative. It does not claim exact device
    identity; it provides useful asset-intelligence hints for inventory and
    defensive review.
    """

    if not vendor or vendor.lower() == "unknown":
        return "Unknown Asset", "Unknown or unmanaged device - validate ownership"

    vendor_lower = vendor.lower()

    rules: list[tuple[list[str], str, str]] = [
        (
            ["cisco", "mikrotik", "ubiquiti", "juniper", "tp-link", "netgear", "aruba", "fortinet", "palo alto", "tibro"],
            "Network Infrastructure",
            "Management or critical network asset - validate admin exposure",
        ),
        (
            ["hikvision", "dahua", "axis", "uniview", "hanwha"],
            "Camera / Surveillance IoT",
            "Surveillance device - verify segmentation and default credentials",
        ),
        (
            ["midea", "broadlink", "espressif", "tuya", "sonoff", "shelly", "philips lighting", "amazon technologies", "google", "nest"],
            "Smart Home / IoT",
            "IoT device - verify isolation, firmware posture, and business need",
        ),
        (
            ["hp", "hewlett", "canon", "epson", "brother", "xerox", "ricoh", "seiko epson"],
            "Printer / Office Device",
            "Often overlooked office asset - review admin interface and firmware",
        ),
        (
            ["apple", "samsung", "xiaomi", "oppo", "oneplus"],
            "Endpoint / Mobile",
            "User-controlled endpoint - validate ownership and access policy",
        ),
        (
            ["intel", "dell", "lenovo", "hewlett-packard", "asustek", "msi"],
            "Workstation / Endpoint",
            "Endpoint-class device - validate EDR and patch coverage",
        ),
        (
            ["vmware", "virtualbox", "qemu", "parallels", "xen", "hyper-v"],
            "Virtualized Asset",
            "Virtual machine or lab asset - validate owner and exposure",
        ),
        (
            ["raspberry", "arduino", "particle", "adafruit"],
            "Embedded / Lab IoT",
            "Embedded device - validate purpose, update path, and network zone",
        ),
    ]

    for keywords, asset_type, risk_hint in rules:
        if any(keyword in vendor_lower for keyword in keywords):
            return asset_type, risk_hint

    return "Generic Network Asset", "Review ownership, business purpose, and monitoring coverage"
