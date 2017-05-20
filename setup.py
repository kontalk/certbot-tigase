from setuptools import setup
from setuptools import find_packages

version = '0.0.1.dev0'

# Please update tox.ini when modifying dependency version requirements
install_requires = [
    'certbot',
    # For pkg_resources. >=1.0 so pip resolves it to a version cryptography
    # will tolerate; see #2599:
    'setuptools>=1.0',
    'zope.component',
    'zope.interface',
]

setup(
    name='certbot-tigase',
    version=version,
    description="Tigase plugin for Certbot",
    url='https://github.com/kontalk/certbot-tigase',
    author="Kontalk devteam",
    author_email='devteam@kontalk.org',
    license='GPL 3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GPL Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'certbot.plugins': [
            'tigase = certbot_tigase.installer:TigaseInstaller',
        ],
    },
)
