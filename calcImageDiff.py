import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    
    # 入力画像を読み込み
    img_thickEdge = cv2.imread( "th0.3_cropDownside.bmp" )
    img_sharpEdge = cv2.imread( "th0.3_dim3_cropDownside.bmp" )
    
    # グレースケール変換
    gray_thickEdge = cv2.cvtColor( img_thickEdge, cv2.COLOR_RGB2GRAY )
    gray_sharpEdge = cv2.cvtColor( img_sharpEdge, cv2.COLOR_RGB2GRAY )

    gray_thickEdge[gray_thickEdge != 0] = 255
    gray_sharpEdge[gray_sharpEdge != 0] = 255

    # cv2.imwrite( 'th0.3_Down.bmp', gray_thickEdge )
    # cv2.imwrite( 'th0.3_dim2_Up.bmp', gray_sharpEdge )

    # height, width = gray_thickEdge.shape[0], gray_thickEdge.shape[1]

    diffImg = cv2.absdiff( gray_thickEdge, gray_sharpEdge )
    # diffImg = gray_thickEdge - gray_sharpEdge
    # diffImg = gray_sharpEdge - gray_thickEdge
    # diffImg = diff_Img( gray_thickEdge, gray_sharpEdge, height, width )

    # print( diffImg )

    cv2.imwrite( 'downdim3.bmp', diffImg )

if __name__ == "__main__":
    main()