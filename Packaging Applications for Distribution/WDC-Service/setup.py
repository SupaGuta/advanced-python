from setuptools import setup

setup(
    name='WDC-Service',
    version='1.0',
    packages=['wdc_service'],
    url='',
    license='',
    author='Gustave Bernier',
    author_email='gustave.bernier@gmail.com',
    description='Web service for Wood Delivery Calculator',
    install_requires=[
        "requests>=2.31.0",
        "Flask>=3.0.3",
        "Flask_Restful>=0.3.10",
        "Flask_HTTPAuth>=4.8.0"
    ],
    package_data={"wdc_service": ["delivery.db"]}
)
