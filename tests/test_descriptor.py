"""Tests for AWSServiceDescriptor"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from aws.main import AWSServiceDescriptor, MyAWS
from aws import SSMService


class TestAWSServiceDescriptor:
    """Test the lazy-loading descriptor mechanism"""

    def test_descriptor_returns_self_when_instance_is_none(self):
        """Test that descriptor returns itself when accessed on the class"""
        descriptor = AWSServiceDescriptor(SSMService, "ssm")
        result = descriptor.__get__(None, MyAWS)
        assert result is descriptor

    def test_descriptor_creates_service_on_first_access(self):
        """Test that service is created on first access"""
        descriptor = AWSServiceDescriptor(SSMService, "ssm")
        
        # Mock instance with session
        instance = Mock()
        instance.session = Mock()
        
        # Mock the service class
        with patch.object(descriptor, 'service_class', wraps=SSMService) as mock_service:
            mock_service.return_value = Mock()
            
            # First access
            result = descriptor.__get__(instance, MyAWS)
            
            # Service should be created
            mock_service.assert_called_once_with(instance.session)

    def test_descriptor_caches_service(self):
        """Test that service is cached after first access"""
        descriptor = AWSServiceDescriptor(SSMService, "ssm")
        
        # Mock instance
        instance = Mock()
        instance.session = Mock()
        mock_service = Mock()
        
        # Set up the cached attribute
        setattr(instance, f"_{descriptor.service_name}_instance", mock_service)
        
        # Access should return cached service
        result = descriptor.__get__(instance, MyAWS)
        assert result is mock_service

    def test_descriptor_attr_name_is_correct(self):
        """Test that descriptor generates correct attribute name"""
        descriptor = AWSServiceDescriptor(SSMService, "test_service")
        assert descriptor.attr_name == "_test_service_instance"

    def test_descriptor_stores_service_class(self):
        """Test that descriptor stores the service class correctly"""
        descriptor = AWSServiceDescriptor(SSMService, "ssm")
        assert descriptor.service_class is SSMService

    def test_descriptor_stores_service_name(self):
        """Test that descriptor stores the service name correctly"""
        descriptor = AWSServiceDescriptor(SSMService, "ssm")
        assert descriptor.service_name == "ssm"
