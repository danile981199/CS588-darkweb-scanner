
import os
import random
import string

def overwrite_delete(input_file, passes=3):
    if not os.path.exists(input_file):
        print("File not found.")
        return
    
    if passes not in [1, 3, 7]:
        #print("Using the default of 3 passes.")
        return
    
    try:
        file_size = os.path.getsize(input_file)
        
        with open(input_file, 'wb') as file:
            for i in range(passes):
                # Alternate between writing 0x00 and 0xFF
                fill_byte = b'\x00' if i % 2 == 0 else b'\xFF'
                file.write(fill_byte * file_size)
                file.flush()  # Ensure data is written to disk
                #
            # Final pass: Overwrite with random ASCII alphanumeric characters
            random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size)).encode()
            file.seek(0)
            file.write(random_data)
            file.flush()

        os.remove(input_file)
        #print(f"File '{input_file}' securely deleted with {passes} passes.")
        return True

    except Exception as e:
        print(f"Error during file deletion: {e}")
        return False

def overwrite_directory(directory):

    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            overwrite_delete(file_path)

def main():
     
     overwrite_directory('./result')
     '''
     delFile = "emResults.txt"
     passes = 3
     if overwrite_delete(delFile,passes):
          print(f"File '{delFile}' securely deleted with {passes} passes.")
     else:
          print(f"Error during file deletion: {delFile}")
    '''
     
    


if __name__ == '__main__':
	main()
