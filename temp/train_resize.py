import os
import cv2
from tqdm import tqdm

#画像入ったディレクトリのpath
img_dir="data/interim"
#リサイズ後の画像を保存するディレクトリのpath
save_dir="data/processed"
#save_dirを作っていない場合、ディレクトリを作成する
if not os.path.isdir(save_dir):
    os.makedirs(save_dir)

files=os.listdir(img_dir)#元画像をリスト化

#リサイズ＆保存の処理
for file in tqdm(files):
    img=os.path.join(img_dir,file)
    read_img=cv2.imread(img)
    #cv2.imshow("readimg",read_img)
    #cv2.waitKey()
    img_resize=cv2.resize(read_img,(64,64))

    save_img_path=os.path.join(save_dir,file)
    cv2.imwrite(save_img_path,img_resize)


