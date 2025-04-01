import os
try:
    # If we're in colab, it'll uses this module
    from google.colab import drive  

    # Mount Google Drive
    drive.mount('/content/drive')  

    # Directory of your Google Drive
    directory = '/content/drive/MyDrive'

except ModuleNotFoundError:
    # Get directory on local
    directory = os.getcwd()


# List files and directories whit their sizes very well
def listCurrentDirectory(directory):  
    try:
        # Print titles well
        files = os.listdir(directory)
        print(f"{'Size':<7} {'unit':<5} {'Name'}" )

        for file in files:
            # Get the absolute path and size of the file/directory
            file_path = os.path.join(directory, file)
            size = os.path.getsize(file_path)

            # Calculate the size and add its determinated unit
            for unit in ["B","KiB", "MiB", "GiB"]:
                if size < 1024:
                    print(f"{size:<7.1f} {unit:<5} {file}")
                    break
                size /= 1024

    except FileNotFoundError as e:  
        print("Directory not found: ", e)

if __name__ == "__main__":
    # Call function
    listCurrentDirectory(directory)
