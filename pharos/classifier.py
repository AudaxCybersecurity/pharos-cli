def classify_asset(vendor: str) -> tuple[str, str]:
    if not vendor or vendor.lower() == "unknown":
        return "Unknown Asset", "Unknown or unmanaged device"

    vendor_lower = vendor.lower()

    network_vendors = [
        "cisco", "mikrotik", "ubiquiti", "juniper", "tp-link",
        "netgear", "aruba", "fortinet", "palo alto"
    ]

    camera_vendors = [
        "hikvision", "dahua", "axis", "uniview", "hanwha"
    ]

    printer_vendors = [
        "hp", "hewlett", "canon", "epson", "brother", "xerox", "ricoh"
    ]

    mobile_vendors = [
        "apple", "samsung", "xiaomi", "oppo", "oneplus"
    ]

    virtualization_vendors = [
        "vmware", "virtualbox", "qemu", "parallels"
    ]

    if any(v in vendor_lower for v in network_vendors):
        return "Network Infrastructure", "Management or critical network asset"

    if any(v in vendor_lower for v in camera_vendors):
        return "Camera / IoT", "Surveillance or unmanaged IoT asset"

    if any(v in vendor_lower for v in printer_vendors):
        return "Printer", "Often overlooked office asset"

    if any(v in vendor_lower for v in mobile_vendors):
        return "Endpoint / Mobile", "User-controlled endpoint device"

    if any(v in vendor_lower for v in virtualization_vendors):
        return "Virtualized Asset", "Virtual machine or lab environment asset"

    return "Generic Network Asset", "Review ownership and business purpose"
