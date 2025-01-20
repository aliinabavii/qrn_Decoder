import os  

def xor_with_hex55(input_bytes):  
    """XOR the input bytes with 0x55."""  
    return bytes(byte ^ 0x55 for byte in input_bytes)  

def process_files():  
    """Process all files in the current directory and save outputs in an 'output' folder."""  
    # Get the current directory where the script is located  
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    
    # Create the output directory if it doesn't exist  
    output_directory = os.path.join(current_directory, 'output')  
    os.makedirs(output_directory, exist_ok=True)  

    # List all files in the current directory  
    files = os.listdir(current_directory)  

    # Check if there are files to process  
    if not files:  
        print("No files found in the current directory.")  
        return  

    for file_name in files:  
        file_path = os.path.join(current_directory, file_name)  

        # Ensure we only process files and exclude the script itself   
        if os.path.isfile(file_path) and file_name != os.path.basename(__file__):  
            try:  
                # Open the input file and the output file  
                with open(file_path, 'rb') as input_file:  
                    output_file_name = f"{file_name}.decoded"  
                    output_file_path = os.path.join(output_directory, output_file_name)  

                    with open(output_file_path, 'wb') as output_file:  
                        # Read and process the file in chunks  
                        while True:  
                            input_bytes = input_file.read(4096)  # Read in chunks of 4096 bytes  
                            if not input_bytes:  # End of file  
                                break  
                            # XOR the bytes with 0x55 and write to the output file  
                            output_bytes = xor_with_hex55(input_bytes)  
                            output_file.write(output_bytes)  

                    print(f"Processed {file_name} -> {output_file_name} saved in 'output' folder.")  

            except MemoryError:  
                print(f"MemoryError: The file {file_name} is too large to process in memory.")  
            except IOError as e:  
                print(f"Error processing {file_name}: {e}")  

if __name__ == "__main__":  
    process_files()
