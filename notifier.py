
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

# Örnek kullaným
if __name__ == "__main__":
    send_notification("AAPL Stock Alert", "AAPL stock price has increased by 5%")
