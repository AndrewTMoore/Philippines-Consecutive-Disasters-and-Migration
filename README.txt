Date: 28th June 2020
This file describes the metadata used in a master's thesis investigating the links between consecutive disaster occurrence and internal migration in the Philippines from 01/05/2005 
to 01/05/2010. For more information, please contact the original author, Andrew Moore: andrew_thomas_moore@hotmail.co.uk

FILES AND DESCRIPTIONs
----------------------
Disaster Migration Regression Analysis:
For each province of the Philippines the following values are listed for 01/05/2005 - 01/05/2010:
	>Net number of migrants moving into/out of that province
	>Number of disasters due to earthquakes, floods, mass movements, tropical cyclones or volcanic activity
	>Number of consecutive disasters
	>Cumulative Disaster Impact Index - which is a measure of the human impact due to each disaster nationwide

Disaster Timeline Philippines 01-May-2005 - 01-May-2010: 
There are 3 sheets in this file
1) For each province of the Philippines, disaster occurrence, consecutive disaster occurrence and cumulative impact are given
2) For each province a timeline of events is give, including:
	>Hazard type	
	>Start date & end date
	>Disaster Impact Index
	>Days between events
	>If disaster was part of a consecutive disaster or not	
3) Chronological lists of disasters in the Philippines, incluidng the following variables
	>Hazard type
	>Start date
	>End date
	>Notes
	>Storm Name (given names for tropical cyclones)
	>Latitude & Longitude
	>Disaster Impact Index 
	>Number of people affected
	>Casualties
	>Cost of damage (in US dollars)
	>People displaced

Metadata for all Original Data Source: 
This contains the name, description, variable, source and various notes about all of the databases used for research in the thesis, including the many sources that were considered but ultimately not used

INTERNAL MIGRATION FOLDER
Census Results Metadata:
The raw data of the 2010 Philippines National Census is 9,400,000+ numbers, which are each 60 digits in length. 
This file explains the meaning of these digits.
The original file is not included in this data collection as it is 500 MB in size. It is available from the International Public Use Microdata Series upon request: https://international.ipums.org/international-action/variables/group

Intermunicipal Migration Extraction:
This is the script written to extract information from the census results about respondents who changed municipality of residence within a chosen province between 01/05/2005 and 01/05/2010 using Python 3.8. 

Interprovincial Migration Extraction:
This is the script written to extract information from the census results about respondents who changed province of residence between 01/05/2005 and 01/05/2010 using Python 3.8. 

Interprovincial Migration Processing:
This file processes the data extracted from the 2010 Philippines National Census in order to calculate the net migrants moving into/out of each province. It contains 7 different sheets:
1) Gives the administrative designation of each province in 2005 and in 2010. Population are also listed
2) Gives the name and number of each province and municipality according to both the 2005 and 2010 time periods
3) Provides a simplified matrix to compare and consolidate differences in provincial classification in 2005 and 2010
4) Is the data extracted from the census using a previously-specified scripts written for Python 3.8. Columns show where respondents lived in 2005 and rows where they lived in 2010
5) Extrapolates provincial movement to the 10.2% population sample from the census up to the entire population. This is done by multiplying each matrix cell by (Province population / people surveyed in that province)
6) Calculates the net migrants into/out of each province based on the data in the previous sheet.
7) Calculates the net migrants into/out of provinces that had to be combined due to differences in the 2005 and 2010 census administrative areas
