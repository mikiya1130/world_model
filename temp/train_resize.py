import os
import cv2

#windowsではpath頭にrもしくはRを記述
dir_imgdirs=r"C:\Users\kota713\Desktop\WorldModels\img"#イメージフォルダの入ったフォルダのパス
imgdirs_list=os.listdir(dir_imgdirs)#ディレクトリpart3,4,5をリスト化

first_loop=True
for imgdir in imgdirs_list:
    imgdirs=os.path.join(dir_imgdirs,imgdir)#フォルダ「part*」までの絶対パス

    files=os.listdir(imgdirs)#フォルダ内の全ファイルを読み取り（フォルダ毎に分けるなら要改善）

    for file in files:
        img=os.path.join(imgdirs,file)#画像ファイルまでのパス
        read_img=cv2.imread(img)#画像ファイル読み込み
        #cv2.imshow("readimg",read_img)
        img_resize=cv2.resize(read_img,(64,64))#画像をリサイズ(64*64)

        if first_loop:
            dir_resize_imgs=os.path.join(dir_imgdirs,"resize_img64px")#画像の保存先フォルダまでのパス
            #print(dir_resize_imgs)
            first_loop=False

        save_path=os.path.join(dir_resize_imgs,file)#画像ファイルの保存(ファイル名を変える場合、2引数目を任意の名称に要変更)
        cv2.imwrite(save_path,img_resize)#先に指定したパスでリサイズ画像を保存
