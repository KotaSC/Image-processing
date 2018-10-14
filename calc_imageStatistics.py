import cv2
import numpy as np

def main():
    
    # 入力画像を読み込み
    img = cv2.imread( "th0.3_cropUpside.bmp" )

    # グレイスケール変換
    gray = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
    
    # 画素値の合計を求める
    sumPixelValue = np.sum( gray[gray != 0] )   

    # 画素値の平均値を求める
    avePixelValue = gray[gray != 0].mean()
    
    # 画素値の分散を求める
    varPixelValue = gray[gray != 0].var()

    # 画素値の標準偏差を求める
    stdPixelValue = gray[gray != 0].std()

    print( "sumPixelValue = " + str( sumPixelValue ) )
    print( "avePixelValue = " + str( avePixelValue ) )
    print( "varPixelValue = " + str( varPixelValue ) )
    print( "stdPixelValue = " + str( stdPixelValue ) )

if __name__ == "__main__":
    main()