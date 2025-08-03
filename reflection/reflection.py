from memory.memory import get_last, find_all_by_emotion, memory, save_memory_to_disk
from memory.embedding import get_embedding
from datetime import datetime
from collections import Counter

def reflect():
    """
    Summarize Ghost's recent emotional history.
    Looks at the last 10 memories and reports the most common emotion.
    """
    recent = get_last(10)
    if not recent:
        return "I don't remember anything."

    emotion_list = [m["emotion"] for m in recent]
    common = Counter(emotion_list).most_common(1)
    return f"I've mostly felt {common[0][0]}." if common else "No strong emotion detected."

def get_dominant_emotion():
    """
    Return the dominant (most common) emotion from Ghost's last 10 memories.
    Used by other modules (like goal and self-model) to adapt behavior.
    """
    recent = get_last(10)
    if not recent:
        return None

    emotion_list = [m["emotion"] for m in recent]
    common = Counter(emotion_list).most_common(1)
    return common[0][0] if common else None

def print_all_by_emotion(emotion):
    """
    Print out all memories that match a given emotion.
    Helpful for debugging or for Ghost to review past states.
    """
    relevant = find_all_by_emotion(emotion)
    for m in relevant:
        print(m["timestamp"], m["text"])

def life_lessons():
    """
    Mine Ghost's entire memory for the most common emotional transition:
    "When I feel X, I usually feel Y next."
    This forms the basis of Ghost's 'wisdom' or pattern learning.
    """
    transitions = {}
    prev_emotion = None

    for mem in memory:
        current = mem["emotion"]
        if prev_emotion is not None:
            pair = (prev_emotion, current)
            transitions[pair] = transitions.get(pair, 0) + 1
        prev_emotion = current

    if not transitions:
        return "Not enough memory for life lessons."

    # Find the most frequent emotion-to-emotion transition
    most_common = max(transitions.items(), key=lambda x: x[1])
    lesson = f"When I feel {most_common[0][0]}, I usually feel {most_common[0][1]} next."
    return lesson

def save_life_lesson(lesson_text):
    """
    Save a new life lesson as a special memory with emotion 'lesson'.
    This lets Ghost remember not just events, but what he's learned.
    """
    memory.append({
        "timestamp": datetime.now().isoformat(),
        "text": lesson_text,
        "emotion": "lesson",
        "intensity": 1.0,
        "embedding": get_embedding("calm", 1.0)  # Can change to match the tone of the lesson
    })
    save_memory_to_disk()