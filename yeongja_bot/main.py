# https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
# https://github.com/mattmakai/slack-starterbot/blob/master/starterbot.py
# pip install slackclient==1.3.2
import os
import time
import re
from slack import SlackClient
from slack_sdk import WebClient # for Slack Handler

# initiate Slack Client
slack_client = SlackClient(
    os.environ.get("SLACK_BOT_TOKEN")
)  # The common practice for Python developers to deal with secret tokens is using the command: `export` in terminal
bot_id = None  # Autometically assigned after bot starts up

# constants
BOT_NAME = "yeongja"
RTM_READ_DELAY = 1  # 1 second delay between reading from RTM*: to prevent entering an infinite loop so early
EXAMPLE_COMMAND = "help"
MENTION_REGEX = "<@(|[WU].+?)>(.*)"  # [CUSTOMED] message example: any message <@UuserID> message body
# RTM*: Slack client connects to the Slack RTM API that calls Web API mehod: `auth.test` to find Bot's user ID
# RTM and infinite loop: each loop runs the client receives any events that arrived from Slack's RTM API.
# Storing Bot's user ID will help the program to understand if someone has mentioned the bot in a message
# RegEx note
# group : (group)
# | : or not / [] : range / . : all character
# repeat : + == {1, } / * == {0, }
# ? : lazy, {0, 1}, or not

# parse_bot_commands(slack_events): Checking any events contains a command for The Bot
def parse_bot_commands(slack_events):
    """
    purpose: parse slack events
    target: events comming from the Slack RTM API
    for: find bot commands
    return:
        - command found: (command, channel)
        - command not found: (None, None)
    """
    for slack_event in slack_events:
        if slack_event["type"] == "message" and not "subtype" in slack_event:
            user_id, message = parse_direct_mention(
                slack_event["text"]
            )  # parse_direct_mention: (mentioned user id, message)
            if user_id == bot_id:
                return message, slack_event["channel"]
    return (
        None,
        None,
    )  # search every slack events, then command is not founded: return None, None


def parse_direct_mention(message_text):
    """
    purpose: find a direct mention
    return: user ID which was mentioned (or None)
    """
    # re.search(pattern, string) : find pattern in string
    # : returns <~span=(start idx, end idx), match = pattern> or None
    matches = re.search(MENTION_REGEX, message_text)  # "<@(|[WU].+?)>(.*)"
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)


def recommend_menu():
    # fill out
    return "칼국수"


def handle_command(command, channel):
    """
    Executes bot command if the command is KNOWN
    """
    # Default response
    # EXAMPLE_COMMAND : help
    default_response = (
        f"Hello! I'm {BOT_NAME}. If you wanna know me, try `{EXAMPLE_COMMAND}` command."
    )

    # Command Match
    if command.startswith(EXAMPLE_COMMAND):  # startswith -> ?
        response = """Greetings! These are commands you can use.
        \t- `추천` : I will suggest today's menu randomly
        """

    # yeongja bot doesn't need any commands. just mention the bot directly.
    MENU = recommend_menu()
    if MENU:
        response = f"점심으로 {MENU} 어때요?"

    # Send the response back to the channel
    slack_client.api_call(
        "chat.postMessage", channel=channel, text=response or default_response
    )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print(f"{BOT_NAME} Bot connected and running!")

        # Read Bot's User ID by calling Web API method `auth.test`
        bot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
