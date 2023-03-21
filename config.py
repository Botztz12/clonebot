#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6047804010:AAGNlAT_-h_r5duNFLBFnAoCBeejUluGEHM")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "21648432"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "967504c26e0ca3e2e321ce04181dd636")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AQFKVDAAo3Lh-x1Ft2QDO1g24KzQtnHVV6TmIJ71dWtsHGKh_Go6tuMYVuHO-fgdk-U5QhGm0POzALcHlcRwsnZVLGylV82-rUrSKfgGQwnSR9po-DaEMGDjZ0ttij2Vdc2K69mNVxSkMCtyi0UIklw0KGwUI6UtDl7d6weF5u9YovaPcwohGae6UVngxWkjan3vl13kwKgzinCkwtdDIEfevjZkZu2o4529MzSfE2nWyvJIa2n-ku-Gk8oxf8zm8QYL7tJ2YISvTUxyBewIel_HEMcceCVc1eSfFSP9gsBbRAk_MCSYyq5AV6wPELWLirzO9It5nb2ICPETlEj1IElm0PfHkgAAAAFho5QuAA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://vbmdkuqz:ZUFifWqND4pmP7VzchMNL8vmobCr1Ig8@floppy.db.elephantsql.com/vbmdkuqz")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
