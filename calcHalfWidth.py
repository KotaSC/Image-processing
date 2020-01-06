import numpy as np
import cv2
import sys
args = sys.argv
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
from matplotlib import cycler

def main():

    colors = cycler('color', ['#EE6666', '#3388BB',
                              '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])


    plt.rc('axes',  facecolor='#E6E6E6', edgecolor='black',
        axisbelow=True, grid=False, prop_cycle=colors)
    plt.rc('grid',  color='w', linestyle='solid')
    plt.rc('xtick', direction='in', color='black')
    plt.rc('ytick', direction='in', color='black')
    plt.rc('patch', edgecolor='#E6E6E6')
    plt.rc('lines', linewidth=2)

    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams["xtick.major.size"] = 10
    plt.rcParams["xtick.minor.size"] = 5
    plt.rcParams["ytick.major.size"] = 10
    plt.rcParams["ytick.minor.size"] = 5
    plt.rcParams["font.size"] = 28

    plt.figure(figsize=(10, 8))
    ax = plt.axes(facecolor='white')
    ax.set_axisbelow(True)


    image = args[1]

    # 入力画像を読み込み
    img = cv2.imread( image )


    # グレースケール変換
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 画像の縦幅と横幅を求める
    height, width = gray_img.shape[0], gray_img.shape[1]

    val = calc_half_width( gray_img, height, width )

    half_val = max( val ) * 0.5
    max_val  = max( val )

    ax.set_xlim([0, height-1])
    ax.set_ylim([0, 255])

    plt.xticks([0.0, 4.0, 8.0, 12.0, 16.0, 20.0])
    plt.yticks([50, 100, 150, 200, 250])

    ax.plot( val, color='black')


    ax.set_xlabel( "horizontal direction", fontsize=22, color='black' )
    ax.set_ylabel( "pixel Value", fontsize=22, color='black' )

    fig_name = args[2]

    save_path = "./img/hw/"
    save_fig = save_path + fig_name

    plt.savefig( save_fig )
    plt.show()

def calc_half_width( gray, h, w ):

    value = []

    for y in range( h ):

        sumx = 0

        for x in range( w ):

            sumx += gray[y, x]

        value.append( sumx/w )

    return value

if __name__ == "__main__":
    main()
