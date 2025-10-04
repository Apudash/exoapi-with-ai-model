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
    },
    {
        "id": "trappist-1e",
        "name": "TRAPPIST-1e",
        "discovery_method": "Transit",
        "discovery_year": 2017,
        "radius": 0.92,
        "radius_confidence": 0.88,
        "mass": 0.69,
        "mass_confidence": 0.82,
        "distance": 39.5,
        "distance_confidence": 0.95,
        "orbital_period": 6.1,
        "temperature": 251,
        "host_star": "TRAPPIST-1",
        "description": "One of seven Earth-sized planets in the TRAPPIST-1 system.",
        "graph_data": [
            {"time": 0, "brightness": 1.000},
            {"time": 1, "brightness": 0.999},
            {"time": 2, "brightness": 0.997},
            {"time": 3, "brightness": 0.995},
            {"time": 4, "brightness": 0.997},
            {"time": 5, "brightness": 0.999},
            {"time": 6, "brightness": 1.000}
        ],
        "ai_model_version": "1.0.0",
        "detection_confidence": 0.85,
        "last_updated": "2024-01-15T10:30:00Z"
    },
    {
        "id": "k2-18b",
        "name": "K2-18b",
        "mission":"Tess",
        "discovery_method": "Transit",
        "discovery_year": 2015,
        "radius": 2.23,
        "radius_confidence": 0.90,
        "mass": 8.63,
        "mass_confidence": 0.78,
        "distance": 124,
        "distance_confidence": 0.92,
        "orbital_period": 33.0,
        "temperature": 265,
        "host_star": "K2-18",
        "description": "A sub-Neptune with water vapor detected in its atmosphere.",
        "graph_data": [
            {"time": 0, "brightness": 1.000},
            {"time": 2, "brightness": 0.999},
            {"time": 4, "brightness": 0.997},
            {"time": 6, "brightness": 0.994},
            {"time": 8, "brightness": 0.991},
            {"time": 10, "brightness": 0.994},
            {"time": 12, "brightness": 0.997},
            {"time": 14, "brightness": 0.999},
            {"time": 16, "brightness": 1.000}
        ],
        "ai_model_version": "1.0.0",
        "detection_confidence": 0.88,
        "last_updated": "2024-01-15T10:30:00Z"
    },
    {
        "id": "hd-209458b",
        "mission":"kepler",
        "name": "HD 209458b",
        "discovery_method": "Transit",
        "discovery_year": 1999,
        "radius": 1.38,
        "radius_confidence": 0.95,
        "mass": 0.69,
        "mass_confidence": 0.90,
        "distance": 159,
        "distance_confidence": 0.98,
        "orbital_period": 3.5,
        "temperature": 1130,
        "host_star": "HD 209458",
        "description": "First exoplanet discovered transiting its star, nicknamed 'Osiris'.",
        "graph_data": [
            {"time": 0, "brightness": 1.000},
            {"time": 0.5, "brightness": 0.998},
            {"time": 1.0, "brightness": 0.995},
            {"time": 1.5, "brightness": 0.992},
            {"time": 2.0, "brightness": 0.995},
            {"time": 2.5, "brightness": 0.998},
            {"time": 3.0, "brightness": 1.000}
        ],
        "ai_model_version": "1.0.0",
        "detection_confidence": 0.92,
        "last_updated": "2024-01-15T10:30:00Z"
    },
    {
        "id": "gliese-667cc",
        "mission":"kepler",
        "name": "Gliese 667Cc",
        "discovery_method": "Radial Velocity",
        "discovery_year": 2011,
        "radius": 1.54,
        "radius_confidence": 0.82,
        "mass": 3.8,
        "mass_confidence": 0.75,
        "distance": 23.6,
        "distance_confidence": 0.90,
        "orbital_period": 28.1,
        "temperature": 277,
        "host_star": "Gliese 667C",
        "description": "A super-Earth in the habitable zone of a red dwarf star.",
        "graph_data": [
            {"time": 0, "velocity": 2.1},
            {"time": 3, "velocity": 4.2},
            {"time": 6, "velocity": 1.8},
            {"time": 9, "velocity": -2.5},
            {"time": 12, "velocity": -4.1},
            {"time": 15, "velocity": -1.9},
            {"time": 18, "velocity": 2.1}
        ],
        "ai_model_version": "1.0.0",
        "detection_confidence": 0.80,
        "last_updated": "2024-01-15T10:30:00Z"
    },
    {
        "id": "toi-715b",
        "mission":"kepler",
        "name": "TOI-715b",
        "discovery_method": "Transit",
        "discovery_year": 2024,
        "radius": 1.55,
        "radius_confidence": 0.88,
        "mass": 3.02,
        "mass_confidence": 0.85,
        "distance": 137,
        "distance_confidence": 0.93,
        "orbital_period": 19.3,
        "temperature": 280,
        "host_star": "TOI-715",
        "description": "A recently discovered super-Earth in the habitable zone.",
        "graph_data": [
            {"time": 0, "brightness": 1.000},
            {"time": 3, "brightness": 0.999},
            {"time": 6, "brightness": 0.997},
            {"time": 9, "brightness": 0.994},
            {"time": 12, "brightness": 0.991},
            {"time": 15, "brightness": 0.994},
            {"time": 18, "brightness": 0.997},
            {"time": 21, "brightness": 0.999},
            {"time": 24, "brightness": 1.000}
        ],
        "ai_model_version": "1.0.0",
        "detection_confidence": 0.87,
        "last_updated": "2024-01-15T10:30:00Z"
    },
    {
    "id": "Test-1",
    "mission":"kepler",
    "name": "AI Detected Planet",  # ✅ Available
    "discovery_method": "Transit",  # ✅ Available
    "discovery_year": 2024,
    "radius": 1.55,
    # Everything else is missing - frontend handles it automatically
    "ai_model_version": "1.0.0",
    "detection_confidence": 0.70
},# When AI improves, just add more fields:
{
    "id": "planet-1", 
    "mission":"kepler",
    "name": "AI Detected Planet",
    "discovery_method": "Transit",
    "discovery_year": 2024,
    "radius": 1.5,  # ✅ Now AI can detect this
    "radius_confidence": 0.85,
    "distance": 200,  # ✅ Now AI can detect this
    "distance_confidence": 0.90,
    # Still missing: mass, orbital_period, temperature, host_star
    "ai_model_version": "1.1.0",  # Updated version
    "detection_confidence": 0.85  # Higher overall confidence
},
    {
        "id": "wasp-96b",
        "mission":"kepler",
        "name": "WASP-96b",
        "discovery_method": "Transit",
        "discovery_year": 2013,
        "radius": 1.2,
        "radius_confidence": 0.90,
        "mass": 0.48,
        "mass_confidence": 0.88,
        "distance": 1150,
        "distance_confidence": 0.95,
        "orbital_period": 3.4,
        "temperature": 1300,
        "host_star": "WASP-96",
        "description": "A hot gas giant with a clear atmosphere, studied by JWST.",
        "graph_data": [
            {"time": 0, "brightness": 1.000},
            {"time": 0.8, "brightness": 0.999},
            {"time": 1.6, "brightness": 0.996},
            {"time": 2.4, "brightness": 0.992},
            {"time": 3.2, "brightness": 0.996},
            {"time": 4.0, "brightness": 0.999},
            {"time": 4.8, "brightness": 1.000}
        ],
        "ai_model_version": "1.0.0",
        "detection_confidence": 0.89,
        "last_updated": "2024-01-15T10:30:00Z"
    } ,
    {
    "id": "wasp-96b",
    "name": "WASP-96b",
    "mission":"kepler",
    "discovery_method": "Transit",
    "discovery_year": 2013,
    "radius": 1.2,
    "radius_confidence": 77,
    "mass": 0.48,
    "mass_confidence": 0.88,
    "distance": 1150,
    "distance_confidence": 0.95,
    "temperature": 1300,
    "graph_data": [
      {
        "time": 0,
        "brightness": 1.0
      },
      {
        "time": 0.8,
        "brightness": 0.999
      },
      {
        "time": 1.6,
        "brightness": 0.996
      },
      {
        "time": 2.4,
        "brightness": 0.992
      },
      {
        "time": 3.2,
        "brightness": 0.996
      },
      {
        "time": 4.0,
        "brightness": 0.999
      },
      {
        "time": 4.8,
        "brightness": 1.0
      }
    ],
    "last_updated": "2024-01-15T10:30:00Z"
  },
  {
    "id": "wasp-97a",
    "mission":"kepler",
    "name": "WASP-96b",
    "discovery_year": 2013,
    "radius_confidence": 0.9,
    "mass": "",
    "mass_confidence": 0.88,
    "distance": "",
    "distance_confidence": 0.95,
    "orbital_period": 3.4,
    "host_star": "WASP-96",
    "ai_model_version": "1.0.0",
    "detection_confidence": 0.89
  },
  {
    "id": "wasp-96b",
    "mission":"kepler",
    "name": "WASP-96b",
    "discovery_method": "Transit",
    "discovery_year": 2013,
    "radius": 1.2,
    "mass_confidence": 0.88,
    "distance": 1150,
    "distance_confidence": "",
    "orbital_period": "",
    "host_star": "WASP-96",
    "description": "A hot gas giant with a clear atmosphere, studied by JWST.",
    "ai_model_version": "1.0.0",
    "last_updated": ""
  },
  {
    "id": "wasp-96b",
    "name": "WASP-96b",
    "mission":"kepler",
    "discovery_method": "Transit",
    "discovery_year": 2013,
    "radius_confidence": 0.9,
    "mass": 0.48,
    "distance": 1150,
    "distance_confidence": 0.95,
    "host_star": "",
    "description": "A hot gas giant with a clear atmosphere, studied by JWST.",
    "ai_model_version": "1.0.0",
    "detection_confidence": "",
    "last_updated": "2024-01-15T10:30:00Z"
  },
  {
    "id": "",
    "mission":"kepler",
    "name": "WASP-96b",
    "discovery_method": "Transit",
    "discovery_year": 2013,
    "radius_confidence": 0.9,
    "mass": 0.48,
    "distance": 1150,
    "distance_confidence": 0.95,
    "orbital_period": 3.4,
    "temperature": 1300,
    "host_star": "WASP-96",
    "ai_model_version": "1.0.0",
    "detection_confidence": 0.89,
    "last_updated": ""
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
