# import sys
# sys.path.append("..")
"""
Module for real predictions
"""
import pandas as pd
import utils as ut


def real_prediction(starting_price, lin_reg_2, poly_reg, model_name):
    """Show real predictions"""
    # starting_price = starting_price
    premium_no = ut.deduce_premium_no(starting_price)
    percent_treshold = int(starting_price * 0.8)
    print('data_begining:', starting_price)
    print('percent_treshold 80%:', percent_treshold)

    x_specific = pd.DataFrame()
    x_specific.insert(0, 'Day', range(0, 364))
    x_specific.insert(1, 'premium', premium_no)
    y_pred_all = lin_reg_2.predict(poly_reg.fit_transform(x_specific))

    print('prediction for' + model_name)
    for i in range(y_pred_all.size):
        if y_pred_all[i] <= percent_treshold:
            print('Begining price(', starting_price, ')',
                  ' should drop to 80% (', y_pred_all[i], ')',
                  ' in ', i, 'day')
            break
    return y_pred_all
