class import_data: 
    def get_df(): 
        import pandas as pd 
        DF1 = pd.read_excel('/Users/tonderaimadamba/Documents/Client Work/Ryan/tax mapper/client_data/Dataset1_SamplePopulation_CandyBeverages_Compiled.xlsx',skiprows = range(0, 3),)
        DF2 = pd.read_excel('/Users/tonderaimadamba/Documents/Client Work/Ryan/tax mapper/client_data/SamplePopulation_Albertsons_CandyBeverages_Compiled.xlsx',skiprows = range(0, 3),usecols=('B:H'),dtype={'UPC': str})
        DF3 = pd.read_excel('/Users/tonderaimadamba/Documents/Client Work/Ryan/tax mapper/client_data/SamplePopulation_Albertsons_HealthBeauty_Compiled.xlsx',skiprows = range(0, 3),usecols=('B:H'),dtype={'UPC': str})
        return DF1, DF2, DF3
