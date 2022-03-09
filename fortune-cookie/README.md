<h1>Your personal fortune teller <small>but not guaranteed :stuck_out_tongue_closed_eyes: </small></h1>

> ChatBot: A Bot replies when a user wants to talk

## 1. Environment Setting

```zsh
# MacOS
$ python3 -m venv venv
$ source venv/bin/activate

# Windows
$ python -m venv venv
$ source venv/Scripts/activate
```

## 2. dependency check

```zsh
# requirements.txt
python == 3.9.10
slack-sdk == 3.15.2
slackclient == 2.9.3
```

## 3. make slack-bot

### Basic function (1)

### & Bot Scope

| OAuth Scope       | Description                                                                                    |
| :---------------- | :--------------------------------------------------------------------------------------------- |
| channels:read     | View basic information about public channels in a workspace                                    |
| groups:read       | View basic information about private channels that fortune-cookie has been added to            |
| im:read           | View basic information about direct messages that fortune-cookie has been added to             |
| mpim:read         | View basic information about group direct messages that fortune-cookie has been added to       |
| channels:history  | View messages and other content in public channels that fortune-cookie has been added to       |
| groups:history    | View messages and other content in private channels that fortune-cookie has been added to      |
| im:history        | View messages and other content in direct messages that fortune-cookie has been added to       |
| mpim:history      | View messages and other content in group direct messages that fortune-cookie has been added to |
| chat:write        | Send messages as fortune-cookie                                                                |
| chat:write.public | Send messages to channels fortune-cookie isn't a member of                                     |

## 4. make slack-bot reply when it mentioned: Enable Bot Event

blank

## reference

- [슬랙 챗봇 만들기 [협업 메신저 끝판왕 슬랙(Slack) 7강]](https://ndb796.tistory.com/201)
