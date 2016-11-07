import unittest
from aqizh.aqi import AQI, NetworkException
import json
from httmock import all_requests, HTTMock
from requests.exceptions import RequestException


class TestAQI(unittest.TestCase):

    def setUp(self):
        print('--------Test Start------')
        self.base_url = 'www.pm25.in'
        self.path = '/api/querys%s.json'
        self.token = 'dummy_token'
        self.aqi = AQI(self.token)

    def tearDown(self):
        print('--------Test Done-------')

    def test_token_missing(self):
        with self.assertRaises(TypeError):
            AQI()

    # test for get_pm25()
    def test_pm25_city_empty(self):
        with self.assertRaises(Exception):
            self.aqi.get_pm25('')

    def test_pm25_wrong_avg(self):
        with self.assertRaises(Exception):
            self.aqi.get_pm25('Beijing', True)

    def test_pm25_wrong_stations(self):
        with self.assertRaises(Exception):
            self.aqi.get_pm25('Beijing', "true", 'a')

    @all_requests
    def pm25_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '/pm2_5')
        querys = url.query.split('&')
        args = {}
        for q in querys:
            kv = q.split('=')
            args[kv[0]] = kv[1]
        self.assertEqual(args.get('city'), 'Beijing')
        self.assertEqual(args.get('avg'), 'true')
        self.assertEqual(args.get('stations'), 'yes')
        self.assertEqual(args.get('token'), self.token)
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    @all_requests
    def failure_mock(self, url, request):
        raise RequestException

    def test_pm25(self):
        with HTTMock(self.pm25_response_content):
            self.aqi.get_pm25('Beijing')

    def test_pm25_fail(self):
        with self.assertRaises(NetworkException):
            with HTTMock(self.failure_mock):
                self.aqi.get_pm25('Beijing')

    # test for get_pm10()
    def test_pm10_city_empty(self):
        with self.assertRaises(Exception):
            self.aqi.get_pm10('')

    def test_pm10_wrong_avg(self):
        with self.assertRaises(Exception):
            self.aqi.get_pm10('Beijing', True)

    def test_pm10_wrong_stations(self):
        with self.assertRaises(Exception):
            self.aqi.get_pm10('Beijing', "true", 'a')

    @all_requests
    def pm10_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '/pm10')
        querys = url.query.split('&')
        args = {}
        for q in querys:
            kv = q.split('=')
            args[kv[0]] = kv[1]
        self.assertEqual(args.get('city'), 'Beijing')
        self.assertEqual(args.get('avg'), 'false')
        self.assertEqual(args.get('stations'), 'no')
        self.assertEqual(args.get('token'), self.token)
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    def test_pm10(self):
        with HTTMock(self.pm10_response_content):
            self.aqi.get_pm10('Beijing', 'false', 'no')

    # test for get_co()
    def test_co_city_empty(self):
        with self.assertRaises(Exception):
            self.aqi.get_co('')

    def test_co_wrong_avg(self):
        with self.assertRaises(Exception):
            self.aqi.get_co('Beijing', True)

    def test_co_wrong_stations(self):
        with self.assertRaises(Exception):
            self.aqi.get_co('Beijing', "true", 'a')

    @all_requests
    def co_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '/co')
        querys = url.query.split('&')
        args = {}
        for q in querys:
            kv = q.split('=')
            args[kv[0]] = kv[1]
        self.assertEqual(args.get('city'), 'Beijing')
        self.assertEqual(args.get('avg'), 'false')
        self.assertEqual(args.get('stations'), 'no')
        self.assertEqual(args.get('token'), self.token)
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    def test_co(self):
        with HTTMock(self.co_response_content):
            self.aqi.get_co('Beijing', 'false', 'no')

    # test for get_no2()
    def test_no2_city_empty(self):
        with self.assertRaises(Exception):
            self.aqi.get_no2('')

    def test_no2_wrong_avg(self):
        with self.assertRaises(Exception):
            self.aqi.get_no2('Beijing', True)

    def test_no2_wrong_stations(self):
        with self.assertRaises(Exception):
            self.aqi.get_no2('Beijing', "true", 'a')

    @all_requests
    def no2_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '/no2')
        querys = url.query.split('&')
        args = {}
        for q in querys:
            kv = q.split('=')
            args[kv[0]] = kv[1]
        self.assertEqual(args.get('city'), 'Beijing')
        self.assertEqual(args.get('avg'), 'false')
        self.assertEqual(args.get('stations'), 'no')
        self.assertEqual(args.get('token'), self.token)
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    def test_no2(self):
        with HTTMock(self.no2_response_content):
            self.aqi.get_no2('Beijing', 'false', 'no')

    # test for get_so2()
    def test_so2_city_empty(self):
        with self.assertRaises(Exception):
            self.aqi.get_so2('')

    def test_so2_wrong_avg(self):
        with self.assertRaises(Exception):
            self.aqi.get_so2('Beijing', True)

    def test_so2_wrong_stations(self):
        with self.assertRaises(Exception):
            self.aqi.get_so2('Beijing', "true", 'a')

    @all_requests
    def so2_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '/so2')
        querys = url.query.split('&')
        args = {}
        for q in querys:
            kv = q.split('=')
            args[kv[0]] = kv[1]
        self.assertEqual(args.get('city'), 'Beijing')
        self.assertEqual(args.get('avg'), 'false')
        self.assertEqual(args.get('stations'), 'no')
        self.assertEqual(args.get('token'), self.token)
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    def test_so2(self):
        with HTTMock(self.so2_response_content):
            self.aqi.get_so2('Beijing', 'false', 'no')

    # test for get_o3()
    def test_o3_city_empty(self):
        with self.assertRaises(Exception):
            self.aqi.get_o3('')

    def test_o3_wrong_avg(self):
        with self.assertRaises(Exception):
            self.aqi.get_o3('Beijing', True)

    def test_o3_wrong_stations(self):
        with self.assertRaises(Exception):
            self.aqi.get_o3('Beijing', "true", 'a')

    @all_requests
    def o3_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '/o3')
        querys = url.query.split('&')
        args = {}
        for q in querys:
            kv = q.split('=')
            args[kv[0]] = kv[1]
        self.assertEqual(args.get('city'), 'Beijing')
        self.assertEqual(args.get('avg'), 'false')
        self.assertEqual(args.get('stations'), 'no')
        self.assertEqual(args.get('token'), self.token)
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    def test_o3(self):
        with HTTMock(self.o3_response_content):
            self.aqi.get_o3('Beijing', 'false', 'no')

    # test for get_aqi_details()
    def test_aqi_details_city_empty(self):
        with self.assertRaises(Exception):
            self.aqi.get_aqi_details('')

    def test_aqi_details_wrong_avg(self):
        with self.assertRaises(Exception):
            self.aqi.get_aqi_details('Beijing', True)

    def test_aqi_details_wrong_stations(self):
        with self.assertRaises(Exception):
            self.aqi.get_aqi_details('Beijing', "true", 'a')

    @all_requests
    def aqi_details_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '/aqi_details')
        querys = url.query.split('&')
        args = {}
        for q in querys:
            kv = q.split('=')
            args[kv[0]] = kv[1]
        self.assertEqual(args.get('city'), 'Beijing')
        self.assertEqual(args.get('avg'), 'false')
        self.assertEqual(args.get('stations'), 'no')
        self.assertEqual(args.get('token'), self.token)
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    def test_aqi_details(self):
        with HTTMock(self.aqi_details_response_content):
            self.aqi.get_aqi_details('Beijing', 'false', 'no')

    # test for get_only_aqi()
    def test_only_aqi_city_empty(self):
        with self.assertRaises(Exception):
            self.aqi.get_only_aqi('')

    def test_only_aqi_wrong_avg(self):
        with self.assertRaises(Exception):
            self.aqi.get_only_aqi('Beijing', True)

    def test_only_aqi_wrong_stations(self):
        with self.assertRaises(Exception):
            self.aqi.get_only_aqi('Beijing', "true", 'a')

    @all_requests
    def only_aqi_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '/only_aqi')
        querys = url.query.split('&')
        args = {}
        for q in querys:
            kv = q.split('=')
            args[kv[0]] = kv[1]
        self.assertEqual(args.get('city'), 'Beijing')
        self.assertEqual(args.get('avg'), 'false')
        self.assertEqual(args.get('stations'), 'no')
        self.assertEqual(args.get('token'), self.token)
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    def test_only_aqi(self):
        with HTTMock(self.only_aqi_response_content):
            self.aqi.get_only_aqi('Beijing', 'false', 'no')

    # test for get_aqis_by_station()
    def test_aqis_by_station_empty(self):
        with self.assertRaises(Exception):
            self.aqi.get_aqis_by_station('')

    @all_requests
    def aqis_by_station_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '/aqis_by_station')
        querys = url.query.split('&')
        args = {}
        for q in querys:
            kv = q.split('=')
            args[kv[0]] = kv[1]
        self.assertEqual(args.get('station_code'), '1367A')
        self.assertEqual(args.get('token'), self.token)
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    def test_aqis_by_station(self):
        with HTTMock(self.aqis_by_station_response_content):
            self.aqi.get_aqis_by_station('1367A')

    # test for get_station_names()
    def test_station_names_city_empty(self):
        with self.assertRaises(Exception):
            self.aqi.get_station_names('')

    @all_requests
    def station_names_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '/station_names')
        querys = url.query.split('&')
        args = {}
        for q in querys:
            kv = q.split('=')
            args[kv[0]] = kv[1]
        self.assertEqual(args.get('city'), 'Beijing')
        self.assertEqual(args.get('token'), self.token)
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    def test_station_names(self):
        with HTTMock(self.station_names_response_content):
            self.aqi.get_station_names('Beijing')

    # test for get_cities()
    @all_requests
    def cities_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '')
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    def test_cities(self):
        with HTTMock(self.cities_response_content):
            self.aqi.get_cities()

    # test for get_all_cities()
    @all_requests
    def all_cities_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '/all_cities')
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    def test_all_cities(self):
        with HTTMock(self.all_cities_response_content):
            self.aqi.get_all_cities()

    # test for get_aqi_ranking()
    @all_requests
    def aqi_ranking_response_content(self, url, request):
        self.assertEqual(url.path, self.path % '/aqi_ranking')
        return json.dumps({'status_code': 200, 'content': 'some thing'})

    def test_aqi_ranking(self):
        with HTTMock(self.aqi_ranking_response_content):
            self.aqi.get_aqi_ranking()


if __name__ == '__main__':
    unittest.main()
