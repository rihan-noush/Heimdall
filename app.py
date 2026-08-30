from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

@app.get("/")
def do_nothing():
    # Returns an empty response with a 204 No Content status
    return Response(status_code=204)
