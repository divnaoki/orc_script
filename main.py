from PIL import Image
import pytesseract
import os

# 実行ディレクトリ取得
dirname = os.path.dirname(__file__)
image_dirname = dirname + "/image/"
# 画像ファイルが存在しない場合、エラー出力実施

# 画像ファイル取得、テキスト化し出力
if not any(filename.endswith(('.png', '.jpg')) for filename in os.listdir(image_dirname)):
  print("対象ファイルが存在しません。処理を終了します。")
else:
  for filename in os.listdir(image_dirname):
    img_path = os.path.join(image_dirname, filename)
    img = Image.open(img_path)
    # Use tesseract to do OCR on the image
    text = pytesseract.image_to_string(img, lang='jpn')
    # Print the text from each image
    print(f'対象ファイル：{filename}:\n{text}\n')
    print("================================================")