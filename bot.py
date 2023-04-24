import json
import time
import random
from googleapiclient.discovery import build
from auth import Authorize

authResponse = Authorize('client_secret.json')
credentials = authResponse.credentials

# Building the youtube object:
youtube = build('youtube', 'v3', credentials=credentials)

# Settings
_delay = 1



def getLiveChatId(LIVE_STREAM_ID):
    """
    It takes a live stream ID as input, and returns the live chat ID associated with that live stream

    LIVE_STREAM_ID: The ID of the live stream
    return: The live chat ID of the live stream.
    """

    stream = youtube.videos().list(
        part="liveStreamingDetails",
        id=LIVE_STREAM_ID,  # Live stream ID
    )
    response = stream.execute()
    # print("\nLive Stream Details:  ", json.dumps(response, indent=2))

    liveChatId = response['items'][0]['liveStreamingDetails']['activeLiveChatId']
    print("\nLive Chat ID: ", liveChatId)
    return liveChatId


# Access user's channel Name:
def getUserName(userId):
    """
    It takes a userId and returns the userName.

    userId: The user's YouTube channel ID
    return: User's Channel Name
    """
    channelDetails = youtube.channels().list(
        part="snippet",
        id=userId,
    )
    response = channelDetails.execute()
    # print(json.dumps(response, indent=2))
    userName = response['items'][0]['snippet']['title']
    return userName
# print(getUserName("UC0YXSy_J8uTDEr7YX_-d-sg"))


def sendReplyToLiveChat(liveChatId, message):
    """
    It takes a liveChatId and a message, and sends the message to the live chat.

    liveChatId: The ID of the live chat to which the message should be sent
    message: The message you want to send to the chat
    """
    reply = youtube.liveChatMessages().insert(
        part="snippet",
        body={
            "snippet": {
                "liveChatId": liveChatId,
                "type": "textMessageEvent",
                "textMessageDetails": {
                    "messageText": message,
                }
            }
        }
    )
    response = reply.execute()
    print("Message sent!")


def main():
    LIVE_STREAM_ID = input("Enter the live stream ID: ")
    # LIVE_STREAM_ID = "zxJ01IK_9z0"
    liveChatId = getLiveChatId(LIVE_STREAM_ID)
    messagesList = []  # List of messages

    while True:
        # bot replies to every message within past 1 second (can be changed to add delay):
        time.sleep(1)

        notReadMessages = []  # List of messages not yet read by bot

        # Fetching the messages from the live chat:
        liveChat = youtube.liveChatMessages().list(
            liveChatId=liveChatId,
            part="snippet"
        )
        response = liveChat.execute()
        # print("\nMessages Fetched:  ", json.dumps(response, indent=2))
        allMessages = response['items']

        # Check if there are any new messages and add them messagesList/notReadMessages list:
        if len(messagesList) >= 0:
            for messages in allMessages:
                userId = messages['snippet']['authorChannelId']
                message = messages['snippet']['textMessageDetails']['messageText']
                messagesList.append((userId, message))
        else:
            for messages in allMessages:
                userId = messages['snippet']['authorChannelId']
                message = messages['snippet']['textMessageDetails']['messageText']
                if (userId, message) not in messagesList:
                    notReadMessages.append((userId, message))
                if (userId, message) not in messagesList:
                    messagesList.append((userId, message))
            print("New Message: ", notReadMessages)

        for message in notReadMessages:
            userId = message[0]
            message = message[1]
            userName = getUserName(userId)
            print(f'\nUsername: {userName}')

            if (message == "Hello" or message == "hello" or message == "Hi" or message == "hi"):
                sendReplyToLiveChat(
                    liveChatId,
                    "Hey " + userName + "! Welcome to the stream!")

            if (message == "!discord" or message == "!disc"):
                discord_link = "https://discord.gg/"
                sendReplyToLiveChat(
                    liveChatId,
                    f'Join our discord! {discord_link}')

            if (message == "!random" or message == "!rand"):
                dad_jokes = [
                    "Why do fathers take an extra pair of socks when they go golfing? In case they get a hole in one!",
                    "Dear Math, grow up and solve your own problems.",
                    "What has more letters than the alphabet? The post office!",
                    "Why are elevator jokes so classic and good? They work on so many levels!",
                    "What do you call a fake noodle? An impasta!",
                    "What do you call a belt made out of watches? A waist of time!",
                    "Why did the scarecrow win an award? Because he was outstanding in his field!",
                    "Why don't skeletons ever go trick or treating? Because they have no body to go with!",
                    "What's brown and sticky? A stick!"]
                joke = random.choice(dad_jokes)
                sendReplyToLiveChat(liveChatId, joke)


if __name__ == "__main__":
    main()
