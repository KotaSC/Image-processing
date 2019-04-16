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


    # 入力画像を3つ読み込み
    image_name1 = args[1]
    img1 = cv2.imread( image_name1 )
    image_name2 = args[2]
    img2 = cv2.imread( image_name2 )
    # image_name3 = args[3]
    # img3 = cv2.imread( image_name3 )

    # グレースケール変換
    gray1 = cv2.cvtColor( img1, cv2.COLOR_RGB2GRAY )
    gray1_nonzero = gray1[gray1>0]  # 輝度値0の部分以外
    gray2 = cv2.cvtColor( img2, cv2.COLOR_RGB2GRAY )
    gray2_nonzero = gray2[gray2>0]  # 輝度値0の部分以外
    # gray3 = cv2.cvtColor( img3, cv2.COLOR_RGB2GRAY )
    # gray3_nonzero = gray3[gray3>0]  # 輝度値0の部分以外

    plt.figure(figsize=(10, 8))
    ax = plt.axes(facecolor='#E6E6E6')
    ax.set_axisbelow(True)

    ax.set_title("Comparison of Two Pixel Value Histgram of Extract and Non Extract Image", fontsize=15)
    # ax.hist([gray1_nonzero.ravel(), gray2_nonzero.ravel()],
    #         bins=100,
    #         color=['blue', 'red'],
    #         alpha=0.5,
    #         label=["default", "th02"])
    # ax.hist([gray1_nonzero.ravel(), gray2_nonzero.ravel(), gray3_nonzero.ravel()],
    #         bins=40,
    #         color=['blue', 'red', 'green'],
    #         alpha=0.5,
    #         label=["dim1", "dim2", "dim3"])
    ax.hist(gray1_nonzero.ravel(), bins=100, color='blue',   alpha=0.5, label="Threshold  = 0.3")
    ax.hist(gray2_nonzero.ravel(), bins=100, color='red',    alpha=0.5, label="Threshold  = 0.3\nDimension = 3.0")
    # ax.hist(gray3_nonzero.ravel(), bins=100, color='green',  alpha=0.5, label="dim3")
    ax.set_xlabel("Pixel value", fontsize=15, color='black')
    ax.set_ylabel("Number of pixels", fontsize=15, color='black')
    ax.set_xlim([0, 255])
    ax.set_ylim([0, 12000])
    ax.legend(fontsize=12)

    # 出力ファイル名
    fig_name = args[3]
    plt.savefig(fig_name)

    plt.show()

if __name__ == "__main__":
    main()