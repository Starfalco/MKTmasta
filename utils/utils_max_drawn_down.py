import pandas as pd

def build_max_drawn_down(my_df):

        MDD = 0
        data = {} 
        
        for index in range(1, len(my_df)):
            gap = my_df.loc[len(my_df)-1,'Close']/my_df.loc[len(my_df) - index,'Close'] - 1
            if gap < MDD:
                
                MDD = gap
                occurrence = my_df.loc[len(my_df)-index,'Date']
                MaxPrice = my_df.loc[len(my_df)-index,'Close']
                data = {'max_drawn_down':[MDD], 'occurrence':[occurrence], 'max_price':[MaxPrice]} 
        
        output = pd.DataFrame(data, index = [0])
        
        return output