# Homework 1

## Introduction

For this homework, 3 datasets from [TCMB website](https://evds2.tcmb.gov.tr/) and relevant datasets from [Google Trends](http://trends.google.com/) was used. The aim is to see if the datasets from TCMB are related with an independant dataset, possibly from Google Trends.

## Model 1 - Clothing Expenditures and Holidays

In Turkey, it is common for people to buy new clothes before the religious holidays, namely Ramadan and Eid. In this sense, the data between clothing expenditures and holidays might be investigated. To have data on how close the holiday dates are and how much people think about these holidays, we can assume that people search about them more when they are close.

### Inspection of the Time Series

The clothing expenditure data can be pulled from TCMB Website and search data can be acquired from Google Trends. All datasets are weekly, ranging from 21/05/2021 to 22/03/2024 with 149 datapoints. 

![Clothing Data From TCMB Website](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/giyim%20data%20plot.jpeg)
Clothing Data From TCMB Website


![Bayram Search Google Trends](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/bayram%20trend%20plot.png)
Bayram Search Google Trends


![Ramazan Search Google Trends](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/ramazan%20trend%20plot.png)
Ramazan Search Google Trends


![Kurban Search Google Trends](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/kurban%20trend%20plot.png)
Kurban Search Google Trends


It can be argued that the peaks of Clothing Data matches with the Bayram dates and the combination of Ramazan and Kurban search trends.

### Pulling and Organizing the Data

After downloading the time series from their respective websites, all datasets were combined into one excel sheet with an additional t value for time purposes. A constant feature for intercept was added afterwards in code.


![All Data Excel](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/all%20data%20excel.png)
Some Observations From The Excel Containing All Data


### Building the Model

Firstly, there appears to be a trend in the Clothing data. The Augmented Dickey–Fuller test gives a p-value of 99.3%. We can also see that the data is not stationary by checking the ACF and PACF plots, .


![ACF Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/acf_normal.png)
ACF Plot


![PACF Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/pacf_normal.png)
PACF Plot


Taking the first difference and plotting again, the ACF and PACF are closer to ideal. The Augmented Dickey–Fuller test gives 1.41e-07%, which indicates a stationary time series. The mean of the data is closer to 0.

![ACF Plot of First Difference](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/acf_diff.png)
ACF Plot


![PACF Plot of First Difference](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/pacf_diff.png)
PACF Plot


The data can now be argued to be stationary, however the residual plot shows some increase in variance.


![First Difference Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/y_diff%20plot.png)
First Difference Plot


To help with this, a log Transformation can be used. Taking the first difference of the log transformed data, new Augmented Dickey–Fuller test gives 9.96e-13% and the plot looks more consistent.


![Log Transform First Difference Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/y_diff_log%20plot.png)
Log Transform First Difference Plot


To see which features to use we can check the correlations between the search data. We get .465 for Bayram and Ramazan, .675 for Bayram and Kurban and -.00145 for Ramazan and Kurban. This is not surprising as the Bayram data closesly resembles the sum of Ramazan and Kurban data. We can try two models with one having bayram and the other having ramazan and kurban.


![Model 1.1](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/model%201.1%20plot.png)
Model 1.1 with feature bayram


![Model 1.2](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/model%201.2%20plot.png)
Model 1.2 with features ramazan and kurban


Both models perform well, but model 1.1 seems to capture the peaks better. Choosing it as the main model 1 and investigating more, we get the following summary.


![Model 1 Summary](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/model%201%20summary.png)
Model 1 Summary


p-value of the F-statistic is very low, showing that the model is promising. The p-value of each feature is also low, indicating that they are significant. R^2 value is close to 1, showing a good fit. All in all, this looks like a good model.


### Conclusion

The significance of coefficients, p-value of the F-statistic, the visualization and everything points to the bayram search data being influential on predicting the Clothes expenditure. The reason why bayram data captured the peaks better than ramazan and kurban might be the fluctuations towards the end. Since the bayram search data has no values there, it is no influenced by those fluctuations. However, it might be the case that the ramazan and kurban data fit too much to those data at the endthat they lose the ability to predict peaks.


## Model 2 - House Sales, Seasonality and House for Sale Search

People buy houses all the time, but the amount might be investigated. A good candidate of a feature predicting how much people think about buying houses might be when people search House for Sales.

### Inspection of the Time Series

TCMB data from House Sales is a monthly time series, from 2013-01 to 2024-02 with 134 datapoints. Plotting the House Sales Time Series, we can try to make some suggestions.


![House Sales Time Series Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model2/House%20Sales%20Plot.png)
House Sales Time Series Plot


There appears to be some seasonality, which we can see by noticing a peak every december, for example. The question we will try to answer is whether seasonilty really has an effect her and can house fo sale search data cover the remaining variance.


![House for Sale Search Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model2/House%20for%20Sale%20Search%20Plot.png)
House for Sale Search Plot

The peak in the summer 2020 on both plots suggest that there might be a correlation between the dependent and independant datt.


### Pulling and Organizing the Data

After downloading the time series from their respective websites, all datasets were combined into one excel sheet with an additional t value for time purposes and dummy variable for each month. A constant feature for intercept was added afterwards in code for one of the models.


![All Data Excel](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model2/all%20data%20excel.png)
Some Observations From The Excel Containing All Data


### Building the Model

The p-value from the Augmented Dickey–Fuller test at first comes out to be 13.4%. This is not low enough, but seasonality plays a big role here. Checking the ACF and PACF plots also show that the non-stationary situation is not that significant.


![ACF Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model2/acf.png)
ACF Plot


![PACF Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model2/pacf.png)
PACF Plot


There are two ways of implementing seasonality: Using all dummy variables and no intercept or using one less dummy variable and using and intercept. The plots of these two will be the same, with the same MAPE of 14.3%, but their interpretations and statistics may vary.


![Model 2 Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model2/model%202.png)
Model 2 Plot


Since the p-values of the coefficients when there is no constant is better, we can take that as the base model and comment on it.


![Model 2 Summary](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model2/model%202%20summary.png)
Model 2 Summary


### Conclusion

Each p-value of the coefficients are very small, so all of them are significant. The low p-value of ev feature shows that House for Sales search was significant in predicting the House Sales. The p-value of the F-statistic is also low, which means that the model is significant. The coefficient of trend is negative, but not very large compared to other numbers, so it can be argued that there is a small trend down. The R^2 value is low, but this can be attributed to the low trend level. 


## Model 3 - Euro EXchange Rate and President

President Recep Tayyip Erdoğan is arguably the most influencial person in Turkey in many aspects. As he is the one having the last say in many decisions, including economy, what he is doing and saying might influance the exchange rates.

### Inspection of the Time Series

The exchange rate of Euro can be used as a standart foreign currency. The data from TCMB goes from 28-05-2021 to 29-03-2024, with 149 datapoints. How much people think that the president is influancing the economy might be related with how much they search his name on Google.


![Euro Time Series](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model3/euro%20time%20series.png)
Euro Time Series


![Recep Tayyip Erdoğan Search Time Series](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model3/rte%20time%20series.png)
Recep Tayyip Erdoğan Search Time Series


The jumps of Euro plot show a relation with the peaks of search data, can be investigated.


### Pulling and Organizing the Data


After downloading the time series from their respective websites, all datasets were combined into one excel sheet with an additional t value for time purposes.


![All Data Excel](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model3/all%20data%20excel.png)
Some Observations From The Excel Containing All Data


### Building the Model


The p-value from the Augmented Dickey–Fuller test at first comes out to be 98.2% because there is a clear trend.


![ACF Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model3/acf_normal.png)
ACF Plot


![PACF Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model3/pacf_normal.png)
PACF Plot


Taking the first difference and trying again, we get a p-value of 8.00e-15.


![ACF Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model3/acf_diffl.png)
ACF Plot


![PACF Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model3/pacf_diff.png)
PACF Plot


Residuals also look stationary.


![Residuals](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model3/residuals.png)
Residuals


Building a linear model with all the features, we get the following plot.


![Model 3.1 Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model3/model%203.1%20plot.png)
Model 3.1 Plot


However, it is easy to see that this is not a good fit. We can try a log transform to capture an exponential growth.


![Model 3.2 Plot](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model3/model%203.2%20plot.png)
Model 3.2 Plot


The summary of this second plot is as follows.


![Model 3 Summary](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model3/model%203%20summary.png)
Model 3 Summary


Low p-values for coefficient and F-statistic and high R^2 value might indicate a good fit. However, the ceofficient of the search data is negative, which is contradictery to the initial assumption.


### Conclusion

Although the statistics are good and the plot is not far off, the sign of the coefficients tell a different story. We can argue that the correlation between the independant and dependant data is not very strong.