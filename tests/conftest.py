"""Pytest configuration and fixtures"""

import pytest
import sys
from pathlib import Path
from unittest.mock import Mock

# Add src to path so we can import aws_boto_adapter in tests
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))


@pytest.fixture
def mock_boto3_session():
    """Fixture providing a mocked boto3 session"""
    return Mock()


@pytest.fixture
def mock_aws_service():
    """Fixture providing a mock AWS service"""
    return Mock()


@pytest.fixture
def aws_instance(mock_boto3_session):
    """Fixture providing a MyAWS instance with mocked session"""
    from aws.main import MyAWS
    
    instance = Mock(spec=MyAWS)
    instance.session = mock_boto3_session
    return instance
