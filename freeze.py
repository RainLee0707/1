from flask_frozen import Freezer
from flask_html import app  # 將 "your_flask_app" 替換為您的 Flask 應用程式實例

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
