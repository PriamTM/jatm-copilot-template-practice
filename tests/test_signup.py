"""Tests for signup endpoint."""
import pytest


class TestSignup:
    """Tests for POST /activities/{activity_name}/signup endpoint."""
    
    def test_signup_new_student_success(self, client):
        """Test successful signup for a new student."""
        response = client.post(
            "/activities/Chess%20Club/signup",
            params={"email": "newstudent@mergington.edu"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "newstudent@mergington.edu" in data["message"]
        assert "Chess Club" in data["message"]
    
    def test_signup_new_student_added_to_activity(self, client):
        """Test that new student is added to activity participants."""
        email = "newstudent@mergington.edu"
        
        # Signup
        client.post(
            "/activities/Chess%20Club/signup",
            params={"email": email}
        )
        
        # Verify student was added
        activities_response = client.get("/activities")
        participants = activities_response.json()["Chess Club"]["participants"]
        assert email in participants
    
    def test_signup_duplicate_student_fails(self, client):
        """Test that duplicate signup returns 400 error."""
        response = client.post(
            "/activities/Chess%20Club/signup",
            params={"email": "michael@mergington.edu"}
        )
        assert response.status_code == 400
        data = response.json()
        assert "already signed up" in data["detail"]
    
    def test_signup_nonexistent_activity_fails(self, client):
        """Test that signup for non-existent activity returns 404."""
        response = client.post(
            "/activities/Nonexistent%20Club/signup",
            params={"email": "newstudent@mergington.edu"}
        )
        assert response.status_code == 404
        data = response.json()
        assert "Activity not found" in data["detail"]
    
    def test_signup_to_multiple_activities(self, client):
        """Test that student can sign up for multiple activities."""
        email = "versatile@mergington.edu"
        
        # Signup to Chess Club
        response1 = client.post(
            "/activities/Chess%20Club/signup",
            params={"email": email}
        )
        assert response1.status_code == 200
        
        # Signup to Programming Class
        response2 = client.post(
            "/activities/Programming%20Class/signup",
            params={"email": email}
        )
        assert response2.status_code == 200
        
        # Verify student is in both
        activities_response = client.get("/activities")
        data = activities_response.json()
        assert email in data["Chess Club"]["participants"]
        assert email in data["Programming Class"]["participants"]
    
    def test_signup_with_special_characters_in_email(self, client):
        """Test signup with email containing special characters."""
        email = "student+test@mergington.edu"
        response = client.post(
            "/activities/Art%20Studio/signup",
            params={"email": email}
        )
        assert response.status_code == 200
        
        # Verify student was added
        activities_response = client.get("/activities")
        participants = activities_response.json()["Art Studio"]["participants"]
        assert email in participants
