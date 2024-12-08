from db_config import Message
from read_all import display_all_messages


def update_message():
    print("更新前")
    display_all_messages()

    msg = Message.get_by_id(4)
    msg.content = "やっほー"
    msg.save()
    print("更新後")
    display_all_messages()


if __name__ == "__main__":
    update_message()
