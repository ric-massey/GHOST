# Ghost

Ghost is a minimal, living cognition simulator with no AI models.
He thinks, feels, remembers, reflects, acts, and learns simple “life lessons” about his own emotional experience.  
Ghost is designed as a simple, hackable framework for anyone curious about how minds might work.

---

## Features

- **Persistent memory:** Remembers all thoughts and emotions between runs (saved to disk)
- **Mood and goal system:** Drifts between emotions, sometimes seeks new feelings, can get “bored” or “ambitious”
- **Reflection:** Summarizes recent emotional history and can mine life lessons from experience
- **Self-model:** Tracks evolving identity traits based on dominant moods
- **Simple action logic:** Behaves differently based on mood, goal, and even the content of his thoughts
- **Extensible:** Every part is modular and easy to hack

---

## How to Run

1. **Clone or download this repo**
2. **Install Python 3.8+** (if you don’t already have it)
3. In your terminal, navigate to the project directory  
4. Run Ghost:

*(If on Mac/Linux, you may need `python3 main_loop.py`)*

Ghost will print his actions, reflections, and life lessons to your terminal as he loops.  
You can stop him any time with `Ctrl+C`.

---

## Files & Structure

- `main_loop.py` — The core loop that runs Ghost’s mind
- `memory/` — Memory storage, retrieval, and embedding logic
- `emotion/` — Emotion state, emotion space, and update logic
- `goal/` — How Ghost chooses what he wants to feel
- `reflection/` — Reflection, dominant mood detection, and life lesson mining
- `action/` — Simple action selection logic
- `self_model/` — Ghost’s evolving identity traits

---

## How To Hack Ghost

- **Add more emotions**: Edit `emotion_space.py` and expand the transition map
- **Change what he remembers**: Edit `memory.py`
- **Make new actions**: Add patterns to `act()` in `action.py`
- **Give him new drives**: Modify `goal.py` for new motivational logic
- **Let him reflect deeper**: Change or add to `reflection.py`

---

## Why?

Ghost is built for curiosity, experimentation, and learning—not to “win” at AI, but to see what emerges from simple parts connected in the right way.  
Fork it, break it, evolve it, or use it to prototype your own mind.

---

**Built by Ric Massey **

## License

This project is licensed under the [MIT License].