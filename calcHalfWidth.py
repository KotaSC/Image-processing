from matplotlib.patches import ArrowStyle
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

    ax.set_xlim([2.0, height-3])
    ax.set_ylim([0, 255])

    plt.xticks([])
    plt.yticks([0.0, 255])
    
    arrowStyle = ArrowStyle('simple')

    ax.annotate('', xy=(4.05, half_val), xytext=(8, half_val), 
                arrowprops=dict(connectionstyle='arc3', arrowstyle=arrowStyle,
                                facecolor='black', edgecolor='black')
                )
    ax.annotate('', xy=(11, half_val), xytext=(7.93, half_val),
                arrowprops=dict(connectionstyle='arc3', arrowstyle=arrowStyle,
                                facecolor='black', edgecolor='black')
                )

    ax.plot([8.0, 0.0], [max_val, max_val],   ls="--", color="black")
    ax.plot([4.0, 0.0], [half_val, half_val], ls="--", color="black")

    plt.text(1.05, max_val-4,      r"$\rm max$", fontsize=25)
    plt.text(1.15, half_val - 3.8, r"$\frac{\rm max}{2}$", fontsize=32)
        
    plt.text(5.8, half_val-17, "half-value width")

    ax.plot(val, color='black')

    ax.set_xlabel( "horizontal direction", fontsize=28, color='black' )
    ax.set_ylabel( "pixel Value", fontsize=28, color='black' )

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
