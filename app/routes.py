from app import app
@app.route('/index')
def index():
    A=34
    B=56
    Sum=A+B
    print(Sum)
    Product=A*B
    print(Product)
    return str(Sum)
    

