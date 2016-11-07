# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
import requests
from requests.exceptions import RequestException


class NetworkException(Exception):
    pass


class AQI(object):

    def __init__(self, token):
        self._base_url = 'http://www.pm25.in/api/querys%s.json'
        self._token = token
        self._interface = None

    @property
    def interface(self):
        return self._interface

    @interface.setter
    def interface(self, p):
        self._interface = p

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, p):
        self._params = {'token': self._token}
        if p:
            del p['interface']
            station_code = p.get('station_code')
            city = p.get('city')
            self.validate_compulsory(city, station_code)
            avg = p.get('avg')
            self.validate_params(avg, ['true', 'false'])
            stations = p.get('stations')
            self.validate_params(stations, ['yes', 'no'])
            self._params.update(p)

    def validate_compulsory(self, city, station_code):
        if city:
            self.validate_type(city)
        elif station_code:
            self.validate_type(station_code)
        else:
            raise Exception("argument can not be empty")

    def validate_type(self, p):
        if not isinstance(p, str):
            raise Exception("argument can only be string")

    def validate_params(self, p, l):
        if p:
            p_str = '%s' % p
            if p_str.lower() not in l:
                raise Exception("Parameter %s is invalid! It can only be %s or %s" % (p, l[0], l[1]))

    def __base_get(self, params):
        url = self._base_url % self.interface
        try:
            r = requests.get(url, params=params)
            return r.json()
        except RequestException:
            raise NetworkException

    def __get(self, **p):
        self.interface = p.get('interface')
        self.params = p
        return self.__base_get(self.params)

    def get_pm25(self, city, avg='true', stations='yes'):
        return self.__get(city=city, avg=avg, stations=stations, interface='/pm2_5')

    def get_pm10(self, city, avg='true', stations='yes'):
        return self.__get(city=city, avg=avg, stations=stations, interface='/pm10')

    def get_co(self, city, avg='true', stations='yes'):
        return self.__get(city=city, avg=avg, stations=stations, interface='/co')

    def get_no2(self, city, avg='true', stations='yes'):
        return self.__get(city=city, avg=avg, stations=stations, interface='/no2')

    def get_so2(self, city, avg='true', stations='yes'):
        return self.__get(city=city, avg=avg, stations=stations, interface='/so2')

    def get_o3(self, city, avg='true', stations='yes'):
        return self.__get(city=city, avg=avg, stations=stations, interface='/o3')

    def get_aqi_details(self, city, avg='true', stations='yes'):
        return self.__get(city=city, avg=avg, stations=stations, interface='/aqi_details')

    def get_only_aqi(self, city, avg='true', stations='yes'):
        return self.__get(city=city, avg=avg, stations=stations, interface='/only_aqi')

    def get_aqis_by_station(self, station_code):
        return self.__get(station_code=station_code, interface='/aqis_by_station')

    def get_station_names(self, city):
        self.interface = '/station_names'
        return self.__get(city=city, interface='/station_names')

    def get_cities(self):
        self.interface = ''
        self.params = None
        return self.__base_get(self.params)

    def get_all_cities(self):
        self.interface = '/all_cities'
        self.params = None
        return self.__base_get(self.params)

    def get_aqi_ranking(self):
        self.interface = '/aqi_ranking'
        self.params = None
        return self.__base_get(self.params)
