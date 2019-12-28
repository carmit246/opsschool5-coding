import json
import sys
from requests import get


def get_data(city):
    url = "http://api.weatherstack.com/current?access_key=605428999402e46807e8cb3b93e67c7b&query=" + city
    rest_result = get(url)
    return rest_result.json()


def get_multiple_arguments():
    cities = sys.argv[1].split(',')
    degrees = sys.argv[2]
    return cities, degrees


def celsius_to_fehrenheit(current_temp):
    return (float(current_temp) * 1.8) + 32


def result_by_degree(city, current_temp, degrees):
    if degrees == "f":
        current_temp = celsius_to_fehrenheit(current_temp)
        result = "The weather in " + city + " today " + str(int(current_temp)) + " Fahrenheit."
    else:
        result = "The weather in " + city + " today " + str(current_temp) + " celsius."
    return result


def check_result(json_result):
    if 'current' in json_result:
        return True
    else:
        return False


def print_error(city):
    print("city " + city + " does not exist. please enter legal city like London,Dublin,Paris etc..")


def main():
    cities, degrees = get_multiple_arguments()
    for city in cities:
        json_result = get_data(city)
        if check_result(json_result):
            current_temp = (json_result['current']['temperature'])
            result = current_temp = result_by_degree(city, current_temp, degrees)
            print(result)
        else:
            print_error(city)


if __name__ == '__main__':
    main()


