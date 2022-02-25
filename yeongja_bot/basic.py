# -*- coding: utf-8 -*-
'''
기본 logic 파악을 위한 basic slack bot

trigger: slack channel의 trigger가 되는 message
action: 해당하는 message를 찾아 thread에 답변

- ref: https://wooiljeong.github.io/python/slack-bot/
- MacOS는 반드시 python3 으로 명령어 실행
- 코드 전부 작성한 후 `python3 filename.py` 로 파일 실행
'''

# from slack_sdk import WebClient
from slack import WebClient     # issue #1 참고

class SlackAPI:
    """
    슬랙 API 핸들러
    """
    def __init__(self, token):
        # 슬랙 클라이언트 인스턴스 생성
        self.client = WebClient(token)
        
    def get_channel_id(self, channel_name):
        """
        슬랙 채널ID 조회
        """
        # conversations_list() 메서드 호출
        result = self.client.conversations_list()
        # print(result)
        # 채널 정보 딕셔너리 리스트
        channels = result.data['channels']
        # 채널 명이 'test'인 채널 딕셔너리 쿼리
        channel = list(filter(lambda c: c["name"] == channel_name, channels))[0]
        # 채널ID 파싱
        channel_id = channel["id"]
        return channel_id

    def get_message_ts(self, channel_id, query):
        """
        슬랙 채널 내 메세지 조회
        """
        # conversations_history() 메서드 호출
        # TODO: The server responded with: {'ok': False, 'error': 'not_in_channel'}
        result = self.client.conversations_history(channel=channel_id)
        print(result)
        # 채널 내 메세지 정보 딕셔너리 리스트
        messages = result.data['messages']
        # 채널 내 메세지가 query와 일치하는 메세지 딕셔너리 쿼리
        message = list(filter(lambda m: m["text"]==query, messages))[0]
        # 해당 메세지ts 파싱
        message_ts = message["ts"]
        return message_ts

    def post_thread_message(self, channel_id, message_ts, text):
        """
        슬랙 채널 내 메세지의 Thread에 댓글 달기
        """
        # chat_postMessage() 메서드 호출
        result = self.client.chat_postMessage(
            channel=channel_id,
            text = text,
            thread_ts = message_ts
        )
        return result


token = "xoxb-3020057638645-3203557476037-RpVrpvigzG8dtqE4bSi5xCuv"
slack = SlackAPI(token)

channel_name = "일반"
query = "슬랙 봇 테스트"
text = "자동 생성 문구 테스트"

# 채널ID 파싱
channel_id = slack.get_channel_id(channel_name)
# 메세지ts 파싱
message_ts = slack.get_message_ts(channel_id, query)
# 댓글 달기
slack.post_thread_message(channel_id, message_ts, text)