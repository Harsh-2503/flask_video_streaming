from app.main import app

if __name__ == '__main__':
    try:
        app.run(debug=True, port=4999)
    except Exception as err:
        print(err)