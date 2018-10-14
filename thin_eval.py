import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    
    # 入力画像を読み込み
    img = cv2.imread( "th0.3_cropDownside.bmp" )
    
    # グレースケール変換
    gray_img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )

    # 画像の縦幅と横幅を求める
    height, width = gray_img.shape[0], gray_img.shape[1]

    val = calc_thin( gray_img, height, width )
    m = max( val ) * 0.5

    print( val )
    print( m )

    plt.xlim( [0, height] )
    plt.ylim( [0, 255] )

    plt.axhline( y=m, color='r' )
    plt.plot( val )

    plt.xlabel( "y-coordinate of image" )
    plt.ylabel( "Pixel Value" )

    plt.savefig( "th0.3_down_hw.png" )

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