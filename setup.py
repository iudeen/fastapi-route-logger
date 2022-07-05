from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='fastapi-route-logger-middleware',
    version='0.0.1',
    packages=['route_logger_middleware', 'route_logger_middleware.backends'],
    extras_require={
        "kafka": ["aiokafka>=0.7.2"],
        "mqtt": ["mqttools"],
        "redis": ["aioredis"]
    },
    url='https://github.com/iudeen/fastapi-route-logger',
    license='MIT',
    author='irfanuddin',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='irfanudeen08@gmail.com',
    description='A middleware to log all requests in FastAPI'
)
