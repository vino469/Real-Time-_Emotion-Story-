import cv2
import time
import textwrap
from deepface import DeepFace
FONT = cv2.FONT_HERSHEY_SIMPLEX
UPDATE_INTERVAL = 3  
FALLBACK_STORIES = {
    "happy": (
        "A young boy spread happiness wherever he went. "
        "His smile inspired everyone around him. "
        "Moral: Positivity changes lives."
    ),
    "sad": (
        "A small bird fell from its nest but never gave up. "
        "It tried again and learned to fly. "
        "Moral: Never lose hope."
    ),
    "angry": (
        "A lion learned that anger destroys peace. "
        "He chose calmness over rage. "
        "Moral: Control your anger."
    ),
    "neutral": (
        "A traveler walked silently through a forest, "
        "observing everything around him carefully. "
        "Moral: Silence gives clarity."
    ),
    "surprise": (
        "A girl opened a mysterious box and discovered a gift "
        "she never expected. Life is full of surprises."
    ),
    "fear": (
        "A boy was afraid of the dark cave, but slowly stepped in "
        "and found it was not scary at all. "
        "Moral: Fear exists only in mind."
    )
}


def wrap_text(text, width=50):
    return textwrap.fill(text, width)


def detect_emotion_story():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Webcam not accessible")
        return

    last_emotion = "neutral"
    last_update_time = time.time()
    story = FALLBACK_STORIES[last_emotion]

    print("Emotion Story Generator Started")
    print("Press Q to quit")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("ERROR: Failed to grab frame")
            break

        try:
            
            result = DeepFace.analyze(
                frame,
                actions=['emotion'],
                enforce_detection=False
            )

            emotion = result[0]['dominant_emotion']

        except Exception:
            emotion = "neutral"

        
        if time.time() - last_update_time > UPDATE_INTERVAL:
            if emotion != last_emotion:
                last_emotion = emotion

            story = FALLBACK_STORIES.get(last_emotion, FALLBACK_STORIES["neutral"])
            last_update_time = time.time()

       
        display_frame = frame.copy()

        cv2.putText(display_frame, f"Emotion: {last_emotion}", (20, 40),
                    FONT, 1, (0, 255, 0), 2)

        y0, dy = 80, 25
        for i, line in enumerate(wrap_text(story, 50).split("\n")):
            y = y0 + i * dy
            cv2.putText(display_frame, line, (20, y),
                        FONT, 0.6, (255, 255, 255), 1)

        cv2.imshow("Emotion Story Generator", display_frame)

      
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_emotion_story()