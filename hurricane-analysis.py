# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# Function to convert strings into numerical updated values and storing them in a new list
def update_damages(damages_list):
    updated_damages = []
    for data in damages_list:
        if data == 'Damages not recorded':
            updated_damages.append('Damages not recorded')
        else:
            # Separate the number from the unit (M or B)
            value = float(data[:-1])  # Extract number part
            unit = data[-1]  # Extract 'M' or 'B'
            # Convert based on the unit
            updated_damages.append(value * conversion[unit])
    
    return updated_damages  # Return after the loop completes


testing_function = update_damages(damages)
print(testing_function)

# 2 
# Creating a Table
# Create and view the hurricanes dictionary
def create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, deaths):
    hurricane_dict = {}
    for i in range(len(names)):
        # Creating a dictionary for each hurricane with all its data
        hurricane_info = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Deaths': deaths[i]
        }
        # Adding the hurricane's data to the main dictionary using the name as the key
        hurricane_dict[names[i]] = hurricane_info
    return hurricane_dict

# Test the function with example data
hurricane_data = create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, deaths)

# Print the result
for name, info in hurricane_data.items():
    print(f"{name}: {info}")
        

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def organize_hurricanes_by_year(hurricane_dict):
    hurricanes_by_year = {}

    for hurricane_name, info in hurricane_dict.items():
        # Extract the year
        year = info['Year']
        # Organizing by year
        if year not in hurricanes_by_year:
            # If the year is not already in the new dictionary, initialize a new empty list
            hurricanes_by_year[year] = []
        
        # Append the hurricane's info to the list for the given year
        hurricanes_by_year[year].append(info)
        
    return hurricanes_by_year

# Test the function with your hurricane data
hurricanes_by_year = organize_hurricanes_by_year(hurricane_data)

# Print the hurricanes organized by year to verify
for year, hurricanes in hurricanes_by_year.items():
    print(f"Year {year}:")
    for hurricane in hurricanes:
        print(hurricane)


# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def count_affected_areas(area_list):
    affected_areas_dict = {}
    # Looping through the list
    for group in area_list:
        # Looping through the list inside the main list
        for area in group:
            # Add 1 if area is already in the list
            if area in affected_areas_dict:
                affected_areas_dict[area] += 1
            # Add the area if it's not in the list
            else:
                affected_areas_dict[area] = 1
    
    return affected_areas_dict

# Testing
affected_areas_count = count_affected_areas(areas_affected)
print(affected_areas_count)


# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def find_most_affected_area(affected_areas_dict):
    # Find the area with the maximum count
    max_area = max(affected_areas_dict, key=affected_areas_dict.get)
    max_count = affected_areas_dict[max_area]
    return max_area, max_count

# Testing the function on the affected areas dictionary
most_area, hit_count = find_most_affected_area(affected_areas_count)

print(f"The area affected by the most hurricanes is {most_area}, which was hit {hit_count} times.")

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def find_deadliest_hurricane(hurricane_dict):
    deadliest_hurricane = None
    max_deaths = 0

    # Looping through each hurricane in the dictionary
    for hurricane_name, hurricane_data in hurricane_dict.items():
        # Accessing the number of deaths caused by the current hurricane
        deaths = hurricane_data['Deaths']

        # Check if this hurricane caused more deaths than the current maximum
        if deaths > max_deaths:
            max_deaths = deaths
            deadliest_hurricane = hurricane_name
    
    # Return the name of the deadliest hurricane and the number of deaths
    return deadliest_hurricane, max_deaths

# Testing
deadliest_name, max_deaths = find_deadliest_hurricane(hurricane_data)
print(f"The deadliest hurricane is {deadliest_name} with {max_deaths} deaths.")


# 7
# Rating Hurricanes by Mortality

# categorize hurricanes in new dictionary with mortality severity as key
def rate_hurricanes_by_mortality(hurricane_dict):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    # Initializing a dictionary to store hurricanes by mortality rating
    hurricanes_by_mortality = {rating: [] for rating in mortality_scale}
    
    # Looping through each hurricane in the dictionary
    for hurricane_name, hurricane_data in hurricane_dict.items():
        # Access the number of deaths
        deaths = hurricane_data['Deaths']

        # Determining the mortality rating for this hurricane
        for rating, upper_bound in sorted(mortality_scale.items()):
            if deaths > upper_bound:
                # Assign the hurricane to the corresponding mortality rating
                current_rating = rating

            else:
                break
        # Appending the hurricane data to the list for the determined rating
        hurricanes_by_mortality[current_rating].append(hurricane_data)
    
    return hurricanes_by_mortality

# Testing
rated_hurricanes = rate_hurricanes_by_mortality(hurricane_data)

for rating, hurricanes in rated_hurricanes.items():
    print(f"Rating {rating}: {len(hurricanes)} hurricanes")
    for hurricane in hurricanes:
        print(f" - {hurricane['Name']} ({hurricane['Deaths']} deaths)")


# 8 Calculating Hurricane Maximum Damage


# Adding 'Damages' key to each hurricane entry
def add_damage_info(hurricane_dict, damages_list):
    for i, (hurricane_name, hurricane_info) in enumerate(hurricane_dict.items()):
        if i < len(damages_list):  # Ensure the index is within the bounds of the damages list
            hurricane_info['Damages'] = damages_list[i]
        else:
            print(f"Warning: No damage information available for hurricane {hurricane_name}")
    
    return hurricane_dict

# Update the hurricane_data dictionary with the 'Damages' information
hurricane_data_with_damages = add_damage_info(hurricane_data, damages)

# Print the updated data to verify
for name, info in hurricane_data_with_damages.items():
    print(f"{name}: {info}")


# find highest damage inducing hurricane and its total cost
def find_most_damaging_hurricane(hurricane_dict):
    max_damage = 0
    most_damaging_hurricane = None

    # Defining a conversion dictionary for damage units
    conversion = {"M": 1000000, "B": 1000000000}

    for hurricane_name, hurricane_data in hurricane_dict.items():
        # Accessing the damage amount
        damage = hurricane_data['Damages']

        if damage != 'Damages not recorded':
            # Converting the damage amount to a numerical value
            value = float(damage[:-1]) # Extracting the number part
            unit = damage[-1] # Extracting the unit (M or B)
            numerical_damage = value * conversion[unit] # Multiplying the value for a million or billion

            # Checking if this hurricane caused more damage than the current maximum
            if numerical_damage > max_damage:
                max_damage = numerical_damage # the max damage is now the current numerical damage
                most_damaging_hurricane = hurricane_name # the most damaging hurricane is now the current hurricane
    
    return most_damaging_hurricane, max_damage


# Testing
most_damaging_name, max_damage = find_most_damaging_hurricane(hurricane_data)
print(f"The hurricane causing the most damage is {most_damaging_name} with a damage cost of ${max_damage:.2f}.")


# 9
# Rating Hurricanes by Damage

# categorize hurricanes in new dictionary with damage severity as key
def rate_hurricanes_by_damage(hurricane_dict):
    # Defining the damage scale
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    
    # Initializing a dictionary to store hurricanes by damage rating
    hurricanes_by_damage_rating = {rating: [] for rating in damage_scale}

    # Defining a conversion dictionary for damage units
    conversion = {"M": 1000000, "B": 1000000000}
    
    # Itarating through each hurricane in the dictionary
    for hurricane_name, hurricane_info in hurricane_dict.items():
        # Accessing the damage amount
        damage = hurricane_info.get('Damages', 'Damages not recorded')

        if damage != 'Damages not recorded':
            # Converting the damage amount to a numerical value
            try:
                value = float(damage[:-1])  # Extracting the number part
                unit = damage[-1]  # Extracting the unit (M or B)
                numerical_damage = value * conversion[unit]
                
                # Determining the damage rating
                rating = 0
                for scale_rating, upper_bound in sorted(damage_scale.items(), reverse=True):
                    if numerical_damage > upper_bound:
                        rating = scale_rating
                        break
                
                # Adding hurricane to the appropriate rating list
                hurricanes_by_damage_rating[rating].append(hurricane_info)
            except KeyError:
                print(f"Warning: Unrecognized damage unit in data for hurricane {hurricane_name}: {damage}")
            except ValueError:
                print(f"Warning: Error converting damage data for hurricane {hurricane_name}: {damage}")
    
    return hurricanes_by_damage_rating

# Testing
hurricanes_by_damage_rating = rate_hurricanes_by_damage(hurricane_data_with_damages)

# Printing the results to verify
for rating, hurricanes in hurricanes_by_damage_rating.items():
    print(f"Damage Rating {rating}:")
    for hurricane in hurricanes:
        print(hurricane)

