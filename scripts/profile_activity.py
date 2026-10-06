"""Render a dated public GitHub activity card; never invent unavailable metrics."""
from __future__ import annotations
import datetime as dt
import html
import json
import os
from pathlib import Path
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/motion/activity.svg'
QUERY='''query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}} repositories(privacy:PUBLIC,first:100,ownerAffiliations:OWNER,orderBy:{field:PUSHED_AT,direction:DESC}){totalCount nodes{name pushedAt primaryLanguage{name} isFork}}}}'''

def streaks(days,today):
    days=sorted((dt.date.fromisoformat(x['date']),int(x['contributionCount'])) for x in days if dt.date.fromisoformat(x['date'])<=today)
    longest=run=0;previous=None
    for date,count in days:
        run=(run+1 if previous and (date-previous).days==1 else 1) if count else 0
        longest=max(longest,run);previous=date
    counts=dict(days);cursor=today if counts.get(today,0) else today-dt.timedelta(days=1);current=0
    while counts.get(cursor,0):
        current+=1;cursor-=dt.timedelta(days=1)
    return current,longest

def text(x,y,value,size=16,color='#eef3ff',font='Arial,sans-serif'):
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{color}">{html.escape(str(value))}</text>'

def render(user,now):
    cal=user['contributionsCollection']['contributionCalendar'];days=[d for w in cal['weeks'] for d in w['contributionDays']]
    current,longest=streaks(days,now.date());repos=user['repositories'];nodes=repos['nodes']
    body=text(35,37,'PUBLIC WORK / LAST 12 MONTHS',13,'#a0b0cb','monospace')+text(35,62,'Updated '+now.strftime('%Y-%m-%d %H:%M UTC'),11,'#a0b0cb','monospace')
    for i,(v,label) in enumerate([(cal['totalContributions'],'CONTRIBUTIONS'),(current,'CURRENT STREAK / DAYS'),(longest,'LONGEST STREAK / DAYS'),(repos['totalCount'],'PUBLIC REPOSITORIES')]):
        x=35+i*290;body+=text(x,125,f'{v:,}',45,'#71c8ff','Arial,sans-serif')+text(x,157,label,11,'#a0b0cb','monospace')
    body+='<line x1="35" y1="183" x2="1165" y2="183" stroke="#253454"/>'
    colors=['#18253d','#2e4689','#4869b5','#628cd7','#8bc8ff']
    for wi,w in enumerate(cal['weeks']):
        for d in w['contributionDays']:
            date=dt.date.fromisoformat(d['date']);count=int(d['contributionCount']);level=0 if not count else 1 if count<3 else 2 if count<6 else 3 if count<10 else 4
            body+=f'<rect x="{35+wi*21}" y="{214+((date.weekday()+1)%7)*17}" width="16" height="13" rx="2" fill="{colors[level]}"><title>{date}: {count} contributions</title></rect>'
    langs=[]
    for r in nodes:
        lang=(r.get('primaryLanguage') or {}).get('name')
        if lang and lang not in langs:langs.append(lang)
    body+=text(35,366,'Recent public repo languages: '+(', '.join(langs[:8]) or 'Not yet available'),14)
    recent=[r['name'] for r in nodes if r.get('pushedAt')][:3]
    body+=text(35,395,'Recently active: '+(' · '.join(recent) or 'Not yet available'),12,'#a0b0cb')
    body+=text(35,428,'Streaks use contribution-calendar dates within this 12-month window. Public data only.',11,'#a0b0cb')
    return '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="455" viewBox="0 0 1200 455" role="img"><title>Daily GitHub public activity snapshot</title><rect width="1200" height="455" rx="12" fill="#0c1327"/>'+body+'</svg>'

def main():
    token=os.environ['GITHUB_TOKEN'];login=os.environ.get('PROFILE_LOGIN','emmanuelacheampong0')
    request=urllib.request.Request('https://api.github.com/graphql',data=json.dumps({'query':QUERY,'variables':{'login':login}}).encode(),headers={'Authorization':'Bearer '+token,'Content-Type':'application/json','User-Agent':'Emmanuel-Profile-Activity'})
    with urllib.request.urlopen(request,timeout=30) as response:result=json.load(response)
    if result.get('errors') or not (result.get('data') or {}).get('user'):raise RuntimeError('GitHub did not return complete activity data; existing card was preserved.')
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(render(result['data']['user'],dt.datetime.now(dt.timezone.utc)))
    print('Updated public activity card.')
if __name__=='__main__':main()
