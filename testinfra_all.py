"""testinfra for HOST"""

import pytest


def test_file_www_exists(host):
    """Checking file var exists."""
    assert host.file('/var/www/').exists

def test_nginx_proc(host):
    """Checking nginx running and enabled."""
    assert host.service("nginx").is_running
    assert host.service("nginx").is_enabled

def test_socket_80(host):
    """Checking nginx on port 80."""
    cmd = "netstat -tupln | grep :80"
    output = host.run(cmd)
    run = host.run(cmd)
    assert output.rc == 0
    if "nginx" not in output.stdout:
        raise AssertionError("No Nginx in port 80")

def test_socket_443(host):
    """Checking nginx on port 443."""
    cmd = "netstat -tupln | grep :443"
    output = host.run(cmd)
    run = host.run(cmd)
    assert output.rc == 0
    if "nginx" not in output.stdout:
        raise AssertionError("No Nginx in port 443")
