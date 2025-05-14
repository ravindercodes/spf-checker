from setuptools import setup, find_packages

setup(
    name='spf-checker',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'dnspython',
        'pyspf'
    ],
    entry_points={
        'console_scripts': [
            'spf-check=spf_checker.__main__:main'
        ]
    },
)
