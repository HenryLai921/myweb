from flask import Flask, render_template

# 建立 Flask 應用程式物件
app = Flask(__name__)

# 定義網站的路由 (Route)
# @app.route('/') 代表網站的根目錄 (首頁)
@app.route('/1')
def index1():
    """
    這是處理首頁請求的函式
    它會渲染 (render) templates 資料夾中的 index.html 檔案並回傳給使用者
    """
    return render_template('index.html')

# 定義網站的路由 (Route)
# @app.route('/') 代表網站的根目錄 (首頁)
@app.route('/2')
def index2():
    """
    這是處理首頁請求的函式
    它會渲染 (render) templates 資料夾中的 index.html 檔案並回傳給使用者
    """
    return render_template('index_2.html')

# 讓這個腳本可以直接被執行
if __name__ == '__main__':
    # 啟動應用程式，debug=True 會讓你在修改程式碼後自動重啟伺服器
    app.run(debug=True)