"""Tests for MyAWS class"""

import pytest
from unittest.mock import Mock, patch
import boto3

from aws.main import MyAWS


class TestMyAWS:
    """Test MyAWS initialization and service access"""

    @patch('src.main.boto3.Session')
    def test_init_creates_session_with_profile_and_region(self, mock_session_class):
        """Test that MyAWS.__init__ creates a boto3 session with correct params"""
        mock_session = Mock()
        mock_session_class.return_value = mock_session
        
        aws = MyAWS(profile="test-profile", region="eu-west-1")
        
        mock_session_class.assert_called_once_with(
            profile_name="test-profile",
            region_name="eu-west-1"
        )
        assert aws.session is mock_session

    @patch('src.main.boto3.Session')
    def test_init_creates_session_without_params(self, mock_session_class):
        """Test that MyAWS.__init__ works with default params"""
        mock_session = Mock()
        mock_session_class.return_value = mock_session
        
        aws = MyAWS()
        
        mock_session_class.assert_called_once_with(
            profile_name=None,
            region_name=None
        )

    @patch('src.main.boto3.Session')
    def test_ssm_attribute_exists(self, mock_session_class):
        """Test that MyAWS has ssm attribute"""
        mock_session_class.return_value = Mock()
        aws = MyAWS()
        
        assert hasattr(aws, 'ssm')

    @patch('src.main.boto3.Session')
    def test_s3_attribute_exists(self, mock_session_class):
        """Test that MyAWS has s3 attribute"""
        mock_session_class.return_value = Mock()
        aws = MyAWS()
        
        assert hasattr(aws, 's3')

    @patch('src.main.boto3.Session')
    def test_secrets_attribute_exists(self, mock_session_class):
        """Test that MyAWS has secrets attribute"""
        mock_session_class.return_value = Mock()
        aws = MyAWS()
        
        assert hasattr(aws, 'secrets')

    def test_session_type_annotation(self):
        """Test that session has correct type annotation"""
        import inspect
        annotations = MyAWS.__annotations__
        assert 'session' in annotations
