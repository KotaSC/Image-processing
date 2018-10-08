import cv2
import numpy as np

def main():
    
    # 入力画像を読み込み
    img = cv2.imread( "th0.3_cropUpside.bmp" )

    # グレイスケール変換
    gray = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )

    height, width = gray.shape[0], gray.shape[1]
    
    # 画素値の合計を求める
    sumPixelValue = np.sum( gray )   

    # 画素値の平均値を求める
    # avePixelValue = np.mean( gray )
    avePixelValue, num = calc_avePixelValue( gray, sumPixelValue, height, width )
 
    # 画素値の分散を求める
    # varPixelValue = np.var( gray )
    varPixelValue = calc_varPixelValue( gray, avePixelValue, height, width, num ) 


    print( "numPixel      = " + str( num ) )
    print( "sumPixelValue = " + str( sumPixelValue ) )
    print( "avePixelValue = " + str( avePixelValue ) )
    print( "varPixelValue = " + str( varPixelValue ) )

# 画素値の平均を求める関数
def calc_avePixelValue( gray_img, total, h, w ):

    # 画素値が0でないピクセルの個数
    numPixel = 0
     
    for y in range( h ):
        for x in range( w ):
            
            # 画素値が0でない場合
            if gray_img[ y, x ] > 0:
                
                numPixel += 1

    return total / numPixel, numPixel

# 画素値の分散を求める関数
def calc_varPixelValue( gray_img, ave, h, w, n ):

    var = 0
    tmp = 0
    
    for y in range( h ):
        for x in range( w ):

             # 画素値が0でない場合
            if gray_img[ y, x ] > 0:
            
                tmp = gray_img[ y, x ] - ave
                var += np.power( tmp, 2 )

    return var / n

if __name__ == "__main__":
    main()