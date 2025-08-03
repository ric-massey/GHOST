import random
from reflection.reflection import get_dominant_emotion
from memory.embedding import EMOTION_SPACE

# ========================
# Ghost's Goal Management
# ========================

# Goal state: what emotion Ghost is currently striving for
goal = {"emotion": "calm"}

# Track how long the same goal has persisted (for "boredom" logic)
goal_counter = 0
last_goal = goal["emotion"]

# Valence scores for each emotion.
# Used when Ghost is stuck in negative moods, to "seek the best feeling."
VALENCE = {
    "curious": 0.5,
    "calm": 0.7,
    "hopeful": 0.8,
    "tired": 0.2,
    "frustrated": 0.1,
}

def update_goal():
    """
    Complex, layered goal selection:
    - If Ghost is bored (goal unchanged for a long time), pick a random new goal.
    - If Ghost's current emotion doesn't match his goal, sometimes switch to a "novel" goal.
    - If stuck in negative moods, seek out the highest-valence (best) emotion.
    - Otherwise, adapt goal to match dominant emotion.
    """
    global goal_counter, last_goal
    dominant = get_dominant_emotion()

    # --- Track goal persistence for "boredom" ---
    if goal["emotion"] == last_goal:
        goal_counter += 1
    else:
        last_goal = goal["emotion"]
        goal_counter = 0

    # --- 1. Goal Fatigue: get bored, pick something new ---
    if goal_counter > 50:
        new_goal = random.choice([e for e in EMOTION_SPACE if e != goal["emotion"]])
        goal["emotion"] = new_goal
        goal_counter = 0
        return

    # --- 2. Curiosity/Novelty: 20% chance to want something else when off-goal ---
    if dominant and dominant != goal["emotion"]:
        if random.random() < 0.2:
            possible = [e for e in EMOTION_SPACE if e != dominant]
            if possible:
                goal["emotion"] = random.choice(possible)
            return

    # --- 3. Valence-Seeking: If stuck in bad mood, chase best emotion ---
    if dominant in ["frustrated", "tired"]:
        best = max(VALENCE.items(), key=lambda x: x[1])[0]
        if best != dominant:
            goal["emotion"] = best
            return

    # --- Default: Adapt goal to dominant emotion ---
    if dominant and dominant != goal["emotion"]:
        goal["emotion"] = dominant

def get_goal():
    """
    Return Ghost's current goal (desired emotion).
    """
    return goal