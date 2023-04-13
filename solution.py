import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 368780632 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.06
    count = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    p_val = proportions_ztest(count, nobs, alternative='larger')[1]
    if p_val <= alpha:
        return True
    else: 
        return False
