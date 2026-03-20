

population = 1000
growth_rate = 0.02
years = 10

for year in range(1, years + 1):
    population = int(population * (1 + growth_rate))
    print(f"Year {year}: {population}")