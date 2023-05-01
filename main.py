from storage import read_from_blob, list_files_in_blob, upload_to_blob, delete_blob

def read_blob(file):
    blob_file_path = file
    byte_data = read_from_blob(blob_file_path)
    return byte_data

def list_blob(folder_name):
    file_ls = list_files_in_blob(folder_name)
    return file_ls

def upload_blob(local_filename, blob_name_file):
    upload_to_blob(local_filename,blob_name_file)

if __name__ == "__main__":
    #read_blob("perfil.jpg")
    #list_blob("")
    upload_blob("C:\\Users\\wever\\Pictures\\Saved Pictures\\pexels-eberhard-grossgasteiger-640809.jpg", "azure/wallpaper")
    delete_blob("wallpaper.txt")
    
    
"""
Link Reference:
https://pub.towardsai.net/how-to-list-read-upload-and-delete-files-in-azure-blob-storage-with-python-836f8efa1c99
"""