from os.path import dirname, join
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'html_similarity_tools/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()


setup(
    name='html-similarity-tools',
    version=version,
    url='http://matiskay.com/code/html-similarity-tools',
    description='A set of similarity metricts to compare html files.',
    long_description=open('README.rst').read(),
    author='Edgar Marca',
    maintainer='Edgar Marca',
    maintainer_email='matiskay@gmail.com',
    license='BSD',
    packages=find_packages(exclude=('tests', 'tests.*')),
    zip_safe=False,
    classifiers=[
    ],
    install_requires=[
        'parsel==1.2.0',
    ],
)
