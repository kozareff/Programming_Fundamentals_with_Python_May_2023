countries = input().split(", ")
capitals = input().split(", ")

information = dict(zip(countries, capitals))
for country, capital in information.items():
    print(f"{country} -> {capital}")