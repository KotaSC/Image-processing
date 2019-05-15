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

    image = args[1]

    # 入力画像を読み込み
    img = cv2.imread( image )

    # グレースケール変換
    gray = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )

    # 画像の縦幅と横幅を求める
    height, width = gray.shape[0], gray.shape[1]

    val         = calc_half_width( gray, height, width )
    halh_val    = max( val ) * 0.5
    max_val     = max( val )
    ind_max_val = np.argmax( val )

    plt.figure( figsize=(10, 8) )
    ax = plt.axes( facecolor='w')
    ax.set_axisbelow( True )

    ax.set_xlim([0, height-1])
    ax.set_ylim([0, 255])

    ax.plot( val, color='black' )

    interSectionA = 5.5
    interSectionB = 8.5

    ax.plot( interSectionA, halh_val, '.', markersize=18, color='black', alpha=1.0, label="Half of the maximum pixel value" )
    ax.plot( interSectionB, halh_val, '.', markersize=18, color='black', alpha=1.0 )

    ax.plot( [interSectionA, interSectionB], [halh_val, halh_val], linestyle='--', color='black', label='Half-Width' )

    ax.set_xticks( [interSectionA, interSectionB, 13] )
    ax.set_yticks( [halh_val, max_val, 255] )

    ax.legend( fontsize=13, frameon=True, facecolor='w' )

    ax.set_xlabel( "Feature region width", fontsize=22, color='black' )
    ax.set_ylabel( "Pixel Value", fontsize=22, color='black' )

    fig_name = args[2]

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
