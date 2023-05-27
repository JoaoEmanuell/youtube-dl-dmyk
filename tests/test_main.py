from youtube_dl import YoutubeDL

def test_answer() -> None:

    # Normal vídeo test

    url_video = r'https://youtu.be/JgPg3QF1bhs'

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url_video, download=False)
        assert type(info_dict) == dict
        assert info_dict['title'] == 'TOGURO THEME SONG (em pleno 2022 version)'
        assert info_dict['id'] == 'JgPg3QF1bhs'

    # Video url
    itag = '140'
    for form in info_dict["formats"]:
        assert type(form) == dict
        if form["format_id"] == itag:
            video_form = form["url"]
            assert type(video_form) == str

    # Playlist info

    url_playlist = r'https://youtube.com/playlist?list=PLnDvRpP8BnewYKI1n2chQrrR4EYiJKbUG'

    ydl_opts = {"quiet": True, "no_warnings": True, "extract_flat": "in_playlist"}
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url_playlist, download=False)
        playlist_urls = [
        f"https://youtube.com/watch/?v={entry['url']}"
        for entry in info_dict["entries"]
    ]

    assert type(playlist_urls) == list
    assert playlist_urls[0] == r'https://youtube.com/watch/?v=qH7rsZBENJo'