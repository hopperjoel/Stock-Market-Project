import pandas as pd
import yfinance as yf

tickers = ["CHGI", "DTPKF", "ECORF", "FGPHF", "GPHBF", "GRPEF", "NNXPF", "HDGHF", "TLGRF", "VRSRF"]


yf.download(tickers, start="2015-01-01", end="2020-12-31")