# YGO Tools for ComfyUI

一组针对游戏王卡图制作的ComfyUI自定义节点集合。

## 功能节点

### Tile Image

- 将输入图像水平平铺指定次数（最多12个）
- 可控制图像之间的间距（基于图像宽度的比例）
- 支持左对齐或右对齐排列
- 输出带有完整mask的图像

### Draw Line

- 绘制自定义线条
- 支持设置线条长度和宽度
- 使用HEX格式设置颜色（如#FFFFFF）
- 支持设置透明度（如#FFFFFFFF）
- 支持任意角度（0-360度）的线条绘制

## 安装

```bash
cd custom_nodes
git clone https://github.com/Ky11le/ygo_tools
```

## 使用方法

节点会在ComfyUI的"ygo_tools"类别下出现。

### Tile Image 参数

- `image`: 输入图像
- `mask`: 输入mask
- `num_tiles`: 要平铺的图像数量（1-12）
- `spacing_factor`: 图像间距系数（相对于图像宽度）
- `align`: 对齐方式（left/right）

### Draw Line 参数

- `length`: 线条长度
- `width`: 线条宽度
- `color`: HEX颜色值（如#FFFFFF）
- `angle`: 线条角度（0-360度）
- `padding`: 边距大小 