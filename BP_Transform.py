import pandas as pd
from BP_Load import load

import re

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def process(value):

    try:
        if '-' in value:
            start, end = map(float, value.split('-'))
            return (start + end) / 2
        elif is_float(value) == True:
            return float(value)
        else:
            return None
    except ValueError:
        print(f"Error processing value: {value}")
        return None


def transform(table):
    # Process each DataFrame in the table list
    for i in table:
        df = pd.DataFrame(i)
        
        # Clean the data
        df.columns = df.iloc[0]
        df.drop(index=0, inplace=True)
        df.columns = df.columns.astype(str)
        df.columns = df.columns.str.replace(' ', '_')
        df.columns = df.columns.str.replace('\n', '_')
        df.columns = df.columns.str.replace('_(', '(')
        df.columns = df.columns.str.replace('/Pigue', '(Pigue)')
        df.columns = df.columns.str.replace('_Liempo', '(Liempo)')
        df.columns = df.columns.str.replace('*', '')
        df.columns = df.columns.str.capitalize()
        df.columns = df.columns.str.replace('(', '_')
        df.columns = df.columns.str.replace(')', '')
        df.columns = df.columns.str.replace('-','_')
        df.rename(columns={'_wcohirtne':'Corn_white'},inplace=True)
        df.rename(columns={'_yceollornw':'Corn_yellow'},inplace=True)
        # Process the 'Market' column
        

        # Update 'City' based on 'Market'
        df['City'] = ''
        for i in range(1,len(df)+1):
            market = df.loc[i, 'Market']
            if market in ['Blumentritt Market', 'Cartimar Market', 'Dagonoy Market', 'Paco Market', 'Pritil Market/Manila', 'Quinta Market/Manila', 'San Andres Market/Manila', 'Trabajo Market']:
                df.loc[i, 'City'] = 'Manila'
            elif market in ['Agora Public Market/San Juan']:
                df.loc[i, 'City'] = 'San Juan'
            elif market in ['Balintawak (Cloverleaf) Market', 'Commonwealth Market/Quezon City', 'Kamuning Public Market', 'Mega Q-mart/Quezon City', 'Muñoz Market/Quezon City', 'Murphy Public Market']:
                df.loc[i, 'City'] = 'Quezon City'
            elif market in ['Bicutan Market', 'Taguig People\'s Market']:
                df.loc[i, 'City'] = 'Taguig'
            elif market in ['Guadalupe Public Market/Makati']:
                df.loc[i, 'City'] = 'Makati'
            elif market in ['La Huerta Market/Parañaque']:
                df.loc[i, 'City'] = 'Parañaque'
            elif market in ['New Las Piñas City Public Market']:
                df.loc[i, 'City'] = 'Las Piñas'
            elif market in ['Malabon Central Market']:
                df.loc[i, 'City'] = 'Malabon'
            elif market in ['Mandaluyong Public Market']:
                df.loc[i, 'City'] = 'Mandaluyong'
            elif market in ['Marikina Public Market']:
                df.loc[i, 'City'] = 'Marikina'
            elif market in ['Maypajo Public Market/Caloocan']:
                df.loc[i, 'City'] = 'Caloocan'
            elif market in ['Pamilihang Lungsod ng Muntinlupa']:
                df.loc[i, 'City'] = 'Muntinlupa'
            elif market in ['Navotas Agora Market']:
                df.loc[i, 'City'] = 'Navotas'
            elif market in ['New Marulas Public Market/Valenzuela']:
                df.loc[i, 'City'] = 'Valenzuela'
            elif market in ['Pasay City Market']:
                df.loc[i, 'City'] = 'Pasay'
            elif market in ['Pasig City Mega Market']:
                df.loc[i, 'City'] = 'Pasig'
            elif market in ['Pateros Market']:
                df.loc[i, 'City'] = 'Pateros'
            else:
                df.loc[i, 'City'] = 'Unknown'  # Or any default value if the market is not found

        # Convert all price ranges to their average price
        cols = [
            'Well_milled_rice_local', 'Corn_white', 'Corn_yellow', 'Tilapia',
            'Galunggong', 'Egg_medium', 'Ampalaya', 'Tomato', 'Cabbage_rareball',
            'Cabbage_scorpio', 'Cabbage_wonderball', 'Pechay_baguio',
            'Red_onion_local', 'Sugar_washed', 'Fresh_pork_kasim_pigue',
            'Frozen_pork_kasim_pigue', 'Fresh_pork_liempo', 'Frozen_pork_liempo',
            'Fresh_whole_chicken'
        ]
        for col in cols:
            if col in df.columns:
                df[col] = df[col].apply(process)  # Ensure 'process' is defined
        
        #Data type format
        cols = df.columns

        
        '''
        print(cols)
        for i, col in enumerate(cols):
            if i == 0 or i == 21:
                df[col] = df[col].astype(str)
            elif i == 20:
                df[col] = pd.to_datetime(df[col])
            else:
                try:
                    df[col] = df[col].astype(float)  # Attempt to convert to float
                except ValueError:
                    print(f"Column {col} could not be converted to float. Column type remains unchanged.")'''
        load(df) 
    #print(df.head())
    
