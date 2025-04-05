from PIL import Image


def resize_with_padding(input_path, output_path, size=(200, 200)):
  img = Image.open(input_path)
  img.thumbnail((size[0], size[1]))  # 按比例缩放到不超过 200×200
  new_img = Image.new("RGB", size, (255, 255, 255))  # 创建白色背景
  # 计算居中位置
  x = (size[0] - img.width) // 2
  y = (size[1] - img.height) // 2
  new_img.paste(img, (x, y))  # 将缩放的图片粘贴到中心
  new_img.save(output_path)


# 示例调用
resize_with_padding("favicon.png", "favicon_output.png")
