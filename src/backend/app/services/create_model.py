import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
import pickle
import os


def train_models(crypto: str, timesteps=30):
    df = get_data(crypto)
    df_rounded = round_up(df)
    close_prices_scaled = separate_data(df_rounded)
    x, y = create_lstm_data(close_prices_scaled)
    model = train_model(x, y, timesteps)
    return save_model(model)


def get_data(crypto: str):
    return yf.download(tickers=crypto, period="5y", interval="1d")


def round_up(df):
    colunas = df.columns
    for coluna in colunas:
        df[coluna] = df[coluna].apply(lambda x: round(x, 2))
    return df


def separate_data(df):
    close_prices = df["Close"].values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    return scaler.fit_transform(close_prices)


def create_lstm_data(data, time_steps=1):
    x, y = [], []
    for i in range(len(data) - time_steps):
        x.append(data[i : (i + time_steps), 0])
        y.append(data[i + time_steps, 0])
    return np.array(x), np.array(y)


def train_model(X, y, timesteps=30):
    x, y = create_lstm_data(X, timesteps)
    x = np.reshape(x, (x.shape[0], x.shape[1], 1))

    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(x.shape[1], 1)))
    model.add(LSTM(units=50))
    model.add(Dense(units=1))
    model.compile(optimizer="adam", loss="mean_squared_error")
    model.fit(x, y, epochs=10, batch_size=32)
    return model


def save_model(model):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(current_dir, "../models")

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    filename = "model.h5"
    file_path = os.path.join(model_dir, filename)

    model.save(file_path)

    return file_path
