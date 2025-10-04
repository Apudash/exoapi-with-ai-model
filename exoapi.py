from fastapi import FastAPI,Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List, Dict, Any
from datetime import datetime

app = FastAPI()

# Allow React frontend to call FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React dev URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Updated exoplanets data with AI model features
exoplanets = [
    {
        "id": "kepler-452b",
        "mission":"kepler",
        "name": "Kepler-452b",
        "discovery_method": "Transit",
        "discovery_year": 2015,
        # AI-detected fields with confidence scores
        "radius": 1.63,
        "radius_confidence": 0.92,
        "mass": 5.0,
        "mass_confidence": 0.88,
        "distance": 1400,
        "distance_confidence": 0.95,
        "orbital_period": 384.8,
        "temperature": 265,
        "host_star": "Kepler-452",
        "description": "Earth's older, bigger cousin in the habitable zone of a Sun-like star.",
        "graph_data": [
            {"time": 0, "brightness": 1.000},
            {"time": 0.5, "brightness": 0.999},
            {"time": 1.0, "brightness": 0.998},
            {"time": 1.5, "brightness": 0.996},
            {"time": 2.0, "brightness": 0.994},
            {"time": 2.5, "brightness": 0.992},
            {"time": 3.0, "brightness": 0.994},
            {"time": 3.5, "brightness": 0.996},
            {"time": 4.0, "brightness": 0.998},
            {"time": 4.5, "brightness": 0.999},
            {"time": 5.0, "brightness": 1.000}
        ],
        # AI model metadata
        "ai_model_version": "1.0.0",
        "detection_confidence": 0.90,
        "last_updated": "2024-01-15T10:30:00Z"
    },
    {
        "id": "proxima-centauri-b",
        "mission":"kepler",
        "name": "Proxima Centauri b",
        "discovery_method": "Radial Velocity",
        "discovery_year": 2016,
        # Example of partial AI detection - some fields missing
        "radius": 1.17,
        "radius_confidence": 0.85,
        # mass: undefined, # AI couldn't detect mass
        "distance": 4.24,
        "distance_confidence": 0.98,
        "orbital_period": 11.2,
        "temperature": 234,
        "host_star": "Proxima Centauri",
        "description": "The closest known exoplanet to Earth, potentially habitable.",
        "graph_data": [
            {"time": 0, "velocity": 5.2},
            {"time": 1, "velocity": 3.1},
            {"time": 2, "velocity": -2.4},
            {"time": 3, "velocity": -5.8},
            {"time": 4, "velocity": -3.2},
            {"time": 5, "velocity": 1.9},
            {"time": 6, "velocity": 5.2}
        ],
        # AI model metadata
        "ai_model_version": "1.0.0",
        "detection_confidence": 0.75,
        "last_updated": "2024-01-15T10:30:00Z"
    }
]

@app.get("/exoplanets")
def list_exoplanets():
    return exoplanets

@app.get("/exoplanets/{planet_id}")
def get_exoplanet(planet_id: str):
    for p in exoplanets:
        if p["id"] == planet_id:
            return p
    return {"error": "Not found"}

# ---- NEW ENDPOINT ----
@app.get("/ai_model")
def get_model_performance(mission: str = Query(..., regex="^(kepler|tess)$")) -> Dict:
    # Mocked sample performance data (replace with real ML results later)
    if mission == "kepler":
        return {
            "mission": "kepler",
            "precision": 0.92,
            "recall": 0.88,
            "f1score": 0.90,
            "performance": 0.91,
            "roc": [
                {"fpr": 0.0, "tpr": 0.0},
                {"fpr": 0.1, "tpr": 0.75},
                {"fpr": 0.2, "tpr": 0.85},
                {"fpr": 0.3, "tpr": 0.92},
                {"fpr": 1.0, "tpr": 1.0},
            ],
            "pr": [
                {"recall": 0.0, "precision": 1.0},
                {"recall": 0.5, "precision": 0.85},
                {"recall": 0.7, "precision": 0.80},
                {"recall": 0.9, "precision": 0.70},
                {"recall": 1.0, "precision": 0.50},
            ],
        }
    else:  # mission == "tess"
        return {
            "mission": "tess",
            "precision": 0.87,
            "recall": 0.90,
            "f1score": 0.88,
            "performance": 0.89,
            "roc": [
                {"fpr": 0.0, "tpr": 0.0},
                {"fpr": 0.1, "tpr": 0.70},
                {"fpr": 0.2, "tpr": 0.82},
                {"fpr": 0.3, "tpr": 0.90},
                {"fpr": 1.0, "tpr": 1.0},
            ],
            "pr": [
                {"recall": 0.0, "precision": 1.0},
                {"recall": 0.4, "precision": 0.80},
                {"recall": 0.6, "precision": 0.75},
                {"recall": 0.8, "precision": 0.65},
                {"recall": 1.0, "precision": 0.55},
            ],
        }