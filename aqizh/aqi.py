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
            station_code = p.get('station_code')
            city = p.get('city')
            self.validate_compulsory(city, station_code)
            avg = p.get('avg')
            self.validate_avg(avg)
            stations = p.get('stations')
            self.validate_stations(stations)
            self._params.update(p)

    def validate_compulsory(self, city, station_code):
        if not station_code and not city:
            raise Exception("argument can not be empty")
        if city and not isinstance(city, str):
            raise Exception("argument can only be string")
        if station_code and not isinstance(station_code, str):
            raise Exception("argument can only be string")


    def validate_avg(self, avg):
        if avg :
            avg_s = '%s' % avg
            if avg_s.lower() not in ['true', 'false']:
                raise Exception("avg can only be true or false")

    def validate_stations(self, stations):
        if stations:
            stations_s = '%s' % stations
            if stations_s.lower() not in ['yes', 'no']:
                raise Exception("avg can only be yes or no")

    def __get(self, params):
        url = self._base_url % self.interface
        try:
            r = requests.get(url, params=params)
            return r.json()
        except RequestException:
            raise NetworkException

    def get_pm25(self, city, avg='true', stations='yes'):
        self.interface = '/pm2_5'
        self.params = {'city': city, 'avg': avg, 'stations': stations}
        return self.__get(self.params)

    def get_pm10(self, city, avg='true', stations='yes'):
        self.interface = '/pm10'
        self.params = {'city': city, 'avg': avg, 'stations': stations}
        return self.__get(self.params)

    def get_co(self, city, avg='true', stations='yes'):
        self.interface = '/co'
        self.params = {'city': city, 'avg': avg, 'stations': stations}
        return self.__get(self.params)

    def get_no2(self, city, avg='true', stations='yes'):
        self.interface = '/no2'
        self.params = {'city': city, 'avg': avg, 'stations': stations}
        return self.__get(self.params)

    def get_so2(self, city, avg='true', stations='yes'):
        self.interface = '/so2'
        self.params = {'city': city, 'avg': avg, 'stations': stations}
        return self.__get(self.params)

    def get_o3(self, city, avg='true', stations='yes'):
        self.interface = '/o3'
        self.params = {'city': city, 'avg': avg, 'stations': stations}
        return self.__get(self.params)

    def get_aqi_details(self, city, avg='true', stations='yes'):
        self.interface = '/aqi_details'
        self.params = {'city': city, 'avg': avg, 'stations': stations}
        return self.__get(self.params)

    def get_only_aqi(self, city, avg='true', stations='yes'):
        self.interface = '/only_aqi'
        self.params = {'city': city, 'avg': avg, 'stations': stations}
        return self.__get(self.params)

    def get_aqis_by_station(self, station_code):
        self.interface = '/aqis_by_station'
        self.params = {'station_code': station_code}
        return self.__get(self.params)

    def get_station_names(self, city):
        self.interface = '/station_names'
        self.params = {'city': city}
        return self.__get(self.params)

    def get_cities(self):
        self.interface = ''
        self.params = None
        return self.__get(self.params)

    def get_all_cities(self):
        self.interface = '/all_cities'
        self.params = None
        return self.__get(self.params)

    def get_aqi_ranking(self):
        self.interface = '/aqi_ranking'
        self.params = None
        return self.__get(self.params)
