import torch
import numpy as np

class TileImage:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
                "num_tiles": ("INT", {"default": 2, "min": 1, "max": 12}),
                "spacing_factor": ("FLOAT", {"default": 0.3, "min": 0.0, "max": 2.0, "step": 0.001}),
                "align": (["right", "left"], {"default": "right"}),
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    RETURN_NAMES = ("image", "mask")
    FUNCTION = "tile"
    CATEGORY = "ygo_tools"

    def tile(self, image, mask, num_tiles, spacing_factor, align):
        # 获取图像尺寸
        b, h, w, c = image.shape
        
        # 根据分辨率和因子计算间距
        spacing = int(w * spacing_factor)
        
        # 固定画布大小为12个图像平铺
        fixed_tiles = 12
        new_width = w * fixed_tiles + spacing * (fixed_tiles - 1)
        new_image = torch.zeros((b, h, new_width, c), dtype=image.dtype)
        
        # 创建新的mask画布，填充为1（完全不透明）
        new_mask = torch.ones((b, h, new_width), dtype=mask.dtype)
        
        # 限制实际平铺次数不超过12
        num_tiles = min(num_tiles, fixed_tiles)
        
        # 复制图像和mask并添加间距
        for i in range(num_tiles):
            if align == "right":
                # 从右往左排列
                tile_index = fixed_tiles - i - 1
            else:
                # 从左往右排列
                tile_index = i
                
            start_x = tile_index * (w + spacing)
            # 直接复制原始图像，保持透明通道不变
            new_image[:, :, start_x:start_x + w, :] = image
            # 复制mask，间隔部分保持透明（0值）
            new_mask[:, :, start_x:start_x + w] = mask
        
        return (new_image, new_mask) 