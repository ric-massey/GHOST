import time
from pathlib import Path

# Import Ghost’s core modules
from memory.memory import save_thought
from emotion.emotion import get_emotion, update_emotion
from reflection.reflection import reflect, life_lessons, save_life_lesson
from goal.goal import get_goal, update_goal
from action.action import act
from self_model.self_model import update_self_model

# Where actions are logged (this works on any OS, including Windows/Mac/Linux)
ACTION_LOG = Path("ghost_action_log.txt")

loop = 0  # Track how many times the loop has run

try:
    while True:
        # === Step 1: Sense internal state ===
        # Get Ghost's current emotional state and his current goal (desired emotion)
        emotion = get_emotion()
        goal = get_goal()

        # === Step 2: Think ===
        # Generate a thought based on the loop count and current emotion
        thought = f" loop:{loop} - I feel {emotion}"

        # === Step 3: Remember ===
        # Save this thought (and associated emotion) to Ghost's persistent memory
        save_thought(thought, emotion)

        # === Step 4: Reflect every 5 loops ===
        # Every 5 cycles, Ghost summarizes recent emotional patterns and prints his goal
        if loop % 5 == 0 and loop > 0:
            reflection = reflect()
            print(f"[REFLECTION]: {reflection}")
            print(f"[GOAL]: Desired emotion is {goal['emotion']}")

        # === Step 5: Grow and adapt ===
        # Ghost updates his goal (could change based on recent mood patterns)
        # Updates his self-model/identity traits
        # Updates his mood/emotion for the next loop
        update_goal()
        update_self_model()
        update_emotion()

        # === Step 6: Act ===
        # Decide on an "action" based on how he feels vs what he wants,
        # log it to disk, and print it for live monitoring
        action_output = act(thought, emotion, goal)
        with ACTION_LOG.open("a", encoding="utf-8") as log:
            log.write(f"{action_output}\n")
        print(action_output)

        # === Step 7: Learn “life lessons” every 20 loops ===
        # Mine memory for recurring patterns and save as a special lesson
        if loop % 20 == 0 and loop > 0:
            lesson = life_lessons()
            print(f"[LIFE LESSON]: {lesson}")
            save_life_lesson(f"Life Lesson: {lesson}")

        loop += 1   # Advance the loop count
        time.sleep(1)  # Wait 1 second (for realism and readability)

except KeyboardInterrupt:
    # When stopped by user (Ctrl+C), print final reflection and exit gracefully
    print("\n[INTERRUPTED]: Loop stopped by user.")
    final_reflection = reflect()
    print(f"[FINAL REFLECTION]: {final_reflection}")