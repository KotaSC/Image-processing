import cv2
import numpy as np
import sys
args = sys.argv

def main():
    
    # 入力画像を読み込み
    image_name = args[1]
    img = cv2.imread( image_name )

    height, width = img.shape[0], img.shape[1]
    
    # 画像の切り出し
    # crop_im = img[415:440, 0:width]
    crop_image = img[20:60, 200:width-200]

    # 出力ファイル名
    crop_image_name = args[2]
    cv2.imwrite( crop_image_name, crop_image )

if __name__ == "__main__":
    main()