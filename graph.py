#!/usr/bin/python
# -*- coding: utf8 -*-

import convert_file as conv
import matplotlib.pyplot as plt

import entropy
import entropy as entr

DIRECTORY_PATH_ANALYZE_FILES = conv.DIRECTORY_PATH_ANALYZE_FILES
DIRECTORY_PATH_ANALYZE_FILES_DAMP = conv.DIRECTORY_PATH_ANALYZE_FILES_DAMP
DIRECTORY_PATH_ENCRYPT_FILES = conv.DIRECTORY_PATH_ENCRYPT_FILES
DIRECTORY_PATH_ENCRYPT_FILES_DAMP = conv.DIRECTORY_PATH_ENCRYPT_FILES_DAMP

arr = [6.0851620967785385, 4.450993809233886, 11.410621824471038, 0.16594916998475207, 0.07004348083772004, 0.07058227684416403, 0.03125016837375201, 2.005398735984569, 0.11368595735968404, 0.7995732735628964, 0.007004348083772003, 0.009698328115992005, 0.02370702428353601, 0.02047424824487201, 0.02047424824487201, 0.02370702428353601, 0.02316822827709201, 0.02047424824487201, 0.01939665623198401, 0.009698328115992005, 0.009698328115992005, 0.18157425417162806, 0.34159666808549616, 0.0010775920128880004, 0.0010775920128880004, 0.14062575768188407, 0.0026939800322200013, 0.0037715720451080015, 0.003232776038664002, 0.0026939800322200013, 0.0005387960064440002, 0.001616388019332001, 0.0005387960064440002, 0.001616388019332001, 0.2974153955570881, 0.004310368051552002, 0.04472006853485202, 0.005387960064440003, 0.0037715720451080015, 0.0005387960064440002, 0.0037715720451080015, 0.0005387960064440002, 0.004310368051552002, 0.0048491640579960025, 0.0026939800322200013, 0.10775920128880004, 0.0005387960064440002, 0.31142409172463215, 0.0005387960064440002, 0.04310368051552002, 0.04310368051552002, 0.0026939800322200013, 0.001616388019332001, 0.0010775920128880004, 0.10075485320502804, 0.02209063626420401, 0.032327760386640016, 0.032866556393084015, 0.19450535832628407, 0.012392308148212006, 0.014008696167544006, 0.018319064219096008, 0.08081940096660004, 0.005387960064440003, 0.0037715720451080015, 0.06519431677972402, 0.03556053642530402, 0.08459097301170804, 0.07112107285060804, 0.018857860225540007, 0.009698328115992005, 0.07758662492793604, 0.07974180895371204, 0.09321170911481204, 0.060345152721728024, 0.018857860225540007, 0.0010775920128880004, 0.005387960064440003, 0.005926756070884003, 0.002155184025776001, 0.21120803452604808, 0.08890134106326004, 0.08782374905037203, 0.08081940096660004, 0.12931104154656006, 0.33405352399528015, 0.09267291310836805, 0.14170334969477205, 0.11637993739190405, 0.02047424824487201, 0.09913846518569605, 0.4089461688909962, 0.24191940689335611, 0.09375050512125604, 0.12392308148212006, 0.34105787207905214, 0.31196288773107617, 0.33351472798883613, 0.05334080463795602, 0.2710143912413321, 0.24245820289980013, 0.09806087317280805, 0.017241472206208006, 0.032327760386640016, 0.007004348083772003, 0.09859966917925204, 0.017241472206208006, 0.011314716135324004, 0.0026939800322200013, 0.06196154074106003, 5.241407550687234, 1.1088421812617524, 2.9353606431069132, 1.2392308148212006, 2.379861960463149, 6.066304236552999, 0.7855645773953525, 1.1228508774292965, 4.04474162037511, 1.4859993857725526, 1.9499027473208368, 3.3038971115146096, 2.227921486645941, 4.79366806933227, 6.8039159693748354, 1.5598144386553807, 3.0926890769885613, 3.336763667907693, 3.965538607427842, 1.9590622794303847, 0.08243578898593204, 0.7386893248347243, 0.27532475929288414, 0.9014057187808124, 0.5802832989401883, 0.15140167781076405, 0.01778026821265201, 1.6158492233255568, 1.5840602589453607, 0.09159532109548005, 0.48868797784470824, 1.3313649319231247, 0.05765117268950803, 0.11368595735968404, 0.049030436586404026, 0.013469900161100005, 0.0010775920128880004, 0.0010775920128880004, 0.2176735866033761, 0.009159532109548004]


def create_database_for_grapf_UTF_8(FILES_PATH):

    arr_size = 0
    arr = []

    with open(FILES_PATH, mode='r+', encoding='utf-8') as f:
        for char in f.readlines():
            try:
                index = int(char)
                #print(char)
            except:
                continue

            #print(chr(index))
            if index >= arr_size:
                arr += [0]*(index-arr_size + 1)
                arr_size = index + 1
            #print(chr(index))
            arr[index] += 1

    total_arr = []
    # иначе очень плохая картинка
    for i in range(len(arr)):
        if arr[i] != 0:
            total_arr.append([arr[i], str(chr(i))])

    return total_arr

def create_graph_for_file_UTF_8(database: list, FILE: str):

    DIRECTORY_PATH = 'GRAPHS/'
    file = DIRECTORY_PATH + FILE + ".png"

    total_sum = sum([i[0] for i in database])
    y = [i[0]/total_sum for i in database]
    x = [str(i[1]) for i in database]

    entropy = entr.entropy_for_arr_chance(y)

    y = [i*100 for i in y]
    fig=plt.figure(figsize=(20,20))
    plt.bar(x, y, label=f'Количество символов: {total_sum}. Entropy: {entropy}')  # Параметр label позволяет задать название величины для легенды
    plt.xlabel('Символ')
    plt.ylabel('Появление символа в процентах')
    plt.title('Гистограмма')
    plt.legend()
    plt.grid(color='blue', linestyle='--', linewidth=0.1)
    #plt.show()
    plt.savefig(file, dpi=fig.dpi)
def create_graph_entropy_for_set_size(FILES_PATH: str, FILE: str, size: int):

    DIRECTORY_PATH = 'ENTROPY_GRAPHS/'
    file = DIRECTORY_PATH + FILE + ".png"


    arr = []

    with open(FILES_PATH, mode='r+', encoding='utf-8') as f:
        for char in f.readlines():
            try:
                index = int(char)
                #print(char)
            except:
                #print(char)
                continue

            arr.append(index)

    #print(len(arr))
    y = []
    x = []

    for i in range(0, len(arr), size):
        entropy = entr.entropy_for_arr(arr[i:i + size])
        if i == 0:
            y.append(entropy)
            x.append(i)

        y.append(entropy)
        x.append(i + size)

    fig = plt.figure(figsize=(20, 20))
    plt.plot(x, y, label="Entropy")
    plt.grid()
    #plt.show()
    plt.savefig(file, dpi=fig.dpi)


def create_graphs_UTF_8(DIRECTORY_PATH):

    if DIRECTORY_PATH[-1] != '/':
        DIRECTORY_PATH += '/'
    if DIRECTORY_PATH[0] == '/':
        DIRECTORY_PATH = DIRECTORY_PATH[1:]

    for FILES in conv.get_files_in_directory(DIRECTORY_PATH):

        FILE_PATH = DIRECTORY_PATH + FILES

        database = create_database_for_grapf_UTF_8(FILE_PATH)
        create_graph_for_file_UTF_8(database, FILES)

def create_graphs_entropy(DIRECTORY_PATH):
    if DIRECTORY_PATH[-1] != '/':
        DIRECTORY_PATH += '/'
    if DIRECTORY_PATH[0] == '/':
        DIRECTORY_PATH = DIRECTORY_PATH[1:]

    for FILES in conv.get_files_in_directory(DIRECTORY_PATH):

        FILE_PATH = DIRECTORY_PATH + FILES

        database = create_database_for_grapf_UTF_8(FILE_PATH)
        create_graph_entropy_for_set_size(FILE_PATH, FILES, size=400)

if __name__ == '__main__':

    #create_graphs_UTF_8(DIRECTORY_PATH_ANALYZE_FILES_DAMP)
    #create_graphs_UTF_8(DIRECTORY_PATH_ENCRYPT_FILES_DAMP)
    #create_graph_entropy_for_set_size(arr, "FILES/ENCRYPT_FILES_DAMP/1.txt_encrypt_damp", "123",  400)
    create_graphs_entropy(DIRECTORY_PATH_ANALYZE_FILES_DAMP)

