"""
Задание #2
Улучшить качество любого плохого изображения (шумы, размытие...) с помощью фильтров
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
class ImageEnhancerNoScipy:
    def __init__(self, image_path):
        self.original = cv2.imread(image_path)
        if self.original is None:
            raise ValueError(f"Не удалось загрузить изображение: {image_path}")
        
        self.processed = self.original.copy()
        
    def remove_noise(self):
        # Используем NLM из OpenCV
        denoised = cv2.fastNlMeansDenoisingColored(
            self.processed, None, 
            h=10, hColor=10, 
            templateWindowSize=7, 
            searchWindowSize=21
        )
        self.processed = denoised
        return self
    
    def enhance_sharpness(self):
        kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])
        sharpened = cv2.filter2D(self.processed, -1, kernel)
        self.processed = sharpened
        return self
    
    def enhance_contrast(self):
        """Улучшение контраста"""
        lab = cv2.cvtColor(self.processed, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        l_enhanced = clahe.apply(l)
        
        lab_enhanced = cv2.merge((l_enhanced, a, b))
        self.processed = cv2.cvtColor(lab_enhanced, cv2.COLOR_LAB2BGR)
        return self
    
    def show_comparison(self):
        """Показать сравнение"""
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        
        original_rgb = cv2.cvtColor(self.original, cv2.COLOR_BGR2RGB)
        processed_rgb = cv2.cvtColor(self.processed, cv2.COLOR_BGR2RGB)
        
        axes[0].imshow(original_rgb)
        axes[0].set_title('Оригинал')
        axes[0].axis('off')
        
        axes[1].imshow(processed_rgb)
        axes[1].set_title('Улучшенное')
        axes[1].axis('off')
        
        plt.tight_layout()
        plt.show()
        return self
    
    def save_result(self, output_path="enhanced.jpg"):
        """Сохранение результата"""
        cv2.imwrite(output_path, self.processed)
        print(f"Сохранено как: {output_path}")
        return self

# Простой пример использования
if __name__ == "__main__":
    enhancer = ImageEnhancerNoScipy("Tosha.png")
    enhancer.remove_noise()
    enhancer.enhance_contrast()
    enhancer.enhance_sharpness()
    enhancer.show_comparison()
    enhancer.save_result()
