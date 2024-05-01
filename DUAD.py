#-------------------------------------------------------------------------------
# Name:             DUAD.py
# Purpose:          Discord uploader and downloader in one file
#
# Author:           MS Productions
#
# Created:          13 03 2024
# License:          Apache License Version 2.0
#
# Developed by:     Meit Sant [Github:MT_276]
#-------------------------------------------------------------------------------


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Functions.py ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

import os, sys
import json, requests
from zipfile import ZipFile, ZIP_DEFLATED
from tkinter.filedialog import askopenfilename

from logging import basicConfig, CRITICAL
basicConfig(level=CRITICAL)

# Trying to import discord-webhook
try:
    from discord_webhook import DiscordWebhook
    
except ModuleNotFoundError:
    print("[ERROR] discord-webhook not found. Installing...\n")
    
    exit_code = os.system("pip install discord-webhook")
    
    if exit_code != 0:
        print("\n[ERROR] Error Code : ",exit_code)
        print("[ERROR] Could not install discord-webhook. Exiting...")
        exit()
    else:
        print("\n[INFO] discord-webhook installed successfully.\n")
        from discord_webhook import DiscordWebhook

def send_message(webhook_url,thread_id,message):
    webhook = DiscordWebhook(url=webhook_url, thread_id=thread_id, content=message)
    webhook.execute()

def send_file(webhook_url,thread_id,folder_path,file_name,file_dict):
    print(f"Uploading file {file_name} to Discord...")
    
    webhook = DiscordWebhook(url=webhook_url, thread_id=thread_id)
    
    with open(f"{folder_path}/{file_name}", "rb") as f:
        # Get the size on disk of the file
        file_size = os.path.getsize(f"{folder_path}/{file_name}")
        
        if file_size > 26203915:
            print(f"File {file_name} is too large to send [Over 25 MB]. Skipping...")
            return file_dict
        
        webhook.add_file(file=f.read(), filename=file_name)
    
    webhook.execute()
    
    webhook_data = webhook.json['attachments'][0]

    file_dict[webhook_data['filename']] = webhook_data['url']
    
    print(f"Uploaded.")
    
    return file_dict
 
def upload_files(webhook_url,thread_id,folder_path):
    files = os.listdir(folder_path)
    files.sort()
    
    file_dict = {}
    
    for file in files:
        file_dict = send_file(webhook_url,thread_id,folder_path,file,file_dict)
    
    # Generating the Key string
    Str = json.dumps(file_dict)
    file_dict = eval(Str)
    New_dict = {}
    for i in file_dict:
        New_dict['File_Name'] = i[:-4]
        break

    for i in file_dict:
        New_dict[i[-3:]] = file_dict[i][39:]
    
    send_message(webhook_url,thread_id,f"  **   **")

    
    str_dict = str(New_dict)
    
    if len(str_dict) > 2000:
        # Write the key to a file
        with open(f"Key_{New_dict['File_Name']}.txt", "w") as f:
            f.write(str_dict)
        send_message(webhook_url,thread_id,f"Key too large. Key was saved in uploader's pc.")
        return
    send_message(webhook_url,thread_id,f"Key for Downloading. Please Copy-Paste this key in the program to download the files.")
    send_message(webhook_url,thread_id,f"```{str_dict}```")
    
def download_files(string):
    folder_path = "./Downloads/RAW/"
    
    if not os.path.exists(folder_path):
        pass
    elif os.path.exists(f"{folder_path[:-1]}_1/"):
        i = 2
        while os.path.exists(f"{folder_path[:-1]}_{i}/"):
            i += 1
        folder_path = f"{folder_path[:-1]}_{i}/"
    else:
        folder_path = f"{folder_path[:-1]}_1/"
    os.makedirs(folder_path)
    file_dict = eval(string)
    #print(file_dict)
    
    if 'File_Name' in file_dict: 
        new_file_dict = {}
        
        for i in file_dict:
            if i == 'File_Name':
                continue
            new_file_dict[f"{file_dict['File_Name']}.zip.{i}"] = f"https://cdn.discordapp.com/attachments/{file_dict[i]}"
        
        file_dict = new_file_dict
    
    for num,i in enumerate(file_dict):
        url = file_dict[i]
        print(f"{num+1}. Downloading {i}...")
        r = requests.get(url, allow_redirects=True)
        if ".zip." in i:
            open(f"{folder_path}{i}", 'wb').write(r.content)
        else:
            open(f"./Downloads/{i}", 'wb').write(r.content)
        print(f"Downloaded.")
    return folder_path
        
def zip_and_split(file_path):
    '''
    Zips the file and splits it into chunks of 25 MB
    '''
    
    # If the path is of a folder, then zip the folder
    if os.path.isdir(file_path):
        
        # Get the base folder name
        folder_name = os.path.basename(file_path)
        # Creating a new folder "Zipped" to store the zipped and split files
        folder_path = "./Zipped/"
        
        if not os.path.exists(folder_path):
            pass
        elif os.path.exists(f"{folder_path[:-1]}_1/"):
            i = 2
            while os.path.exists(f"{folder_path[:-1]}_{i}/"):
                i += 1
            folder_path = f"{folder_path[:-1]}_{i}/"
        else:
            folder_path = f"{folder_path[:-1]}_1/"
        os.makedirs(folder_path)
        
        # Zip the folder
        with ZipFile(f'{folder_path}{folder_name}.zip', 'w') as zip_archive:
            for foldername, subfolders, filenames in os.walk(file_path):
                for filename in filenames:
                    # Create a complete filepath
                    file_path = os.path.join(foldername, filename)
                    # Add file to zip
                    zip_archive.write(file_path, os.path.relpath(file_path, file_path))
        file_path = f"{folder_path}{folder_name}.zip"
        path_of_zip_file = file_path
    else:
        # Creating a new folder "Zipped" to store the zipped and split files
        folder_path = "./Zipped/"
        if not os.path.exists(folder_path):
            pass
        elif os.path.exists(f"{folder_path[:-1]}_1/"):
            i = 2
            while os.path.exists(f"{folder_path[:-1]}_{i}/"):
                i += 1
            folder_path = f"{folder_path[:-1]}_{i}/"
        else:
            folder_path = f"{folder_path[:-1]}_1/"
        os.makedirs(folder_path)
            
        filename = os.path.basename(file_path)
        # Open the archive in write mode
        with ZipFile(f'{folder_path}/{filename}.zip', 'w') as zip_archive:
            # Add only the file (not the parent directory)
            zip_archive.write(file_path, filename)  # Specify filename within the archive
        path_of_zip_file = f"{folder_path}/{filename}.zip"
        
    filename = os.path.basename(file_path)
    base_file_name = filename
    
    # Split the zip file into chunks
    with open(path_of_zip_file, "rb") as f_in:
        byte = f_in.read(1)
        chunk_count = 1
        while byte:
            chunk_file_name = f"{folder_path}{base_file_name}.{str(chunk_count).zfill(3)}"
            with open(chunk_file_name, "wb") as f_out:
                f_out.write(byte)
                Chunk = int(24.99 * 1024.0 * 1024.0) +1
                #print(type(Chunk), f"{Chunk}")
                for _ in range(Chunk - 1):  # -1 for the byte already read
                    byte = f_in.read(1)
                    if not byte: break
                    f_out.write(byte)
            chunk_count += 1
            byte = f_in.read(1)

    os.remove(path_of_zip_file)
    return folder_path

def Choose_File(Type):
    '''
    Get the file path from user by opening an Explorer window
    '''
    try:
        # Open a Explorer window to choose a file
        filename = askopenfilename()
    except :
        print("[ERROR] Could not open explorer window.")
        filename = input("\nPlease enter the path of the image manually: ")
    if filename == '':
        return # If the user closes the window without choosing a file, then do nothing.
    return filename

def zip_merge():
    '''
    Merge the split files and unzip them
    '''
    folder_path = "./Downloads/RAW/"
    
    # Arrange files in ascended order
    file_names_list = os.listdir(folder_path)
    file_names_list.sort()

    # Unzip the files
    base_file_name = file_names_list[0][:-8]

    # Concatenate
    with open(f"{folder_path[:-4]}{base_file_name}.zip", "wb") as outfile:
        for i in file_names_list:
            with open(f"{folder_path}{i}", "rb") as infile:
                outfile.write(infile.read())

    print(f"\nFile {base_file_name}.zip merged successfully.")
    print(f"Unzipping {base_file_name}.zip...")
    
    with ZipFile(f"{folder_path[:-4]}{base_file_name}.zip", "r") as zip_ref:
        try:
            zip_ref.extractall(folder_path[:-4])
            os.remove(f"{folder_path[:-4]}{base_file_name}.zip")

        except IsADirectoryError:
            # Checking if a folder with the same name as the base file name already exists
            if os.path.exists(f"./{base_file_name}"):
                print(f"[ERROR] A folder with the name {base_file_name} already exists.")
                zip_ref.extractall(f"./{base_file_name}_New")
            else:
                zip_ref.extractall(f"./{base_file_name}")
            
        
        except:
            print(f"[ERROR] Could not extract {base_file_name}.zip")
            sys.exit()
    
def update_webhook(webhook_url,Version,mode):
    '''
    Update the name of the webhook
    '''
    
    new_name = f"[{mode}] Database Bot V{Version}"

    headers = { "Content-Type": "application/json",}
    data = {"name": new_name,}

    response = requests.patch(webhook_url, headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        print(f"[ERROR] Could not update the webhook. Error Code: {response.status_code}")
        sys.exit()
    else:
        return
        

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main.py ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

Program_version = "1.8"
mode = "Stable"

print(f'Discord Uploader and Downloader V{Program_version}')
print('Developed by     : Meit Sant')
print('Licence          : Apache License Version 2.0')

option = input('\nUpload [U] or Download [D] : ')


if option in ['U','u','Upload','upload']:
    
    webhook_url = input('\nEnter the webhook URL : ')
    thread_id = input('Enter the thread ID : ')
    
    update_webhook(webhook_url,Program_version,mode)

    option = input('\nUpload a file [A] or a folder [B] : ')

    if option in ['A','a','File','file']:
        file_path = input('\nEnter the file path : ')

        # Checking if the entered string is empty.
        if file_path == "":
            print('\n[ERROR] Invalid file path. Exiting...')
            sys.exit()

        file_path = file_path.replace('"','')

        #Check if file exists
        if not os.path.isfile(file_path):
            print(f"\n[ERROR] Could not find {file_path}. Exiting...")
            sys.exit()

        # Checking size of file
        file_size = os.path.getsize(file_path)

        # If file size is greater than 25 MB, zip and split the file
        if file_size > 26203915:
            
            # Getting base name of the file
            file_name = os.path.basename(file_path)
            
            print(f"\n[WARN] File {file_name} is too large to send independently [Over 25 MB].")
            print('\n[INFO] Zipping and splitting file...')
            
            # Calculating the number of files to be zipped
            num = file_size//26203915
            if file_size%26203915 != 0:
                num += 1
            print(f'[INFO] The file will be zipped in chunks of {num} files.')
            if num > 10:
                print(f'[INFO] This may take a while...')

            folder_path = zip_and_split(file_path)

            print('[INFO] Zipped.\n\n[INFO] Uploading files...\n')


            upload_files(webhook_url,thread_id,folder_path)

            # Delete the zipped folder
            for i in os.listdir(folder_path):
                os.remove(f"{folder_path}{i}")
            os.rmdir(folder_path)

            print('\n[INFO] Files uploaded. Exiting...')
            sys.exit()
        else:
            # If the file size is less than 25 MB, send the file directly
            
            print('\n[INFO] Uploading file...\n')
            # Getting base name of the file
            file_name = os.path.basename(file_path)
            # Getting the directory of the file
            folder_path = os.path.dirname(file_path)
            # Sending the file
            file_dict = send_file(webhook_url,thread_id,folder_path,file_name,{})
            # Sending the sharing link
            send_message(webhook_url,thread_id,f"File - `{file_name}` sharing link : {file_dict[file_name]}```{file_dict[file_name]}```")
            sys.exit()

    if option in ['B','b','Folder','folder']:
        
        # Getting folder path
        folder_path = input('\nEnter the folder path : ')
        folder_path = folder_path.replace('"','')

        #Check if folder exists
        if not os.path.isdir(folder_path):
            print(f"\n[ERROR] Could not find {folder_path}. Exiting...")
            sys.exit()

        print('\n[INFO] Uploading files...\n')
        list_files = os.listdir(folder_path)
        list_files.sort()
        file_dict = {}
        for i,file in enumerate(list_files):
            print(f"{i+1}. ",end='')
            file_dict = send_file(webhook_url,thread_id,folder_path,file,file_dict)
        send_message(webhook_url,thread_id,f"  **   **")

        # Generating the Key string
        str_dict = str(file_dict)

        if len(str_dict) > 1994:
            # Write the key to a file
            dir_name = os.path.basename(folder_path)
            # Checking if a key with same name exists
            if os.path.isfile(f"Key_Folder-{dir_name}.txt"):
                if os.path.isfile(f"Key_Folder-{dir_name}_1.txt"):
                    i = 2
                    while os.path.isfile(f"Key_Folder-{dir_name}_{i}.txt"):
                        i += 1
                    dir_name = f"{dir_name}_{i}"
                else:
                    dir_name = f"{dir_name}_1"
            with open(f"Key_Folder-{dir_name}.txt", "w") as f:
                f.write(str_dict)
            send_message(webhook_url,thread_id,f"Key too large. Key was saved in uploader's pc.")

        send_message(webhook_url,thread_id,f"Key for Downloading. Please Copy-Paste this key in the program to download the files.")
        send_message(webhook_url,thread_id,f"```{str_dict}```")
        print('\n[INFO] Files uploaded. Exiting...')
        sys.exit()
            
        """
        # Code has been commented as folder zipping was giving errors and did not work.
        
        option = input('\nDo you want to upload \n- The contents of the folder [A] or \n- Folder as a zip [B] : ')

        if option in ['A','a','Contents','contents']:
            print('\n[INFO] Uploading files...\n')
            list_files = os.listdir(folder_path)
            list_files.sort()
            file_dict = {}
            for i,file in enumerate(list_files):
                print(f"{i+1}. ",end='')
                file_dict = send_file(webhook_url,thread_id,folder_path,file,file_dict)
            send_message(webhook_url,thread_id,f"  **   **")

            # Generating the Key string
            str_dict = str(file_dict)

            if len(str_dict) > 1994:
                # Write the key to a file
                dir_name = os.path.basename(folder_path)
                # Checking if a key with same name exists
                if os.path.isfile(f"Key_Folder-{dir_name}.txt"):
                    if os.path.isfile(f"Key_Folder-{dir_name}_1.txt"):
                        i = 2
                        while os.path.isfile(f"Key_Folder-{dir_name}_{i}.txt"):
                            i += 1
                        dir_name = f"{dir_name}_{i}"
                    else:
                        dir_name = f"{dir_name}_1"
                with open(f"Key_Folder-{dir_name}.txt", "w") as f:
                    f.write(str_dict)
                send_message(webhook_url,thread_id,f"Key too large. Key was saved in uploader's pc.")

            send_message(webhook_url,thread_id,f"Key for Downloading. Please Copy-Paste this key in the program to download the files.")
            send_message(webhook_url,thread_id,f"```{str_dict}```")
            print('\n[INFO] Files uploaded. Exiting...')
            sys.exit()
        
        if option in ['B','b','Zip','zip']:
            print('\n[INFO] Zipping and splitting folder...')
            zipped_folder = zip_and_split(folder_path)
            print('[INFO] Zipped.\n\n[INFO] Uploading files...\n')

            upload_files(webhook_url,thread_id,f"{zipped_folder}/")

            # Delete the zipped folder
            for i in os.listdir(zipped_folder):
                os.remove(f"{zipped_folder}/{i}")
            os.rmdir(zipped_folder)

            print('\n[INFO] Files uploaded. Exiting...')
            sys.exit()"""

    else:
        print('\n[ERROR] Invalid option. Exiting...')
        sys.exit()

if option in ['D','d','Download','download']:
    string = input('\nEnter the key or or directly the path of the file containing the Key \n->')

    # Checking if the entered string is empty.
    if string == "":
        print('\n[ERROR] Invalid key. Exiting...')
        sys.exit()

    # Checking if the entered string is a path to the file containing the key.
    if string[0] != "{":
        string = string.replace('"','')
        if os.path.isfile(string):
            # Checking if the file is a txt.
            if string[-4:] != ".txt":
                print('\n[ERROR] Invalid file. It needs to be a .txt file. Exiting...')
                sys.exit()

            with open(string, "r") as f:
                string = f.read()
        else:
            print('\n[ERROR] Could not find the file. Exiting...')
            sys.exit()

    print('\n[INFO] Downloading files...\n')
    folder_path=download_files(string)

    try:
        # Checks if the RAW folder is empty
        os.rmdir(folder_path)
        print("\n[INFO] Files downloaded. Exiting...")
    except:
        print("\n[INFO] Files downloaded. Merging files...")
        zip_merge()
        print("\n[INFO] Files merged.\n[INFO] Original reconstructed successfully. Exiting...")

        # Delete the RAW folder
        for file in os.listdir(folder_path):
            os.remove(f"./Downloads/RAW/{file}")
        os.rmdir(folder_path)

else:
    print('\n[ERROR] Invalid option. Exiting...')
    sys.exit()

