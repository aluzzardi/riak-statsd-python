try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='riak-statsd',
    version='0.1.0',
    description='Transport proxy for instrumenting Riak clients',
    author='Andrea Luzzardi',
    author_email='andrea@luzzardi.com',
    url='https://github.com/aluzzardi/riak-statsd-python',
    packages=['riak_statsd'],
    install_requires=[
            'statsd>=0.5.1',
            'riak>=1.3.0'
    ],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
