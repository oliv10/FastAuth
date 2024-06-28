from setuptools import setup, find_packages

setup(
    name='FastAuth',
    author='Oliver Scotten',
    author_email='revi99@me.com',
    description='FastAuth is an authorization framework for FastAPI applications.',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'fastapi==0.111.0',
        'PyJWT==2.8.0',
        'redis==5.0.7',
        'passlib==1.7.4'
    ],
)