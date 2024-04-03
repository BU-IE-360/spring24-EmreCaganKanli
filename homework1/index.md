# Homework 1

## Introduction

For this homework, 3 datasets from [TCMB website](https://evds2.tcmb.gov.tr/) and relevant datasets from [Google Trends](http://trends.google.com/) was used. The aim is to see if the datasets from TCMB are related with an independant dataset, possibly from Google Trends.

## Model 1 - Clothing Expenditures and Holidays

### Inspection of the Time Series

In Turkey, it is common for people to buy new clothes before the religious holidays, namely Ramadan and Eid. In this sense, the data between clothing expenditures and holidays might be investigated. To have data on how close the holiday dates are and how much people think about these holidays, we can assume that people search about them more when they are close.

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

After downloading the time series from their respective websites, all datasets were combined into one excel sheet with an additional t value for time purposes.


![All Data Excel](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/all%20data%20excel.png)
Some Observations From The Excel Containing All Data

### Building the Model

Firstly, checking the correlations between the search datas, we get .465 for Bayram and Ramazan, 0.675 for Bayram and Kurban and -0.00145 for Ramazan and Kurban. This is not surprising as the Bayram data closesly resembles the sum of Ramazan and Kurban data. We can use all and then decide which one to delete by checking the importance of coefficients.

There appears to be a trend in the Clothing data. The Augmented Dickey–Fuller test gives a p-value of 99.3%. We can also see that the data is not stationary by checking the ACF and PACF plots, .


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


Setting d = 1 and trying different p and q values, the set (2, 1, 1) has been chosen. Using SARIMAX to add the search data to the model, we get a model with MAPE 9.21%. If the search data was not used, the MAPE turns out to be 10.5%.


![Model 1](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/model%201.png)
Model 1


The MAPE drop and the visualizaiton both show a significant effect of the search data, but we can also check the p-values of coefficients.


![Model 1 Summary](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/model%20summary.png)
Model 1 Summary


The only non-significant p-value is for the kurban search data, so we can take that feature out and neither the MAPE nor the visuals change drastically. 

We can also try the model by splitting the data into train and test. If we choose a holdout percentage of 20 and build the model again, we get a MAPE of 7.32% for the model without search data and 6.88% for the model including the search data.


![Model 1 with Holdout](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/model%201%20holdout.png)
Model 1 with Holdout


### Conclusion

The MAPE difference, the significance of coefficients, the visualization and everything points to the search data being influential on predicting the Clothes expenditure. The reason why Kurban data had a low p-value for significance or coefficient might be that since Ramazan is only a couple of months before Kurban, people might be buying clothes for Ramazan and using them for Kurban also. This can be seen on the Clothing plot, the peaks of Ramazan are higher than Kurban. So the model chose bayram because if explained the peaks, but then also chose Ramazan because it explained the height difference between Ramazan and Kurban.



Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```
