import os
import shutil
from pdf2image import convert_from_path
from PIL import Image

# Folder tempat file PDF berada
input_folder = r'D:\BOT\convert\pdf'
output_folder = r'D:\BOT\convert\hasil convert pdf to image\dr. Selvia Gusrina.'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop untuk memproses setiap file di folder input
for file_name in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file_name)

    # Jika file adalah PDF, lakukan konversi
    if file_name.endswith('.pdf'):
        pdf_path = input_path
        # Konversi PDF menjadi gambar
        pages = convert_from_path(pdf_path, 300)  # Resolusi 300 DPI
        
        # Menyimpan setiap halaman PDF sebagai gambar
        for i, page in enumerate(pages):
            output_image_path = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}_page_{i+1}.png')
            page.save(output_image_path, 'PNG')

        print(f"{file_name} berhasil dikonversi menjadi gambar.")
    
    # Jika file adalah gambar (png atau jpg), pindahkan ke folder output
    elif file_name.endswith(('.png', '.jpg', '.jpeg')):
        # Tentukan lokasi tujuan file di folder output
        output_image_path = os.path.join(output_folder, file_name)
        # Pindahkan file gambar ke folder output
        shutil.move(input_path, output_image_path)
        print(f"{file_name} berhasil dipindahkan ke folder output.")
