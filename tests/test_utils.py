import pytest

from setappversion.utils import replace_ver


def test_replace_version_1():
    old_version_text = """
        apiVersion: v2
        name: homepage
        description: A Helm chart for Papermerge homepage
        type: application
        version: 0.3.12
        appVersion: "0.3.0"
    """
    new_version_text = """
        apiVersion: v2
        name: homepage
        description: A Helm chart for Papermerge homepage
        type: application
        version: 0.3.12
        appVersion: "0.4.0"
    """
    assert replace_ver(old_version_text, "0.4.0") == new_version_text



def test_replace_version_2():
    old_version_text = """
    appVersion: "1.5.5"
    """
    new_version_text = """
    appVersion: "1.5.6"
    """
    assert replace_ver(old_version_text, "1.5.6") == new_version_text
