import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[
    logging.FileHandler("event_log.log"),
    logging.StreamHandler()
])

def log_event(event):
    logging.info(f"Event: {event}")

def simulate_events():
    events = ["Obstacle detected", "Low battery", "Path deviation"]
    for event in events:
        log_event(event)
        time.sleep(2)  # Simulate time between events

if __name__ == "__main__":
    simulate_events()
