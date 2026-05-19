"""Tests for activities endpoints."""
import pytest


class TestGetActivities:
    """Tests for GET /activities endpoint."""
    
    def test_get_activities_returns_all_activities(self, client):
        """Test that get_activities returns all activities."""
        response = client.get("/activities")
        assert response.status_code == 200
        data = response.json()
        
        # Check that all activities are present
        assert "Chess Club" in data
        assert "Programming Class" in data
        assert "Gym Class" in data
        assert "Soccer Practice" in data
        assert "Swimming Club" in data
        assert "Art Studio" in data
        assert "Drama Club" in data
        assert "Debate Team" in data
        assert "Math Olympiad" in data
    
    def test_get_activities_returns_correct_structure(self, client):
        """Test that activities have correct structure."""
        response = client.get("/activities")
        data = response.json()
        
        for activity_name, activity in data.items():
            assert "description" in activity
            assert "schedule" in activity
            assert "max_participants" in activity
            assert "participants" in activity
            assert isinstance(activity["participants"], list)
    
    def test_get_activities_has_initial_participants(self, client):
        """Test that activities have initial participants."""
        response = client.get("/activities")
        data = response.json()
        
        assert "michael@mergington.edu" in data["Chess Club"]["participants"]
        assert "daniel@mergington.edu" in data["Chess Club"]["participants"]
        assert "emma@mergington.edu" in data["Programming Class"]["participants"]
