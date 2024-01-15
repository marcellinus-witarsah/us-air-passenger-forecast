import pandas as pd
import numpy as np
from typing import Union

def bias(y_true: Union[pd.Series, np.array, list], y_pred: Union[pd.Series, np.array, list]):
    """
    Calculate Bias (Average Difference Between Prediction and Actual Values)
    
    Args:
        y_true (pd.Series, np.array, list): Actual Values.
        y_pred (pd.Series, np.array, list): Prediction Values.
    
    Returns:
        float: Bias Result.
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    assert len(y_pred) == len(y_true)
    return np.mean(y_pred - y_true)

def mae(y_true: Union[pd.Series, np.array, list], y_pred: Union[pd.Series, np.array, list]):
    """
    Calculate Mean Absolute Error (Average of Absolute Difference Between Prediction and Actual Values)
    
    Args:
        y_true (pd.Series, np.array, list): Actual Values.
        y_pred (pd.Series, np.array, list): Prediction Values.
    
    Returns:
        float: Bias Result.
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    assert len(y_pred) == len(y_true)
    return np.mean(np.abs(y_pred - y_true)) 

def mape(y_true: Union[pd.Series, np.array, list], y_pred: Union[pd.Series, np.array, list]):
    """
    Calculate Bias (Average Absolute Percentage Difference Between Prediction and Actual Values)
    
    Args:
        y_true (pd.Series, np.array, list): Actual Values.
        y_pred (pd.Series, np.array, list): Prediction Values.
    
    Returns:
        float: Bias Result.
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    assert len(y_pred) == len(y_true)
    return np.mean(np.abs((y_pred - y_true)/ y_true)*100)