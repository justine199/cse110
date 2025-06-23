
# Life Expectancy Analyzer
# Creative addition: User can type a country name to view its min, max, and average life expectancy

filename = "life-expectancy.csv"

# Initialize tracking variables for global stats
max_life = -1
min_life = 999
max_life_country = ""
max_life_year = ""
min_life_country = ""
min_life_year = ""

# To store data in memory
all_data = []

# Load and parse the file
with open("life-expectancy.csv") as file:
    next(file)  # Skip the header
    for line in file:
        parts = line.strip().split(',')
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        
        # Save data for later queries
        all_data.append({
            "country": country,
            "year": year,
            "life": life_expectancy
        })

        # Global min/max tracking
        if life_expectancy > max_life:
            max_life = life_expectancy
            max_life_country = country
            max_life_year = year

        if life_expectancy < min_life:
            min_life = life_expectancy
            min_life_country = country
            min_life_year = year

# Display global stats
print(f"The overall max life expectancy is: {max_life} from {max_life_country} in {max_life_year}")
print(f"The overall min life expectancy is: {min_life} from {min_life_country} in {min_life_year}")

# Prompt for year of interest
year_input = int(input("\nEnter the year of interest: "))
year_life_total = 0
year_count = 0
year_max = -1
year_min = 999
year_max_country = ""
year_min_country = ""

for record in all_data:
    if record["year"] == year_input:
        life = record["life"]
        country = record["country"]

        year_life_total += life
        year_count += 1

        if life > year_max:
            year_max = life
            year_max_country = country
        if life < year_min:
            year_min = life
            year_min_country = country

if year_count > 0:
    year_avg = round(year_life_total / year_count, 2)
    print(f"\nFor the year {year_input}:")
    print(f"The average life expectancy across all countries was {year_avg}")
    print(f"The max life expectancy was in {year_max_country} with {year_max}")
    print(f"The min life expectancy was in {year_min_country} with {year_min}")
else:
    print(f"No data found for year {year_input}")

# Optional creative feature: Country-specific stats
country_input = input("\nOptional: Enter a country to view stats or press enter to exit: ").strip()
if country_input:
    country_life = []
    for record in all_data:
        if record["country"].lower() == country_input.lower():
            country_life.append(record["life"])
    
    if country_life:
        avg_country = round(sum(country_life) / len(country_life), 2)
        print(f"\n{country_input.title()} stats:")
        print(f"Max: {max(country_life)}")
        print(f"Min: {min(country_life)}")
        print(f"Average: {avg_country}")
    else:
        print(f"No data found for {country_input}")
