from emotion.emotion_space import EMOTION_SPACE

def get_embedding(emotion, intensity=0.5):
    """
    Generate a compact numeric embedding for each thought/memory.

    Embedding is a 9-dimensional vector made of:
      - One-hot encoding for the emotion (5 floats, one for each possible emotion)
      - Intensity (1 float: how strongly the emotion was felt)
      - Valence scores (3 floats: [positive, neutral, negative] weights)

    This lets Ghost do fast, semantic similarity searches and emotional pattern mining.
    """
    # One-hot encoding: Mark the index of the active emotion as 1.0, all others 0.0
    one_hot = [1.0 if e == emotion else 0.0 for e in EMOTION_SPACE]

    # Valence mapping: "How positive/neutral/negative is this emotion?"
    valence_map = {
        "curious":     [0.2, 0.8, 0.0],  # Mostly neutral, a little positive
        "hopeful":     [0.9, 0.1, 0.0],  # Strongly positive
        "calm":        [0.7, 0.3, 0.0],  # Positive, slightly neutral
        "tired":       [0.1, 0.3, 0.6],  # Mostly negative, some neutral
        "frustrated":  [0.0, 0.2, 0.8]   # Strongly negative, slight neutral
    }
    valence = valence_map.get(emotion, [0.3, 0.4, 0.3])  # Fallback: balanced

    # Return the full embedding: one-hot + intensity + valence (9 floats total)
    return one_hot + [intensity] + valence