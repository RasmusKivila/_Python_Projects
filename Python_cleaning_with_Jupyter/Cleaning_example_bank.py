import pandas as pd

class MyClass():
    def __init__(self, dataframe):
        self.dataframe = dataframe

def read_csv_file(file):
    df = pd.read_csv(file)  
    return df  

#def replace_number_columns(df):
 #   replacement_dict = {
 #       'HasCrCard': {0: 'No', 1: 'Yes'},
 #       'IsActiveMember': {0: 'No', 1: 'Yes'},
 #       'Exited': {0: 'No', 1: 'Yes'}
 #   }
 #   df.replace(replacement_dict, inplace=True)
    

def clean_data(df):
    # List of columns to apply the logic to
    columns_to_clean = ['RowNumber', 'CustomerId', 'Surname', 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Exited']
    columns_to_clean = df.drop_duplicates('CustomerId')
    # Apply the logic to the specified columns
    for column in columns_to_clean:
        df[column] = df[column].apply(lambda x: 'Unknown' if '?' in str(x) else x)

def save_to_file():
    output_file_path = "cleaned_bank_data.csv" 
    data_frame.to_csv(output_file_path, index=False)
    
# Instantiera
if __name__ == "__main__":
    file_path = "Churn_Modeling.csv"
    data_frame = read_csv_file(file_path)
    #replace_number_columns(data_frame)
    clean_data(data_frame)
    save_to_file()

