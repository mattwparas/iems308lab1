# Import necessary libraries
import pandas as pd
import numpy as np

# Read in the data
c_size = 10000000
data = pd.read_csv('Medicare_Provider_Util_Payment_PUF_CY2016.txt', sep = "\t", chunksize=c_size)

output = pd.DataFrame(data.get_chunk(c_size))
output = output.iloc[1:]
output = output.reset_index(drop=True)

chicago_zip_codes = [60007, 60018, 60068, 60106, 60131, 60176, 60601, 
60602, 60603, 60604, 60605, 60606, 60607, 60608, 60609, 60610, 60611, 
60612, 60613, 60614, 60615, 60616, 60617, 60618, 60619, 60620, 60621, 
60622, 60623, 60624, 60625, 60626, 60628, 60629, 60630, 60631, 60632, 
60633, 60634, 60636, 60637, 60638, 60639, 60640, 60641, 60642, 60643, 
60644, 60645, 60646, 60647, 60649, 60651, 60652, 60653, 60654, 60655, 
60656, 60657, 60659, 60660, 60661, 60706, 60707, 60714, 60804, 60827]

chicago_zip_codes = [str(x) for x in chicago_zip_codes]

Peer into the data
output['NPPES_PROVIDER_ZIP']

output['NPPES_PROVIDER_ZIP'] = output['NPPES_PROVIDER_ZIP'].astype(str).str[:5]
output['NPPES_PROVIDER_ZIP'] = output['NPPES_PROVIDER_ZIP'].str.replace('.', "")

output = output.loc[output['NPPES_PROVIDER_ZIP'].isin(chicago_zip_codes)]
output = output.loc[output['NPPES_PROVIDER_STATE'] == "IL"]
output = output.loc[output['NPPES_ENTITY_CODE'] == 'I']

output.to_csv("chicago_data.csv", index = False)

