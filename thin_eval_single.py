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

    image_name = args[1]

    # 入力画像を読み込み
    img = cv2.imread( image_name )

    # グレースケール変換
    gray    = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
    gray_nonzero = gray[gray > 0]

    # 画像の縦幅と横幅を求める
    height, width = gray.shape[0], gray.shape[1]

    val = calc_thin( gray, height, width )
    m   = max( val ) * 0.5

    # print( val )
    # print( m )

    plt.figure( figsize=(10, 8) )
    ax = plt.axes( facecolor='#E6E6E6' )
    ax.set_axisbelow( True )

    ax.set_xlim([0, height-1])
    ax.set_ylim([0, 255])

    ax.plot( val, color='b' )

    plt.axhline( y=m, color='r', linestyle='--' )

    interSectionA = 8.6
    interSectionB = 15.4

    lengthAB = round( interSectionB - interSectionA, 1 )
    centerAB = ( interSectionA + interSectionB ) * 0.5

    plt.plot( interSectionA, m, 'o', color='black' )
    plt.text( interSectionA-1.0, m+5, str( interSectionA ), size=12 )
    plt.plot( interSectionB, m, 'o', color='black' )
    plt.text( interSectionB+0.3, m+5, str( interSectionB ), size=12 )
    plt.plot( [interSectionA, interSectionB], [m, m], linestyle='-', color='black' )
    plt.annotate( str(lengthAB),
				  xy=(centerAB, m-3),
				  xytext=(centerAB, m-30),
                  size=12,
				  arrowprops=dict( connectionstyle='arc3, rad=0.0', width=3, headwidth=12, headlength=10 ) )

    ax.set_title("Result of Half-Width Analysis", fontsize=12)
    ax.set_xlabel("Vertical component of Edge", fontsize=12, color='black')
    ax.set_ylabel("Pixel Value", fontsize=12, color='black')

    fig_name = args[2]

    plt.savefig( fig_name )

    plt.show()

def calc_thin( gray, h, w ):

	value = []

	for y in range( h ):

		sumx = 0

		for x in range( w ):

			# x軸方向の画素値の合計を求める
			sumx += gray[ y, x ]

		value.append( sumx / w )

	return value

if __name__ == "__main__":
    main()