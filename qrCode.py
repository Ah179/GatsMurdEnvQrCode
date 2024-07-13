import os
import qrcode

# GitHub repository information
username = 'Ah179'
repository = 'GatsMurdEnvQrCode'
branch = 'main'  # Replace with your branch name if different
base_url = f'https://raw.githubusercontent.com/{username}/{repository}/{branch}/'

# Function to generate QR code
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
    # List character folders in the current directory
    character_folders = [folder for folder in os.listdir() if os.path.isdir(folder)]

    # Generate QR codes for each character's A and B folders
    for character in character_folders:
        # Path to character folder locally
        character_path = os.path.join(os.getcwd(), character)

        # List A and B folders inside the character folder
        for subfolder in ['A', 'B']:
            subfolder_path = os.path.join(character_path, subfolder)

            # Check if A or B folder exists inside the character folder locally
            if not os.path.exists(subfolder_path):
                print(f'Folder {subfolder} does not exist in {character}.')
                continue
            
            # List all images in the A or B folder
            images = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
            
            if not images:
                print(f'No images found in {subfolder} of {character}.')
                continue
            
            # Generate QR codes for each image
            for image in images:
                image_url = f'{base_url}{character}/{subfolder}/{image}'
                qr_data = image_url
                qr_filename = os.path.join(subfolder_path, f"{os.path.splitext(image)[0]}_qr_code.png")
                generate_qr_code(qr_data, qr_filename)
                print(f'Generated QR code for {image}')

if __name__ == '__main__':
    main()
