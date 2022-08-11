#!/usr/bin/env python
from setuptools import setup


setup(
    name='django-crontab',
    description='dead simple crontab powered job scheduling for django',
    version='0.7.1',
    author='Lars Kreisz',
    author_email='lars.kreisz@gmail.com',
    license='MIT',
    url='https://github.com/kraiz/django-crontab',
    long_description=open('README.rst').read(),
    packages=[
        'django_crontab',
        'django_crontab.management',
        'django_crontab.management.commands'],
    install_requires=[
        'Django>=1.8'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: System :: Installation/Setup'
    ]
)
