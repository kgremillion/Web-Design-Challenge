import pandas as pd

# Use Pandas to read CSV & save into variable
city_data = pd.read_csv("../Resources/cities.csv")

# Convert dataframe into html table and save to file
city_data.to_html("City_Table.html")

# Save html table into variable
city_html = city_data.to_html()