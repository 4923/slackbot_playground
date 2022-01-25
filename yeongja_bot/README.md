# Clone coding | Lunch suggestion bot: Yeongju Bot | Python 3.9.7

## Contents
  * [Flow](#flow)
    + [1. Enviromental Settings](#1-enviromental-settings)
    + [2. Install `slackclient` library](#2-install--slackclient--library)
    + [3. Create Slack `User Bot`](#3-create-slack--user-bot)
    + [4. Add OAuth Scopes](#4-add-oauth-scopes)
    + [5. `Install to Workspace` every scopes](#5--install-to-workspace--every-scopes)
    + [6. Code your Bot](#6-code-your-bot)
  * [ref](#ref)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

<hr>

## Flow

### 1. Enviromental Settings
1. Create Virtual Enviroment (Python `venv`)
    ```bash
    $ python -m venv yeongja_bot_venv
    ```
2. Activate venv
    ```bash
    $ source yeongja_bot_venv/Scripts/activate
    ```

### 2. Install `slackclient` library
```bash
$ pip install slackclient
```

### 3. Create Slack `User Bot` ([Slack API](https://api.slack.com/bot-users))
1. Getting Started ![slack api page](https://user-images.githubusercontent.com/60145951/151020221-d4035eb5-3836-4062-a61f-d5b4ae864cad.png)
2. Create your Slack app - From scratch
    |Create app|fill out app name, workspace name|
    |:-:|:-:|  
    |![Create app](https://user-images.githubusercontent.com/60145951/151020550-4c8313b7-d98a-42f3-bbd1-c7d081567ae6.png) | ![Fill out your app name, workspace name](https://user-images.githubusercontent.com/60145951/151032397-92ff29fe-6ff3-4404-acd8-ead66575fee3.png)|
    - manifest : Metadata file (e.g. Android manifest file) 

### 4. Add OAuth Scopes
- OAuth : Open Authorization
1. Add features : `bots` -> redirect App Home page
    ![Add features](https://user-images.githubusercontent.com/60145951/151032509-db11a2ec-2de4-4e1d-8e2f-85fb10c1ea9d.png)
2. at App Home page -> `Review Scopes to Add` 
    ![Review Scopes to Add](https://user-images.githubusercontent.com/60145951/151032646-7b1b12b4-041c-4e43-aae4-7557161db25e.png)
3. Set `OAuth Scopes`
    |will activate after setting Scopes|Add OAuth Scopes|
    |:-:|:-:|
    |![install to workspace](https://user-images.githubusercontent.com/60145951/151032743-af1bb9d3-6284-4a2c-acae-d0bdaa262202.png)|![Add scopes](https://user-images.githubusercontent.com/60145951/151024970-f80532f0-62b3-493c-a5eb-ff94bad6db92.png)|
    - Search API methods in [API Methods page](https://api.slack.com/methods)
    - Major Web API Method
        - example: To write chat message a bot, `chat.postMessage` **method** will needed. The method requires `chat:write` **scopes**. ([api page](https://api.slack.com/methods/chat.postMessage))
            |method|goal|required scopes|
            |:-:|:-:|:-:|
            |chat.postMessage|Sends a message to a channel|chat:write|

            ![chat post message](https://user-images.githubusercontent.com/60145951/151028553-6dea04ff-7e8a-4996-b5fc-d69f84020438.png)
        - Follow these flow, clarify the actions of a bot and search Slack API method that describes the actions best
        - To suggest Lunch, The bot needs...
            1. suggest menu on time: post a message
                - chat.postMessage
            2. Reaction: search message through certain channel or mention function (e.g. @yeongja)
            3. How to reply?: reply on thread
                1. check channel code -> how?
                2. Track message code: `thread_ts`
                3. Create thread: put `thread_ts` at chat.postMessage
                > `conversation.replies`
        - `Add an OAuth Scope`
            |An example of adding scope (for bot)|Add|Search|
            |:-:|:-:|:-:|
            |![An example of adding scope](https://user-images.githubusercontent.com/60145951/151033479-291eea9a-5d4b-4871-8234-596fbf7c6100.png)|![Add scope](https://user-images.githubusercontent.com/60145951/151034001-b8941dd2-bd1f-43dd-8981-5afcb39f226a.png)|![search](https://user-images.githubusercontent.com/60145951/151034144-eb6fe57d-0f8d-421b-ace9-e268fda8ff0f.png)

### 5. `Install to Workspace` every scopes
After adding OAuth Scopes and scroll up, `Install to Workspace` button will activate. push to install.
Then, `OAuth Tokens for Your Workspace` will be generated.

|Activated button|Request workspace auth|Token generation
|:-:|:-:|:-:|
|![Install scope](https://user-images.githubusercontent.com/60145951/151034232-77abbddc-cafb-4a33-9490-3e860c546978.png)|![workspace auth](https://user-images.githubusercontent.com/60145951/151034565-65e1367e-9fec-46ba-bfbd-e727817d1ee4.png)|![Token generation](https://user-images.githubusercontent.com/60145951/151034800-fc9094f0-6cf1-402d-a219-141d8dd20b7f.png)|


### 6. Code your Bot




## ref
- [간단한 Slack Bot 만들어 배포해보기|개미의 개발노트](https://ugaemi.com/slack/Deploy-simple-slack-bot/)
- [mattmakai/slack-starterbot](https://github.com/mattmakai/slack-starterbot/blob/master/starterbot.py)
- [how to build your first slack bot with python](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)
- [파이썬 - 슬랙 api로 슬랙봇 만들기 <1편 환경세팅>](https://nanchachaa.tistory.com/44)
- [슬랙Slack - API로 thread 생성 및 reply 달기, chat.postMessage](https://blog.naver.com/PostView.naver?blogId=jogilsang&logNo=222272481593&categoryNo=104&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView)
- [threading message](https://api.slack.com/messaging/managing#threading)
- [파이썬 Python - 슬랙 api로 슬랙봇 slackbot 만들기 <2편 환경세팅>](https://nanchachaa.tistory.com/77)