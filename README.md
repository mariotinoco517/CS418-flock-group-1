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

## Revised Research Question(s)

- Does the presence of Flock cameras impact the amount of crimes, or more specifically, traffic violations, in Chicago?<br/>
- Does the local density of Flock cameras in specific Chicago police districts correspond to a drop in vehicle crimes?

## Dataset Basics<br/>

1. Regarding red-light and speed-cameras, and flock relations...
   - The exploration of the datasets is broken down in two phases.
   - Phase one analyzes the relation between red-light cameras and speed cameras.
   - Phase two anaylzes the relation between the red-light cameras and flock cameras, and speed cameras and flock cameras.

## Anomalies<br/>

Regarding red-light and speed-cameras, and flock relations...

- There is a sudden and abrupt rise in speed violations in the year of 2021. This is very strange because prior to this year, the number of speed violations on average was a lot lower, fluctucation between 20 to 50 mean violations per record. But, after the year of 2021, the number rose sharply from between 40 to 100 mean veiolations per record.

## Significant Findings<br/>

Regarding red-light and speed-cameras, and flock relations...

- Phase One Findings:
  - Speed-camera violations are higher and more variable month to month than red-light-camera violations. Speed-camera monthly means range from about 12 in February 2021 to 99 in July 2021; red-light-camera means are comparatively steadier, ranging from about 3.8 to 9.5.
- Phase Two Findings:
  - Red-light-camera sites within 500 m of a mapped Flock camera have a higher median site-level mean number of violations per exported record (about 5.14) than sites more than 2 km away (about 4.26). For speed cameras, the pattern is reversed: sites within 500 m have a lower median (about 24.37) than sites more than 2 km away (about 42.91). One thing to note is that these comparisons describe proximity patterns; they do not count violations recorded by Flock cameras or show that Flock cameras caused the differences.

## Data Documentation

See [DATASHEET.md](DATASHEET.md)
