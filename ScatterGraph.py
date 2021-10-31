import pandas as pd
import plotly.express as px

df = pd.read_csv("Data.csv")
graph = px.scatter(df, x = "Population", y = "Per capita", color = "Country", title = "Per Capita Income", size = "Percentage", size_max = 60)
graph.show()
