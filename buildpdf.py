from PIL import Image
import os

images = [f for f in os.listdir('.')]
images.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

images = [Image.open(f) for f in images]

pdf_path = str(os.getcwd()) + '/' + 'new1.pdf'
    
images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
