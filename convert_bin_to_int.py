import os
import convert_file as conv



def convert_bin_to_int_file(FILE) -> Exception:

    FileName, FileExcension = os.path.splitext(FILE)

    if (FileExcension != ".bin"):
        return Exception("Не то расширение файла")

    with open(FILE, "rb") as file_src:
        with open(FileName.replace("BIN_DAMP", "ANALYZE_FILES_DAMP") + ".bin.txt", "w+", encoding="utf-8") as file_dest:
            for i in file_src.read()[0:10000000]:
                file_dest.write(str(i) + '\n')

    return True

def convert_bin_to_int_directory(DIRECTORY_SRC):

    if DIRECTORY_SRC[-1] != '/':
        DIRECTORY_SRC += '/'

    for FILES in conv.get_files_in_directory(DIRECTORY_SRC):
        convert_bin_to_int_file(DIRECTORY_SRC + FILES)



