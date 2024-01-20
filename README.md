# Air Passenger Forecast
![Airport Image](images/aiport.jpg)
# Project Overview

This project is about implementing autoregressive integrated moving average (`ARIMA`) and seasonal autoregressive integrated moving average (`SARIMA`) model for forecasting passenger that will visit one of the airports in the United States of America. The goal is to assist airport management in effectively allocating staff and facilities to handle the incoming passenger traffic.


# Installation and Setup
## Resources Used
- **Code Editor:** Visual Studio Code
- **Python Version:** 3.10.13

## Python Package Used
- **General Purpose:** General purpose packages like `time, os, sys, and dotenv`.
- **Data Manipulation:** Packages used for handling and importing dataset such as `pandas and numpy`.
- **Data Visualization:** Packages used to plot graphs in the analysis or for understanding the data as `seaborn, and matplotlib`.
- **Forecasting:** Packages that were used to generate the forecast model such as `statsmodel`, etc.

Install libraries and dependencies are needed by creating Python environment and install all libraries with their specific versions that are available in the requirements.txt

```bash
  conda install -n <environment_name> python==3.10.13
  conda activate <environment_name>
  cd us-air-passenger-forecast
  pip install -r requirements.txt
```
# Data

## Data Source
The dataset that we used can be downloaded from [DATA.GOV](https://catalog.data.gov/dataset/air-traffic-passenger-statistics). The data consist of 15 columns:
- Activity Period (Number): The year and month when this activity occurred
- Activity Period Start Date (Date & Time): Start date of the activity period
- Operating Airline (Plain Text): Airline name for the operator of aircraft with passenger activity.
- Operating Airline IATA Code	(Plain Text): The International Air Transport Association (IATA) two-letter designation for the Operating Airline.
- Published Airline (Plain Text): Airline name that issues the ticket and books revenue for passenger activity.
- Published Airline IATA Code	(Plain Text): The International Air Transport Association (IATA) two-letter designation for the Published Airline.
- GEO Summary (Plain Text): Designates whether the passenger activity in relation to SFO arrived from or departed to a location within the United States (“domestic”), or outside the United States (“international”) without stops.
- GEO Region (Plain Text):Provides a more detailed breakdown of the GEO Summary field to designate the region in the world where activity in relation to SFO arrived from or departed to without stops.
- Activity Type Code (Plain Text): A description of the physical action a passenger took in relation to a flight, which includes boarding a flight (“enplanements”), getting off a flight (“deplanements”) and transiting to another location (“intransit")
- Price Category Code (Plain Text): A categorization of whether a Published Airline is a low-cost carrier or not a low-cost carrier.
- Terminal (Plain Text): Name of a terminal of the airport
- Boarding Area (Plain Text): Letter that represents a boarding area
- Passenger Count (Number): Total number of passengers this month
- data_as_of (Date & Time): Datetime of data as of
- data_loaded_at (Date & Time): Datetime of data loaded at

## Data Acquisition
Acquiring the data by download the file at DATA.GOV [website](https://catalog.data.gov/dataset/air-traffic-passenger-statistics).

## Data Preprocessing
In this project, columns that were used are `Activity Period Start Date and Passenger Count` columns. Therefore a group by sum operation performed on the data just like shown below.

```python
# Data Preprocessing
df['Activity Period Start Date'] = pd.to_datetime(df['Activity Period Start Date'])
df = df.groupby(by=['Activity Period Start Date']).agg({'Passenger Count': 'sum'}).reset_index()
df = df.rename(columns={
    "Activity Period Start Date": "date",
    "Passenger Count": "passenger_count"
})
```

## Code Structure
```
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

# Results & Evaluation
From this project, there are three key points:
## 1. Dataset Behavior of Pre and Post Covid 19 Are Different
Covid 19 is something that people would not expect because it shutted down almost all business sectors including flight business. This cause a changing in behavior of the dataset which can be seen in Figure 1. Relying on the past data is not viable option. This is the reason why the data is splitted. 
| ![Passenger Count by Pre and Post Covid 19](/images/air_passenger_count.png) |
|:--:| 
| *Figure 1 Air Passenger Count Separated By Pre and Post Covid 19 Period.* |

## 2. Components of Pre Covid and Post Covid 19 Time Series Dataset
The dataset behavior prior to Covid 19 has an **increasing trend** and **yearly seasonality**. From Figure 2, we could see increasing trend of data in overall. This shows an increasing trend as year goes by the number of passenger count increases. We can also spot the same pattern which indicates yearly seasonality.
| ![Components Passenger Count by Pre Covid 19](/images/precovid_components.png) |
|:--:| 
| *Figure 2 Trend and Seasonality Air Passenger Count Prior to Covid 19.* |

In Figure 3 shows that there are peaks at lag of 12, 24, etc. This support the existence of yearly patterns where the each observations has high correlation with its previous 12, 24, and so on lags.
| ![Pre Covid 19 ACF Plot](/images/precovid_acf.png) | 
|:--:| 
| *Figure 3 Pre Covid 19 ACF Plot.* |

The dataset after the Covid 19 has also an **increasing trens** and **yearly seasonality** as well. From Figure 4, we can see an increasing trend due to the recovery phase after the Covid 19 breakout. We can also spot the same pattern that every July until August the number of air passenger was the higher throughout each year.
| ![Components Passenger Count by Post Covid 19](/images/postcovid_components.png) |
|:--:| 
| *Figure 4 Trend and Seasonality Air Passenger Count After Covid 19.* |

## 3. Modelling and Evaluation of the dataset
The best statistical model for this project is `SARIMA` which is a combination of **autoregression** (take into account n-lags values), **differentiation**, **moving average** (take into account n-lags noises), and **seasonality** (take into account pattern at n-lag for each observations). 

The evaluation metric that we used are: 
- **Bias**: average difference between actual and predicted values. The purpose of this metrics just to know if we overshoot (positive) or undershoot (negative) the forecast.
- **Mean Absolute Error (MAE)**: average absolute difference between actual and predicted values. The purpose is just to know how far the forecast from the actual value in absolute manner.
- **Mean Absolute Percentage Error (MAPE)**: average absolute percentage difference between actual and predicted values. The puprpose is to just to know how big the residuals (forecast - actual) relative to the actual value.

Here are the performance of ARIMA vs SARIMA on Pre Covid 19 test dataset. SARIMA definitely outperforms SARIMA.
|        | Bias       | MAE       | MAPE%  |
|--------|------------|-----------|--------|
| ARIMA  | -925,712.90 | 927,505.16 | 18.31% |
| SARIMA | -120,876.19 | 131,763.17 | 2.73%  |

*Table 1 Model Performance on Pre Covid 19 Testing Dataset.*

| ![Components Passenger Count by Pre Covid 19](/images/precovid_forecast.png) |
|:--:| 
| *Figure 6 Model Forecast on Air Passenger Count for The Next 12 Months (Pre Covid 19).* |

Here are the performance of ARIMA vs SARIMA on Post Covid 19 test dataset. SARIMA definitely outperforms SARIMA.
|        | Bias        | MAE        | MAPE%  |
|--------|-------------|------------|--------|
| ARIMA  | -1,044,922.42 | 1,045,578.08 | 20.73% |
| SARIMA | 533,477.42   | 534,612.42  | 12.75% |

*Table 2 Model Performance on Post Covid 19 Testing Dataset.*

| ![Components Passenger Count by Pre Covid 19](/images/postcovid_forecast.png) |
|:--:| 
| *Figure 6 Model Forecast on Air Passenger Count for The Next 12 Months (Post Covid 19).* |


# Conclusion
Incorporating seasonality into this type of dataset is impactfull in increasing forecast performance for both dataset. But the recent data was 1 October 2023 and the forecast for the next 12 months will be, around `54,909,397` in total passenger count. For the break down by months you can see Table 3.

|  Date       | Passenger Count|
|-------------|----------------|
|  2023-11-01 |       4,125,989|
|  2023-12-01 |       4,217,649|
|  2024-01-01 |       3,831,677|
|  2024-02-01 |       3,609,890|
|  2024-03-01 |       4,339,008|
|  2024-04-01 |       4,450,808|
|  2024-05-01 |       4,845,277|
|  2024-06-01 |       5,145,179|
|  2024-07-01 |       5,432,148|
|  2024-08-01 |       5,199,164|
|  2024-09-01 |       4,797,180|
|  2024-10-01 |       4,915,428|

*Table 3 Model Forecast on Air Passenger Count for The Next 12 Months (from 1 November 2023 - 1 October 2024).*

# Future Work
* [ ] Leverage other libraries that are faster and efficient such as [StatsForecast](https://github.com/Nixtla/statsforecast)
* [ ] Modularize code for generate ARIMA and SARIMA model for reproducibility
* [ ] Implement other statistic models such as Exponential Smoothing