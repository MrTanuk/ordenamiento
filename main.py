import os
try:
    from google.colab import drive  

    # Mount Google Drive
    drive.mount('/content/drive')  

    # Directory of your Google Drive
    directory = '/content/drive/MyDrive/'  

except ModuleNotFoundError:
    directory = os.getcwd()


# List files and directories
def listCurrentDirectory(directory):  
    try:  
        files = os.listdir(directory)
        print(f"{'Size':<7} {'unit':<5} {'Name'}" )
        for file in files:
            size = os.path.getsize(file)
            unit = ""
            
            for unit in ["B","KiB", "MiB", "GiB"]:
                if size < 1024:
                    print(f"{size:<7.1f} {unit:<5} {file}")
                    break
                size /= 1024

    except FileNotFoundError:  
        print("Directory not found")

if __name__ == "__main__":
    # Call function
    listCurrentDirectory(directory)
