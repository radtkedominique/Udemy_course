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
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload File</title>
    <style>
        body {
            font-family: "Arial", sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #ffe6e6;
            margin: 0;
        }
        .upload-container {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            border: 2px solid #ff6b6b;
        }
        h2 {
            color: #ff6b6b;
        }
        input[type="file"] {
            margin: 10px 0;
            padding: 8px;
            border: 1px solid #ffb6b6;
            border-radius: 8px;
            background: #ffe6e6;
            color: #ff6b6b;
            cursor: pointer;
        }
        input[type="submit"] {
            background-color: #ff6b6b;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s ease-in-out;
            font-weight: bold;
        }
        input[type="submit"]:hover {
            background-color: #ff4d4d;
        }
    </style>
</head>
<body>
    <div class="upload-container">
        <h2>🎀 Upload Your File 🎀</h2>
        <form action="/upload" enctype="multipart/form-data" method="post">
            <input name="file" type="file" required>
            <br>
            <input type="submit" value="Upload 💕">
        </form>
    </div>
</body>
</html>

    '''
    return HTMLResponse(content=content) #when sending a get response to '/'  return HTML Protocol from above?
#triggers post request to '/upload' and prompts upload function from above?
