# Import SQL Library and Pandas
import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connections for the databases
conn1 = sqlite3.connect('planets.db')
conn2 = sqlite3.connect('dogs.db')
conn3 = sqlite3.connect('babe_ruth.db')

# View planets data by selecting all
planets_data = pd.read_sql("""SELECT * FROM planets; """, conn1)
print("\n\n--- Planets Data ---")
print(planets_data)

# PART 1: BASIC FILTERING

# 1. Return all the columns for planets that have 0 moons.
df_no_moons = pd.read_sql(""" SELECT * FROM planets WHERE num_of_moons = 0 """, conn1)
print("\n\n No Moons:")
print(df_no_moons)

# 2. Return the name and mass of each planet that has a name with exactly 7 letters. Avoid hard-coding this filter subset as much as possible.
df_name_seven = pd.read_sql(""" SELECT name, mass FROM planets WHERE LENGTH(name) = 7 """, conn1)
print("\n\n Planets with 7 letter names:")
print(df_name_seven)

# PART 2: ADVANCED FILTERING

# 3. Return the name and mass for each planet that has a mass that is less than or equal to 1.00.
df_mass = pd.read_sql(""" SELECT name, mass FROM planets WHERE mass <= 1 """, conn1)
print("\n\n Planets with mass <= 1:")
print(df_mass)

# 4. Return all the columns for planets that have at least one moon and a mass less than 1.00.
df_mass_moon = pd.read_sql(""" SELECT * FROM planets WHERE num_moons >= 1 AND mass < 1.00 """, conn1)
print("\n\n Planets with atleast 1 moon and mass <= 1:")
print(df_mass_moon)

# 5. Return the name and color of planets that have a color containing the string "blue".
df_blue = pd.read_sql(""" SELECT name, color FROM planets WHERE color LIKE '%blue' """, conn1)
print("\n\n Planets that are blue:")
print(df_blue)

# PART 3: ORDERING AND LIMITING

# View dogs data by selecting all
dog_data = pd.read_sql(""" SELECT * FROM dogs;""", conn2)
print("\n\n Planets with atleast 1 moon and mass <= 1:")
print(df_mass_moon)

# 6. Return the name, age, and breed of all dogs that are hungry (binary flag of 1) and sort them from youngest to oldest.
df_hungry = pd.read_sql(""" SELECT name, age, breed FROM dogs WHERE hungry =1 ORDER BY age ASC""", conn2)
print("\n\n--- Hungry dogs ---")
print(df_hungry)

# 7. Return the name, age, and hungry columns for hungry dogs between the ages of two and seven. This query should also sort these dogs in alphabetical order.
df_hungry_ages = pd.read_sql(""" SELECT name, age, hungry FROM dogs WHERE hungry =1 AND age
                             BETWEEN 2 AND 7 ORDER BY name ASC""", conn2)
print("\n\n--- Hungry dogs between 2-7 alphabetically ---")
print(df_hungry_ages)

# 8. Return the name, age, and breed for the 4 oldest dogs. Sort the result alphabetically based on the breed
df_4_oldest = pd.read_sql(""" SELECT name, age, breed FROM dogs ORDER BY age DESC LIMIT 4""", conn2)
print("\n\n--- Name, age, and breed of 4 oldest dogs---")
print(df_4_oldest)

# PART 4: AGGREGATION

# View Babe Ruth data by selecting all
babe_ruth_data = pd.read_sql(""" SELECT * FROM babe_ruth_stats; """, conn3)
print("\n\n--- Babe Ruth's Data ---")
print(babe_ruth_data)

# 9. Return the total number of years that Babe Ruth played professional baseball.
df_ruth_years = pd.read_sql(""" SELECT COUNT(*) AS total_years FROM babe_ruth_stats """, conn3)
print("\n\n--- Total number of years played ---")
print(df_ruth_years)

# 10. Return the total number of home runs hit by Babe Ruth during his career.
df_hr_total = pd.read_sql(""" SELECT SUM(HR) AS total_home_runs FROM babe_ruth_stats """, conn3)
print("\n\n--- Total number of home runs during career ---")
print(df_hr_total)

# PART 5: GROUPING AND AGGREGATION

# 11. For each team that Babe Ruth has played on, return the team name and the number of years he played on that team, aliased as number_years.
df_teams_years = pd.read_sql(""" SELECT team, COUNT(*) AS number_years FROM babe_ruth_stats  GROUP BY team""", conn3)
print("\n\n--- Total number of years played on each team ---")
print(df_teams_years)

# 12. For each team that Babe Ruth played on and averaged over 200 at-bats with, return the team name and average number of at-bats, aliased as average_at_bats.
df_at_bats = pd.read_sql(""" SELECT team, AVG(AB) AS average_at_bats FROM babe_ruth_stats GROUP BY team HAVING AVG(AB) > 200""", conn3)
print("\n\n--- For each team average of over 200 at bats ---")
print(df_at_bats)

# Close each connection
conn1.close()
conn2.close()
conn3.close()