import numpy as np
import cv2
import sys
args = sys.argv
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
from matplotlib import cycler

def main():

    colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
    plt.rc('axes', facecolor='#E6E6E6', edgecolor='none', axisbelow=True, grid=False, prop_cycle=colors)
    plt.rc('grid', color='w', linestyle='solid')
    plt.rc('xtick', direction='out', color='black')
    plt.rc('ytick', direction='out', color='black')
    plt.rc('patch', edgecolor='#E6E6E6')
    plt.rc('lines', linewidth=2)


    # 入力画像を読み込み
    image_name = args[1]
    img = cv2.imread( image_name )

    # グレースケール変換
    gray = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
    gray_nonzero = gray[gray>0]   # 輝度値0の部分以外

    plt.figure(figsize=(10, 8))
    ax = plt.axes(facecolor='#E6E6E6')
    ax.set_axisbelow(True)

    ax.set_title("Histgram of Pixel Value of Gray Scale Image", fontsize=15)
    ax.hist(gray_nonzero.ravel(), bins=100, color='blue', alpha=0.5)
    ax.set_xlabel("Pixel value", fontsize=15, color='black')
    ax.set_ylabel("Number of pixels", fontsize=15, color='black')
    ax.set_xlim([0, 255])
    # ax.set_ylim([0, 12000])

    # 出力ファイル名
    fig_name = args[2]
    plt.savefig(fig_name)

    plt.show()

if __name__ == "__main__":
    main()