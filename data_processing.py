import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)
def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps

def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = []
    for item in dict_list:
        try:
            temps.append(float(item[aggregation_key]))
        except ValueError:
            temps.append(item[aggregation_key])
    return aggregation_function(temps)


# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

print("All cities in Germany")
filtered_list = filter(lambda x: x["country"]  == "Germany", cities)
germany = aggregate('city', lambda x: x, filtered_list)
print(germany)
print()

# Print all cities in Spain with a temperature above 12°C

print("All cities in Spain with a temperature above 12°C")
filtered_list = filter(lambda x: x["country"] == "Spain", cities)
spain_above12 = filter(lambda x: float(x['temperature']) > 12 ,filtered_list)
city_only = aggregate('city', lambda x: x, spain_above12)
print(city_only)
print()
# Count the number of unique countries

print("Number of unique countires")
all_count = aggregate('country', lambda x:x,cities)
all_count = set(all_count)
print(len(all_count))
print()
# Print the average temperature for all the cities in Germany

print("Average temperature for all the cities in Germany")
germany = filter(lambda x:x["country"] == "Germany",cities)
avg = aggregate('temperature',lambda x:sum(x)/len(x),germany)
print(avg)
print()
# Print the max temperature for all the cities in Italy

print("Max temperature for all the cities in Italy")
ita = filter(lambda x:x['country'] == "Italy",cities)
ita_max = aggregate('temperature',lambda x:max(x),ita)
print(ita_max)
print()
