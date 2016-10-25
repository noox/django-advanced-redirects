from distutils.core import setup

VERSION = __import__("advanced_redirects").__version__

setup(
    name='django-advanced-redirects',
    packages=['advanced_redirects'],
    version=VERSION,
    description='Advanced redirect management for Django applications.',
    author='Eric Ressler',
    author_email='eric@ericressler.com',
    download_url="https://github.com/noox/django-advanced-redirects/tarball/{0}".format(VERSION),
    keywords=['django', 'redirects', 'seo'],
    classifiers=[],
    install_requires=[
        'django>=1.7'
    ]
)
