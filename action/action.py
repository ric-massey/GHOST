def act(thought, emotion, goal):
    """
    Decide Ghost's action based on both:
      - His current emotion vs. his goal (what he wants to feel)
      - The *content* of his latest thought (text analysis)

    This makes Ghost more context-aware and allows for unique actions if certain ideas or moods arise.
    """
    # Lowercase the thought for simple, case-insensitive keyword matching
    text = thought.lower()

    # --- Special action triggers based on thought content and mood ---

    # If Ghost is feeling curious AND thinking about "explore", take a special action
    if "explore" in text and emotion == "curious":
        return "[ACTION]: My curiosity drives me to explore new ideas."

    # If his thought mentions "tired", or his emotion is tired, suggest resting
    if "tired" in text or emotion == "tired":
        return "[ACTION]: I should rest and recharge."

    # --- Default action logic ---

    # If his current emotion does NOT match his goal, he rests (pauses, reflects, or tries to change)
    if emotion != goal["emotion"]:
        return f"[ACTION]: I want to feel {goal['emotion']}, but I feel {emotion}. I will rest."
    # If his current emotion matches his goal, he keeps going
    else:
        return f"[ACTION]: I feel as I desire: {emotion}. I continue."