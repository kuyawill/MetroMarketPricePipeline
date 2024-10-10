from sqlalchemy import create_engine
import pandas as pd

from Shared_func import save_data, today_links

def load(dataframe):

    username = ''#your user name
    password = ''#your password
    host = 'localhost'  # or your host
    port = '3306'  # default MySQL port
    database = 'sql_bantaypresyodb'

    # Create a connection engine using MySQLdb
    try:
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@{host}:{port}/{database}')
    except Exception as e:
        print(f"Connection error occured: {e}")

    try:
    # Append data to the existing table
        df = dataframe
        df.to_sql('bantay_presyo', con=engine, if_exists='append', index=False)
        print("Data appended successfully!")
        save_data(today_links)
    except Exception as e:
        print(f"An error occurred: {e}")
