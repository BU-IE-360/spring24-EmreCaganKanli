# Homework 1

## Introduction

For this homework, 3 datasets from [TCMB website](https://evds2.tcmb.gov.tr/) and relevant datasets from [Google Trends](http://trends.google.com/) was used. The aim is to see if the datasets from TCMB are related with an independant dataset, possibly from Google Trends.

## Model 1 - Clothing Expenditures and Holidays

### Inspection of the Time Series

In Turkey, it is common for people to buy new clothes before the religious holidays, namely Ramadan and Eid. In this sense, the data between clothing expenditures and holidays might be investigated.

Assuming that people search about these holidays more when the date is close, the Google Trends data for search "Bayram" or "Ramazan" or "Kurban" can be checked.


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

Firstly, there appears to be a trend in the Clothing data. Fittin a linear regression gives 22.8% MAPE, which is not bad but the plot shows that there is room for improvement.


![Linear Regression of Clothing Data](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/lr%20wo%20log.png)
Linear Regression of Clothing Data


Visually, a log transformation seems it would be a better fit, and trying it gives 10.4% MAPE.


![Regression of Clothing Data with log Transformation](https://raw.githubusercontent.com/BU-IE-360/spring24-EmreCaganKanli/main/homework1/photos/model1/lr%20wo%20log.png)
Regression of Clothing Data with log Transformation



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
