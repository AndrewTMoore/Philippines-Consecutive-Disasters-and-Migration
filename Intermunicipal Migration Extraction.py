###This code imports data for the 2010 Census of Population and Housing of the Philippines
###Each line of the imported file is a 60-digit number, with the meaning of each digit given in Census Results Metadata.docx
###A province from the census is selected and responses are recorded for respondents that had changed municipality of residence since 2005
import numpy as np
import pandas as pd
import xlwt

data_import    = pd.read_csv('ipumsi_00008.dat') #Imports entire original input data file
length         = len(data_import)                #Defines length of data file i.e. number of data entries
counter        = 0                               #Every loop that finds a resident that has moved municipality within the selected province will +1 to this counter
mun_2005       = []                              #This list is used to store 2005 municipal information
mun_2010       = []                              #This list is used to store 2010 municipal information
exception_list = [0000, 9997, 9998, 9999]        #This provides list of municipal codes to be rejected: 0000 = same city/municpality; 9997 = foreign country; 9998 = unknown;9999 = not in universe

###Records municipality of residence in 2005 and in 2010 for a selected province
for i in range(length - 1):                                         #Iterates through every surveyed individual from input data file
    if  int(data_import.loc[i][0][25:27]) == 01:                    #Filters for selected province, 01 = Abra province. Other codes shown in Census Results Metadata.docx
        if int(data_import.loc[i][0][56:60]) not in exception_list: #Filters for all responses that were not 0000 = previous residence was same province & municipality, 9997, 9998 or 9999
                mun_2005.append(data_import.loc[i][0][-4:])         #Adds IPUMS 2005 municipality code to list
                mun_2010.append(data_import.loc[i][0][37:42])       #Adds IPUMS 2010 municipality code to list
                counter = counter + 1

###Saves migration array to xls file
book   = xlwt.Workbook()                       #Defines xls workbook file
sheet1 = book.add_sheet("Municipal Migration") #Defines 1st sheet of xls file
for i in range(counter):                       #Iterates over as many rows of the migration_array as there were individuals that lived in a different municipality than in 2005
    sheet1.row(i+1).write(0, mun_2005[i])      #Writes each row of migration array (i.e. each respondent that moved municipality within their province) to output file
    sheet1.row(i+1).write(1, mun_2010[i])      #Writes each row of migration array (i.e. each respondent that moved municipality within their province) to output file
sheet1.row(0).write(0, '2005 Municipality')    #Automatically writes headers 
sheet1.row(0).write(1, '2010 Municipality')
book.save("IPUMS8_Kalinga_Municipal_Migration.xls")


 
