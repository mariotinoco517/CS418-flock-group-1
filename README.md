# CS418-flock-group-1

Repository for use for flock group 1 in CS418

## Groups Members <br/>

- Mario Tinoco
- Haseeb Mohajir
- Joe Wu
- Neel Pastakia

# Data Acquisition<br/>

## Group's research questions(pulled from question memo)<br/>

- Does the presence of flock cameras in areas lower traffic violations?
- Do flock cameras actually help reduce crime?

## Primary Datasets that seem to address the question(s)<br/>

- chicago-city.json: Taken from class github, useful for mapping out data
- chicago-ward-incsome.csv: Taken from class github, useful for context on population
- Crimes\_-_2026_20260928.csv: Taken from the [Chicago Data Portal](https://data.cityofchicago.org/Public-Safety/Crimes-2026/f6bk-yv3r/about_data), csv containing all crime reports from 2001 to present

## Secondary Datasets expected to join or compare against the primary datasets<br/>

- camera.geojson: taken from [deflock.org](https://maps.deflock.org/?lat=39.8283&lng=-98.5795&zoom=4.00) containing locations of flock cameras
- red_light_100000.csv: Taken from [Chicago Data Portal](https://data.cityofchicago.org/Transportation/Red-Light-Camera-Violations/spqx-js37/about_data), csv containing Chicago's red-light camera violations from 2014 to present
- speed_violations_150000.csv: Taken from [Chicago Data Portal](https://data.cityofchicago.org/Transportation/Speed-Camera-Violations/hhkd-xvj4/about_data), csv contained Chicago's speed traffic violations from 2014 to present

## Report on the basic shape of the data<br/>

- camera.geojson: 140,678 rows and 14 columns. Each row is a unique flock camera in the US. Important columns will be osmID (i64), operator (str), longitude (f64), and latitude (f64)
- chicago-ward-income.csv: 50 rows and 10 columns: Each row is a different ward in chicago. Important columns will be ward (i64) and median_household_income_est (i64)
- Crimes\_-_2026_20260928.csv: 167,474 rows and 22 columns: Each row is a different reported crime. Important columns will be ID (i64), Date (str), and Location (str)
- red_light_100000.csv: 100,000 rows and 10 columns: Each row is a different reported violation. Important columns will be Address (str), Camera ID (int), Violation Date (str), and Location (str).
- speed_violations_150000.csv: 150,000 rows and 9 columns: Each row is a different reported violation. Important columns will be Address (str), Camera ID (int), Violation Date (str), Violations (int), and Location (str).

# Exploratory Analysis<br/>
## Revised Research Questions
-
## Dataset Basics<br/>
-
## Anomalies<br/>
-
## Significant Findings<br/>
-
