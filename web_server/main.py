import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_numbers():
    return [1,2,3]

@app.get('/pagina', response_class = HTMLResponse)
def get_contact():
    return """
        <h1>Mi primer pagina con FastAPI</h1>
        <p>Mi primer API</p>
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()