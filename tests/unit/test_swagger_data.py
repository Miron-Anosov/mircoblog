"""Tests developers dependencies."""

import pytest

from src.back_core import swagger_info


@pytest.mark.test_config
def test_type_static_swag_docs_version_api():
    """Test VERSION_API swagger."""
    assert isinstance(swagger_info.VERSION_API, str)


@pytest.mark.test_config
def test_type_static_swag_docs_title():
    """Test TITLE swagger."""
    assert isinstance(swagger_info.TITLE, str)


@pytest.mark.test_config
def test_type_static_swag_docs_summary():
    """Test SUMMARY swagger."""
    assert isinstance(swagger_info.SUMMARY, str)


@pytest.mark.test_config
def test_type_static_swag_docs_api_server_data():
    """Test SERVERS swagger."""
    url = 0
    assert isinstance(swagger_info.SERVERS, list)
    assert isinstance(swagger_info.SERVERS[url], dict)


@pytest.mark.test_config
def test_type_static_swag_docs_tags_meta():
    """Test TAGS_METADATA swagger."""
    meta_index = 0
    assert isinstance(swagger_info.TAGS_METADATA, list)
    assert isinstance(swagger_info.TAGS_METADATA[meta_index], dict)
