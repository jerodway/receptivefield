from setuptools import setup

VERSION = '0.5.4'

setup(
    name='receptivefield',
    packages=['receptivefield'],
    version=VERSION,
    description='Gradient based Receptive field estimation library for Tensorflow and Pytorch',
    author='ShelfWise.ai',
    author_email='krzysztof.kolasinski@shelfwise.ai',
    url='https://github.com/fornaxai/receptivefield',
    download_url=f'https://github.com/fornaxai/receptivefield/archive/{VERSION}.tar.gz',
    keywords=['tensorflow', 'pytorch'],
    install_requires=[
        'pillow>=6.2.0',
        'matplotlib>=3.1.0',
        'numpy>=1.17.0',
        'lmfit>=1.3.0'
    ],
    classifiers=[],
    include_package_data=True
)
