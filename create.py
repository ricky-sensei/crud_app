from db_config import Message

def create_message():
    # インスタンスを作成するパターン
    message = Message(user="Bob", content="Hello Tom")
    message.save()

    # インスタンスを作成しないパターン
    Message.create(user="Tom", content="Hello Bob")

if __name__ == "__main__":
    create_message()
