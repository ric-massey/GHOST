# ========================
# Master List of Emotions
# ========================
# This file defines all emotions Ghost can feel or target as a goal.
# It acts as the "source of truth" for emotion names—import this everywhere!

EMOTION_SPACE = [
    "curious",
    "calm",
    "frustrated",
    "hopeful",
    "tired"
]

"""
EMOTION_SPACE:
- List of all valid emotional states for Ghost.
- Used for one-hot embeddings, novelty selection, valence mapping, and more.
- Edit this list if you want Ghost to recognize, feel, or pursue new emotions!
"""