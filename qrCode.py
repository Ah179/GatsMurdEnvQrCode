import os
import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def main():
    # Define the parent directory where subdirectories like Arnie, Tom, etc., are located
    parent_directory = os.getcwd()
    
    # Check if the parent directory exists
    if not os.path.exists(parent_directory):
        print(f'Error: Parent directory {parent_directory} not found.')
        return
    
    # List all directories (folders) in the parent directory
    subdirectories = [os.path.join(parent_directory, d) for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]
    
    if not subdirectories:
        print(f'No subdirectories found in {parent_directory}.')
        return
    
    for subdir in subdirectories:
        # Check if subdir has folders A and B
        if os.path.exists(os.path.join(subdir, 'A')) and os.path.exists(os.path.join(subdir, 'B')):
            # Generate QR code for folder A
            qr_data_A = f"Access to A folder: file://{os.path.join(subdir, 'A')}/"
            qr_filename_A = os.path.join(subdir, 'A', "A_qr_code.png")
            generate_qr_code(qr_data_A, qr_filename_A)
            print(f'Generated QR code for A folder in {subdir}')
            
            # Generate QR code for folder B
            qr_data_B = f"Access to B folder: file://{os.path.join(subdir, 'B')}/"
            qr_filename_B = os.path.join(subdir, 'B', "B_qr_code.png")
            generate_qr_code(qr_data_B, qr_filename_B)
            print(f'Generated QR code for B folder in {subdir}')

if __name__ == '__main__':
    main()
