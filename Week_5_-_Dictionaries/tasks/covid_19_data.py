from pprint import pprint

dataset = {
    "countries": {
        "Nigeria": {
            "population": 5000000,
            "total_cases": 250000,
            "active_cases": 16500,
            "deaths": 3500,
            "recoveries": 230000,
            "testing": 1200000,
            "vaccination": {
                "first_dose": 3500000,
                "fully_vaccinated": 3200000,
                "boosters": 1800000
            },
            "monthly_cases": {
                "Jan": 45000,
                "Feb": 32000,
                "Mar": 25000,
                "Apr": 18000,
                "May": 15000,
                "Jun": 10000
            }
        },
        "Ghana": {
            "population": 8000000,
            "total_cases": 420000,
            "active_cases": 23800,
            "deaths": 6200,
            "recoveries": 390000,
            "testing": 1900000,
            "vaccination": {
                "first_dose": 5100000,
                "fully_vaccinated": 4800000,
                "boosters": 2500000
            },
            "monthly_cases": {
                "Jan": 80000,
                "Feb": 65000,
                "Mar": 40000,
                "Apr": 25000,
                "May": 12000,
                "Jun": 8000
            }
        },
        "England": {
            "population": 3000000,
            "total_cases": 180000,
            "active_cases": 5900,
            "deaths": 2100,
            "recoveries": 172000,
            "testing": 950000,
            "vaccination": {
                "first_dose": 2100000,
                "fully_vaccinated": 1950000,
                "boosters": 900000
            },
            "monthly_cases": {
                "Jan": 35000,
                "Feb": 30000,
                "Mar": 20000,
                "Apr": 12000,
                "May": 8000,
                "Jun": 5000
            }
        },
        "Kenya": {
            "population": 6500000,
            "total_cases": 350000,
            "active_cases": 15200,
            "deaths": 4800,
            "recoveries": 330000,
            "testing": 1600000,
            "vaccination": {
                "first_dose": 3900000,
                "fully_vaccinated": 3500000,
                "boosters": 1600000
            },
            "monthly_cases": {
                "Jan": 70000,
                "Feb": 50000,
                "Mar": 35000,
                "Apr": 20000,
                "May": 10000,
                "Jun": 5000
            }
        }
    },
    "global": {
        "total_cases": 1200000,
        "active_cases": 61400,
        "total_deaths": 16600,
        "total_recoveries": 1122000,
        "total_vaccines_distributed": 25000000
    },
    "variants": {
        "Alpha": {"first_detected": "Sep 2020", "transmissibility": "Medium"},
        "Beta": {"first_detected": "Oct 2020", "transmissibility": "Medium"},
        "Delta": {"first_detected": "Dec 2020", "transmissibility": "High"},
        "Omicron": {"first_detected": "Nov 2021", "transmissibility": "Very High"}
    }
}

# Task 1
# Find the country with the highest number of active cases

highest_active_cases = 0
country_name = None

for country, data in dataset["countries"].items():
    if data["active_cases"] > highest_active_cases:
        highest_active_cases = data["active_cases"]
        country_name = country

print(f"\nThe country with the highest active COVID-19 cases is {country} with {highest_active_cases:,} cases.")


# Task 2
#  Calculate the ratio of active cases to population for each country

active_cases_ratio = {}

for country, data in dataset["countries"].items():
    active_cases = data["active_cases"]
    population = data["population"]

    country_case_ratio = (active_cases / population) * 100

    active_cases_ratio[country] = round(country_case_ratio, 2)


print("\n***************************** RATIO OF ACTIVE CASES TO POPULATION *****************************")
pprint(active_cases_ratio)

# Task 3
#  Find the country with the highest recovery rate (recoveries/total_cases)

# DRY Principle
# Do not Repeat Yourself

highest_recovery_rate = 0
country_with_highest_recovery = None

country_recovery_rate = {}

for country, data in dataset["countries"].items():
    recovery_rate = data["recoveries"] / data["total_cases"]

    country_recovery_rate[country] = f"{recovery_rate:.2f}"

    if recovery_rate > highest_recovery_rate:
        highest_recovery_rate = recovery_rate
        country_with_highest_recovery = country


highest_recovery_rate = highest_recovery_rate * 100

print(f"\nCountry with highest recovery rate: {country_with_highest_recovery} with {highest_recovery_rate:.2f}%")

print("")
print(country_recovery_rate)

#  Task 9
#  Calculate what percentage of global active cases each country represents. Represent the result as a dictionary.

percentages = {}

for country, data in dataset["countries"].items():
    percentage_active_cases = (data["active_cases"] / dataset["global"]["active_cases"]) * 100
    percentages[country] = f"{round(percentage_active_cases, 2)}%"

print("\nPercentage of global active cases for each country")
pprint(percentages)