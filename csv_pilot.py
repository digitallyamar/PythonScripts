import pandas as pd

df = pd.read_csv('ssd1306_data.csv')

if __name__ == "__main__":
    # Let's say we want to read other_tags column data
    col_name = 'other_tags'

    tags = []

    # Read each row of the column
    for row in df[col_name]:
        # Add comma separated tags in row to tags list
        print(row)
        print(row.split(','))    

