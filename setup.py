from setuptools import setup, find_packages

setup( name='rea',
    version = '0.0.1',
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
    install_requires = [
        # 'Django>=1.4',
        # 'django-polymorphic',
        # 'pymongo',
        # 'django_xworkflows',
        # 'djangorestframework',
        'django-denormalize-build-fix',
    ],
    dependency_links = [
        'hg+ssh://hg@bitbucket.org/darylantony/django-denormalize-build-fix#egg=django-denormalize-build-fix',
    ],
)
