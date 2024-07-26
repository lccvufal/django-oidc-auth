# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='django-oidc-auth',
    version='2.1.0',
    description='OpenID Connect client for Django applications',
    long_description='WIP',
    author='Lucas S. Magalhães, Daniel Pimentel',
    author_email='lucas.sampaio@intelie.com.br, danielpimentel@lccv.ufal.br',
    packages=find_packages(exclude=['*.tests']),
    include_package_data=True,
    install_requires=[
        'Django==5.0.7',
        'pyjwkest==1.4.2',
        'requests==2.32.3',
    ],
    zip_safe=True
)
