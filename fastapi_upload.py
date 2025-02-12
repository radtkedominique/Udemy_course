from fastapi import FastAPI, Request, UploadFile, HTTPException, status
from fastapi.responses import HTMLResponse
import aiofiles

app = FastAPI()

@app.post("/upload") #post request an /upload
async def upload(file: UploadFile):
    content_file = await file.read()
    async with aiofiles.open(file.filename, 'wb') as f:
        await f.write(content_file)

    return {'message': f'Successfuly uploaded {file.filename}'}


# Access the form at 'http://127.0.0.1:8000/' from your browser
@app.get('/')
async def main():
    content = '''
    <body>
    <form action='/upload' enctype='multipart/form-data' method='post'>
    <input name='file' type='file'>
    <input type='submit'>
    </form>
    </body>
    '''
    return HTMLResponse(content=content)
