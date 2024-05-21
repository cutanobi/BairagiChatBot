from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "1807588434"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "https://t.me/+FSkhK9hV1TtkNTk9")
UPDATE_CHNL = getenv("UPDATE_CHNL", "ll_BAIRAGI_DP_ll")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ll_BAIRAGI_ll")

# Random Start Images
IMG = [
    "https://graph.org/file/1d5063e2b9f08c0109108.jpg",
    "https://graph.org/file/a1c1884f8132d2c4463dd.jpg",
    "https://graph.org/file/aa8dac7ab7aec317929da.jpg",
    "https://graph.org/file/78912103eb258da099584.jpg",
    "https://graph.org/file/07214f35e4c5cf89685c2.jpg",
    "https://graph.org/file/74350033a7caed10dfb79.jpg",
    "https://graph.org/file/523184671fb2ede1c68fe.jpg",
    "https://graph.org/file/8bc2fff277ac87a7c589b.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgEAAxkBAAIJomRdLhVJVebkx0JRsp1STwTv3t3eAAJrAgAClpxhRD4z4bgqlIF0LwQ",
    "CAACAgUAAxkBAAIJo2RdLhjLjCpmPipMT8ksrqwUjGAIAAK1BQACLZ8oVFVNmhalU8eOLwQ",
    "CAACAgUAAx0CekRwCQADYWWaUnQ2oJqJLbDTZgZbXRT58wuqAAKECgACkgnhVLC0s4joaxF4HgQ",
]


EMOJIOS = [
    "❤️",
    "🧡",
    "💛",
    "💚",
    "💙",
    "💜",
    "🤎",
    "🖤",
    "🤍",
    "♥️",
]
