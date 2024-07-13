import os
import qrcode
import http.server
import socketserver
import threading

# Set the parent directory where subfolders are located
PARENT_DIRECTORY = os.getcwd()

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

def start_local_server(port, directory):
    os.chdir(directory)
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serving at port {port}...")
        httpd.serve_forever()

def main():
    # Start local web server in a separate thread
    server_port = 8000  # Choose an available port
    server_thread = threading.Thread(target=start_local_server, args=(server_port, PARENT_DIRECTORY))
    server_thread.start()
    
    # List all directories (subfolders) in the parent directory
    subdirectories = [os.path.join(PARENT_DIRECTORY, d) for d in os.listdir(PARENT_DIRECTORY) if os.path.isdir(os.path.join(PARENT_DIRECTORY, d))]
    
    if not subdirectories:
        print(f'No subdirectories found in {PARENT_DIRECTORY}.')
        return
    
    for subdir in subdirectories:
        # Check if subdir has folders A and B
        folder_A = os.path.join(subdir, 'A')
        folder_B = os.path.join(subdir, 'B')
        
        if os.path.exists(folder_A) and os.path.exists(folder_B):
            # Generate QR code for folder A
            qr_data_A = f"Download images from A folder: http://localhost:8000/{os.path.basename(subdir)}/A/"
            qr_filename_A = os.path.join(folder_A, "A_qr_code.png")
            generate_qr_code(qr_data_A, qr_filename_A)
            print(f'Generated QR code for A folder in {subdir}')
            
            # Generate QR code for folder B
            qr_data_B = f"Download images from B folder: http://localhost:8000/{os.path.basename(subdir)}/B/"
            qr_filename_B = os.path.join(folder_B, "B_qr_code.png")
            generate_qr_code(qr_data_B, qr_filename_B)
            print(f'Generated QR code for B folder in {subdir}')

    # Wait for the server thread to finish
    server_thread.join()

if __name__ == '__main__':
    main()
