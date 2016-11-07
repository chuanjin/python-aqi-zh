Python-AQI-ZN
=================
[![PyPI version](https://badge.fury.io/py/aqizh.svg)](https://badge.fury.io/py/aqizh)
[![Build Status](https://travis-ci.org/chuanjin/python-aqi-zh.svg?branch=master)](https://travis-ci.org/chuanjin/python-aqi-zh)
[![Coverage Status](https://coveralls.io/repos/github/chuanjin/python-aqi-zh/badge.svg?branch=master)](https://coveralls.io/github/chuanjin/python-aqi-zh?branch=master)
[![Code Climate](https://codeclimate.com/github/chuanjin/python-aqi-zh/badges/gpa.svg)](https://codeclimate.com/github/chuanjin/python-aqi-zh)
[![Dependency Status](https://gemnasium.com/badges/github.com/chuanjin/python-aqi-zh.svg)](https://gemnasium.com/github.com/chuanjin/python-aqi-zh)

Python API for getting real time AQI of Chinese cities. Data from 

Air Quality Index API for China. Thanks [pm25.in](http://www.pm25.in)  for provide all the AQI raw data. To use this module a token is needed to apply from them.
 
**Installation**

    pip install aqizh
    or
    pip3 install aqizh
   

**Usage**

    from aqizh import AQI
    aqi = AQI('your_token')
    aqi.get_cities()
    aqi.get_all_cities()
    aqi.get_aqi_ranking()
    aqi.get_station_names('Beijing')
    aqi.get_aqis_by_station('1301A')
    aqi.get_pm25(city='Beijing', avg='false', stations='yes')
    # same for get_pm10, get_co, get_no2, get_so2, get_o3, get_aqi_details, get_only_aqi

Detail API docs can be found from [pm25.in](http://www.pm25.in/api_doc) 




