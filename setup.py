from setuptools import setup, find_packages

setup(
    name='fastauth',
    author='Oliver Scotten',
    author_email='revi99@me.com',
    description='FastAuth is an authorization framework for FastAPI applications.',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'fastapi~=0.115.0',
        'PyJWT~=2.9.0',
        'redis~=5.2.0',
        'passlib~=1.7.4'
    ],
    extras_require={
        "dev": [
            "pytest~=8.3.0",
            "pipreqs~=0.5.0",
            "fakeredis~=2.26.0",
            "pytest-cov~=5.0.0"
        ],
    },
)