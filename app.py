import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import RedirectResponse


app = FastAPI(
    title = "Sample FastAPI",
    description = "This are some sample FastAPI endpoints"
)

# Requirements:
# fastapi==0.85.1
# uvicorn==0.19.0
# python-multipart==0.0.5

# Check docs: Localhost:8000/docs


@app.get('/hello')
async def hello():
    '''
    Say hello!
    '''
    return f'Hello!'

@app.get('/call')
async def call_name(name: str):
    '''
    Call the given name
    '''

    return f'Hello {name}!'

@app.post('/predict')
async def predict(
    input: int
):
    '''
    Sample endpoint to perform prediction

    1. The user input is all the input variables to your model

    2. Place codes to pass your input into the model to get prediction
    
    3.  Return a response in the format that your user would like to have. Eg: string, dict(JSON), etc

    For example: This is a model that multiplies the input by 2
    '''
    
    
    # Run model
    output = input * 2

    return {"prediction": output}
    

# A FastAPI to upload file
# Send POST request to localhost:8000/file 
@app.post('/file')
async def create_file(file: UploadFile = File(...)):
    '''
    Upload a file and return filename
    '''
    # To read a the file as a buffer async (async is preferred, but you can read as sync too)
    # file_buffer = await file.read()
    return f'You have uploaded a file named {file.filename}'


@app.get("/", include_in_schema=False)
def redirect_response():
    # Redirect response to "/docs" if user hit the "/" endpoint. Set include_in_schema=False to exclude this endpoint from displaying in Swagger UI
    return RedirectResponse("/docs")


if __name__ == '__main__':
    # Start server at port 8000
    # Auto restart server whenever there is code change with reload=True
    uvicorn.run(app="app:app", host='0.0.0.0', reload=True, port=8000) 

    # Use the following code to start server using HTTPS at port 5006
    # Generate key.pem and cert.pem using this (and answer some qns): openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256

    # uvicorn.run(app="app:app", host='0.0.0.0', port=5006,ssl_keyfile="./key.pem", 
    #             ssl_certfile="./cert.pem")