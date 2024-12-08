import sqlite3

dbname = "main.db"

# 接続情報
conn = sqlite3.connect(dbname)

# cursorカーソル　一行ずつ処理を進めるときの現在位置を表す
cur = conn.cursor()

# テーブルの作成Create
cur.execute("CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, price INTEGER)")

# テーブル情報の更新Update
cur.execute('INSERT INTO items values(0, "りんご", 100)')

# 変更をコミット（しないと保存されない）
conn.commit()

# itemsテーブルから情報をすべて持ってくる
cur.execute('SELECT * FROM items')

for row in cur:
    print(row)

conn.close()
