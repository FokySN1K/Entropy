import convert_file as conv
import graph as gr

def init_FILES():

    conv.convert_txt_file_to_damp_UTF_8(conv.DIRECTORY_PATH_ANALYZE_FILES, conv.DIRECTORY_PATH_ANALYZE_FILES_DAMP)
    conv.convert_txt_file_to_encrypt_files_UTF_8(conv.DIRECTORY_PATH_ANALYZE_FILES, conv.DIRECTORY_PATH_ENCRYPT_FILES)
    conv.convert_txt_file_to_damp_UTF_8(conv.DIRECTORY_PATH_ENCRYPT_FILES, conv.DIRECTORY_PATH_ENCRYPT_FILES_DAMP)

def create_graphs():
    gr.create_graphs_UTF_8(conv.DIRECTORY_PATH_ANALYZE_FILES_DAMP)
    gr.create_graphs_UTF_8(conv.DIRECTORY_PATH_ENCRYPT_FILES_DAMP)

def create_entopy_graphs():
    gr.create_graphs_entropy(conv.DIRECTORY_PATH_ANALYZE_FILES_DAMP)
    gr.create_graphs_entropy(conv.DIRECTORY_PATH_ENCRYPT_FILES_DAMP)

if __name__ == '__main__':

    init_FILES()
    create_graphs()
    create_entopy_graphs()
