"""
画像ファイルを1スタートから0からスタートで番号をリネームしていく。
また方角に関しても北を0として、時計周りに1, 2, 3にリネームする。なお、方角に関しては3グループに別れているので全て統一させる。
今回使用するのは、画像のファイル名で3079~4402に相当するファイル。これを0000~1323にする。
"""

import os
import glob

"""
必要な画像ファイルのpathだけをfile_listに格納する。
"""


def append_list(file_list, files):
    for file in files:
        basename = os.path.basename(file)
        stem = basename.split(".")[0]
        stem = int(stem.split("_")[1])
        if stem != 0 and stem != 5:
            file_list.append(file)

    return file_list


"""
画像ファイル名をここで0スタートにしてrenameする。（方角に関してはここでは何もしない）
"""


def rename_number(file_list):
    path_list = []
    path_4_list = []
    for file in file_list:
        path_1 = os.path.basename(file)
        path_2 = path_1.split(".")[0]
        path_3 = int(path_2.split("_")[0])
        path_4 = str(path_3 - 3079)
        path_4_list.append(path_4)
        path_5 = path_4.zfill(6)
        path_list.append(path_5)

    return path_list, path_4_list


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

    return path_list


if __name__ == '__main__':
    path_3 = './data/raw/part3/*.jpg'
    path_4 = './data/raw/part4/*.jpg'
    path_5 = './data/raw/part5/*.jpg'

    file_list = []
    file_list_3 = sorted(glob.glob(path_3))
    file_list_4 = sorted(glob.glob(path_4))
    file_list_5 = sorted(glob.glob(path_5))

    file_list = append_list(file_list, file_list_3[879 * 6:])
    file_list = append_list(file_list, file_list_4)
    file_list = append_list(file_list, file_list_5[:18])
    path_list, path_4_list = rename_number(file_list)

    group_1 = [str(i) for i in range(0, 123)] + [
        str(i) for i in range(321, 569)
    ] + [str(i) for i in range(1051, 1323)]
    group_2 = [str(i) for i in range(123, 321)] + [
        str(i) for i in range(569, 765)
    ] + [str(i) for i in range(766, 1051)]
    group_3 = ["765"]

    path_list = rename_direction(path_list, path_4_list)

    new_dir_path = "./data/interim"
    os.mkdir(new_dir_path, exist_ok=True)

    path_list_fin = []
    for path in path_list:
        path__ = new_dir_path + "/" + path + ".jpg"
        path_list_fin.append(path__)

    for file in file_list:
        os.rename(file_list, path_list_fin)
