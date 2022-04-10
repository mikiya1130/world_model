"""
画像ファイルを1スタートから0からスタートで番号をリネームしていく。
また方角に関しても北を0として、時計周りに1, 2, 3にリネームする。なお、方角に関しては3グループに別れているので全て統一させる。
今回使用するのは、画像のファイル名で3079~4402に相当するファイル。これを0000~1323にする。
実行に関してはどの階層でもいいですが、part3,4,5の画像保存場所によってはエラーが起きるので、一部下記パスを適宜修正して下さい。
"""

import os
import glob

#画像ファイルのパスをいじりたい場合はここ
path_3 = './world_model/dataset/part3/*.jpg'
path_4 = './world_model/dataset/part4/*.jpg'
path_5 = './world_model/dataset/part5/*.jpg'

file_list = []
file_list_3 = sorted(glob.glob(path_3))
file_list_4 = sorted(glob.glob(path_4))
file_list_5 = sorted(glob.glob(path_5))
"""
必要な画像ファイルのpathだけをここで格納する。
"""


def append_list(files):
    for file in files:
        stem = file.split(".")[1]
        stem = int(stem.split("_")[2])
        if stem != 0 and stem != 5:
            file_list.append(file)


path_list = []
path_4_list = []
"""
画像ファイル名をここで0スタートにしてrenameする。（方角に関してはここでは何もしない）
"""


def rename_number(path_list, path_4_list, file_list):
    for file in file_list:
        path_1 = os.path.basename(file)
        path_2 = path_1.split(".")[0]
        path_3 = int(path_2.split("_")[0])
        path_4 = str(path_3 - 3079)
        path_4_list.append(path_4)
        path_5 = path_4.zfill(6)
        path_list.append(path_5)


append_list(file_list_3[879 * 6:])
append_list(file_list_4)
append_list(file_list_5[:18])
rename_number(path_list, path_4_list, file_list)

group_1 = [str(i)
           for i in range(0, 123)] + [str(i) for i in range(321, 569)
                                      ] + [str(i) for i in range(1051, 1323)]
group_2 = [str(i)
           for i in range(123, 321)] + [str(i) for i in range(569, 765)
                                        ] + [str(i) for i in range(766, 1051)]
group_3 = 765
"""
画像ファイル名の方角をここでrenameする。
"""


def rename_direction(path_list, path_4_list):
    for i in range(len(path_list)):
        if i % 4 == 0:
            if path_4_list[i] in group_1:
                path_list[i] = path_list[i] + "_" + "1"
            elif path_4_list[i] in group_2:
                path_list[i] = path_list[i] + "_" + "2"
            else:
                path_list[i] = path_list[i] + "_" + "3"
        elif i % 4 == 1:
            if path_4_list[i] in group_1:
                path_list[i] = path_list[i] + "_" + "2"
            elif path_4_list[i] in group_2:
                path_list[i] = path_list[i] + "_" + "3"
            else:
                path_list[i] = path_list[i] + "_" + "0"
        elif i % 4 == 2:
            if path_4_list[i] in group_1:
                path_list[i] = path_list[i] + "_" + "3"
            elif path_4_list[i] in group_2:
                path_list[i] = path_list[i] + "_" + "0"
            else:
                path_list[i] = path_list[i] + "_" + "1"
        else:
            if path_4_list[i] in group_1:
                path_list[i] = path_list[i] + "_" + "0"
            elif path_4_list[i] in group_2:
                path_list[i] = path_list[i] + "_" + "1"
            else:
                path_list[i] = path_list[i] + "_" + "2"


rename_direction(path_list, path_4_list)

path_list_fin = []
for i in range(len(path_list)):
    path__ = "./world_model/dataset/rename_file/" + path_list[i] + ".jpg"
    path_list_fin.append(path__)

for i in range(len(file_list)):
    os.rename(file_list[i], path_list_fin[i])
