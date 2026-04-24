"""Tests for AWS services"""

import pytest
from unittest.mock import Mock, patch

from aws import SSMService, S3Service, ParamStoreService


class TestSSMService:
    """Test SSM service initialization"""

    def test_ssm_service_initialization(self):
        """Test that SSMService can be initialized with a session"""
        mock_session = Mock()
        service = SSMService(mock_session)
        
        assert service is not None

    def test_ssm_service_stores_session(self):
        """Test that SSMService stores the session"""
        mock_session = Mock()
        service = SSMService(mock_session)
        
        # Check if session is accessible (implementation may vary)
        # This depends on how SSMService is implemented
        assert hasattr(service, 'session') or hasattr(service, '_session')


class TestS3Service:
    """Test S3 service initialization"""

    def test_s3_service_initialization(self):
        """Test that S3Service can be initialized with a session"""
        mock_session = Mock()
        service = S3Service(mock_session)
        
        assert service is not None

    def test_s3_service_stores_session(self):
        """Test that S3Service stores the session"""
        mock_session = Mock()
        service = S3Service(mock_session)
        
        # Check if session is accessible
        assert hasattr(service, 'session') or hasattr(service, '_session')


class TestParamStoreService:
    """Test ParamStore (Secrets Manager) service initialization"""

    def test_param_store_service_initialization(self):
        """Test that ParamStoreService can be initialized with a session"""
        mock_session = Mock()
        service = ParamStoreService(mock_session)
        
        assert service is not None

    def test_param_store_service_stores_session(self):
        """Test that ParamStoreService stores the session"""
        mock_session = Mock()
        service = ParamStoreService(mock_session)
        
        # Check if session is accessible
        assert hasattr(service, 'session') or hasattr(service, '_session')
