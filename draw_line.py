import torch
import numpy as np
import math

class DrawLine:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "length": ("INT", {"default": 512, "min": 1, "max": 4096}),
                "width": ("INT", {"default": 8, "min": 1, "max": 1024}),
                "color": ("STRING", {"default": "#FFFFFF", "multiline": False}),
                "angle": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 360.0, "step": 1.0}),
                "padding": ("INT", {"default": 0, "min": 0, "max": 1024}),
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    RETURN_NAMES = ("image", "mask")
    FUNCTION = "draw"
    CATEGORY = "ygo_tools"

    def hex_to_rgba(self, hex_color):
        """将HEX颜色值转换为RGBA。支持#RGB，#RGBA，#RRGGBB，#RRGGBBAA格式"""
        hex_color = hex_color.lstrip('#')
        
        if len(hex_color) == 3:  # RGB格式
            r = int(hex_color[0] + hex_color[0], 16) / 255.0
            g = int(hex_color[1] + hex_color[1], 16) / 255.0
            b = int(hex_color[2] + hex_color[2], 16) / 255.0
            a = 1.0
        elif len(hex_color) == 4:  # RGBA格式
            r = int(hex_color[0] + hex_color[0], 16) / 255.0
            g = int(hex_color[1] + hex_color[1], 16) / 255.0
            b = int(hex_color[2] + hex_color[2], 16) / 255.0
            a = int(hex_color[3] + hex_color[3], 16) / 255.0
        elif len(hex_color) == 6:  # RRGGBB格式
            r = int(hex_color[0:2], 16) / 255.0
            g = int(hex_color[2:4], 16) / 255.0
            b = int(hex_color[4:6], 16) / 255.0
            a = 1.0
        elif len(hex_color) == 8:  # RRGGBBAA格式
            r = int(hex_color[0:2], 16) / 255.0
            g = int(hex_color[2:4], 16) / 255.0
            b = int(hex_color[4:6], 16) / 255.0
            a = int(hex_color[6:8], 16) / 255.0
        else:
            # 无效格式，使用白色
            r, g, b, a = 1.0, 1.0, 1.0, 1.0
            
        return r, g, b, a
    
    def draw(self, length, width, color, angle, padding):
        # 解析颜色
        r, g, b, a = self.hex_to_rgba(color)
        
        # 通过角度计算线条的实际尺寸和方向
        angle_rad = math.radians(angle)
        
        # 计算旋转后线条的边界框大小
        diagonal = math.sqrt(length**2 + width**2)
        
        # 考虑旋转后的边界，确保线条完全可见
        canvas_size = int(diagonal) + 2 * padding
        
        # 创建一个正方形画布
        image = torch.zeros((1, canvas_size, canvas_size, 4), dtype=torch.float32)
        mask = torch.zeros((1, canvas_size, canvas_size), dtype=torch.float32)
        
        # 计算中心点
        center_x = canvas_size // 2
        center_y = canvas_size // 2
        
        # 计算旋转后的线条坐标
        for y in range(canvas_size):
            for x in range(canvas_size):
                # 相对于中心点的坐标
                rel_x = x - center_x
                rel_y = y - center_y
                
                # 将坐标旋转到线条方向
                rotated_x = rel_x * math.cos(-angle_rad) - rel_y * math.sin(-angle_rad)
                rotated_y = rel_x * math.sin(-angle_rad) + rel_y * math.cos(-angle_rad)
                
                # 检查点是否在线条区域内
                if abs(rotated_y) <= width/2 and -length/2 <= rotated_x <= length/2:
                    # 设置点的颜色
                    image[0, y, x, 0] = r
                    image[0, y, x, 1] = g
                    image[0, y, x, 2] = b
                    image[0, y, x, 3] = a
                    
                    # 更新掩码
                    mask[0, y, x] = a
        
        return (image, mask) 