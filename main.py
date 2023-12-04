from PIL import Image
import pytesseract
import os

# 実行ディレクトリ取得
dirname = os.path.dirname(__file__)
image_dirname = dirname + "/image/"
# 画像ファイルが存在しない場合、エラー出力実施

# 画像ファイル取得、テキスト化し出力
for filename in os.listdir(image_dirname):
    if filename.endswith(('.png', '.jpg')):
        img_path = os.path.join(image_dirname, filename)
        try:
            img = Image.open(img_path)
            # Use tesseract to do OCR on the image
            text = pytesseract.image_to_string(img, lang='jpn')
            # Print the text from each image
            print(f'対象ファイル：{filename}:\n{text}\n')
            print("================================================")
        except IOError:
            print(f'ファイル{filename}を開けませんでした。')
    else:
        print(f'非画像ファイル{filename}は無視されました。')