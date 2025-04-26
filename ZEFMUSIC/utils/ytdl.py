import asyncio
import os
from typing import Dict, List, Union

import yt_dlp
from yt_dlp import YoutubeDL

from ZEFMUSIC import LOGGER

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "prefer_ffmpeg": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

ytdl = YoutubeDL(ydl_opts)


def get_file_extension_from_url(url: str) -> str:
    url_path = url.split("?")[0]
    return os.path.splitext(url_path)[1]


async def get_yt_info_id(videoid: str) -> Dict:
    try:
        x = ytdl.extract_info(videoid, download=False)
        return x
    except Exception as e:
        LOGGER.error(f"Error extracting info: {e}")
        return None


async def get_yt_info_url(url: str) -> Dict:
    try:
        x = ytdl.extract_info(url, download=False)
        return x
    except Exception as e:
        LOGGER.error(f"Error extracting info: {e}")
        return None


async def download_yt_audio(videoid: str) -> str:
    try:
        x = ytdl.extract_info(videoid, download=True)
        return f"downloads/{x['id']}.mp3"
    except Exception as e:
        LOGGER.error(f"Error downloading audio: {e}")
        return None


async def download_yt_video(videoid: str) -> str:
    try:
        x = ytdl.extract_info(videoid, download=True)
        return f"downloads/{x['id']}.mp4"
    except Exception as e:
        LOGGER.error(f"Error downloading video: {e}")
        return None

__all__ = ["ytdl", "get_file_extension_from_url", "get_yt_info_id", "get_yt_info_url", "download_yt_audio", "download_yt_video"] 