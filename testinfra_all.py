"""testinfra for HOST"""

import pytest


def test_file_www_exists(host):
    """Checking file var exists."""
    assert host.file('/var/www/').exists
