import json
import sys
from requests import get


def get_data(city):
    token_file = open('token.txt')
    token = token_file.read()
    url = "http://api.weatherstack.com/current?access_key={}{}".format(token, city)
    rest_result = get(url)
    return rest_result.json()


def get_multiple_arguments():
    if len(sys.argv) < 3:
        print("usage: weather.pl <city list-comma separated> <degrees:-s|-f>.\n Example: weather.py Paris,London -f")
        sys.exit(1)
    if sys.argv[2] != '-f' and sys.argv[2] != '-c':
        print("usage: weather.pl <city list-comma separated> <degrees:-s|-f>.\n Example: weather.py Paris,London -f")
        sys.exit(1)
    cities = sys.argv[1].split(',')
    degrees = sys.argv[2]
    return cities, degrees


def celsius_to_fehrenheit(current_temp):
    return (float(current_temp) * 1.8) + 32


def result_by_degree(city, current_temp, degrees):
    if degrees == "-f":
        current_temp = celsius_to_fehrenheit(current_temp)
        result = "The weather in {} today is {} Fahrenheit.".format(city, current_temp)
    else:
        result = "The weather in {} today is {} celsius.".format(city, current_temp)
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


