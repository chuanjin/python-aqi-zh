from distutils.core import setup


install_requires = [
    'httmock==1.2.5',
    'requests==2.11.1'
]

setup(
  name = 'aqizh',
  packages = ['aqizh'],
  version = '0.2',
  description = 'Python API for AQI in China',
  author = 'Chuan Jin',
  author_email = 'chuan.jin.813@gmail.com',
  install_requires=install_requires,
  url = 'https://github.com/chuanjin/python-aqi-zh',
  download_url = 'https://github.com/chuanjin/python-aqi-zh/releases',
  keywords = ['AQI', 'China', 'python'],
  classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
],

)
