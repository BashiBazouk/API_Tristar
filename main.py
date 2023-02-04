# imports
import requests
import json
import matplotlib.pyplot
import time
import numpy as np
from cWeather_Stations import Weather_Station

# hardcoding
# links

# Tristar :
stations = 'http://api.zdiz.gdynia.pl/ri/rest/weather_stations'
weather_at_station = 'http://api.zdiz.gdynia.pl/ri/rest/weather_station_data?weatherStationId='

def Check_api_status(api_adress):
    '''check response type of api and returns status'''

    try:
        response = requests.get(api_adress)
        response.raise_for_status()
        status_Code = response.status_code
        status_Continue = True
        # TODO what else this should return? go/nogo

    except requests.exceptions.HTTPError as errh:
        status_Code = errh
        status_Continue = False
        
    except requests.exceptions.ConnectionError as errc:
        status_Code = errc
        status_Continue = False
        
    except requests.exceptions.Timeout as errt:
        status_Code = errt
        status_Continue = False
        
    except requests.exceptions.RequestException as err:
        status_Code = err
        status_Continue = False

    return status_Code, status_Continue


def ListaStacji():
    # TODO rename function? 
    # get list of stations
    print('script start')
    # start = time.time()
    response = requests.get(stations)
    data = response.json()
    print(response.status_code)
    # store data in json
    # with open('json_data.json', 'w') as outfile:
    #     json.dump(data, outfile)

    # weather_stations = []

    # for station in range(len(data['weatherStations'])):
    #     Weather_Station.id = data['weatherStations'][station]['id']
    #     weather_stations.append(Weather_Station)
    #     # print(data['weatherStations'][station]['id'])
    #     # print(data['weatherStations'][station]['code'])
    #     # print(data['weatherStations'][station]['street'])
    #     # print(data['weatherStations'][station]['id'])
    #     # print(data['weatherStations'][station]['location']['coordinates'])
    #     # print(data['weatherStations'][station]['lastUpdate'])
    
    # print(weather_stations[1].id)
    # print('json acquired')

    # add info to class Weather_Stations

def get_sensors_data(id):
    start = time.time()
    data_request = weather_at_station +str(id)
    response = requests.get(data_request)
    data = response.json() # result is list of dictionaries
    # https://pythonexamples.org/python-list-of-dictionaries/

    #just some measuring how long it takes to get all data
    print(f'get sensor data took {round((time.time() - start),2)}') 

    # list of lists
    airTemperature_list = []
    surfaceTemperature_list = []
    foundationTemperature_list = []
    dewPoint_list = []
    measureTime_list = []

    # filling lists
    for measurement in range(len(data)):
        airTemperature_list.append(data[measurement]['airTemperature'])
        surfaceTemperature_list.append(data[measurement]['surfaceTemperature'])
        foundationTemperature_list.append(data[measurement]['foundationTemperature'])
        dewPoint_list.append(data[measurement]['dewPoint'])
        measureTime_list.append(data[measurement]['measureTime'])

    # matplotlib.pyplot.plot_date(measureTime_list, airTemperature_list)
    # fix too many ticks: https://matplotlib.org/stable/gallery/ticks/ticks_too_many.html
    x = np.asarray(measureTime_list, dtype='datetime64[s]')
    matplotlib.pyplot.plot_date(x, airTemperature_list, label='Air Temperature')
    matplotlib.pyplot.plot_date(x, surfaceTemperature_list, label= 'Surface Temperature')
    matplotlib.pyplot.plot_date(x, foundationTemperature_list, label= 'Foundation Temperature')
    matplotlib.pyplot.plot_date(x, dewPoint_list, label= 'Dew Point')
    matplotlib.pyplot.legend()
    matplotlib.pyplot.grid(True)
    matplotlib.pyplot.show()

    #np.asarray(x, float)
    # param_list = []
    # param_id = []

    # for parameters in range(len(data)):
    #     param_list.append(data[parameters]['param']['paramName'])
    #     param_id.append(data[parameters]['id'])

    # measurement_values = []
    # measurement_times = []
    # for id in param_id:
    #     measurement_time, measurement_value = get_parameteres_data(id)
    #     measurement_values.append(measurement_value)
    #     measurement_times.append(measurement_time)

    # text = ""
    # for item in range(len(param_list)):
    #     text = text  + f'{param_list[item]} : \t {measurement_values[item]} measured at: \t {measurement_times[item]}<br>'
    
    
    # return text

def get_parameteres_data(id):
    start = time.time()
    data_request = data_from_sensor + str(id)

    response = requests.get(data_request)
    data = response.json()
    # print(data)
    try:
        measurement_time = data['values'][0]['date']
    except TypeError:
        measurement_time = 'n/a'
    except IndexError:
        measurement_time = 'n/a'
    try:
        measurement_value = data['values'][0]['value']
    except TypeError:
        measurement_value = 'n/a'
    except IndexError:
        measurement_value = 'n/a'

    # print(measurement_value, measurement_time)
    print(f'get parameters data took {round((time.time() - start),2)}')
    return measurement_time,  measurement_value



if __name__ == '__main__':
    
    Check_api_status(stations)
    # ListaStacji()

    #just some testing `<br>
    # get_sensors_data(5)
    # get_parameteres_data(10120)

