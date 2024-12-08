from db_config import Message
def delete_message():
    msg_id = input("削除するメッセージのIDを入力してください >")
    msg = Message.get_by_id(msg_id)
    # msg.delete_instance()

    # もし失敗したらエラーメッセージを表示
    if not msg.delete_instance():
        print("削除に失敗しました IDをかくにんしてね！")

def main():
    user_name = input("ユーザー名を入力してください")
    while True:
        for msg in Message.select():
            print(f"{msg.id} {msg.user} {msg.content} {msg.pub_date}")

        message = input("メッセージを入力してください")

        if message == "\\q":
            break

        if message == "\\d":
            delete_message()
            continue  # スキップしてループを再開

        Message.create(user=user_name, content=message)


if __name__ == "__main__":
    main()
