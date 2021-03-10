import os
import pandas as pd
import numpy as np

os.chdir(os.path.dirname(__file__))
source = pd.read_excel("") # Insert source XLSX file
# source["Student ID"] = source["Student ID"] + 1000000

for cohort in range(6,11):
    mysource = source[source["Cohort"] == cohort]
    destination = pd.read_csv("Group {}.csv".format(cohort))
    destination["HW4 [Total Pts: 18 Score] |20026"] = [None] * destination.shape[0]
    for index, row in mysource.iterrows():
        if not row["Student ID"] in list(destination["Student ID"]):
            print(row["Student ID"])
        else:
            destination["HW4 [Total Pts: 18 Score] |20026"][destination["Student ID"] == row["Student ID"]] = row["Grade"]
    # destination.to_csv("Group {} - filled.csv".format(cohort))
