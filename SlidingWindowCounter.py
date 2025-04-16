from collections import deque, defaultdict

class SlidingWindowCounter:
    def __init__(self, window_size=300):
        self.window_size = window_size
        self.events = deque()
        self.user_counts = defaultdict(int)
    
    def add_event(self, event):
        timestamp = event.get['timestamp']
        user_id = event.get['user_id']
        self.events.append((timestamp, user_id))
        self.user_counts[user_id] += 1
        self._evict_old_events(timestamp)
    
    def _evict_old_events(self, current_time):
        while self.events and self.events[0][0] <= current_time - self.window_size:
            old_time, old_user = self.events.popleft()
            self.user_counts[old_user] -= 1
            if self.user_counts == 0:
                self.user_counts.pop(old_user, None)
    
    def get_unique_user_count(self):
        return len(self.user_counts)
