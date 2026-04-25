from pharos.classifier import classify_asset


def test_unknown_vendor():
    assert classify_asset("Unknown") == ("Unknown Asset", "Unknown or unmanaged device")


def test_network_vendor():
    asset_type, _ = classify_asset("Cisco Systems")
    assert asset_type == "Network Infrastructure"


def test_camera_vendor():
    asset_type, _ = classify_asset("Hikvision Digital Technology")
    assert asset_type == "Camera / IoT"
