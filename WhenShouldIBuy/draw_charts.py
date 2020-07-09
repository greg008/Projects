"""
        This module implements wisualisation for datasets and predictions
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd


def real_prediction_plot(plot_name, y_pred_all, line_x, line_y):
    """Visualisations for prediction datasets"""
    plt.title('Prediction ' + plot_name + ' - 80% price')
    x_num = range(0, 364)
    pred_list = []
    for i in range(0, 364):
        pred_price = y_pred_all[i]
        pred_list.append(pred_price)
    pred_list = np.asarray(pred_list)
    y_num = pred_list
    plt.xlabel('Day')
    plt.ylabel('Price(GBP)')
    plt.axvline(x=line_x, linewidth=3, color='r',
                label='day when price achieve 80%')
    plt.axhline(y=line_y, linewidth=3, color='g', label='80% of price')
    plt.legend()
    plt.plot(x_num, y_num)
    plt.savefig('predict-' + plot_name + '.png')
    plt.show()


def draw_graphs(premium_no, dataset, lin_reg_2, poly_reg):
    """Draw graphs"""
    x_specific = pd.DataFrame()
    x_specific.insert(0, 'Day', range(0, 364))
    x_specific.insert(1, 'premium', premium_no)
    main_df = dataset[dataset.iloc[:, 4] == premium_no]
    y_raw = main_df.iloc[0:364, 3]
    y_num = lin_reg_2.predict(poly_reg.fit_transform(x_specific))
    plt.plot(range(0, 364), y_raw, color='blue')
    plt.plot(range(0, 364), y_num, color='red')


def grid_of_subplots(dataset, lin_reg_2, poly_reg):
    """Draw grid of subplots"""
    fig = plt.figure(figsize=(10, 10))
    fig.subplots_adjust(hspace=0.7)
    fig.suptitle('Polynomial cellphone price', fontsize=16)
    red_patch = mpatches.Patch(color='red', label='prediction')
    blue_patch = mpatches.Patch(color='blue', label='orginal_data')
    fig.legend(handles=[red_patch, blue_patch], loc='upper right')

    plt.subplot(4, 2, 1)
    plt.title('Huawei P9 Lite')
    plt.xlabel('Day')
    plt.ylabel('Price(GBP)')
    draw_graphs(2, dataset, lin_reg_2, poly_reg)

    plt.subplot(4, 2, 2)
    plt.title('Samsung Galaxy A5')
    plt.xlabel('Day')
    plt.ylabel('Price(GBP)')
    draw_graphs(3, dataset, lin_reg_2, poly_reg)

    plt.subplot(4, 2, 3)
    plt.title('Huawei Honor 10 (4GB RAM)')
    plt.xlabel('Day')
    plt.ylabel('Price(GBP)')
    draw_graphs(4, dataset, lin_reg_2, poly_reg)

    plt.subplot(4, 2, 4)
    plt.title('Huawei P20 128GB')
    plt.xlabel('Day')
    plt.ylabel('Price(GBP)')
    draw_graphs(5, dataset, lin_reg_2, poly_reg)

    plt.subplot(4, 2, 5)
    plt.title('Samsung Galaxy S8 64GB')
    plt.xlabel('Day')
    plt.ylabel('Price(GBP)')
    draw_graphs(6, dataset, lin_reg_2, poly_reg)

    plt.subplot(4, 2, 6)
    plt.title('Samsung Galaxy S9 64GB')
    plt.xlabel('Day')
    plt.ylabel('Price(GBP)')
    draw_graphs(7, dataset, lin_reg_2, poly_reg)

    plt.subplot(4, 2, 7)
    plt.title('Samsung Galaxy Note 9 128GB')
    plt.xlabel('Day')
    plt.ylabel('Price(GBP)')
    draw_graphs(8, dataset, lin_reg_2, poly_reg)
    plt.savefig("charts.png")
    plt.show()
