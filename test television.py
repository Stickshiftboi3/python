import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "TV [Status: Off, Channel: 0, Volume: 0, Unmuted]"

def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == "TV [Status: On, Channel: 0, Volume: 0, Unmuted]"
    tv.power()
    assert str(tv) == "TV [Status: Off, Channel: 0, Volume: 0, Unmuted]"

def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert str(tv) == "TV [Status: On, Channel: 0, Volume: 0, Muted]"
    tv.mute()
    assert str(tv) == "TV [Status: On, Channel: 0, Volume: 0, Unmuted]"

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "TV [Status: On, Channel: 1, Volume: 0, Unmuted]"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  # Wrap around to MIN_CHANNEL
    assert str(tv) == "TV [Status: On, Channel: 0, Volume: 0, Unmuted]"

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()  # Wrap around to MAX_CHANNEL
    assert str(tv) == "TV [Status: On, Channel: 3, Volume: 0, Unmuted]"

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "TV [Status: On, Channel: 0, Volume: 1, Unmuted]"
    tv.volume_up()
    tv.volume_up()  # Stays at MAX_VOLUME
    assert str(tv) == "TV [Status: On, Channel: 0, Volume: 2, Unmuted]"

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_down()  # Already at MIN_VOLUME
    assert str(tv) == "TV [Status: On, Channel: 0, Volume: 0, Unmuted]"
