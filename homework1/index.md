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


![Model 1.1](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/model%201.1.png)
Model 1.1 with feature bayram


![Model 1.2](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/model%201.2.png)
Model 1.2 with features ramazan and kurban


Both models perform well, but model 1.1 seems to capture the peaks better. Choosing it as the main model 1 and investigating more, we get the following summary.


![Model 1 Summary](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/model%201%20summary.png)
Model 1 Summary


p-value of the F-statistic is very low, showing that the model is promising. The p-value of each feature is also low, indicating that they are significant. R^2 value is close to 1, showing a good fit. All in all, this looks like a good model.


### Conclusion

The significance of coefficients, p-value of the F-statistic, the visualization and everything points to the bayram search data being influential on predicting the Clothes expenditure. The reason why bayram data captured the peaks better than ramazan and kurban might be the fluctuations towards the end. Since the bayram search data has no values there, it is no influenced by those fluctuations. However, it might be the case that the ramazan and kurban data fit too much to those data at the endthat they lose the ability to predict peaks.





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
