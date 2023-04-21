import os
import sys
import tempfile
import subprocess


class WireGuardConnector:
    def __init__(self, config_path: str):
        self.config_path = config_path

    def establish_connection(self) -> None:
        subprocess.run(["wireguard", "/installtunnelservice", self.config_path], check=True)
        print("WireGuard connection established.")

    def close_connection(self) -> None:
        file_name_without_extension = os.path.splitext(os.path.basename(self.config_path))[0]
        subprocess.run(["wireguard", "/uninstalltunnelservice", file_name_without_extension], check=True)
        print("WireGuard connection closed.")


def connect_to_wireguard(config_path: str) -> WireGuardConnector:
    wg_connector = WireGuardConnector(config_path)
    wg_connector.establish_connection()
    return wg_connector

def force_close_wireguard() -> None:
    subprocess.run(["taskkill", "/f", "/im", "wireguard.exe"], check=True)
    print("WireGuard closed.")
    subprocess.run(["wireguard"], check=True)
