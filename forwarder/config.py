from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5833869275:AAE1gLQmOf_BQrmdCcHMEIFpO68PBlXoPCI"  # Your bot API key
    OWNER_ID = 6234365091  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [6234365091]  # List of chat id's to forward messages from.
    TO_CHATS = [-1001230414925]  # List of chat id's to forward messages to.

    REMOVE_TAG = True
    WORKERS = 4
