import cv2
import numpy as np

def main():
    
    # 入力画像を読み込み
    img = cv2.imread( "th0.3_dim2_cropUpside.bmp" )

    # グレイスケール変換
    gray = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )

    height, width = gray.shape[0], gray.shape[1]
    
    # 画素値の合計を求める
    sumPixelValue = np.sum( gray )   

    # 画素値の平均値を求める
    avePixelValue = gray[gray != 0].mean()
    
    # 画素値の分散を求める
    varPixelValue = gray[gray != 0].var()

    print( "sumPixelValue = " + str( sumPixelValue ) )
    print( "avePixelValue = " + str( avePixelValue ) )
    print( "varPixelValue = " + str( varPixelValue ) )

if __name__ == "__main__":
    main()