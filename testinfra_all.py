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
    run = host.run(cmd)
    assert run.rc == 0
    assert "nginx" in run.stdout

def test_socket_443(host):
    """Checking nginx on port 443."""
    cmd = "netstat -tupln | grep :443"
    run = host.run(cmd)
    assert run.rc == 0
    assert "nginx" in run.stdout
