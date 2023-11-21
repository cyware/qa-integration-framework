"""
Copyright (C) 2015-2023, Cyware Inc.
Created by Cyware, Inc. <info@cyware.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
# Protocols
UDP = 'UDP'
TCP = 'TCP'
TCP_UDP = 'TCP,UDP'


def is_udp(protocol: str = None) -> bool:
    """Return True if the protocol is UDP, otherwise return False.

    Args:
        protocol (str): String to be verified.
    """
    return protocol.upper() == UDP


def is_tcp(protocol: str = None) -> bool:
    """Return True if the protocol is TCP, otherwise return False.

    Args:
        protocol (str): String to be verified.
    """
    return protocol.upper() == TCP


def is_tcp_udp(protocol: str = None) -> bool:
    """Return True if the protocol is 'TCP,UDP', otherwise return False.

    Args:
        protocol (str): String to be verified.
    """
    _protocol = protocol.replace(' ', '').upper().split(',')
    _protocol.sort()
    return ','.join(_protocol) == TCP_UDP
