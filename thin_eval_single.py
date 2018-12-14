import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():

    # 入力画像を読み込み
    img = cv2.imread( "plane/th04_dim2/edge.bmp" )

    # グレースケール変換
    gray_img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )

    # 画像の縦幅と横幅を求める
    height, width = gray_img.shape[0], gray_img.shape[1]

    val = calc_thin( gray_img, height, width )
    m   = max( val ) * 0.5

    print( val )
    print( m )

    plt.xlim( [0, height] )
    plt.ylim( [0, 255] )

    plt.plot( val, color='b' )

    plt.axhline( y=m, color='r', linestyle='--' )

    interSectionA = 19.5
    interSectionB = 21.8

    lengthAB = round( interSectionB - interSectionA, 1 )
    centerAB = ( interSectionA + interSectionB ) * 0.5

    plt.plot( interSectionA, m, 'o', color='black' )
    plt.text( interSectionA-2.5, m+5, str( interSectionA ), size=8 )
    plt.plot( interSectionB, m, 'o', color='black' )
    plt.text( interSectionB+0.6, m+5, str( interSectionB ), size=8 )
    plt.plot( [interSectionA, interSectionB], [m, m], linestyle='-', color='black' )
    plt.annotate( str(lengthAB),
				  xy=(centerAB, m-3),
				  xytext=(centerAB-5, m-30),
				  arrowprops=dict( connectionstyle='arc3, rad=0.3', width=2, headwidth=10, headlength=7 ) )

    plt.xlabel( "Vertical component of edge" )
    plt.ylabel( "Pixel Value" )

    plt.savefig( "plane/th04_dim2/edge_hw.png" )

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