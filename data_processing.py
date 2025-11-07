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
for i in cities:
    if i["country"].lower() == "germany":
        print(f"-{i["city"]}")
print()

# Print all cities in Spain with a temperature above 12°C
print('All cities in Spain with a temperature above 12°C')
for i in cities:
    if i["country"].lower() == "spain" and float(i["temperature"])>12:
        print(f"-i{["city"]}")
print()

# Count the number of unique countries
print('Number of unique countries')
con=[]
for i in cities:
    if i["country"] not in con:
        con.append(i["country"])
    else:
        continue
print(len(con))
print()

# Print the average temperature for all the cities in Germany
print('Average temperature for all the cities in Germany')
count = 0
sum = 0
for i in cities:
    if i['country'].lower() == "germany":
        count+=1
        sum += float(i['temperature'])
    else:
        continue
avg = sum/count
print(avg)
print()

# Print the max temperature for all the cities in Italy
print('Max temperature for all the cities in Italy')
rec = []
for i in cities:
    if i['country'].lower() == 'italy':
        rec.append(i['country'])
    else:
        continue
print(max(rec))
print()

