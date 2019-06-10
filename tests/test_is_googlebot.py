import pytest
import is_googlebot


googlebot_ip = '66.249.66.1'
not_googlebot_ip = '162.241.216.134'  # foobar.com

# from https://support.google.com/webmasters/answer/1061943
user_agents = [
    'APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)',
    'Mediapartners-Google',
    'Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)',
    'AdsBot-Google (+http://www.google.com/adsbot.html)',
    'Googlebot-Image/1.0',
    'Googlebot-News',
    'Googlebot-Video/1.0',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    'Googlebot/2.1 (+http://www.google.com/bot.html)',
    'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'compatible; Mediapartners-Google/2.1; +http://www.google.com/bot.html',
    'AdsBot-Google-Mobile-Apps',
    'FeedFetcher-Google; (+http://www.google.com/feedfetcher.html)',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36 (compatible; Google-Read-Aloud; +https://support.google.com/webmasters/answer/1061943)',
    'google-speakr'
]


def test_googlebot():
    for user_agent in user_agents:
        assert is_googlebot.test(googlebot_ip, user_agent) is True


def test_googlebot_ip_only():
    assert is_googlebot.test(googlebot_ip) is True


def test_not_googlebot_ip():
    for user_agent in user_agents:
        assert is_googlebot.test(not_googlebot_ip, user_agent) is False


def test_not_googlebot_ua():
    assert is_googlebot.test(googlebot_ip, 'Foo') is False
