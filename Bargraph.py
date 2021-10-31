import pandas as pd
import plotly.express as px

df = pd.read_csv("Data.csv")
graph = px.bar(df, x = "Country", y = "InternetUsers")
graph.show()
