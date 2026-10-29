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

  # Access and Reuse

  ## Using FAIR (Findable, Accessible, Interoperable, Reusable)

- Crimes\_-_2026_20260928.csv<br>
  - [Link to database](https://data.cityofchicago.org/Public-Safety/Crimes-2026/f6bk-yv3r/about_data)
  - Downloaded September 20th 2026 in .csv format. Dataset is open to the public

* Chcago-city.geojson<br>
  - [Link to database](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-City/qqq8-j68g/about_data)
  - Downloaded September 2025 in .geojson format. Dataset is open to the public

* Chicago-ward-income.csv<br>
  - [Link to database](https://data.cityofchicago.org/Community-Economic-Development/ACS-5-Year-Data-by-Ward-Most-Recent-Year/k5pk-wpt9/about_data)
  - Downloaded dataset pertaining to 2023 data in .csv format. Dataset is open to the public

- cameras.geojson<br>
  - [Link to database (click on share in top right -> download geojson)](https://maps.deflock.org/?lat=39.8283&lng=-98.5795&zoom=4.00)
  - Downloaded September 20th 2026 in .geojson format. Dataset is open to the public

* red_light_100000.csv<br>
  - [Link to database](https://data.cityofchicago.org/Transportation/Red-Light-Camera-Violations/spqx-js37/about_data)
  - Downloaded September 2025 in .csv format. Dataset is open to the public

* speed_violations_150000.csv<br>
  - [Link to database](https://data.cityofchicago.org/Transportation/Speed-Camera-Violations/hhkd-xvj4/about_data)
  - Downloaded September 2025 in .csv format. Dataset is open to the public

 ## Crimes Dataset

Source: `Crimes_-_2026_20260928.csv`

| Name | Data type | Units | What it means | Range or allowed values | Missing values | Source / derivation |
|---|---|---|---|---|---|---|
| `ID` | Integer | Record identifier | Unique identifier assigned to a crime record. | Positive integer | Blank becomes null | Raw `Crimes_-_2026_20260928.csv`. |
| `Case Number` | String | Case identifier | Chicago Police Department case number. | Identifier as recorded | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Date` | String timestamp | Local date and time | Date and time associated with the reported incident. | Timestamp as recorded in the source export. | Blank or unparsable value becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Block` | String | Street address text | Block-level location of the incident; exact address is masked. | Text as recorded; may include a block number and street name. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `IUCR` | String | Crime code | Illinois Uniform Crime Reporting code for the offense. | Code as recorded by CPD. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Primary Type` | String | Category | Broad category assigned to the reported crime. | Crime category as recorded by CPD. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Description` | String | Category | More specific description of the offense. | Description as recorded by CPD. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Location Description` | String | Category | Description of the place where the incident occurred. | Location category as recorded by CPD. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Arrest` | Boolean | Indicator | Whether an arrest was reported for the incident. | `true` or `false`. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Domestic` | Boolean | Indicator | Whether the incident was identified as domestic-related. | `true` or `false`. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Beat` | Integer | CPD beat identifier | Police beat associated with the incident. | CPD beat code as recorded. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `District` | Integer | CPD district identifier | Police district associated with the incident. | Chicago Police district code as recorded. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Ward` | Integer | Ward identifier | Chicago ward associated with the incident. | Ward 1–50 for Chicago wards | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. Also used to form `crime_count` in `chicago_ward_income (1).ipynb`. |
| `Community Area` | Integer | Community-area identifier | Chicago community area associated with the incident. | Community area 1–77. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `FBI Code` | String | Crime code | FBI offense classification code. | Code as recorded by CPD. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `X Coordinate` | Integer | State Plane coordinate (feet) | Projected east-west coordinate supplied for the incident. | Chicago-area coordinate in the source projection | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Y Coordinate` | Integer | State Plane coordinate (feet) | Projected north-south coordinate supplied for the incident. | Chicago-area coordinate in the source projection | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Year` | Integer | Calendar year | Year associated with the incident record. | Year in the source export, from 2001 through the export period. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Updated On` | String timestamp | Local date and time | Date and time the source record was last updated. | Timestamp as recorded in the source export. | Blank or unparsable value becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Latitude` | Number | Decimal degrees | Geographic latitude supplied for the incident. | Chicago-area latitude | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Longitude` | Number | Decimal degrees | Geographic longitude supplied for the incident. | Chicago-area longitude | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |
| `Location` | String | Coordinate pair text | Source-formatted location, typically a latitude/longitude pair. | Coordinate text as supplied by the portal. | Blank becomes null. | Raw `Crimes_-_2026_20260928.csv`. |

## Chicago Ward Income Dataset

Source: `chicago-ward-income.csv`

| Name | Data type | Units | What it means | Range or allowed values | Missing values | Source / derivation |
|---|---|---|---|---|---|---|
| `ward` | Integer | Ward identifier | Chicago ward represented by the row. | 1–50; one row per ward. | N/A | Raw `chicago-ward-income.csv`. |
| `acs_year` | Integer | Calendar year | ACS estimate year. | 2023 in the supplied file. | N/A | Raw `chicago-ward-income.csv`. |
| `households_under_25k` | Integer | Households | Estimated households with income below $25,000. | Nonnegative count. | N/A | Raw `chicago-ward-income.csv`. |
| `households_25k_to_50k` | Integer | Households | Estimated households in the $25,000–$49,999 income bracket. | Nonnegative count. | N/A | Raw `chicago-ward-income.csv`. |
| `households_50k_to_75k` | Integer | Households | Estimated households in the $50,000–$74,999 income bracket. | Nonnegative count. | N/A | Raw `chicago-ward-income.csv`. |
| `households_75k_to_125k` | Integer | Households | Estimated households in the $75,000–$124,999 income bracket. | Nonnegative count. | N/A | Raw `chicago-ward-income.csv`. |
| `households_125k_plus` | Integer | Households | Estimated households with income of $125,000 or more. | Nonnegative count. | N/A | Raw `chicago-ward-income.csv`. |
| `households_total` | Integer | Households | Estimated total households in the ward. | Nonnegative count | N/A | Raw `chicago-ward-income.csv`. |
| `pct_households_125k_plus` | Number | Percent (%) | Percentage of households in the $125,000-or-more bracket. | 0–100. | N/A | Raw `chicago-ward-income.csv`. |
| `median_household_income_est` | Integer | US dollars per year | Estimated median household income for the ward. | Nonnegative dollar estimate. | N/A | Raw `chicago-ward-income.csv`. Also used in the income-versus-crime plot. |

## Flock Cameras Dataset

Source: `cameras.geojson`

| Name | Data type | Units | What it means | Range or allowed values | Missing values | Source / derivation |
|---|---|---|---|---|---|---|
| `osmId` | Integer | OpenStreetMap identifier | OpenStreetMap object identifier for the mapped camera/location. | Positive integer. | Missing property or JSON `null` becomes null. | `properties.osmId` in `cameras.geojson`. |
| `osmType` | String | Object type | OpenStreetMap object type. | `node`, `way`, or `relation` as present in the file. | Missing property or JSON `null` becomes null. | `properties.osmType` in `cameras.geojson`. |
| `brand` | String | Brand label | Camera brand recorded in the map. | Text as recorded | Missing property or JSON `null` becomes null. | `properties.brand` in `cameras.geojson`. |
| `operator` | String | Operator label | Organization listed as operating the camera/location. | Text as recorded. | Missing property or JSON `null` becomes null. | `properties.operator` in `cameras.geojson`. |
| `ref` | String | Reference text | Reference or route identifier attached to the mapped feature. | Text as recorded. | Missing property or JSON `null` becomes null. | `properties.ref` in `cameras.geojson`. |
| `startDate` | String | Date/year text | Start date or year associated with the mapped feature. | Text as recorded. | Missing property or JSON `null` becomes null. | `properties.startDate` in `cameras.geojson`. |
| `osmTimestamp` | String timestamp | UTC date and time | Last-edit timestamp for the OpenStreetMap object. | ISO 8601 timestamp as recorded. | Missing property or JSON `null` becomes null. | `properties.osmTimestamp` in `cameras.geojson`. |
| `osmVersion` | Integer | Version number | OpenStreetMap object version. | Positive integer. | Missing property or JSON `null` becomes null. | `properties.osmVersion` in `cameras.geojson`. |
| `direction` | Number | Degrees clockwise from north | Direction associated with the mapped camera. | Bearing from 0 inclusive to 360 exclusive. | Missing property or JSON `null` becomes null. | `properties.direction` in `cameras.geojson`. |
| `directionCardinal` | String | Compass direction | Cardinal direction associated with the camera. | Compass label as recorded, such as `N`, `NE`, `E`, `SE`, `S`, `SW`, `W`, or `NW`. | Missing property or JSON `null` becomes null. | `properties.directionCardinal` in `cameras.geojson`. |
| `directions` | List of numbers | Degrees clockwise from north | One or more directions associated with the mapped feature. | List of bearings, each from 0 inclusive to 360 exclusive. | Missing property or JSON `null` becomes null. | `properties.directions` in `cameras.geojson`. |
| `mountType` | String | Mount type | Mounting type recorded for the camera. | Text as recorded, for example `pole`. | Missing property or JSON `null` becomes null. | `properties.mountType` in `cameras.geojson`. |
| `surveillanceZone` | String | Zone category | Type of area or activity monitored, when supplied. | Text as recorded, for example `traffic`. | Missing property or JSON `null` becomes null. | `properties.surveillanceZone` in `cameras.geojson`. |
| `geometry.coordinates` | List of numbers | Decimal degrees | GeoJSON Point coordinates, ordered as longitude then latitude. | Longitude -180 to 180; latitude -90 to 90. | Missing or null geometry is not usable for the distance calculation. | Raw `geometry.coordinates` in `cameras.geojson`. |
| `longitude` | Number | Decimal degrees | Longitude extracted from element 0 of the GeoJSON Point coordinates. | -180 to 180 | Null if geometry or coordinates are missing. | Created in `TrafficViolationFlockRelation.ipynb` from `geometry.coordinates[0]`. |
| `latitude` | Number | Decimal degrees | Latitude extracted from element 1 of the GeoJSON Point coordinates. | -90 to 90 | Null if geometry or coordinates are missing. | Created in `TrafficViolationFlockRelation.ipynb` from `geometry.coordinates[1]`. |

## Chicago City Dataset

Source: `chicago-city.geojson`

| Name | Data type | Units | What it means | Range or allowed values | Missing values | Source / derivation |
|---|---|---|---|---|---|---|
| `geometry.type` | String | Geometry type | Type of boundary geometry. | `MultiPolygon` in the supplied feature. | N/A | Raw `geometry.type` in `chicago-city.geojson`. |
| `geometry.coordinates` | Nested coordinate arrays | Decimal degrees | Polygon rings defining the Chicago city boundary. Coordinate order is longitude then latitude. | Coordinates lie in the Chicago area. | N/A | Raw `geometry.coordinates` in `chicago-city.geojson`. |

## Red Light and Speed Violations Datasets

Sources: `red_light_100000.csv` and `speed_violations_150000.csv`

| Name | Data type | Units | What it means | Range or allowed values | Missing values | Source / derivation |
|---|---|---|---|---|---|---|
| `VIOLATION DATE` | String date | Local calendar date | Date the traffic-camera violation record was issued. | `MM/DD/YYYY`. | Invalid or blank date parses as null. | Raw field in each traffic CSV. |
| `VIOLATIONS` | String in CSV; parsed number in analysis | Violations per exported record | Number of violations recorded for the row. Commas are removed before numeric parsing. | Nonnegative count | Invalid or blank values parse as null; such rows are dropped from monthly means and excluded from site summaries. | Raw field in each traffic CSV; parsed in `TrafficViolationFlockRelation.ipynb`. |
| `CAMERA ID` | String | Camera identifier | Traffic-camera identifier used to group records into sites. | Identifier as recorded. | Blank becomes null.| Raw field in each traffic CSV. |
| `LATITUDE` | Number | Decimal degrees | Latitude of the traffic-camera record. | -90 to 90 | Blank or invalid value parses as null. | Raw field in each traffic CSV. |
| `LONGITUDE` | Number | Decimal degrees | Longitude of the traffic-camera record. | -180 to 180 | Blank or invalid value parses as null. | Raw field in each traffic CSV. |

## Precomputed Monthly Comparison Datasets

Sources: `Clean_Monthly_Crimes.csv`, `Clean_Monthly_Red_Light.csv`, and
`Clean_Monthly_Speed.csv`

| Name | Data type | Units | What it means | Range or allowed values | Missing values | Source / derivation |
|---|---|---|---|---|---|---|
| `Timestamp` | Date | Month, represented by first day | Month to which each monthly measure applies. | `YYYY-MM-DD`; month starts from 2014-07-01 through 2026-08-01. | N/A | Raw column in each `Clean_Monthly_*.csv`; parsed by `pandas.to_datetime` in `TotalVehicleCrimeRelationToSpeedingAndRedLights.ipynb`. |
| `Total_Vehicle_Crimes` | Integer | Crime records per month | Precomputed monthly total of vehicle crimes. | Nonnegative integer count. | N/A | Raw `Clean_Monthly_Crimes.csv`.. |
| `Crime_Norm` | Number | Unitless normalized score | Precomputed normalized crime measure used to compare time patterns. | Numeric score. | N/A | Raw `Clean_Monthly_Crimes.csv`. |
| `Red_Light_Tickets` | Integer | Tickets per month | Precomputed monthly red-light-camera ticket total. | Nonnegative integer count. | N/A | Raw `Clean_Monthly_Red_Light.csv`. |
| `Red_Light_Norm` | Number | Unitless normalized score | Precomputed normalized red-light measure used to compare time patterns. | Numeric score. | N/A | Raw `Clean_Monthly_Red_Light.csv`. |
| `Speed_Tickets` | Integer | Tickets per month | Precomputed monthly speed-camera ticket total. | Nonnegative integer count. | N/A | Raw `Clean_Monthly_Speed.csv`. |
| `Speed_Norm` | Number | Unitless normalized score | Precomputed normalized speed measure used to compare time patterns. | Numeric score. | N/A | Raw `Clean_Monthly_Speed.csv`. |
