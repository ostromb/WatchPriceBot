import pandas as pd
def main():
    df = pd.read_csv('PriceOverviewK4035.csv')
    #df['Price Difference'] = df['Lowest Price'] - df['price']
    #df['Discount'] = df['Lowest Price']/df['price'] 
    df1 = df[['Watchmodel','Price','Lowest Price','Price Difference','Volume','Discount','Certified']]
    print(df1.sort_values('Discount',ascending=False).head(60))
    
main()