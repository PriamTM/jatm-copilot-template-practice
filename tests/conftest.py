"""Shared test fixtures and configuration."""
import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the activities database before each test."""
    from src.app import activities
    
    # Store original state
    original_state = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Soccer Practice": {
            "description": "Team training sessions for soccer players of all skill levels",
            "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 25,
            "participants": ["liam@mergington.edu", "ava@mergington.edu"]
        },
        "Swimming Club": {
            "description": "Lap swimming, stroke improvement, and water safety drills",
            "schedule": "Tuesdays and Thursdays, 5:00 PM - 6:30 PM",
            "max_participants": 20,
            "participants": ["noah@mergington.edu", "mia@mergington.edu"]
        },
        "Art Studio": {
            "description": "Explore painting, drawing, and mixed media art projects",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": ["isabella@mergington.edu", "lucas@mergington.edu"]
        },
        "Drama Club": {
            "description": "Practice acting, stagecraft, and put on school performances",
            "schedule": "Fridays, 4:00 PM - 6:00 PM",
            "max_participants": 18,
            "participants": ["amelia@mergington.edu", "elijah@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop public speaking, research, and argumentation skills",
            "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
            "max_participants": 16,
            "participants": ["charlotte@mergington.edu", "benjamin@mergington.edu"]
        },
        "Math Olympiad": {
            "description": "Solve challenging math problems and prepare for competitions",
            "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 14,
            "participants": ["harper@mergington.edu", "jackson@mergington.edu"]
        }
    }
    
    # Clear activities and restore original state
    activities.clear()
    activities.update(original_state)
    
    yield
