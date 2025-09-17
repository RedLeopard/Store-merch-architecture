# Mock Consumer (Python)
# run: python consumer.py (watches /tmp/bus_price.jsonl and writes to SQLite)
import json, sqlite3, time, os
DB="/tmp/projections.db"
conn=sqlite3.connect(DB)
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS price (sku TEXT, location TEXT, price REAL, currency TEXT, ts REAL)")
conn.commit()

print("Watching /tmp/bus_price.jsonl ... Ctrl+C to exit")
seen = 0
while True:
    if not os.path.exists("/tmp/bus_price.jsonl"):
        time.sleep(0.5)
        continue
    with open("/tmp/bus_price.jsonl") as f:
        lines=f.readlines()
    for i,line in enumerate(lines[seen:]):
        evt=json.loads(line)
        cur.execute("INSERT INTO price VALUES (?,?,?,?,?)", (evt['sku'],evt['location'],evt['new_price'],evt['currency'],evt['ts']))
        conn.commit()
        print("applied:", evt)
    seen=len(lines)
    time.sleep(1)
