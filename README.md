# LNG Market Analysis ML Model

## Introduction
This project develops a machine learning model to analyze and predict trends in the Liquefied Natural Gas (LNG) market. By harnessing the predictive power of neural networks and sentiment analysis, this model aims to provide actionable insights into LNG pricing, demand, and optimal routing for trading strategies.

## Background
**LNG**: A critical component of the global energy market, LNG includes primarily **methane** and **ethane**. Its trade is influenced by various factors, including economic indicators, market sentiment, and geopolitical events.

**Liquefied Petroleum Gas**

**Arbitrage Routing**


## Model Description
### Neural Network
#### Baseline Model
The baseline neural network model is designed to predict LNG prices based on historical data. It will serve as a comparison point for more complex models.

### LLM for Sentiment Analysis 

#### OpenAI Fine Tuning (Baseline) 
The baseline model incorporates sentiment analysis using OpenAI's fine-tuning capabilities to interpret market sentiment from news sources and social media.

#### Local LLAMA 3 Model with Fine Tuning (with QLoRA)
An advanced version, Local LLAMA 3, fine-tunes the sentiment analysis specifically for LNG market nuances, aiming for greater accuracy in sentiment prediction.

## Project Structure
```
├── README.md          <- The top-level README for developers using this project
├── data
│   ├── Fine-Tuning    <- Pretrain data for LLM fine tuning
│   ├── Physical Date  <- Macro data
│   ├── Platts MOC Physical
│   └── WSJ            <- News data related to LNG collected from WSJ
│
├── docs               <- Project related documentation
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering)
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── LICENSE
```

## Installation and Usage
### Prerequisite
Python >= 3.6, Pip/Conda
```sh
$ pip install -r requirements.txt
```


## Results


## Future Work


## References
### Data Source
- Bloomberg
- S&P Global
- The Wall Street Journal