"""testinfra for HOST"""

import pytest


def test_nginx_on_port_443(host):
    """check_nginx_port_443."""
    assert host.socket.connect(('localhost', 443))
