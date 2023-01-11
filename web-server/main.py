import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app =  FastAPI()

@app.get('/')
def get_list():
    return[1,2,3,4]

@app.get('/contact', response_class=HTMLResponse)
def get_company():
    return """
        <h1>Hello, I'm a website</h1>
        <p>Company name: JP Morgan</p>
    """

def run():
    store.get_categories()


if __name__ == '__main__':
    run()