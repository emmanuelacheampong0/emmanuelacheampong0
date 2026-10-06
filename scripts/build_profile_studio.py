"""Original GitHub-safe vector identity. No scripts, external fonts or tracking."""
from pathlib import Path
from html import escape
import math
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/profile-studio'
OUT.mkdir(parents=True,exist_ok=True)
INK='#191722'; PAPER='#ede9f7'; PURPLE='#7246d8'; ACID='#dfff79'; MUTED='#635c75'; PINK='#f3b8d4'
def text(x,y,value,size=20,color=INK,weight=400,extra=''):
 return f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}" {extra}>{escape(value)}</text>'
def star(x,y,r,color=PURPLE):
 return f'<g transform="translate({x} {y})"><g>'+''.join(f'<path d="M0 -{r}V{r}" stroke="{color}" stroke-width="{max(3,r/8)}" transform="rotate({a})"/>' for a in [0,45,90,135])+f'<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="30s" repeatCount="indefinite"/></g></g>'
def svg(name,w,h,body,title,bg=PAPER):
 out=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><defs><linearGradient id="gloss" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#fff8ff"/><stop offset=".25" stop-color="#dbbdf8"/><stop offset=".52" stop-color="#9f64e0"/><stop offset=".8" stop-color="#5326a7"/><stop offset="1" stop-color="#b8f0df"/></linearGradient></defs><rect width="{w}" height="{h}" rx="4" fill="{bg}"/>{body}</svg>'
 (OUT/(name+'.svg')).write_text(out)
 return out
b=text(46,45,'EMMANUEL SEFAH ACHEAMPONG  /  THE PUBLIC LAB',13,INK,700,extra='letter-spacing="2"')
b+=text(46,130,'Hello, I’m',43)+text(40,239,'Emmanuel.',112,INK,700,extra='letter-spacing="-7"')
b+=text(49,300,'A technical mind.',35,PURPLE)+text(49,345,'A designer’s eye.',35,PURPLE)
b+=text(49,420,'Computer Science @ Elon University',22)+text(49,456,'Design enthusiast  ×  Builder  ×  Product thinker',17,MUTED)
b+='<g transform="translate(950 270)"><g><ellipse rx="168" ry="142" fill="none" stroke="url(#gloss)" stroke-width="78" transform="rotate(-32)"/><ellipse rx="168" ry="142" fill="none" stroke="#ffffff" stroke-opacity=".35" stroke-width="2" transform="rotate(-32)"/><animateTransform attributeName="transform" type="rotate" values="-8;8;-8" dur="9s" repeatCount="indefinite"/></g></g>'
b+=star(687,129,41)+text(850,63,'CURIOSITY IN MOTION',12,MUTED,700,extra='letter-spacing="2"')
b+='<g transform="translate(762 403) rotate(-14)"><circle r="67" fill="'+ACID+'"/>'+text(0,-15,'ALWAYS',15,INK,700,'text-anchor="middle"')+text(0,7,'LEARNING',15,INK,700,'text-anchor="middle"')+text(0,34,'↗',27,INK,400,'text-anchor="middle"')+'</g>'
b+='<path d="M46 495H1154" stroke="#c9c2d8"/>'+text(46,525,'GHANAIAN PERSPECTIVE. ENDLESS ROOM TO EXPLORE.',11,MUTED,400,'letter-spacing="1.5"')+text(1154,525,'CODE / DESIGN / PEOPLE',11,MUTED,400,'text-anchor="end" letter-spacing="1.5"')
svg('hello',1200,550,b,'Hello, I’m Emmanuel Acheampong. A technical mind. A designer’s eye. Computer Science at Elon University. Design enthusiast, builder and product thinker.')
b=text(40,43,'LEARNING IN PUBLIC / ONE EXPERIMENT AT A TIME',12,ACID,700,'letter-spacing="2"')+text(38,101,'I’m building what I learned',44,'#f5f0ff',700)+text(38,158,'two minutes ago.',53,ACID,700)
b+=star(1070,111,52,PINK)
svg('two-minutes',1200,196,b,'I’m building what I learned two minutes ago.',INK)
sections=[('philosophy','01','Build to understand.','TAKE APART. QUESTION. FIX. REBUILD.'),('work','02','Made to be explored.','PLAYABLE GAMES / PRODUCT / CULTURE'),('design','03','Make it mean something.','A VISUAL MIND / SELECTED DESIGN WORK'),('research','04','What if we asked better?','RESEARCH LAB / QUESTIONS IN PROGRESS'),('learning','05','Always becoming.','WHAT I’M LEARNING / AND WHY'),('principles','06','Care goes into the code.','FIVE PRINCIPLES / A WORK IN PROGRESS'),('community','07','Better, with people.','COMMUNITY / LEADERSHIP / COLLABORATION'),('notebook','08','Free Read Code.','OPEN NOTES. OPEN SOURCE. OPEN QUESTIONS.'),('activity','09','The lab keeps moving.','A DATED SNAPSHOT / PUBLIC ACTIVITY'),('connect','10','Got a good question?','LET’S MAKE SOMETHING THOUGHTFUL.')]
for i,(name,n,title,sub) in enumerate(sections):
 bg=[PAPER,'#e1f3d5','#f8d6c5'][i%3]
 b=text(35,47,n,17,PURPLE,700)+text(103,48,sub,12,MUTED,700,'letter-spacing="1.5"')+text(100,112,title,48,INK,700,extra='letter-spacing="-2"')+star(1120,86,30)
 svg('section-'+name,1200,151,b,title+' '+sub,bg)
for name,label in [('play','PLAY GAME ↗'),('explore','EXPLORE ↗'),('research','READ RESEARCH ↗'),('prototype','TRY PROTOTYPE ↗'),('linkedin','LINKEDIN ↗'),('email','SAY HELLO ↗'),('github','FOLLOW ON GITHUB ↗'),('portfolio','ENTER THE PLAYGROUND ↗')]:
 svg(name,280,60,'<rect x="2" y="2" width="276" height="56" rx="28" fill="'+ACID+'"/>'+text(140,37,label,15,INK,700,'text-anchor="middle"'),label,INK)
b=text(30,36,'01 / ROSHAMBO',13,'#efe9f9',700,'letter-spacing="2"')+text(28,105,'Small game.',49,'#efe9f9',700)+text(28,161,'Big learning.',49,ACID,700)
for i,(x,y,c,ch) in enumerate([(116,256,ACID,'R'),(300,244,PINK,'P'),(484,256,PAPER,'S')]):
 b+=f'<g><circle cx="{x}" cy="{y}" r="58" fill="{c}"/>'+text(x,y+20,ch,61,INK,700,'text-anchor="middle"')+f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -{8+i*3};0 0" dur="{3+i*.5}s" repeatCount="indefinite"/></g>'
svg('roshambo',600,345,b,'Roshambo. Small game. Big learning. Click to play.',INK)
b=text(30,36,'02 / NEDDLE',13,INK,700,'letter-spacing="2"')+text(28,105,'Five letters.',49,INK,700)+text(28,161,'One more try.',49,PURPLE,700)
for i,c in enumerate('BUILD'):
 x=37+i*107;b+=f'<rect x="{x}" y="217" width="95" height="89" rx="8" fill="'+([PURPLE,INK,'#68805d',PURPLE,INK][i])+'"/>'+text(x+47,280,c,53,'#fff',700,'text-anchor="middle"')
svg('neddle',600,345,b,'Neddle. Five letters. One more try. Click to play.',ACID)
b=text(30,37,'RESEARCH PROTOTYPE / AI × FINTECH',12,INK,700)+text(28,106,'Good advice',47,INK,700)+text(28,160,'invites questions.',47,PURPLE,700)
for x,label in [(30,'EVIDENCE'),(219,'LIMITS'),(407,'REFLECTION')]:
 b+=f'<path d="M{x} 205h158" stroke="{INK}" stroke-width="2"/>'+text(x,236,label,13,INK,700)
b+=text(30,304,'Fictional scenarios. No study results.',14,MUTED)
svg('budget',600,345,b,'AI budgeting interface study. Evidence, limits and reflection. Proposal and fictional prototype.',PAPER)
b=text(30,37,'RESEARCH BRIEF / AI × DRUG DISCOVERY',12,INK,700)+text(28,106,'How sure',52,INK,700)+text(28,162,'is the model?',52,PURPLE,700)
b+='<g fill="none" stroke="#7246d8" stroke-width="2"><path d="M50 253L96 225 144 253 190 225 238 253 284 225"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="{PINK}"/>' for x,y in [(50,253),(96,225),(144,253),(190,225),(238,253),(284,225)])+'</g>'
b+=text(30,313,'Public-data benchmark proposal. No model results.',14,MUTED)
svg('compound',600,345,b,'Uncertainty-aware compound prioritization. Public-data benchmark proposal, no models or results.', '#f8d6c5')
b=''
for i,(title,main,sub) in enumerate([('ENGINEERING','Python · HTML · Git','Functions, testing, modularity'),('PRODUCT','Discovery · metrics','User needs, prioritization'),('DESIGN','Figma · UI/UX','Prototypes, flows, accessibility'),('RESEARCH','Questions · methods','Literature, evidence, evaluation'),('CREATIVE','Adobe Creative Cloud','Visual storytelling, brand systems'),('DEVELOPMENT','VS Code · GitHub','Build, debug, document')]):
 x=35+(i%3)*400;y=20+(i//3)*150
 b+=text(x,y+27,title,12,PURPLE,700,'letter-spacing="1.5"')+text(x,y+70,main,22,INK,700)+text(x,y+103,sub,14,MUTED)
b+='<path d="M1120 195l-25 21-15-12-7 6 16 15-16 15 7 6 15-12 25 21 12-5v-51zm0 17v26l-16-13z" fill="#007ACC"/>'
svg('toolkit',1200,330,b,'Toolkit: Engineering, Product, Design, Research, Creative and Development. Tools in use or being learned.')
b=text(42,75,'Building with curiosity.',46,INK,700)+text(42,133,'Building with people in mind.',46,PURPLE,700)+text(44,193,'THANKS FOR VISITING / EMMANUEL SEFAH ACHEAMPONG',12,MUTED,700,'letter-spacing="1.5"')+star(1091,109,57)
svg('footer',1200,230,b,'Building with curiosity. Building with people in mind. Thanks for visiting.',ACID)
print('Created',len(list(OUT.glob('*.svg'))),'GitHub-safe SVG assets')
