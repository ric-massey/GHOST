# =========================
# Ghost's Self-Model System
# =========================

# Core identity data for Ghost
self_state = {
    "name": "Ghost",             # The agent's name
    "version": "0.1",            # Agent version (update as you evolve Ghost)
    "identity": ["curious", "reflective"]  # Ghost's current core traits (emotional history)
}

from reflection.reflection import get_dominant_emotion  # Import to check recent dominant emotion

def update_self_model():
    """
    Check what Ghost's dominant emotion is right now.
    If it's a new emotional experience (not already in his identity),
    add it to his list of core traits.
    Keep only the 5 most recent/important traits to avoid unbounded growth.
    """
    dominant = get_dominant_emotion()
    if dominant and dominant not in self_state["identity"]:
        self_state["identity"].append(dominant)
        # Keep only the last 5 identity traits (oldest dropped first)
        if len(self_state["identity"]) > 5:
            self_state["identity"] = self_state["identity"][-5:]