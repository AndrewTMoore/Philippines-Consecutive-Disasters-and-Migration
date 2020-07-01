###This code imports data for the 2010 Census of Population and Housing of the Philippines
###Each line of the imported file is a 60-digit number, with the meaning of each digit given in Census Results Metadata.docx
###Respondents that lived in a different municipality in 2005 and 2010 are selected, with a matrix used to record the total movement between provinces
import numpy as np
import pandas as pd
import xlwt
 
data_import       = pd.read_csv('ipumsi_00008.dat')         #Imports entire original input data file of original IPUMS_00008.dat file
length            = len(data_import)                        #Defines length of data file i.e. number of data entries
output_data_array = []                                      #Creates empty array for outputing cleaned version (i.e. only inter-provincial migrants) 
migration_array   = np.zeros(shape=(99,99), dtype=int)      #Creates a 99x99 2D array for calculating number of migrants between each and every province. This means for province 1, how many migrants from province 2, 3, 4 etc.; for province 2, how many migrants from province 1, 3, 4 etc.
height            = migration_array.shape[0]                #Defines height of interprovincial migration array
width             = migration_array.shape[1]                #Defines width of interprovincial migration array
in_mig_array      = np.zeros(width)                         #Creates array for total in-migration for each province
out_mig_array     = np.zeros(height)                        #Creates array for total out-migration for each province
exception_list    = [97, 99]                                #Creates list of exceptions for 2005 province codes i.e. 97 (foreign country) and 99 (not in universe)

###Records previous & current province of residence for all interprov migrants
for i in range(length - 1):                                      #Iterates through every surveyed individual from input data file.
    if  int(data_import.loc[i][0][54:56]) not in exception_list: #Tests if each surveyed individual has changed province of residence within country (i.e. previous province code not equal to 97 or 99)
        prov_2010   = int(data_import.loc[i][0][25:27])          #Reads 26th-27th digits of data entry i.e. 2010 province of residence code (e.g. 01 = Abra). There are some differences in province codes between 2010 & 2005 data (see Philippines Interprovincial Migration Excel file)
        prov_2005   = int(data_import.loc[i][0][54:56])          #Reads 55th-56th digits of data entry i.e. 2005 province of residence code (e.g. 01 = Abra). There are some differences in province codes between 2010 & 2005 data (see Philippines Interprovincial Migration Excel file)
        migration_array[prov_2010 -1, prov_2005 -1] = migration_array[prov_2010 -1, prov_2005 -1] + int(1) #Adds +1 to the row and column of the migration matrix corresponding to the xth 2010 province 
                                                                                                           #and the yth 2005 province. As the 1st provinces are both labelled 1, but numpy arrays begin indexing at 0, a -1 is added
###Saves migration array to xls file
book   = xlwt.Workbook()            #Defines xls workbook file
sheet1 = book.add_sheet("Sheet 1")  #Defines 1st sheet of xls file

#Calculates in-migration
for i in range(height):                                                 #Iterates over each migration_array row
    sheet1.row(i+1).write(0, 'Province ' + str(i+1))                    #Automatically writes row headers (starting on 2nd row, hence the i+1 term)
    sheet1.row(i+1).write(width + 1, int(sum(migration_array[i,:])))    #Automatically sums total in-migration for 2010 province i
    in_mig_array[i] = sum(migration_array[i,:])                         #Records total in-migration for ith province
    for j in range(width):                                              #Iterates over each migration_array column
         sheet1.row(i+1).write(j+1, int(migration_array[i,j]))          #Adds filtered data to output xls file (starting on 2nd row, hence the i+1 term)

#Calculates out-migration
for j in range(width):                                                  #Iterates over each migration_array column
    sheet1.row(0).write(j+1, 'Province ' + str(j+1))                    #Automatically writes column headers
    sheet1.row(height + 1).write(j + 1, int(sum(migration_array[:,j]))) #Automatically sums total out-migration for 2005 province j
    out_mig_array[j] = sum(migration_array[:,j])                        #Records total out-migration for jth province

#Calculates net migration
net_migration = in_mig_array - out_mig_array                            #Calculates net migration (i.e. net in-migration is positive)
for i in range(height):                                                 #Iterates over every province once (i.e. every province over the 2005-2010 period)
    sheet1.row(i+1).write(width+2, net_migration[i])                    #Writes calculated net migration to xls file

#Calculates number of people surveyed in each province for normalisation purposes
prov_num_counter = np.zeros(shape = (99,1), dtype=int)                     #Defines array for storing counts of how many individuals are surveyed from each province
for i in range(length - 1):                                                #Iterates over every row in imported data (except last one due to some error discovered earlier on in coding process)
    prov_number = int(data_import.loc[i][0][25:27])                        #26th & 27th digits of data entry are 2010 province number 
    prov_num_counter[prov_number] = prov_num_counter[prov_number] + int(1) #Adds 1 to respective row in province counter array
for i in range(99):                                                        #Iterates over each row in province counter array
    sheet1.row(i+1).write(width+3, int(prov_num_counter[i]))               #Writes calculated people surveyed per province to xls file. int() function is because code failed without using it

#Writes headers for output file
sheet1.row(height + 1).write(0, 'Total Out-migration')                  #Automatically writes header for total out-migration
sheet1.row(0).        write(width+1, 'Total In-migration')              #Automatically writes header for total in-migration
sheet1.row(0).        write(width+2, 'Total Net Migration')             #Automatically writes header for total out-migration
sheet1.row(0).        write(width+3, 'Total People Surveyed')           #Automatically writes header for total people surveyed in each province
book.save("IPUMS8 2010 Census.xls")



 
