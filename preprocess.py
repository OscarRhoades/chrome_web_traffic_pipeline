import csv
import pandas as pd


def append_to_csv(file_path, new_row):
    try:
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(new_row)
        print(f"Row added to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
        
def read_csv_process_time(file):
    df = pd.read_csv(file, header=None)
    df.columns = ['time', 'info', 'type']
    
    df['time'] = pd.to_datetime(df['time'])

    
    df['time_delta'] = df['time'].diff().dt.total_seconds().fillna(0)
    print(df)
    return df
    

def create_action_list_with_variable_deltas():

    action_list = []

    df = read_csv_process_time('action_data.csv')
    for _, row in df.iterrows():
        action_list.append('t<' + str(row['time_delta']) + '>')
        action_list.append(f'{row['type']}' + " : " +  f'{row['info']}')
        
    
    
    for row in action_list:
        print(row)
        append_to_csv('action_tokens.csv', [row])
    
    return action_list   
        
create_action_list_with_variable_deltas()