import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd


def draw_plot_polynomial(premium_no, dataset, lin_reg_2, poly_reg):
    dataset = pd.read_csv('data/out_concat.csv')
    X_specific = pd.DataFrame()
    X_specific.insert(0, 'Day', range(0, 364))
    X_specific.insert(1, 'premium', premium_no)
    mainDf = dataset[dataset.iloc[:, 4] == premium_no]
    y_raw = mainDf.iloc[0:364, 3]
    y = lin_reg_2.predict(poly_reg.fit_transform(X_specific))
    plt.plot(range(0, 364), y_raw, color='blue')
    plt.plot(range(0, 364), y, color='red')

def plot_charts(dataset, lin_reg_2, poly_reg):
    fig = plt.figure(figsize=(10, 10))
    fig.subplots_adjust(hspace=0.7)
    fig.suptitle('Polynomial cellphone price', fontsize=16)
    red_patch = mpatches.Patch(color='red', label='prediction')
    blue_patch = mpatches.Patch(color='blue', label='orginal_data')
    fig.legend(handles=[red_patch, blue_patch], loc='upper right')

    plt.subplot(4, 2, 1)
    plt.title('Huawei P9 Lite')
    plt.xlabel('Day')
    plt.ylabel('Price')
    draw_plot_polynomial(2, dataset, lin_reg_2, poly_reg)

    plt.subplot(4, 2, 2)
    plt.title('Samsung Galaxy A5 SM-A520F')
    plt.xlabel('Day')
    plt.ylabel('Price')
    draw_plot_polynomial(3, dataset, lin_reg_2, poly_reg)

    plt.subplot(4, 2, 3)
    plt.title('Huawei Honor 10 (4GB RAM)')
    plt.xlabel('Day')
    plt.ylabel('Price')
    draw_plot_polynomial(4, dataset, lin_reg_2, poly_reg)

    plt.subplot(4, 2, 4)
    plt.title('Huawei P20 128GB')
    plt.xlabel('Day')
    plt.ylabel('Price')
    draw_plot_polynomial(5, dataset, lin_reg_2, poly_reg)

    plt.subplot(4, 2, 5)
    plt.title('Samsung Galaxy S8 64GB')
    plt.xlabel('Day')
    plt.ylabel('Price')
    draw_plot_polynomial(6, dataset, lin_reg_2, poly_reg)

    plt.subplot(4, 2, 6)
    plt.title('Samsung Galaxy S9 64GB')
    plt.xlabel('Day')
    plt.ylabel('Price')
    draw_plot_polynomial(7, dataset, lin_reg_2, poly_reg)

    plt.subplot(4, 2, 7)
    plt.title('Samsung Galaxy Note 9 128GB')
    plt.xlabel('Day')
    plt.ylabel('Price')
    draw_plot_polynomial(8, dataset, lin_reg_2, poly_reg)
    plt.savefig("charts.png")
    plt.show()
