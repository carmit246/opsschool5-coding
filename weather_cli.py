import click
import json
import sys
from requests import get


def get_data(token, city):
    url = "http://api.weatherstack.com/current?access_key={}&query={}".format(token, city)
    rest_result = get(url)
    return rest_result.json()


def get_multiple_arguments(token, cities, degree):
    return click.echo(token), click.echo(cities), click.echo(degree)


def celsius_to_fehrenheit(current_temp):
    return (float(current_temp) * 1.8) + 32


def result_by_degree(city, current_temp, degrees):
    if degrees == "F":
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


@click.command()
@click.option("--token", prompt=True)
@click.option("--cities", prompt=True)
@click.option('-t', "--degree")
def cli(token, cities, degree):
    cities_arr = cities.split(",")
    for city in cities_arr:
        json_result = get_data(token, city)
        if check_result(json_result):
            current_temp = (json_result['current']['temperature'])
            result = current_temp = result_by_degree(city, current_temp, degree)
            print(result)
        else:
            print_error(city)


if __name__ == '__main__':
    cli()
