import re,json,sys
def pages(fn):
    return open(fn,encoding="utf-8").read().split("\f")
HDR=re.compile(r"^\s*(https?://t\.me/\S+.*|10[–-]14 November.*)$")
def norm(t):return re.sub(r"[^a-z0-9]+"," ",t.lower()).strip()
out=[];stat={"pages":0,"noq":0,"noopt":0,"noans":0}
for part,fn in (("P1","p1.txt"),("P2","p2.txt")):
    for pi,pg in enumerate(pages(fn),1):
        lines=[l.rstrip() for l in pg.splitlines() if not HDR.match(l)]
        stat["pages"]+=1
        # blocks separated by blank lines
        blocks=[];cur=[]
        for l in lines:
            if l.strip():cur.append(l.strip())
            elif cur:blocks.append(cur);cur=[]
        if cur:blocks.append(cur)
        if not blocks or not re.match(r"^\d+\.\s",blocks[0][0]):stat["noq"]+=1;continue
        # stem = blocks up to and including the one ending with '?'
        k=None
        for i,b in enumerate(blocks[:4]):
            if b[-1].rstrip().endswith("?"):k=i;break
        if k is None or k+1>=len(blocks):stat["noopt"]+=1;continue
        stem=" ".join(" ".join(b) for b in blocks[:k+1])
        stem=re.sub(r"^\d+\.\s*","",stem)
        opts=blocks[k+1]
        if len(opts)<2 or len(opts)>7:stat["noopt"]+=1;continue
        ans=None
        for b in blocks[k+2:k+6]:
            nb=norm(" ".join(b))
            for j,o in enumerate(opts):
                no=norm(o)
                if no and (nb==no or nb.startswith(no+" ") and len(b)==1):ans=j;break
            if ans is not None:break
        if ans is None:stat["noans"]+=1
        out.append(dict(part=part,page=pi,stem=stem,opts=opts,ans=ans,raw=[" ".join(b) for b in blocks[k+2:]][:4]))
print(stat,len(out),"with answer:",sum(1 for o in out if o["ans"] is not None))
json.dump(out,open("parsed.json","w"),ensure_ascii=False)
for o in out[:6]:print(o["page"],o["stem"][:90],"|",o["opts"],"|",o["ans"])
