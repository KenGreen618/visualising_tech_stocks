## Visualizing Tech Stocks

In this project you will analyze and visualize the top 5 highest valued technology stocks, as of the end of the first half of 2019:
* Microsoft (NASDAQ:MSFT)
* Amazon (NASDAQ:AMZN)
* Apple (NASDAQ:AAPL)
* Alphabet (NASDAQ:GOOG)
* Facebook (NASDAQ:FB).

Using Pandas, Pandas-Datarader, and Matplotlib, you will take a visual look into the similarities and differences between these stocks during the six month period from January through June 2019. In your analysis you will perform the following:
1. Visualize the stock prices using matplotlib
2. Calculate and visualize the daily simple rate of return 
3. Calculate and visualize the mean rates of return
4. Calculate and visualize the variances of the returns
5. Calculate and visualize the standard deviations of the returns
6. Write a short thesis based on the correlations between the tech stocks

### 1. Import Packages

#### Step 1: Import Data Manipulation Packages
Import the pandas and numpy module as `pd` and `np`, respectively


```python
import pandas as pd
import numpy as np
```

#### Step 2: Import Financial Package
Import the pandas data reader module as `web`. (Ensure the module is installed with `pip install pandas-datareader` on the command line)


```python
import pandas_datareader.data as web
```

#### Step 3: Import Visualization Package
Import the matplotlib `pyplot` module as `plt`. (Write `%matplotlib inline` below the import statement to allow your visualizations to appear beneath the code that generates them)


```python
from matplotlib import pyplot as plt
%matplotlib inline
from datetime import datetime
```

### 2. Load the adjusted closings for the top 5 tech stocks.

#### Step 1: Define Stocks
Create a list named `symbols` containing the symbols for the top 5 tech stocks.
#### Step 2: Create Dates
Create a datetime object representing January 1st, 2019 named `start_date` and a datetime object representing July 1st, 2019 named `end_date`.
#### Step 3: Retrieve Data
Call the function `web.get_data_yahoo()` with arguments `symbols`, `start_date` and `end_date` and save the result to `stock_data`.
#### Step 4: View Data
View both `stock_data` and `stock_data['Adj Close']`. What information is stored in these DataFrames?


```python
symbols = ['MSFT', 'AMZN', 'AAPL', 'GOOG', 'FB']
start_date = datetime(2019, 1, 1)
end_date = datetime(2019, 7, 1)

stock_data = web.get_data_yahoo(symbols, start_date, end_date)
print(stock_data)
print(stock_data['Adj Close'])
```

    Attributes   Adj Close                                                   \
    Symbols           MSFT         AMZN       AAPL         GOOG          FB   
    Date                                                                      
    2019-01-02   97.580658  1539.130005  38.277527  1045.849976  135.679993   
    2019-01-03   93.990868  1500.280029  34.464798  1016.059998  131.740005   
    2019-01-04   98.362320  1575.390015  35.936077  1070.709961  137.949997   
    2019-01-07   98.487770  1629.510010  35.856094  1068.390015  138.050003   
    2019-01-08   99.201866  1656.579956  36.539616  1076.280029  142.529999   
    ...                ...          ...        ...          ...         ...   
    2019-06-25  129.788330  1878.270020  47.789978  1086.349976  188.839996   
    2019-06-26  130.274673  1897.829956  48.823631  1079.800049  187.660004   
    2019-06-27  130.488647  1904.280029  48.808968  1076.010010  189.500000   
    2019-06-28  130.303864  1893.630005  48.364223  1080.910034  193.000000   
    2019-07-01  131.976883  1922.189941  49.251266  1097.949951  193.000000   
    
    Attributes       Close                                                   ...  \
    Symbols           MSFT         AMZN       AAPL         GOOG          FB  ...   
    Date                                                                     ...   
    2019-01-02  101.120003  1539.130005  39.480000  1045.849976  135.679993  ...   
    2019-01-03   97.400002  1500.280029  35.547501  1016.059998  131.740005  ...   
    2019-01-04  101.930000  1575.390015  37.064999  1070.709961  137.949997  ...   
    2019-01-07  102.059998  1629.510010  36.982498  1068.390015  138.050003  ...   
    2019-01-08  102.800003  1656.579956  37.687500  1076.280029  142.529999  ...   
    ...                ...          ...        ...          ...         ...  ...   
    2019-06-25  133.429993  1878.270020  48.892502  1086.349976  188.839996  ...   
    2019-06-26  133.929993  1897.829956  49.950001  1079.800049  187.660004  ...   
    2019-06-27  134.149994  1904.280029  49.935001  1076.010010  189.500000  ...   
    2019-06-28  133.960007  1893.630005  49.480000  1080.910034  193.000000  ...   
    2019-07-01  135.679993  1922.189941  50.387501  1097.949951  193.000000  ...   
    
    Attributes        Open                                                   \
    Symbols           MSFT         AMZN       AAPL         GOOG          FB   
    Date                                                                      
    2019-01-02   99.550003  1465.199951  38.722500  1016.570007  128.990005   
    2019-01-03  100.099998  1520.010010  35.994999  1041.000000  134.690002   
    2019-01-04   99.720001  1530.000000  36.132500  1032.589966  134.009995   
    2019-01-07  101.639999  1602.310059  37.174999  1071.500000  137.559998   
    2019-01-08  103.040001  1664.689941  37.389999  1076.109985  139.889999   
    ...                ...          ...        ...          ...         ...   
    2019-06-25  137.250000  1911.839966  49.607498  1112.660034  192.880005   
    2019-06-26  134.350006  1892.479980  49.442501  1086.500000  189.539993   
    2019-06-27  134.139999  1902.000000  50.072498  1084.000000  189.880005   
    2019-06-28  134.570007  1909.099976  49.669998  1076.390015  190.550003   
    2019-07-01  136.630005  1922.979980  50.792500  1098.000000  195.210007   
    
    Attributes      Volume                                                 
    Symbols           MSFT       AMZN         AAPL       GOOG          FB  
    Date                                                                   
    2019-01-02  35329300.0  7983100.0  148158800.0  1532600.0  28146200.0  
    2019-01-03  42579100.0  6975600.0  365248800.0  1841100.0  22717900.0  
    2019-01-04  44060600.0  9182600.0  234428400.0  2093900.0  29002100.0  
    2019-01-07  35656100.0  7993200.0  219111200.0  1981900.0  20089300.0  
    2019-01-08  31514400.0  8881400.0  164101200.0  1764900.0  26263800.0  
    ...                ...        ...          ...        ...         ...  
    2019-06-25  33327400.0  3012300.0   84281200.0  1546900.0  16750300.0  
    2019-06-26  23657700.0  2441900.0  104270000.0  1810900.0  12808600.0  
    2019-06-27  16557500.0  2141700.0   83598800.0  1004300.0  11159000.0  
    2019-06-28  30043000.0  3037400.0  124442400.0  1693200.0  16378900.0  
    2019-07-01  22613500.0  3192100.0  109012000.0  1436300.0  14181800.0  
    
    [125 rows x 30 columns]
    Symbols           MSFT         AMZN       AAPL         GOOG          FB
    Date                                                                   
    2019-01-02   97.580658  1539.130005  38.277527  1045.849976  135.679993
    2019-01-03   93.990868  1500.280029  34.464798  1016.059998  131.740005
    2019-01-04   98.362320  1575.390015  35.936077  1070.709961  137.949997
    2019-01-07   98.487770  1629.510010  35.856094  1068.390015  138.050003
    2019-01-08   99.201866  1656.579956  36.539616  1076.280029  142.529999
    ...                ...          ...        ...          ...         ...
    2019-06-25  129.788330  1878.270020  47.789978  1086.349976  188.839996
    2019-06-26  130.274673  1897.829956  48.823631  1079.800049  187.660004
    2019-06-27  130.488647  1904.280029  48.808968  1076.010010  189.500000
    2019-06-28  130.303864  1893.630005  48.364223  1080.910034  193.000000
    2019-07-01  131.976883  1922.189941  49.251266  1097.949951  193.000000
    
    [125 rows x 5 columns]
    

### 3. Plot the adjusted closing prices over time.

Create a plot with matplotlib that shows the adjusted closing prices of each stock over time. Set the x label to `"Date"`. Set the y label to `"Adjusted Closing Price Over Time"`. Set the graph title to `"Tech Stocks Adjusted Price"`.


```python
adj_close_df = stock_data['Adj Close']
print(adj_close_df)

adj_close_df.plot()
plt.ylabel("Adjusted Closing Price Over Time")
plt.xlabel("Date")
plt.title("Tech Stocks Adjusted Price")
plt.show()
```

    Symbols           MSFT         AMZN       AAPL         GOOG          FB
    Date                                                                   
    2019-01-02   97.580658  1539.130005  38.277527  1045.849976  135.679993
    2019-01-03   93.990868  1500.280029  34.464798  1016.059998  131.740005
    2019-01-04   98.362320  1575.390015  35.936077  1070.709961  137.949997
    2019-01-07   98.487770  1629.510010  35.856094  1068.390015  138.050003
    2019-01-08   99.201866  1656.579956  36.539616  1076.280029  142.529999
    ...                ...          ...        ...          ...         ...
    2019-06-25  129.788330  1878.270020  47.789978  1086.349976  188.839996
    2019-06-26  130.274673  1897.829956  48.823631  1079.800049  187.660004
    2019-06-27  130.488647  1904.280029  48.808968  1076.010010  189.500000
    2019-06-28  130.303864  1893.630005  48.364223  1080.910034  193.000000
    2019-07-01  131.976883  1922.189941  49.251266  1097.949951  193.000000
    
    [125 rows x 5 columns]
    


    
![png](output_14_1.png)
    


### 4. Calculate and plot the daily simple rate of return over time.
Create a plot with matplotlib that shows the daily simple rate of return for each tech stock over time. Label the graph appropriately. 


```python

stock_returns_df = adj_close_df.pct_change()
stock_returns_df.plot()
plt.ylabel("Returns Over Time")
plt.xlabel("Date")
plt.title("Tech Stocks Returns")
plt.figure(figsize=(16,9))
plt.show()
```


    
![png](output_16_0.png)
    



    <Figure size 1152x648 with 0 Axes>


### 5. Create subplots of daily simple rate of return.
In order to better visualize the daily returns, create a subplot for each tech stock. 


```python
plt.figure(figsize=(15,15))
plt.subplot(3,2,1)
stock_returns_df['MSFT'].plot()
plt.ylabel("Returns Over Time")
plt.xlabel("Date")
plt.title("MSFT Returns")

plt.subplot(3,2,2)
stock_returns_df['AMZN'].plot()
plt.ylabel("Returns Over Time")
plt.xlabel("Date")
plt.title("AMZN Returns")

plt.subplot(3,2,3)
stock_returns_df['AAPL'].plot()
plt.ylabel("Returns Over Time")
plt.xlabel("Date")
plt.title("AAPL Returns")

plt.subplot(3,2,4)
stock_returns_df['GOOG'].plot()
plt.ylabel("Returns Over Time")
plt.xlabel("Date")
plt.title("GOOG Returns")

plt.subplot(3,2,5)
stock_returns_df['FB'].plot()
plt.ylabel("Returns Over Time")
plt.xlabel("Date")
plt.title("FB Returns")

plt.subplots_adjust(wspace=0.35, hspace=0.65)
plt.show()
```


    
![png](output_18_0.png)
    


### 6. Calculate and plot the mean of each tech stock's daily simple rate of return

#### Step 1: Calculate mean rate of return
For each stock, calculate the mean daily simple rate of return.
#### Step 2: Plot bar chart
Use matplotlib to create a bar chart comparing the mean daily simple rate of return for each stock. Label the chart appropriately
#### Step 3: Analyze mean rate of return
Based on the mean rate of return, which stock would be the best option to invest in?


```python
# my method
average_returns = stock_returns_df.mean()
plt.bar(range(len(list(average_returns))), list(average_returns))
ax = plt.subplot()
ax.set_xticks(range(len(list(average_returns))))
ax.set_xticklabels(symbols)
plt.ylabel("Average Returns")
plt.xlabel("Stock")
plt.title("Average return comparison")
plt.show()

# solution method

daily_mean = stock_returns_df.mean()
print(daily_mean)
print(daily_mean.keys())
height = []
for key in daily_mean.keys():
    height.append(daily_mean[key])
height
x_pos = np.arange(len(daily_mean.keys()))

plt.bar(x_pos, height)
plt.xticks(x_pos, daily_mean.keys())
plt.xlabel("Tech_Stocks")
plt.ylabel("daily mean")
plt.title("daily mean rate of return")

plt.show()
```


    
![png](output_21_0.png)
    


    Symbols
    MSFT    0.002532
    AMZN    0.001933
    AAPL    0.002208
    GOOG    0.000522
    FB      0.003046
    dtype: float64
    Index(['MSFT', 'AMZN', 'AAPL', 'GOOG', 'FB'], dtype='object', name='Symbols')
    


    
![png](output_21_2.png)
    


Facebook has the highest mean simple rate of return over the period of data collected. Thus Facebook would have been a good choice for investment over this period of time. Google, on the other hand, has the lowest mean simple rate of return over the period.

### 7. Calculate and plot the variance.

#### Step 1: Calculate the variance
For each stock, calculate the variance of the mean daily simple rate of return.
#### Step 2: Plot bar chart
Use matplotlib to create a bar chart comparing the variance for each stock. Label the chart appropriately
#### Step 3: Analyse the variance
Based on the variance, which stock would be the riskiest to invest in?


```python
returns_variance = stock_returns_df.var()

height = []
for key in returns_variance.keys():
    height.append(returns_variance[key])
x_pos = np.arange(len(returns_variance.keys()))

plt.bar(x_pos, height)
plt.xticks(x_pos, returns_variance.keys())
plt.xlabel("Tech_Stocks")
plt.ylabel("Variance")
plt.title("Daily Variance comparision")

plt.show()
```


    
![png](output_25_0.png)
    


Facebook shows the highest variance of all the stocks, indicating it can be a riskier investment. Google shows the lowest variance, indicating that the returns are more predictable. This goes along with the typical understanding of higher return, high risks stocks, and lower return, low risk stocks.

### 8. Calculate and plot the standard deviation

#### Step 1: Calculate the standard deviation
For each stock, calculate the standard deviation of the mean daily simple rate of return.

#### Step 2: Plot the bar chart
Use matplotlib to create a bar chart comparing the standard deviation of the mean daily simple rate of return of each stock. Label the chart appropriately

#### Step 3: Analyze the standard deviation
Based on the standard deviation of the rates of return, which stock would you choose to invest in and why?


```python
returns_std_dev= stock_returns_df.std()
returns_std_dev
height = []
for key in returns_std_dev.keys():
    height.append(returns_std_dev[key])
x_pos = np.arange(len(returns_std_dev.keys()))

plt.bar(x_pos, height)
plt.xticks(x_pos, returns_std_dev.keys())
plt.xlabel("Tech_Stocks")
plt.ylabel("Variance")
plt.title("Daily Std Deviation comparision")

plt.show()
```


    
![png](output_29_0.png)
    


The answer to this question depends on your investment preferences. Facebook is the most volatile stock, as it has the largest standard deviation. It also, however, has the largest mean return. If you are a more risky investor, this could be your stock of choice. Google, on the other hand, is the least volatile stock, but has the lowest mean return.

### 9. Calculate the correlations
Calculate the correlations between each of the stocks. Which stocks are positively correlated? Which are negatively correlated? Which have little correlation?


```python
stock_returns_df.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Symbols</th>
      <th>MSFT</th>
      <th>AMZN</th>
      <th>AAPL</th>
      <th>GOOG</th>
      <th>FB</th>
    </tr>
    <tr>
      <th>Symbols</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSFT</th>
      <td>1.000000</td>
      <td>0.731493</td>
      <td>0.652943</td>
      <td>0.636986</td>
      <td>0.454093</td>
    </tr>
    <tr>
      <th>AMZN</th>
      <td>0.731493</td>
      <td>1.000000</td>
      <td>0.610110</td>
      <td>0.721504</td>
      <td>0.572073</td>
    </tr>
    <tr>
      <th>AAPL</th>
      <td>0.652943</td>
      <td>0.610110</td>
      <td>1.000000</td>
      <td>0.569773</td>
      <td>0.438761</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>0.636986</td>
      <td>0.721504</td>
      <td>0.569773</td>
      <td>1.000000</td>
      <td>0.633440</td>
    </tr>
    <tr>
      <th>FB</th>
      <td>0.454093</td>
      <td>0.572073</td>
      <td>0.438761</td>
      <td>0.633440</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



None of the stocks are negatively correlated. Microsoft and Google are highly correlated, while Facebook and Apple exhibit the lowest correlation.
