class import_data: 
    def get_df(): 
        import pandas as pd 
        DF1 = pd.read_excel('Compiled_1.xlsx',skiprows = range(0, 3),)
        DF2 = pd.read_excel('Compiled_2.xlsx',skiprows = range(0, 3),usecols=('B:H'),dtype={'UPC': str})
        DF3 = pd.read_excel('Compiled_3.xlsx',skiprows = range(0, 3),usecols=('B:H'),dtype={'UPC': str})
        return DF1, DF2, DF3
