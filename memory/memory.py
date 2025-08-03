from datetime import datetime
from memory.embedding import get_embedding
import json
import os

# ============================
# Persistent Memory Management
# ============================

MEMORY_FILE = "ghost_memory.json"  # Where Ghost's memory is saved

# ---------------------------
# Load memory from disk at startup
# ---------------------------
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)   # Load previous thoughts and experiences
else:
    memory = []  # Start with empty memory if no file found

def save_memory_to_disk():
    """
    Write the entire memory list to disk as a JSON file.
    Keeps Ghost's thoughts/experiences safe between runs.
    """
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

def save_thought(text, emotion, intensity=0.5):
    """
    Create and store a new memory/thought with timestamp, emotion, and embedding.
    Also saves updated memory to disk.
    """
    embedding = get_embedding(emotion, intensity)  # Generate numeric vector for memory search
    memory.append({
        "timestamp": datetime.now().isoformat(),    # When this thought occurred
        "text": text,                              # Content of the thought
        "emotion": emotion,                        # Emotional tag for later recall
        "intensity": intensity,                    # How strong the emotion was
        "embedding": embedding                     # Numeric embedding for similarity search
    })
    save_memory_to_disk()                          # Persist to disk immediately

def get_last(n=5):
    """
    Retrieve the last n memories (default: 5).
    Used for reflection and trend analysis.
    """
    return memory[-n:]

def find_similar_thoughts(target_embedding, threshold=0.8):
    """
    Find recent thoughts with a high cosine similarity to a given embedding.
    Returns the 5 most recent close matches.
    """
    def cosine_similarity(a, b):
        dot = sum(i*j for i, j in zip(a, b))
        norm_a = sum(i**2 for i in a) ** 0.5
        norm_b = sum(j**2 for j in b) ** 0.5
        return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0

    similar = [
        m for m in memory
        if cosine_similarity(m["embedding"], target_embedding) > threshold
    ]
    return similar[-5:]

def find_all_by_emotion(emotion):
    """
    Return all memories labeled with the specified emotion.
    Useful for emotional pattern mining or debugging.
    """
    return [m for m in memory if m["emotion"] == emotion]

def find_by_phrase(phrase):
    """
    Return all memories whose text contains the given phrase (case-insensitive).
    Lets Ghost search for ideas or events by keyword.
    """
    return [m for m in memory if phrase.lower() in m["text"].lower()]