from reflection.reflection import get_dominant_emotion
from goal.goal import get_goal

# =======================
# Emotion System for Ghost
# =======================

# Start with a default mood (Ghost "wakes up" curious)
mood = "curious"

# How emotions drift over time if not disturbed ("emotion gravity" map)
transitions = {
    "frustrated": "tired",   # If frustrated, mood tends toward tiredness
    "tired": "calm",         # Tiredness drifts toward calm
    "calm": "curious",       # Calm drifts back toward curiosity
    "curious": "hopeful",    # Curiosity becomes hope
    "hopeful": "calm"        # Hopeful settles to calm
}

def get_emotion():
    """
    Return Ghost's current emotional state.
    """
    global mood
    return mood

def update_emotion(current_emotion=None):
    """
    Adjust Ghost's mood based on:
    - His current goal (desired emotion)
    - Recent emotional history (dominant memory)
    - Predefined transition/decay rules

    This lets Ghost drift, adapt, or get "stuck" in ruts like a real mind.
    """
    global mood

    # Get what Ghost wants to feel (his "goal" emotion)
    goal = get_goal()
    goal_emotion = goal.get("emotion")

    # Find out what emotion has dominated his recent experiences
    dominant = get_dominant_emotion()

    # --- Step 1: If Ghost's mood is NOT what he wants, increase tension ---
    if mood != goal_emotion:
        if dominant == "frustrated":
            # If feeling frustrated, spiral toward tiredness (simulate emotional exhaustion)
            mood = "tired"
        elif dominant:
            # Otherwise, adopt the most common recent mood
            mood = dominant
        else:
            # If no dominant mood, default to "frustrated" (simulate unease)
            mood = "frustrated"

    # --- Step 2: If Ghost is on-goal, let mood decay "downward" ---
    else:
        # Follow the transition/decay map for natural emotional drift
        mood = transitions.get(mood, "curious")  # Fallback to "curious" if mood is unknown