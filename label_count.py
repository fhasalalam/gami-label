# import packages
import os
import pandas as pd
import numpy as np

# define function
def extract_label(folder_path):
    label_list = []
    identifier_list = []
    # for every .txt file
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            # open file
            with open(file_path, 'r') as file:
                content = file.read().split()
                # store identifiers
                identifier_list.append(content[0])
                # murmur label list
                for i, word in enumerate(content):
                    if word == "#Murmur:" and i + 1 < len(content) and content[i + 1] in ["Absent", "Present", "Unknown"]:
                        label_list.append(content[i + 1])

    # create pd df and save as csv
    df = pd.DataFrame({"identifier": identifier_list, "murmur_label": label_list})
    df["label_quality"] = np.where(df["murmur_label"].isin(["Absent", "Present"]), "Good Label", "Bad Label")
    df.to_csv('murmur_labels.csv')
    
# run the function
extract_label("/Users/fhasalalam/Downloads/physionet_cau_umn_sub6/data")