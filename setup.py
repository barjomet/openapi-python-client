from setuptools import setup

setup(
    name='openapi-python-client',
    version='dev',
    entry_points={
        'console_scripts': [
            'openapi-python-client=openapi_python_client.cli:app',
        ]
    }
)