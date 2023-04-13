import pandas as pd
import numpy as np


chat_id = 694882183 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1 = x_success/x_cnt
    p2 = y_success/y_cnt
    d = (p2-p1)/np.sqrt((p1 * (1 - p1) / x_cnt) + (p2 * (1-p2) / y_cnt))
    d = d > norm.ppf(0.99)
    return d
