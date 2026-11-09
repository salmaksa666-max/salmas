import re,html,json,subprocess,time
posts={}
before=None
while True:
    url="https://t.me/s/AlhomraniUpdates"+(f"?before={before}" if before else "")
    s=subprocess.run(["curl","-sS","-m","40",url],capture_output=True,text=True).stdout
    chunks=re.split(r'(?=<div class="tgme_widget_message_wrap)',s)[1:]
    if not chunks: print("empty",before); break
    ids=[]
    for p in chunks:
        m=re.search(r'data-post="AlhomraniUpdates/(\d+)"',p)
        if not m: continue
        pid=int(m.group(1)); ids.append(pid)
        t=re.search(r'<time datetime="([^"]+)"',p)
        def txt(rx):
            mm=re.search(rx,p,re.S)
            if not mm: return ""
            return html.unescape(re.sub(r'<[^>]+>','',re.sub(r'<br\s*/?>','\n',mm.group(1)))).strip()
        body=txt(r'<div class="tgme_widget_message_text js-message_text[^"]*"[^>]*>(.*?)</div>')
        reply=txt(r'<a class="tgme_widget_message_reply"[^>]*>(.*?)</a>')
        rid=re.search(r'<a class="tgme_widget_message_reply"[^>]*href="https://t.me/AlhomraniUpdates/(\d+)"',p)
        photos=[u for u in re.findall(r"tgme_widget_message_photo_wrap[^>]*background-image:url\('([^']+)'\)",p)]
        docs=re.findall(r'tgme_widget_message_document_title[^>]*>(.*?)<',p)
        posts[pid]=dict(id=pid,date=t.group(1) if t else "",text=body,reply=reply,reply_id=int(rid.group(1)) if rid else None,photos=photos,docs=docs)
    if not ids: break
    mn=min(ids)
    d=posts[mn]["date"]
    print(mn,d,len(posts),flush=True)
    if d and d<"2026-08-31": break
    before=mn
    time.sleep(0.6)
json.dump(posts,open("posts.json","w"),ensure_ascii=False)
