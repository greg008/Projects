import sys
sys.path.append("..")
import utils as ut
import pandas as pd

def real_prediction(price_begining, lin_reg_2, poly_reg, model_name):
    price_begining = price_begining
    premium_no = ut.choose(price_begining)
    percent_treshold = int(price_begining * 0.8)
    print('data_begining:', price_begining)
    print('percent_treshold 80%:', percent_treshold)

    x_specific = pd.DataFrame()
    x_specific.insert(0, 'Day', range(0, 364))
    x_specific.insert(1, 'premium', premium_no)
    y_pred_all = lin_reg_2.predict(poly_reg.fit_transform(x_specific))

    print('prediction for' + model_name)
    for i in range(y_pred_all.size):
        if y_pred_all[i] <= percent_treshold:
            print('Begining price(', price_begining, ')', ' should drop to 80% (', y_pred_all[i], ')', ' in ', i, 'day')
            break
    return y_pred_all