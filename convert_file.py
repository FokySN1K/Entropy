import os
from cryptography.fernet import Fernet

DIRECTORY_PATH_ANALYZE_FILES = 'FILES/ANALYZE_FILES/'
DIRECTORY_PATH_ANALYZE_FILES_DAMP = 'FILES/ANALYZE_FILES_DAMP/'
DIRECTORY_PATH_ENCRYPT_FILES = 'FILES/ENCRYPT_FILES/'
DIRECTORY_PATH_ENCRYPT_FILES_DAMP = 'FILES/ENCRYPT_FILES_DAMP/'

def get_files_in_directory(DIRECTORY_PATH):
    return os.listdir(DIRECTORY_PATH)

def convert_txt_file_to_damp_UTF_8(DIRECTORY_SRC, DIRECTORY_DEST):

    if DIRECTORY_SRC[-1] != '/':
        DIRECTORY_SRC += '/'
    if DIRECTORY_DEST[-1] != '/':
        DIRECTORY_DEST += '/'

    for FILES in get_files_in_directory(DIRECTORY_SRC):

        FILE_PATH_SRC = DIRECTORY_SRC + FILES
        FILE_PATH_DEST = DIRECTORY_DEST + FILES + "_damp"

        with open(FILE_PATH_SRC, mode='r+', encoding='utf-8') as f_src:

            with open(FILE_PATH_DEST, mode='w+', encoding='utf-8') as f_dest:

                for char in f_src.read():
                    byte = ord(char)
                    f_dest.write(str(byte) + '\n')

def convert_txt_file_to_encrypt_files_UTF_8(DIRECTORY_SRC, DIRECTORY_DEST):

    if DIRECTORY_SRC[-1] != '/':
        DIRECTORY_SRC += '/'
    if DIRECTORY_DEST[-1] != '/':
        DIRECTORY_DEST += '/'


    for FILES in get_files_in_directory(DIRECTORY_SRC):


        FILE_PATH_SRC = DIRECTORY_SRC + FILES
        FILE_PATH_DEST = DIRECTORY_DEST + FILES + "_encrypt"

        key = Fernet.generate_key()
        cipher_suite = Fernet(key)


        with open(FILE_PATH_SRC, mode='r+', encoding='utf-8') as f_src:

            with open(FILE_PATH_DEST, mode='w+', encoding='utf-8') as f_dest:

                data = bytes(f_src.read(), encoding='utf8')
                encrypted_data = cipher_suite.encrypt(data).decode('utf-8')

                f_dest.write(encrypted_data)

                #decrypted_data = cipher_suite.decrypt(encrypted_data).decode('utf-8')


if __name__ == '__main__':


    convert_txt_file_to_damp_UTF_8(DIRECTORY_PATH_ANALYZE_FILES, DIRECTORY_PATH_ANALYZE_FILES_DAMP)
    convert_txt_file_to_encrypt_files_UTF_8(DIRECTORY_PATH_ANALYZE_FILES, DIRECTORY_PATH_ENCRYPT_FILES)
    convert_txt_file_to_damp_UTF_8(DIRECTORY_PATH_ENCRYPT_FILES, DIRECTORY_PATH_ENCRYPT_FILES_DAMP)













