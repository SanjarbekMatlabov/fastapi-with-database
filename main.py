from fastapi import FastAPI
from schemas.validata import *
from models.model import *

app = FastAPI(title="Online_Tickets")

@app.post("/plane")
def create_plane(data: Plane):
    db = session()
    new_plane = Plane(plane_model = data.plane_model,spaces_bus = data.spaces_bus,spaces_eco = data.spaces_eco)
    db.add(new_plane)
    db.commit()
    db.refresh(new_plane)
    db.close()
    return new_plane