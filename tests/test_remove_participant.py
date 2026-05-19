"""Tests for remove participant endpoint."""
import pytest


class TestRemoveParticipant:
    """Tests for DELETE /activities/{activity_name}/participant endpoint."""
    
    def test_remove_existing_participant_success(self, client):
        """Test successful removal of a participant."""
        response = client.delete(
            "/activities/Chess%20Club/participant",
            params={"email": "michael@mergington.edu"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "michael@mergington.edu" in data["message"]
        assert "Chess Club" in data["message"]
    
    def test_remove_participant_actually_removes(self, client):
        """Test that participant is actually removed from activity."""
        email = "michael@mergington.edu"
        
        # Verify student is present before removal
        response = client.get("/activities")
        assert email in response.json()["Chess Club"]["participants"]
        
        # Remove student
        client.delete(
            "/activities/Chess%20Club/participant",
            params={"email": email}
        )
        
        # Verify student was removed
        response = client.get("/activities")
        assert email not in response.json()["Chess Club"]["participants"]
    
    def test_remove_nonexistent_participant_fails(self, client):
        """Test that removing non-existent participant returns 404."""
        response = client.delete(
            "/activities/Chess%20Club/participant",
            params={"email": "nonexistent@mergington.edu"}
        )
        assert response.status_code == 404
        data = response.json()
        assert "Participant not found" in data["detail"]
    
    def test_remove_from_nonexistent_activity_fails(self, client):
        """Test that removing from non-existent activity returns 404."""
        response = client.delete(
            "/activities/Nonexistent%20Club/participant",
            params={"email": "michael@mergington.edu"}
        )
        assert response.status_code == 404
        data = response.json()
        assert "Activity not found" in data["detail"]
    
    def test_remove_and_readd_same_participant(self, client):
        """Test that removed participant can be re-added."""
        email = "michael@mergington.edu"
        activity = "Chess Club"
        
        # Remove participant
        client.delete(
            f"/activities/{activity}/participant",
            params={"email": email}
        )
        
        # Re-add participant
        response = client.post(
            f"/activities/{activity}/signup",
            params={"email": email}
        )
        assert response.status_code == 200
        
        # Verify participant is back
        activities_response = client.get("/activities")
        assert email in activities_response.json()[activity]["participants"]
    
    def test_remove_all_participants_except_one(self, client):
        """Test removing all but one participant from an activity."""
        activity = "Chess Club"
        emails = ["michael@mergington.edu", "daniel@mergington.edu"]
        
        # Remove first participant
        client.delete(
            f"/activities/{activity}/participant",
            params={"email": emails[0]}
        )
        
        # Verify only one participant remains
        response = client.get("/activities")
        participants = response.json()[activity]["participants"]
        assert emails[0] not in participants
        assert emails[1] in participants
