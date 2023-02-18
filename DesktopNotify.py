from plyer import notification

title = 'Notification'

message='Take a short break...'

notification.notify(
    title=title,
    message=message,
    timeout=5  # seconds
)
