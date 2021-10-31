import pandas as pd
import plotly.express as px

df = pd.read_csv("LineChart.csv")
graph = px.line(df, x = "Year", y = "Per capita income", color = "Country", title = "Per Capita Income")
graph.show()
