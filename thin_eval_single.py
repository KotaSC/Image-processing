import numpy as np
import cv2
import sys
args = sys.argv
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
from matplotlib import cycler

def main():

    colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
    plt.rc('axes', facecolor='#E6E6E6', edgecolor='none', axisbelow=True, grid=True, prop_cycle=colors)
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
    # gray_nonzero = gray[gray > 0]
    # 画像の縦幅と横幅を求める
    height, width = gray.shape[0], gray.shape[1]
    # height, width = gray_nonzero.shape[0], gray_nonzero.shape[1]

    val = calc_thin( gray, height, width )
    m   = max( val ) * 0.5
    mx  = max( val )
    x = np.argmax( val )

    # print( val )
    # print( m )

    plt.figure( figsize=(10, 8) )
    ax = plt.axes( facecolor='#E6E6E6' )
    ax.set_axisbelow( True )

    ax.set_xlim([0, height-1])
    ax.set_ylim([0, 255])

    ax.plot( val )

    # ax.axhline( y=m, color='blue' ,linestyle='--', alpha=0.7 )

    interSectionA = 12.50
    interSectionB = 21.40

    lengthAB = round( interSectionB - interSectionA, 1 )
    centerAB = ( interSectionA + interSectionB ) * 0.5

    plt.plot( interSectionA, m, 'o', color='black' )
    plt.text( interSectionA-2.0, m+5, "10.50", size=12 )
    plt.plot( interSectionB, m, 'o', color='black' )
    plt.text( interSectionB+0.3, m+5, "13.50", size=12 )
    plt.plot( [interSectionA, interSectionB], [m, m], linestyle='-', color='black' )

    plt.plot( x, mx-1, 'o', color='black' )
    plt.plot( [5, interSectionA-0.1], [m, m], linestyle='--', color='b', alpha=0.7 )
    plt.plot( [5, x-0.1], [mx, mx], linestyle='--', color='b', alpha=0.7 )

    plt.text( 3.3, mx-1, r"$f_{max}$", size=12)
    plt.text( 3.3, m-2, r"$\frac{f_{max}}{2}$", size=15)
    plt.text( centerAB-1.50, m-9.0, r"$HW = 8.90$", size=11 )
    # plt.annotate( str(lengthAB),
	# 			  xy=(centerAB, m-3),
	# 			  xytext=(centerAB, m-30),
    #               size=12,
	# 			  arrowprops=dict( connectionstyle='arc3, rad=0.0', width=3, headwidth=12, headlength=10 ) )

    ax.set_title("Result of Half-Width Analysis", fontsize=12)
    ax.set_xlabel("Y coordinates of the feature region image", fontsize=12, color='black')
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