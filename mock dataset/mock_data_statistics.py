from category_encoders import *
import pandas as pd
import numpy as np

malware_names_file = "./MalwareTrainingSets-master/malware_names.csv"

fitDataFrame = pd.DataFrame(allEventsAndSensors)
windowDataFrame = pd.DataFrame(window)
 
print(fitDataFrame)

fitDataEvents = fitDataFrame.drop('sensor', axis = 1)
onlyWindowEvents = windowDataFrame.drop('sensor', axis = 1)
onlyWindowSensors = windowDataFrame.drop('event', axis = 1)

encoder = OneHotEncoder(cols=['event'])
encoder.fit(fitDataEvents)

allEvents = encoder.transform(fitDataEvents)
windowEvents = encoder.transform(onlyWindowEvents)
#sensors = sensor_encoder.transform(y)

print(allEvents)
print(windowEvents)

#print(sensors)