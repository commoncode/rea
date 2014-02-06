from setuptools import setup, find_packages

setup( name='rea',
    version = '0.0.2',
    description = 'Resources, Events & Agents marketplace models',
    author = 'Daryl Antony',
    author_email = 'daryl@commoncode.com.au',
    url = 'https://github.com/commoncode/rea',
    keywords = ['django',],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    dependency_links = [
        'http://github.com/commoncode/cqrs/tarball/master#egg=cqrs-0.0.1',
    ],
    install_requires = [
        'Django>=1.4',
        'django-polymorphic',
        'django-xworkflows',
        'cqrs',
    ]
)
