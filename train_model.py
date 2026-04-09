import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
    "age":[45,54,63,37,41,56,57,62],
    "cholesterol":[230,250,180,210,190,240,300,280],
    "bp":[130,140,120,110,135,150,160,145],
    "max_hr":[150,140,130,170,160,120,110,115],
    "target":[1,1,1,0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df.drop("target",axis=1)
y = df["target"]

model = RandomForestClassifier()
model.fit(X,y)

pickle.dump(model,open("model.pkl","wb"))

print("Model created successfully")