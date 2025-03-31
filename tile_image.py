import torch
import numpy as np

class TileImage:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
                "num_tiles": ("INT", {"default": 2, "min": 1}),
                "spacing": ("INT", {"default": 0, "min": 0}),
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    RETURN_NAMES = ("image", "mask")
    FUNCTION = "tile"
    CATEGORY = "image/processing"

    def tile(self, image, mask, num_tiles, spacing):
        # 获取图像尺寸
        b, h, w, c = image.shape
        
        # 创建新的画布，使用完全透明的背景
        new_width = w * num_tiles + spacing * (num_tiles - 1)
        new_image = torch.zeros((b, h, new_width, c), dtype=image.dtype)
        
        # 创建新的mask画布，填充为1（完全不透明）
        new_mask = torch.ones((b, h, new_width), dtype=mask.dtype)
        
        # 复制图像和mask并添加间距
        for i in range(num_tiles):
            start_x = i * (w + spacing)
            # 直接复制原始图像，保持透明通道不变
            new_image[:, :, start_x:start_x + w, :] = image
            # 复制mask，间隔部分保持透明（0值）
            new_mask[:, :, start_x:start_x + w] = mask
        
        return (new_image, new_mask) 