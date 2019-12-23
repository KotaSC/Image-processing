import numpy as np
import cv2
import sys
args = sys.argv
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
from matplotlib import cycler

def main():

    colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
    plt.rc('axes',  facecolor='#E6E6E6', edgecolor='black', axisbelow=True, grid=False, prop_cycle=colors)
    plt.rc('grid',  color='w', linestyle='solid')
    plt.rc('xtick', direction='in', color='black')
    plt.rc('ytick', direction='in', color='black')
    plt.rc('patch', edgecolor='#E6E6E6')
    plt.rc('lines', linewidth=2)

    # 目盛りに関する設定
    plt.rcParams["xtick.major.size"] = 10
    plt.rcParams["xtick.minor.size"] = 5
    plt.rcParams["ytick.major.size"] = 10
    plt.rcParams["ytick.minor.size"] = 5
    plt.rcParams["font.size"]        = 14

    # 凡例に関する設定
    plt.rcParams["legend.markerscale"] = 1
    plt.rcParams["legend.fancybox"] = False
    plt.rcParams["legend.framealpha"] = 1
    plt.rcParams["legend.edgecolor"] = 'black'

    image_th = args[1]
    image_d1 = args[2]
    image_d2 = args[3]
    image_d3 = args[4]

    # 入力画像を読み込み
    img_th = cv2.imread( image_th )
    img_d1 = cv2.imread( image_d1 )
    img_d2 = cv2.imread( image_d2 )
    img_d3 = cv2.imread( image_d3 )


    # グレースケール変換
    gray_th = cv2.cvtColor( img_th, cv2.COLOR_RGB2GRAY )
    gray_d1 = cv2.cvtColor( img_d1, cv2.COLOR_RGB2GRAY )
    gray_d2 = cv2.cvtColor( img_d2, cv2.COLOR_RGB2GRAY )
    gray_d3 = cv2.cvtColor( img_d3, cv2.COLOR_RGB2GRAY )


    # 画像の縦幅と横幅を求める
    height, width = gray_th.shape[0], gray_th.shape[1]

    val_th      = calc_half_width( gray_th, height, width )
    val_d1      = calc_half_width( gray_d1, height, width )
    val_d2      = calc_half_width( gray_d2, height, width )
    val_d3      = calc_half_width( gray_d3, height, width )

    halh_val    = max( val_th ) * 0.5
    max_val     = max( val_th )
    ind_max_val = np.argmax( val_th )

    plt.figure( figsize=(10, 8) )
    ax = plt.axes( facecolor='w')
    ax.set_axisbelow( True )

    ax.set_xlim([0, height-1])
    ax.set_ylim([0, 255])

    plt.xticks([0.0, 4.0, 8.0, 12.0, 16.0, 20.0])
    plt.yticks([50, 100, 150, 200, 250])

    ax.plot( val_th, color='#fa8072', label='Non Thinning' )
    ax.plot( val_d1, color='#4169e1', label='Thinning $d=1$' )
    ax.plot( val_d2, color='#3cb371', label='Thinning $d=2$' )
    ax.plot( val_d3, color='#9370db', label='Thinning $d=3$' )

    # interSectionA = 4.1
    # interSectionB = 18.0

    # ax.plot( interSectionA, halh_val, '.', markersize=18, color='black', alpha=1.0, label="Half of the maximum pixel value" )
    # ax.plot( interSectionB, halh_val, '.', markersize=18, color='black', alpha=1.0 )

    # ax.plot( [interSectionA, interSectionB], [halh_val, halh_val], linestyle='--', color='black', label='Half-Width' )

    # ax.set_xticks( [0, interSectionA, interSectionB, 22] )
    # ax.set_yticks( [halh_val, max_val, 255] )

    ax.legend( fontsize=13, frameon=True, facecolor='w' )

    ax.set_xlabel( "Feature region width", fontsize=22, color='black' )
    ax.set_ylabel( "Pixel Value", fontsize=22, color='black' )

    fig_name = args[5]

    plt.savefig( fig_name )
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
