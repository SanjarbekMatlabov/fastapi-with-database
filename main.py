from fastapi import FastAPI
from schemas.validata import *
from models.model import *

app = FastAPI(title="Online_Tickets")

@app.post("/plane")
def create_plane(data: PlaneModel):
    db = SessionLocal()
    new_plane = Plane(plane_model = data.model,spaces_bus = data.space_bus,spaces_eco = data.space_eco)
    db.add(new_plane)
    db.commit()
    db.refresh(new_plane)
    db.close()
    return new_plane