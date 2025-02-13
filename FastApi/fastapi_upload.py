from fastapi import FastAPI, Request, UploadFile, HTTPException, status
from fastapi.responses import HTMLResponse
import aiofiles

print("Docker is magic!")
app = FastAPI()

@app.post("/upload") #post request to api endpoint: /upload
async def upload(file: UploadFile): #takes in uploaded file as param
    try:
        content_file = await file.read() #reads file and saves content to content_file
        async with aiofiles.open(file.filename, 'wb') as f: #creates/opens file under same file name
            await f.write(content_file) #and writes content of the uploaded file to the new file
            #for saving file on server?
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='There was an error uploading the file')
    finally:
        await file.close() #why close when with.open() closes itself?

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
    return HTMLResponse(content=content) #when sending a get response to '/'  return HTML Protocol from above?
#triggers post request to '/upload' and prompts upload function from above?
