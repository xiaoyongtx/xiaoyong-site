#!/usr/bin/env python3
from PIL import Image, ImageDraw
import os

def create_icon():
    size = 512
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 创建紫色渐变背景
    for i in range(size):
        y = i / size
        r = int(147 + (90 - 147) * y)
        g = int(51 + (34 - 51) * y)
        b = int(234 + (135 - 234) * y)
        draw.line([(0, i), (size, i)], fill=(r, g, b, 255))

    # 创建圆形蒙版
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse([20, 20, size-20, size-20], fill=255)
    img.putalpha(mask)

    center = size // 2

    # 外圈
    draw.ellipse([80, 80, size-80, size-80], outline='white', width=8)

    # 头部
    head_center = (center, center - 30)
    head_radius = 100
    draw.ellipse([head_center[0]-head_radius, head_center[1]-head_radius,
                  head_center[0]+head_radius, head_center[1]+head_radius],
                 fill='white')

    # 眼睛
    eye_offset = 30
    eye_radius = 15
    draw.ellipse([head_center[0]-eye_offset-eye_radius, head_center[1]-20-eye_radius,
                  head_center[0]-eye_offset+eye_radius, head_center[1]-20+eye_radius],
                 fill='#9333ea')
    draw.ellipse([head_center[0]+eye_offset-eye_radius, head_center[1]-20-eye_radius,
                  head_center[0]+eye_offset+eye_radius, head_center[1]-20+eye_radius],
                 fill='#9333ea')

    # 嘴巴
    draw.arc([head_center[0]-40, head_center[1]+20, head_center[0]+40, head_center[1]+50],
             start=0, end=180, fill='#9333ea', width=6)

    # 天线
    draw.line([center, head_center[1]-head_radius, center, head_center[1]-head_radius-50],
              fill='white', width=8)
    draw.ellipse([center-15, head_center[1]-head_radius-65, center+15, head_center[1]-head_radius-35],
                 fill='white')

    # 保存
    os.makedirs('icons', exist_ok=True)
    img.save('favicon-512.png', 'PNG')

    for s in [16, 32, 64, 128, 256]:
        resized = img.resize((s, s), Image.Resampling.LANCZOS)
        resized.save(f'icons/favicon-{s}x{s}.png', 'PNG')
        if s == 256:
            resized.save('apple-touch-icon.png', 'PNG')

    img_ico = img.resize((256, 256), Image.Resampling.LANCZOS)
    img_ico.save('favicon.ico', format='ICO', sizes=[(256,256),(128,128),(64,64),(32,32),(16,16)])

    print("图标生成成功！")
    for f in ['favicon.ico', 'favicon-512.png']:
        print(f"  {f}: {os.path.getsize(f)/1024:.1f} KB")

if __name__ == '__main__':
    create_icon()
