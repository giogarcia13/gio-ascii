import sys
import subprocess
from setuptools import setup, find_packages

def install_package(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Check for the '--with-audio' argument and handle it
with_audio = False
if "--with-audio" in sys.argv:
    with_audio = True
    sys.argv.remove("--with-audio")

# Install required packages
install_package('opencv-python')
if with_audio:
    install_package('pyaudio')

setup(
    name="video_to_ascii",
    version="1.3.0",
    author="Joel Ibaceta",
    author_email="mail@joelibaceta.com",
    license='MIT',
    description="It is a simple python package to play videos in the terminal",
    long_description="A simple tool to play a video using ascii characters instead of pixels",
    url="https://github.com/joelibaceta/video-to-ascii",
    project_urls={
        'Source': 'https://github.com/joelibaceta/video-to-ascii',
        'Tracker': 'https://github.com/joelibaceta/video-to-ascii/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=['xtermcolor', 'ffmpeg-python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='video ascii terminal opencv',
    entry_points={
        "console_scripts": [
            'video-to-ascii=video_to_ascii.cli:main'
        ]
    }
)
