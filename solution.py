import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
from scipy import stats

chat_id = 368780632 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.06
    u = stats.norm.ppf((1-alpha)/2+0.5)
    p_x = x_success / x_cnt
    p_y = y_success / y_cnt
    return p_y < p_x - u * np.sqrt(p_x * (1 - p_x) / x_cnt)
