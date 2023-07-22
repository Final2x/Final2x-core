import os

from setuptools import setup

_version: str = "1.0.4"


def My_find_packages(*tops):
    packages = []
    for d in tops:
        for root, dirs, files in os.walk(d, followlinks=True):
            packages.append(root)
    return packages


# python setup.py sdist
setup(
    name='Final2x-core',
    version=_version,
    description='',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Tohrusky',
    url='https://github.com/Tohrusky/Final2x-core',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        # 目标 Python 版本
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    packages=My_find_packages('Final2x_core'),
    entry_points={
        'console_scripts': [
            'Final2x-core=Final2x_core.__main__:main'
        ]
    },
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=['numpy',
                      'opencv-python',
                      'PyYAML',
                      'loguru',
                      'realcugan_ncnn_py >= 1.3.0',
                      'realesrgan_ncnn_py >= 1.3.0',
                      'waifu2x_ncnn_py >= 1.3.0',
                      'srmd_ncnn_py >= 1.3.0']
)
