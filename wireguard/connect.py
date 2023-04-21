from wireguard.WireGuardConnector import connect_to_wireguard, force_close_wireguard
import os
import random
from util.files import random_connection


def start_random_connection():
    config_path = random_connection()
    return connect_to_wireguard(config_path)


def close_connection(connection):
    connection.close_connection()


def force_quit_connection():
    force_close_wireguard()
