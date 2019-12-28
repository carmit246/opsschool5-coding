import json


def get_data():  # Read the json file and return 2 data dictionaries
    with open('hw.json') as input_file:
        data = json.load(input_file)
    people = data["ppl_ages"]
    buckets = data["buckets"]
    buckets.sort()
    return people, buckets


def create_buckets(buckets, minimum, maximum):  # Calculate age ranges and return buckets dictionary with ranges keys
    t = {}
    for bucket_age in buckets:
        age_range = str(minimum) + "-" + str(bucket_age)
        t[age_range] = []
        minimum = bucket_age+1
    last_range = str(buckets[-1]+1) + "-" + str(maximum)
    t[last_range] = []
    result = dict(t)
    return result


def get_max_age(people):  # Return the maximum age
    max_age = max(zip(people.values(), people.keys()))[0]
    maximum_age = int(max_age)
    return maximum_age


def group_people_by_age(people,result):  # group the people names by bucket ranges, return list of name for every range
    for person,age in people.items():
        for key in result:
            if int(age) >= int(key.split('-')[0]) and int(age) < int(key.split('-')[1]):
                result[key].append(person)
    return result


def print_result(result):  # Print the result in yml format
    print("---")
    for key,value in result.items():
        print("-  " +key + ":")
        for pers in value:
            print("  -  " + pers)


def main():
    minimum_age = 0
    people, buckets = get_data()
    maximum_age = get_max_age(people)
    result = create_buckets(buckets, minimum_age, maximum_age)
    result = group_people_by_age(people, result)
    print_result(result)


if __name__ == '__main__':
    main()