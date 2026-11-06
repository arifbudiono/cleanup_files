import os
import glob
import time

def delete_old_files(folder_path, num_files_to_keep=3):
    # Ambil semua file di folder
    files = glob.glob(os.path.join(folder_path, '*'))
    # Urutkan file berdasarkan waktu modifikasi (terbaru ke terlama)
    files.sort(key=os.path.getmtime, reverse=True)
    
    # Hapus file yang lebih lama dari num_files_to_keep
    for file in files[num_files_to_keep:]:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting file {file}: {e}")

def main():
    # Daftar folder yang ingin diproses
    folders = [
        "D:\LAB TESTING\DELETE FOLDER FOR 3 DAYS\A", #sesuaikan directory anda
        "D:\LAB TESTING\DELETE FOLDER FOR 3 DAYS\B",
        "D:\LAB TESTING\DELETE FOLDER FOR 3 DAYS\C"
    ]
    
    for folder in folders:
        if os.path.exists(folder):
            print(f"Processing folder: {folder}")
            delete_old_files(folder)
        else:
            print(f"Folder not found: {folder}")

if __name__ == "__main__":
    main()
