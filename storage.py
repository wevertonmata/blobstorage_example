from azure.storage.blob import BlobServiceClient, BlobClient
import os


def get_details():
    connection_string = 'AZURE_STORAGE_CONNECTION_STRING'
    container_name = 'AZURE_STORAGE_CONTAINER_NAME'
    return connection_string, container_name

def get_clients_with_connection_string():
    connection_string, container_name = get_details()
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    return container_client


## Read 

def read_from_blob(blob_file_path):
    container_client = get_clients_with_connection_string()
    blob_client = container_client.get_blob_client(blob_file_path)
    byte_data = blob_client.download_blob().readall()
    return byte_data


# List

def list_files_in_blob(folder_name):
    container_client = get_clients_with_connection_string()
    file_ls =  [file['name'] for file in list(container_client.list_blobs(name_starts_with=folder_name))]
    return file_ls

# Upload

def upload_to_blob(file_name,blob_name):
    connection_string, container_name = get_details()
    blob = BlobClient.from_connection_string(connection_string, container_name=container_name, blob_name=blob_name)
    with open(file_name, "rb") as data:
        try:
            blob.upload_blob(data)
            print("upload finish")
        except Exception as err:
            print(err)
       
#Delete

def delete_blob(blob_name):
    connection_string, container_name = get_details()
    blob = BlobClient.from_connection_string(connection_string, container_name=container_name, blob_name=blob_name)
    blob.delete_blob(delete_snapshots="include")
    print(f"Deleted {blob_name}")
        

# Utils

def read_from_local_system(local_filename):
    with open(f'{local_filename}', 'rb') as f:
        binary_content = f.read()
    return binary_content 

def save_to_local_system(byte_file, filename):
    with open(f'{filename}', 'wb') as f:
        f.write(byte_file)
