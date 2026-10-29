# Datasheets

- Crimes\_-_2026_20260928.csv<br>
  ![alt text](image-9.png)

* Chcago-city.geojson<br>
  ![alt text](image-10.png)

* Chicago-ward-income.csv<br>
  ![alt text](image-11.png)

# Scope

- Does the presence of flock cameras in areas lower traffic violations?
  - Target population are traffic violations within the city of chicago starting in July 2022
  - Access frame are cameras reported in cameras.geojson and traffic violations reported by CPD in our time frame
  - Sample is traffic violations through Septermber 2026 joined to cameras in cameras.geojson.
- Do flock cameras actually help reduce crime
  - Target population are reported crimes within the city of chicago starting in July 2022
  - Access frame are cameras reported in cameras.geojson and crimes reported by CPD in our time frame
  - Sample is crimes through Septermber 2026 joined to cameras in cameras.geojson.

## Crimes Dataset

Source: `Crimes_-_2026_20260928.csv`

| Name                   | Data type        | Units                         | What it means                                                   | Range or allowed values                                         | Missing values                          | Source / derivation                                                                                   |
| ---------------------- | ---------------- | ----------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `ID`                   | Integer          | Record identifier             | Unique identifier assigned to a crime record.                   | Positive integer                                                | Blank becomes null                      | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Case Number`          | String           | Case identifier               | Chicago Police Department case number.                          | Identifier as recorded                                          | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Date`                 | String timestamp | Local date and time           | Date and time associated with the reported incident.            | Timestamp as recorded in the source export.                     | Blank or unparsable value becomes null. | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Block`                | String           | Street address text           | Block-level location of the incident; exact address is masked.  | Text as recorded; may include a block number and street name.   | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `IUCR`                 | String           | Crime code                    | Illinois Uniform Crime Reporting code for the offense.          | Code as recorded by CPD.                                        | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Primary Type`         | String           | Category                      | Broad category assigned to the reported crime.                  | Crime category as recorded by CPD.                              | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Description`          | String           | Category                      | More specific description of the offense.                       | Description as recorded by CPD.                                 | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Location Description` | String           | Category                      | Description of the place where the incident occurred.           | Location category as recorded by CPD.                           | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Arrest`               | Boolean          | Indicator                     | Whether an arrest was reported for the incident.                | `true` or `false`.                                              | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Domestic`             | Boolean          | Indicator                     | Whether the incident was identified as domestic-related.        | `true` or `false`.                                              | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Beat`                 | Integer          | CPD beat identifier           | Police beat associated with the incident.                       | CPD beat code as recorded.                                      | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `District`             | Integer          | CPD district identifier       | Police district associated with the incident.                   | Chicago Police district code as recorded.                       | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Ward`                 | Integer          | Ward identifier               | Chicago ward associated with the incident.                      | Ward 1–50 for Chicago wards                                     | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`. Also used to form `crime_count` in `chicago_ward_income (1).ipynb`. |
| `Community Area`       | Integer          | Community-area identifier     | Chicago community area associated with the incident.            | Community area 1–77.                                            | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `FBI Code`             | String           | Crime code                    | FBI offense classification code.                                | Code as recorded by CPD.                                        | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `X Coordinate`         | Integer          | State Plane coordinate (feet) | Projected east-west coordinate supplied for the incident.       | Chicago-area coordinate in the source projection                | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Y Coordinate`         | Integer          | State Plane coordinate (feet) | Projected north-south coordinate supplied for the incident.     | Chicago-area coordinate in the source projection                | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Year`                 | Integer          | Calendar year                 | Year associated with the incident record.                       | Year in the source export, from 2001 through the export period. | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Updated On`           | String timestamp | Local date and time           | Date and time the source record was last updated.               | Timestamp as recorded in the source export.                     | Blank or unparsable value becomes null. | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Latitude`             | Number           | Decimal degrees               | Geographic latitude supplied for the incident.                  | Chicago-area latitude                                           | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Longitude`            | Number           | Decimal degrees               | Geographic longitude supplied for the incident.                 | Chicago-area longitude                                          | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |
| `Location`             | String           | Coordinate pair text          | Source-formatted location, typically a latitude/longitude pair. | Coordinate text as supplied by the portal.                      | Blank becomes null.                     | Raw `Crimes_-_2026_20260928.csv`.                                                                     |

## Chicago Ward Income Dataset

Source: `chicago-ward-income.csv`

| Name                          | Data type | Units               | What it means                                                | Range or allowed values      | Missing values | Source / derivation                                                       |
| ----------------------------- | --------- | ------------------- | ------------------------------------------------------------ | ---------------------------- | -------------- | ------------------------------------------------------------------------- |
| `ward`                        | Integer   | Ward identifier     | Chicago ward represented by the row.                         | 1–50; one row per ward.      | N/A            | Raw `chicago-ward-income.csv`.                                            |
| `acs_year`                    | Integer   | Calendar year       | ACS estimate year.                                           | 2023 in the supplied file.   | N/A            | Raw `chicago-ward-income.csv`.                                            |
| `households_under_25k`        | Integer   | Households          | Estimated households with income below $25,000.              | Nonnegative count.           | N/A            | Raw `chicago-ward-income.csv`.                                            |
| `households_25k_to_50k`       | Integer   | Households          | Estimated households in the $25,000–$49,999 income bracket.  | Nonnegative count.           | N/A            | Raw `chicago-ward-income.csv`.                                            |
| `households_50k_to_75k`       | Integer   | Households          | Estimated households in the $50,000–$74,999 income bracket.  | Nonnegative count.           | N/A            | Raw `chicago-ward-income.csv`.                                            |
| `households_75k_to_125k`      | Integer   | Households          | Estimated households in the $75,000–$124,999 income bracket. | Nonnegative count.           | N/A            | Raw `chicago-ward-income.csv`.                                            |
| `households_125k_plus`        | Integer   | Households          | Estimated households with income of $125,000 or more.        | Nonnegative count.           | N/A            | Raw `chicago-ward-income.csv`.                                            |
| `households_total`            | Integer   | Households          | Estimated total households in the ward.                      | Nonnegative count            | N/A            | Raw `chicago-ward-income.csv`.                                            |
| `pct_households_125k_plus`    | Number    | Percent (%)         | Percentage of households in the $125,000-or-more bracket.    | 0–100.                       | N/A            | Raw `chicago-ward-income.csv`.                                            |
| `median_household_income_est` | Integer   | US dollars per year | Estimated median household income for the ward.              | Nonnegative dollar estimate. | N/A            | Raw `chicago-ward-income.csv`. Also used in the income-versus-crime plot. |

## Flock Cameras Dataset

Source: `cameras.geojson`

| Name                   | Data type        | Units                        | What it means                                                        | Range or allowed values                                                           | Missing values                                                       | Source / derivation                                                              |
| ---------------------- | ---------------- | ---------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `osmId`                | Integer          | OpenStreetMap identifier     | OpenStreetMap object identifier for the mapped camera/location.      | Positive integer.                                                                 | Missing property or JSON `null` becomes null.                        | `properties.osmId` in `cameras.geojson`.                                         |
| `osmType`              | String           | Object type                  | OpenStreetMap object type.                                           | `node`, `way`, or `relation` as present in the file.                              | Missing property or JSON `null` becomes null.                        | `properties.osmType` in `cameras.geojson`.                                       |
| `brand`                | String           | Brand label                  | Camera brand recorded in the map.                                    | Text as recorded                                                                  | Missing property or JSON `null` becomes null.                        | `properties.brand` in `cameras.geojson`.                                         |
| `operator`             | String           | Operator label               | Organization listed as operating the camera/location.                | Text as recorded.                                                                 | Missing property or JSON `null` becomes null.                        | `properties.operator` in `cameras.geojson`.                                      |
| `ref`                  | String           | Reference text               | Reference or route identifier attached to the mapped feature.        | Text as recorded.                                                                 | Missing property or JSON `null` becomes null.                        | `properties.ref` in `cameras.geojson`.                                           |
| `startDate`            | String           | Date/year text               | Start date or year associated with the mapped feature.               | Text as recorded.                                                                 | Missing property or JSON `null` becomes null.                        | `properties.startDate` in `cameras.geojson`.                                     |
| `osmTimestamp`         | String timestamp | UTC date and time            | Last-edit timestamp for the OpenStreetMap object.                    | ISO 8601 timestamp as recorded.                                                   | Missing property or JSON `null` becomes null.                        | `properties.osmTimestamp` in `cameras.geojson`.                                  |
| `osmVersion`           | Integer          | Version number               | OpenStreetMap object version.                                        | Positive integer.                                                                 | Missing property or JSON `null` becomes null.                        | `properties.osmVersion` in `cameras.geojson`.                                    |
| `direction`            | Number           | Degrees clockwise from north | Direction associated with the mapped camera.                         | Bearing from 0 inclusive to 360 exclusive.                                        | Missing property or JSON `null` becomes null.                        | `properties.direction` in `cameras.geojson`.                                     |
| `directionCardinal`    | String           | Compass direction            | Cardinal direction associated with the camera.                       | Compass label as recorded, such as `N`, `NE`, `E`, `SE`, `S`, `SW`, `W`, or `NW`. | Missing property or JSON `null` becomes null.                        | `properties.directionCardinal` in `cameras.geojson`.                             |
| `directions`           | List of numbers  | Degrees clockwise from north | One or more directions associated with the mapped feature.           | List of bearings, each from 0 inclusive to 360 exclusive.                         | Missing property or JSON `null` becomes null.                        | `properties.directions` in `cameras.geojson`.                                    |
| `mountType`            | String           | Mount type                   | Mounting type recorded for the camera.                               | Text as recorded, for example `pole`.                                             | Missing property or JSON `null` becomes null.                        | `properties.mountType` in `cameras.geojson`.                                     |
| `surveillanceZone`     | String           | Zone category                | Type of area or activity monitored, when supplied.                   | Text as recorded, for example `traffic`.                                          | Missing property or JSON `null` becomes null.                        | `properties.surveillanceZone` in `cameras.geojson`.                              |
| `geometry.coordinates` | List of numbers  | Decimal degrees              | GeoJSON Point coordinates, ordered as longitude then latitude.       | Longitude -180 to 180; latitude -90 to 90.                                        | Missing or null geometry is not usable for the distance calculation. | Raw `geometry.coordinates` in `cameras.geojson`.                                 |
| `longitude`            | Number           | Decimal degrees              | Longitude extracted from element 0 of the GeoJSON Point coordinates. | -180 to 180                                                                       | Null if geometry or coordinates are missing.                         | Created in `TrafficViolationFlockRelation.ipynb` from `geometry.coordinates[0]`. |
| `latitude`             | Number           | Decimal degrees              | Latitude extracted from element 1 of the GeoJSON Point coordinates.  | -90 to 90                                                                         | Null if geometry or coordinates are missing.                         | Created in `TrafficViolationFlockRelation.ipynb` from `geometry.coordinates[1]`. |

## Chicago City Dataset

Source: `chicago-city.geojson`

| Name                   | Data type                | Units           | What it means                                                                                  | Range or allowed values                 | Missing values | Source / derivation                                   |
| ---------------------- | ------------------------ | --------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- | -------------- | ----------------------------------------------------- |
| `geometry.type`        | String                   | Geometry type   | Type of boundary geometry.                                                                     | `MultiPolygon` in the supplied feature. | N/A            | Raw `geometry.type` in `chicago-city.geojson`.        |
| `geometry.coordinates` | Nested coordinate arrays | Decimal degrees | Polygon rings defining the Chicago city boundary. Coordinate order is longitude then latitude. | Coordinates lie in the Chicago area.    | N/A            | Raw `geometry.coordinates` in `chicago-city.geojson`. |

## Red Light and Speed Violations Datasets

Sources: `red_light_100000.csv` and `speed_violations_150000.csv`

| Name             | Data type                                | Units                          | What it means                                                                         | Range or allowed values | Missing values                         | Source / derivation                                                             |
| ---------------- | ---------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------- | ----------------------- | -------------------------------------- | ------------------------------------------------------------------------------- |
| `VIOLATION DATE` | String date                              | Local calendar date            | Date the traffic-camera violation record was issued.                                  | `MM/DD/YYYY`.           | Invalid or blank date parses as null.  | Raw field in each traffic CSV.                                                  |
| `VIOLATIONS`     | String in CSV; parsed number in analysis | Violations per exported record | Number of violations recorded for the row. Commas are removed before numeric parsing. | Nonnegative count       | Invalid or blank values parse as null. | Raw field in each traffic CSV; parsed in `TrafficViolationFlockRelation.ipynb`. |
| `CAMERA ID`      | String                                   | Camera identifier              | Traffic-camera identifier used to group records into sites.                           | Identifier as recorded. | Blank becomes null.                    | Raw field in each traffic CSV.                                                  |
| `LATITUDE`       | Number                                   | Decimal degrees                | Latitude of the traffic-camera record.                                                | -90 to 90               | Blank or invalid value parses as null. | Raw field in each traffic CSV.                                                  |
| `LONGITUDE`      | Number                                   | Decimal degrees                | Longitude of the traffic-camera record.                                               | -180 to 180             | Blank or invalid value parses as null. | Raw field in each traffic CSV.                                                  |

## Precomputed Monthly Comparison Datasets

Sources: `Clean_Monthly_Crimes.csv`, `Clean_Monthly_Red_Light.csv`, and
`Clean_Monthly_Speed.csv`

| Name                   | Data type | Units                           | What it means                                                           | Range or allowed values                                        | Missing values | Source / derivation                                                                                                                  |
| ---------------------- | --------- | ------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `Timestamp`            | Date      | Month, represented by first day | Month to which each monthly measure applies.                            | `YYYY-MM-DD`; month starts from 2014-07-01 through 2026-08-01. | N/A            | Raw column in each `Clean_Monthly_*.csv`; parsed by `pandas.to_datetime` in `TotalVehicleCrimeRelationToSpeedingAndRedLights.ipynb`. |
| `Total_Vehicle_Crimes` | Integer   | Crime records per month         | Precomputed monthly total of vehicle crimes.                            | Nonnegative integer count.                                     | N/A            | Raw `Clean_Monthly_Crimes.csv`..                                                                                                     |
| `Crime_Norm`           | Number    | Unitless normalized score       | Precomputed normalized crime measure used to compare time patterns.     | Numeric score.                                                 | N/A            | Raw `Clean_Monthly_Crimes.csv`.                                                                                                      |
| `Red_Light_Tickets`    | Integer   | Tickets per month               | Precomputed monthly red-light-camera ticket total.                      | Nonnegative integer count.                                     | N/A            | Raw `Clean_Monthly_Red_Light.csv`.                                                                                                   |
| `Red_Light_Norm`       | Number    | Unitless normalized score       | Precomputed normalized red-light measure used to compare time patterns. | Numeric score.                                                 | N/A            | Raw `Clean_Monthly_Red_Light.csv`.                                                                                                   |
| `Speed_Tickets`        | Integer   | Tickets per month               | Precomputed monthly speed-camera ticket total.                          | Nonnegative integer count.                                     | N/A            | Raw `Clean_Monthly_Speed.csv`.                                                                                                       |
| `Speed_Norm`           | Number    | Unitless normalized score       | Precomputed normalized speed measure used to compare time patterns.     | Numeric score.                                                 | N/A            | Raw `Clean_Monthly_Speed.csv`.                                                       
# Share the Recipe

### Ward Income and Crime Data Preparation

**Code reference:** `notebooks/chicago_ward_income.ipynb`

1. Loaded `chicago-ward-income.csv` and `Crimes_-_2026_20260928.csv` using Polars.
2. Read the crime CSV using `infer_schema_length=10000` and `ignore_errors=True`.
3. Filtered crime records to include only valid Chicago wards (1–50).
4. Grouped crime records by `Ward` and counted the number of crimes in each ward, creating `crime_count`.
5. Performed an inner join using `ward` from the income dataset and `Ward` from the crime dataset.
6. Selected `ward`, `median_household_income_est`, and `crime_count` for analysis.
7. Created a scatter plot and calculated the Pearson correlation coefficient.

**Join results:**

- Matched wards: 50
- Unmatched income wards: 0
- Unmatched crime wards: 0
- Final dataframe: 50 rows and 3 columns

All 50 wards matched successfully. No ward-level records were lost during the join. Crime records with invalid ward numbers were excluded before the join.

### Crime Dataset Preparation

**Code reference:** `notebooks/crimes.ipynb`

1. Loaded `Crimes_-_2026_20260928.csv` using Polars.
2. Examined the dataset's shape, column types, summary statistics, and missing values.
3. Divided the 22 columns into smaller groups for easier inspection.
4. Identified 304 records with missing geographic coordinates.
5. Counted reported crimes by `Primary Type` to examine the distribution of crime categories.
6. Counted reported crimes by `Ward` to compare crime counts across Chicago wards.
7. Created bar charts showing the number of reported crimes by crime type and ward.

**Data preparation results:**

- Original dataset: 167,474 rows and 22 columns.
- Records with missing geographic coordinates: 304.
- No joins were performed in this notebook.
- The notebook identifies missing-location records for removal, but does not currently contain code that removes them.
- The original crime records were used to create the distribution charts.
  
### Camera Dataset Preparation

**Code reference:** `notebooks/camera.ipynb`

1. Loaded `cameras.geojson` using Python's `json` library.
2. Extracted the camera records from the GeoJSON `features` list.
3. Converted the records into a Polars dataframe.
4. Extracted longitude and latitude from the geometry coordinates and created two new columns: `longitude` and `latitude`.
5. Expanded the nested `properties` structure into separate columns using `unnest()`.
6. Removed the original `type` and `geometry` columns after extracting the required information.
7. Divided the columns into smaller groups for easier inspection.
8. Checked the dataset's shape, data types, missing values, and summary statistics.
9. Identified missing values in columns such as `operator`, `surveillanceZone`, and `startDate`.
10. Created bar charts showing camera counts by operator and surveillance zone.

**Data preparation results:**

- Original dataset: 140,678 camera records.
- Extracted dataframe: 140,678 rows and 14 columns.
- No geographic filtering was performed in this notebook.
- Missing operator values were excluded when calculating operator frequencies.
- Missing surveillance-zone values were excluded when calculating surveillance-zone frequencies.
- The notebook discusses excluding `startDate` from future analysis, but does not actually remove it from the main dataframe.
- No joins were performed in this notebook.

### Chicago City Boundary Dataset Preparation

**Code reference:** `notebooks/chicago_city.ipynb`

1. Loaded `chicago-city.geojson` using Python's `json` library.
2. Extracted the geographic features from the GeoJSON `features` list.
3. Created a Polars dataframe containing `feature_id`, `geometry_type`, `properties_count`, and `has_geometry`.
4. Checked for missing geometry, duplicate features, invalid coordinates, and unclosed polygon rings.
5. Extracted polygon rings and their longitude and latitude coordinates.
6. Identified 156 consecutive duplicate coordinate points but kept them unchanged to preserve the original boundary.
7. Created a geographic plot showing Chicago's city boundary.

**Data preparation results:**

- Original GeoJSON: 1 geographic feature.
- Profiling dataframe: 1 row and 4 columns.
- Total coordinate entries: 12,731 across 5 polygon rings.
- Missing geometries: 0.
- No geographic features or coordinate points were removed.
- No joins were performed in this notebook.

### Red-Light and Speed-Camera Violations Preparation

**Code reference:** `notebooks/eda.ipynb`
(Red-light and speed-camera relationship analysis)

1. Loaded `red_light_100000.csv` and `speed_violations_150000.csv` using Polars.
2. Read the `VIOLATIONS` column as a string to handle values containing commas.
3. Converted `VIOLATION DATE` into a date using the format `MM/DD/YYYY`.
4. Extracted the year and month into a new column named `month`, formatted as `YYYY-MM`.
5. Removed commas from `VIOLATIONS` and converted the values to numbers.
6. Dropped records with missing or invalid values in the selected date and violation columns.
7. Grouped each dataset by `month`.
8. Calculated the average number of violations per record for each month, creating `mean_violations`.
9. Sorted the monthly results chronologically.
10. Created a line chart comparing monthly averages for red-light and speed-camera violations.

**Data preparation results:**

- Original red-light dataset: 100,000 rows.
- Original speed-camera dataset: 150,000 rows.
- Both datasets were aggregated separately by month.
- No dataframe join was performed for this particular comparison.
- The resulting monthly averages were plotted together.

### Monthly Vehicle Crime and Traffic Violations Preparation

**Code reference:** `notebooks/TotalVehicleCrimeRelationToSpeedingAndRedLights.ipynb`

1. Loaded three precomputed CSV files using pandas:
   - `Clean_Monthly_Crimes.csv`
   - `Clean_Monthly_Red_Light.csv`
   - `Clean_Monthly_Speed.csv`
2. Each dataset contains monthly observations identified by a common column named `Timestamp`.
3. Performed an outer join between the monthly crime and red-light datasets using `Timestamp`.
4. Performed a second outer join between the combined dataframe and the monthly speed-violation dataset using `Timestamp`.
5. Replaced missing values in the combined dataframe with zero using `fillna(0)`.
6. Converted the `Timestamp` column to datetime using `pd.to_datetime()`.
7. Created separate time-series plots showing monthly vehicle crimes, red-light tickets, and speed-camera tickets.
8. Created a combined visualization comparing the three normalized monthly trends.

**Data Preparation Results:**

- Original monthly crime dataset: 146 rows.
- Original monthly red-light dataset: 146 rows.
- Original monthly speed dataset: 146 rows.
- Final combined dataframe: 146 rows.

**Join 1 — Monthly Crimes and Red-Light Violations**

- Join type: Outer join.
- Join key: `Timestamp`.
- Matched months: 146.
- Unmatched crime months: 0.
- Unmatched red-light months: 0.

**Join 2 — Combined Data and Speed Violations**

- Join type: Outer join.
- Join key: `Timestamp`.
- Matched months: 146.
- Unmatched combined months: 0.
- Unmatched speed months: 0.

All three datasets contain the same 146 monthly timestamps, so no monthly observations were lost during the joins.

**Reproducibility Note:**

The monthly comparison analysis uses three precomputed datasets:
`Clean_Monthly_Crimes.csv`, `Clean_Monthly_Red_Light.csv`,
and `Clean_Monthly_Speed.csv`.

These datasets contain 146 monthly observations each, with matching
timestamps from July 2014 through August 2026.

The notebook documents how these datasets are joined, how missing
values are handled, and how the resulting data is visualized.

However, the repository does not currently contain an identified
script or notebook showing how the three cleaned monthly datasets
were generated from their original sources.

Therefore, the monthly comparison can be reproduced using the
precomputed CSV files, but the complete upstream cleaning process
cannot currently be independently reproduced from the documented code.

This is a limitation of the current data preparation pipeline.

### Flock Camera Proximity and Traffic Violations Preparation

**Code reference:** `notebooks/TrafficViolationFlockRelation.ipynb`

1. Loaded `cameras.geojson` using Python's json library and converted its features into a Polars dataframe.
2. Extracted longitude and latitude from the GeoJSON geometry coordinates.
3. Filtered the camera records to include only those labeled `Flock Safety` and located within the approximate Chicago-area coordinate bounds:
   - Latitude: 41.5 to 42.1
   - Longitude: -88.0 to -87.5
4. Loaded `red_light_100000.csv` and `speed_violations_150000.csv` using Polars.
5. Converted the traffic-camera latitude, longitude, and violation counts into numeric values.
6. Removed traffic records with missing or invalid coordinates, coordinates outside the selected geographic bounds, or missing violation counts.
7. Grouped the remaining traffic records by `CAMERA ID`.
8. Calculated the mean latitude, longitude, and number of violations per exported record for each traffic-camera site.
9. Used the Haversine distance formula to calculate the distance from each traffic-camera site to its nearest mapped Flock Safety camera.
10. Classified traffic-camera sites into three distance categories:
    - Within 500 meters
    - Between 500 meters and 2 kilometers
    - More than 2 kilometers
11. Grouped the traffic-camera sites by proximity category and calculated the median site-level mean violations.
12. Created comparison plots for red-light and speed-camera violations by proximity to mapped Flock cameras.

**Data Preparation Results:**

- Original red-light dataset: 100,000 records.
- Red-light records with coordinates: 94,383.
- Red-light records included in the final site groups: 90,383.
- Final red-light camera sites: 358.

- Original speed-camera dataset: 150,000 records.
- Speed-camera records with coordinates: 150,000.
- Speed-camera records included in the final site groups: 150,000.
- Final speed-camera sites: 231.

**Geographic Matching:**

The traffic-camera datasets and Flock camera dataset do not share a common camera identifier.

Therefore, no traditional dataframe join was performed. Instead, traffic-camera sites were compared with mapped Flock Safety locations using geographic distance.

Each traffic-camera site was assigned the distance to its nearest mapped Flock Safety camera.

**Red-Light Camera Sites by Proximity:**

- Within 500 m: 50 sites.
- Between 500 m and 2 km: 196 sites.
- More than 2 km: 112 sites.

**Speed-Camera Sites by Proximity:**

- Within 500 m: 34 sites.
- Between 500 m and 2 km: 143 sites.
- More than 2 km: 54 sites.

**Limitations:**

The geographic filtering uses a rectangular coordinate range rather than the exact Chicago city boundary.

The analysis compares traffic-camera violations with proximity to mapped Flock Safety cameras. It does not measure violations recorded by Flock cameras or establish that Flock cameras caused changes in traffic violations.

# Access and Reuse

## Using FAIR (Findable, Accessible, Interoperable, Reusable)

- Crimes\_-_2026_20260928.csv<br>
  - [Link to database](https://data.cityofchicago.org/Public-Safety/Crimes-2026/f6bk-yv3r/about_data)
  - Downloaded September 20th 2026 in .csv format. Initial dataset is open to the public and so is out processed data

* Chcago-city.geojson<br>
  - [Link to database](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-City/qqq8-j68g/about_data)
  - Downloaded September 2025 in .geojson format. Initial dataset is open to the public and so is out processed data

* Chicago-ward-income.csv<br>
  - [Link to database](https://data.cityofchicago.org/Community-Economic-Development/ACS-5-Year-Data-by-Ward-Most-Recent-Year/k5pk-wpt9/about_data)
  - Downloaded dataset pertaining to 2023 data in .csv format. Initial dataset is open to the public and so is out processed data

- cameras.geojson<br>
  - [Link to database (click on share in top right -> download geojson)](https://maps.deflock.org/?lat=39.8283&lng=-98.5795&zoom=4.00)
  - Downloaded September 20th 2026 in .geojson format. Initial dataset is open to the public and so is out processed data

* red_light_100000.csv<br>
  - [Link to database](https://data.cityofchicago.org/Transportation/Red-Light-Camera-Violations/spqx-js37/about_data)
  - Downloaded September 2025 in .csv format. Initial dataset is open to the public and so is out processed data

* speed_violations_150000.csv<br>
  - [Link to database](https://data.cityofchicago.org/Transportation/Speed-Camera-Violations/hhkd-xvj4/about_data)
  - Downloaded September 2025 in .csv format. Initial dataset is open to the public and so is out processed data

 ## Considering People

  Throughout the project we used datasets that indirectly capture people. The datasets that describe crimes/infractions (Crimes\_-_2026_20260928.csv, red_light_100000, speed_violations_150000.csv)
  indirectly capture the actions of individuals. While no personal data is represented in these datasets they still capture the actions of people. And as Arvind Narayanan showed in [How To Break Anonymity of the Netflix Prize Dataset](https://arxiv.org/abs/cs/0610105) these actions can be traced back to individuals given effort. Because of this these datasets can indirectly misrepresent individuals who have commited a crime/infraction.
