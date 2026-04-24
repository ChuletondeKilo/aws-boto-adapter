# AWS Boto Adapter

A lazy-loading AWS service wrapper with strong typing support using Python's generic types and descriptors.

## Features

- 🚀 **Lazy Loading**: Services are only initialized when first accessed
- 🔒 **Type Safe**: Full type hints with `Generic[T]` for IDE autocomplete and type checking
- 📦 **Modular Design**: Easy to extend with new AWS services
- 🎯 **Clean API**: Simple, intuitive interface for AWS interactions

## Supported Services

- **SSM**: Systems Manager Parameter Store
- **S3**: Simple Storage Service
- **Secrets Manager**: Secret management (via Parameter Store adapter)

## Installation

```bash
pip install aws-boto-adapter
```

Or with development dependencies:

```bash
pip install -e ".[dev]"
```

## Quick Start

### Basic Usage

```python
from aws_boto_adapter import MyAWS

# Initialize with optional profile and region
aws = MyAWS(profile="my-profile", region="eu-west-1")

# Services are lazily initialized on first access
param = aws.ssm.get_parameter(name="/my/parameter")

# S3 operations
aws.s3.list_buckets()

# Secrets Manager
secret = aws.secrets.get_secret(secret_id="my-secret")
```

### Type-Safe Usage

The adapter provides full type hints:

```python
from aws_boto_adapter import MyAWS

aws = MyAWS()

# Type checker knows that `aws.ssm` is SSMService
# Autocomplete works perfectly in your IDE
response = aws.ssm.get_parameter(name="/path/to/param")
```

## How It Works

The project uses **Python descriptors** and **generic types** for lazy loading:

1. **Descriptors**: Services are defined as `AWSServiceDescriptor` instances, which only create the actual service when first accessed
2. **Generics**: `Generic[T]` ensures type checkers know exactly which service type is being accessed
3. **Lazy Initialization**: Services are only instantiated when needed, saving resources

## Architecture

```
src/
├── __init__.py          # Public API exports
├── main.py              # MyAWS class and AWSServiceDescriptor
└── aws/
    ├── __init__.py      # Service exports
    ├── ssm/             # SSM service module
    ├── s3/              # S3 service module
    └── param_store/     # Parameter Store / Secrets manager
```

## Development

### Running Tests

```bash
pytest tests/
```

### Type Checking

```bash
pyright .
```

## Requirements

- Python 3.12+
- boto3 >= 1.42.36
- pydantic >= 2.12.5

## License

MIT License - see LICENSE file for details

## Contributing

Contributions welcome! Please ensure:
- Type hints are complete
- Tests are included
- Code follows PEP 8
