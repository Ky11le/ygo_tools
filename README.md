# Tile Image Node for ComfyUI

一个简单的ComfyUI自定义节点，用于将图像水平平铺多次。

## 功能

- 将输入图像水平平铺指定次数
- 可以控制图像之间的间距
- 保持原始图像的高度不变
- 输出带有完整mask的图像

## 安装

```bash
cd custom_nodes
git clone https://github.com/yourusername/ComfyUI-TileImage TileImage
```

## 使用方法

节点会在ComfyUI的"image/processing"类别下出现，名称为"Tile Image"。

### 参数

- `image`: 输入图像
- `mask`: 输入mask
- `num_tiles`: 要平铺的图像数量
- `spacing`: 图像之间的间距（像素） 