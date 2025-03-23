import albumentations as A
import cv2
import os

def processar_imagens(input_dir, output_dir, target_size=(640, 640), augmentations_per_image=3):
    """
    Redimensiona e aplica transformações em imagens, salvando as originais e modificadas.
    
    Args:
        input_dir (str): Diretório contendo as imagens originais.
        output_dir (str): Diretório para salvar as imagens processadas.
        target_size (tuple): Tamanho final das imagens (width, height).
        augmentations_per_image (int): Quantas imagens aumentadas gerar para cada original.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Configuração de transformações do Albumentations
    transform = A.Compose([
        A.HorizontalFlip(p=0.6),
        A.RandomBrightnessContrast(brightness_limit=0.3, contrast_limit=0.3, p=0.5),  
        A.GaussianBlur(blur_limit=(3, 7), p=0.5),  
        A.CoarseDropout(max_holes=25, max_height=45, max_width=45, p=0.7), 
        A.Rotate(limit=180, p=0.6),  
        A.RandomCrop(width=500, height=500, p=0.4),
    ])
    
    for img_file in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_file)
        
        if not img_file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff', '.webp')):
            continue

        image = cv2.imread(img_path)
        if image is None:
            print(f"Não foi possível carregar a imagem: {img_file}")
            continue
    
        resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_LINEAR)
        
        filename, ext = os.path.splitext(img_file)
        original_save_path = os.path.join(output_dir, f"{filename}_original{ext}")
        cv2.imwrite(original_save_path, resized_image)
        print(f"Imagem original redimensionada salva: {original_save_path}")
        
        for i in range(augmentations_per_image):
            augmented = transform(image=resized_image)
            augmented_image = augmented["image"]
            
            augmented_save_path = os.path.join(output_dir, f"{filename}_aug_{i+1}{ext}")
            cv2.imwrite(augmented_save_path, augmented_image)
            print(f"Imagem aumentada salva: {augmented_save_path}")


input_dir = "CaminhoDasImagens"
output_dir = "CaminhoDeDestinoDasImagens"  
target_size = (640, 640) #Tamanho em que as imagens serão redimencionadas(640x640 e o ideal para o YOLO) 
augmentations_per_image = 7 #Quantidade de imagens com augmentation (7 + Original)

processar_imagens(input_dir, output_dir, target_size, augmentations_per_image)