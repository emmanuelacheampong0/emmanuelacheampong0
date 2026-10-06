from pathlib import Path
from html import escape as e
P=Path(__file__).resolve().parents[1]/'assets/motion';P.mkdir(parents=True,exist_ok=True)
ink='#eef3ff'; muted='#a0b0cb';paper='#0c1327';accent='#71c8ff';olive='#8c8bff';line='#253454'
def svg(name,w,h,body,title):
 P.joinpath(name+'.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{e(title)}</title><rect width="{w}" height="{h}" rx="12" fill="{paper}"/>'+body+'</svg>')
def t(x,y,text,size=16,color=ink,font='Arial,sans-serif',extra=''):
 return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{color}" {extra}>{e(text)}</text>'
body=f'<path d="M24 0h270" stroke="{accent}" stroke-width="6"/>'
body+=t(52,54,'EA / THE PUBLIC LAB',16,muted,'monospace')+t(52,112,'Hello, I’m',36,ink,'Arial,sans-serif')+t(48,189,'Emmanuel',76,ink,'Arial,sans-serif')+t(48,266,'Acheampong.',76,accent,'Arial,sans-serif', 'font-weight="700"')
body+=t(52,316,'Computer Science @ Elon University',23)+t(52,352,'Student. Builder. Design enthusiast. Product thinker.',17,muted)+t(52,421,'BUILDING WITH CURIOSITY.',13,olive,'monospace')+t(52,445,'BUILDING WITH PEOPLE IN MIND.',13,olive,'monospace')
body+=f'<rect x="755" y="52" width="393" height="370" rx="6" fill="#182441" stroke="{line}"/><circle cx="953" cy="208" r="109" fill="none" stroke="#4960a2"/><ellipse cx="953" cy="208" rx="66" ry="128" transform="rotate(35 953 208)" fill="none" stroke="#4960a2" stroke-dasharray="4 5"/><circle cx="1030" cy="132" r="8" fill="{accent}"/><path d="M856 189l-19 19 19 19m194-38l19 19-19 19" fill="none" stroke="{olive}" stroke-width="3"/>'
body+=t(786,86,'curiosity.py',12,muted,'monospace')+t(894,216,'make()',24,ink,'monospace')+f'<rect x="778" y="307" width="347" height="85" rx="4" fill="#14213d" stroke="{line}"/>'
body+=t(798,337,'notice → understand → build',16)+t(798,365,'test → reflect → improve',14,muted,'monospace')
svg('cover',1200,480,body,'Hello, I’m Emmanuel Acheampong. Computer Science at Elon University. Student, builder, design enthusiast and product thinker.')
for name,label in [('play','PLAY GAME →'),('explore','EXPLORE →'),('research','READ RESEARCH →'),('prototype','TRY PROTOTYPE →'),('linkedin','LINKEDIN ↗'),('email','SAY HELLO ↗'),('github','FOLLOW ON GITHUB ↗')]:
 svg(name,230,54,f'<rect x="1" y="1" width="228" height="52" rx="5" fill="{ink}"/>'+t(115,33,label,13,'#0c1327','monospace','text-anchor="middle"'),label)
for name,num,title,subtitle in [('philosophy','01','Build to understand.','Curiosity is a practice, not a personality badge.'),('work','02','Small builds. Real questions.','Code, play, product thinking and visual storytelling.'),('design','03','A technical mind. A designer’s eye.','Selected visual work from my own projects.'),('research','04','Questions worth staying with.','An emerging undergraduate research workspace.'),('learning','05','Always learning and building.','The subject matters. So does the reason.'),('principles','06','How I try to work.','Care, curiosity, clarity and useful things.'),('community','07','Learning happens with people.','University, community, creative work and collaboration.'),('notebook','08','Free Read Code.','Open source, open notes, unfinished questions.'),('activity','09','The lab, in motion.','A daily snapshot of public GitHub activity.'),('connect','10','Let’s build something thoughtful.','Open to teams that learn, question and make.')]:
 b=f'<line x1="0" y1="1" x2="1200" y2="1" stroke="{line}"/>'+t(8,50,num,15,accent,'monospace')+t(70,57,title,35,ink,'Arial,sans-serif')+t(70,90,subtitle,16,muted)
 svg('section-'+name,1200,115,b,title+' '+subtitle)
b=t(32,34,'ROSHAMBO / PYTHON → PLAY',12,muted,'monospace')
for x,l,label in [(110,'R','ROCK'),(300,'P','PAPER'),(490,'S','SCISSORS')]:
 b+=f'<circle cx="{x}" cy="131" r="59" fill="#14213d" stroke="{line}"/>'+t(x,150,l,50,accent,'Arial,sans-serif','text-anchor="middle"')+t(x,225,label,12,muted,'monospace','text-anchor="middle"')
svg('roshambo',600,265,b,'Roshambo: Rock, Paper, Scissors. Python foundations, browser playable.')
b=t(32,34,'NEDDLE / SIX TRIES. FIVE LETTERS.',12,muted,'monospace')
for row,word in enumerate(['BUILD','LEARN']):
 for col,c in enumerate(word):
  x=113+col*76;y=59+row*81;color=olive if row==0 and col in (0,3) else '#4270c6' if row==0 and col==2 else '#253454'
  b+=f'<rect x="{x}" y="{y}" width="65" height="68" rx="4" fill="{color}"/>'+t(x+32,y+46,c,30,'#14213d' if row==0 else ink,'monospace','text-anchor="middle"')
b+=t(300,244,'a little word puzzle; a lot of careful logic',12,muted,'monospace','text-anchor="middle"');svg('neddle',600,265,b,'Neddle, a six-attempt word game with duplicate-letter-aware feedback.')
b=t(32,34,'FORMA / AI INTERFACE STUDY',12,muted,'monospace')+f'<rect x="32" y="58" width="536" height="177" rx="5" fill="#14213d" stroke="{line}"/>'+t(53,91,'Good advice leaves room to think.',24,ink,'Arial,sans-serif')
for x,title,sub in [(53,'EVIDENCE','What supports it?'),(231,'LIMITS','What is missing?'),(409,'REFLECTION','Would I accept it?')]:
 b+=f'<line x1="{x}" y1="118" x2="{x+135}" y2="118" stroke="{accent}" stroke-width="2"/>'+t(x,151,title,11,olive,'monospace')+t(x,181,sub,14)
b+=t(53,213,'Fictional prototype · proposal · no study results',11,muted,'monospace');svg('budget',600,265,b,'Explainable AI budgeting prototype: evidence, limits and reflection. Research proposal, no study results.')
b=t(32,34,'AI × DRUG DISCOVERY / RESEARCH BRIEF',12,muted,'monospace')
pts=[(105,132),(170,94),(235,132),(235,207),(170,242),(105,207)]
b+='<path d="M105 132L170 94 235 132 235 207 170 242 105 207Z" fill="none" stroke="#969e8b" stroke-width="3"/>'
for x,y in pts:b+=f'<circle cx="{x}" cy="{y}" r="8" fill="{olive}"/>'
b+=t(298,108,'Which prediction',26,ink,'Arial,sans-serif')+t(298,142,'deserves confidence?',26,accent,'Arial,sans-serif')+t(298,185,'Scaffold-aware evaluation.',14,muted)+t(298,214,'Uncertainty-aware decisions.',14,muted);svg('compound',600,275,b,'A proposed computational study of uncertainty-aware compound prioritization, no models or results claimed.')
b=''
for i,(title,main,sub) in enumerate([('ENGINEERING','Python · HTML','Functions, tests, Git'),('PRODUCT','Discovery · metrics','Needs before features'),('DESIGN','Figma · UI/UX','Flows, clarity, access'),('RESEARCH','Questions · methods','Literature, evidence'),('CREATIVE','Adobe Creative Cloud','Visual storytelling'),('DEVELOPMENT','VS Code · GitHub','Build, debug, document')]):
 x=25+(i%3)*400;y=20+(i//3)*145
 b+=t(x,y+25,title,12,accent,'monospace')+t(x,y+65,main,21)+t(x,y+98,sub,14,muted)
# recognizable VS Code mark beside development tools
b+='<path d="M1075 170l-37 31-22-17-9 7 23 21-23 21 9 7 22-17 37 31 16-7v-70zm0 22v40l-24-20z" fill="#007ACC"/>'
svg('toolkit',1200,300,b,'Toolkit organized into Engineering, Product, Design, Research, Creative and Development. Python, HTML, Figma, Adobe Creative Cloud, VS Code and GitHub. Learning and project use.')
svg('footer',1200,145,t(600,58,'Building with curiosity. Building with people in mind.',30,ink,'Arial,sans-serif','text-anchor="middle"')+t(600,101,'THANKS FOR VISITING / EMMANUEL SEFAH ACHEAMPONG',13,accent,'monospace','text-anchor="middle"'),'Building with curiosity. Building with people in mind. Thanks for visiting.')
print('Created',len(list(P.glob('*.svg'))),'custom SVG assets')
# The animated artwork below is drawn from mathematical paths and type, not edited photographs.
from PIL import Image,ImageDraw,ImageFont
import math
S=2;W=1200;H=390
fonts={n:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+name,size*S) for n,name,size in [('name','DejaVuSans-Bold.ttf',73),('label','DejaVuSansMono.ttf',14),('subtitle','DejaVuSans.ttf',24),('small','DejaVuSans.ttf',18)]}
def drawtext(d,xy,s,font,c):d.text((xy[0]*S,xy[1]*S),s,font=fonts[font],fill=c)
frames=[]
for f in range(20):
 phase=f/20*math.tau;im=Image.new('RGB',(W*S,H*S),'#0c1327');d=ImageDraw.Draw(im)
 # a gently flowing field of contour lines, clear of the text
 for j in range(24):
  points=[]
  for x in range(694,1220,5):
   u=(x-694)/526;y=150+62*math.sin(u*math.tau*.78+phase+j*.10)+j*4.2+27*u
   points.append((x*S,y*S))
  color=(int(78+2*j),int(117+3*j),int(210+j))
  d.line(points,fill=color,width=2*S)
 # quiet motion across the lower wave bands
 for j,c in [(0,'#15224b'),(1,'#203674'),(2,'#365baa')]:
  pts=[(0,H*S)]
  for x in range(0,W+8,8):
   y=340+j*16+12*math.sin(x/220+phase+j*.7);pts.append((x*S,y*S))
  pts.append((W*S,H*S));d.polygon(pts,fill=c)
 drawtext(d,(48,34),'HELLO / I’M EMMANUEL SEFAH ACHEAMPONG','label','#a0b0cb')
 drawtext(d,(44,74),'Emmanuel','name','#f4f7ff')
 drawtext(d,(44,159),'Acheampong.','name','#83cfff')
 drawtext(d,(49,260),'Computer Science @ Elon University','subtitle','#edf2ff')
 drawtext(d,(49,306),'Builder  /  Design enthusiast  /  Always learning','small','#a0b0cb')
 drawtext(d,(797,52),'CODE × DESIGN × PEOPLE','label','#c2cff0')
 d.ellipse((1040*S,287*S,1048*S,295*S),fill='#80d2ff')
 im=im.resize((900,292),Image.Resampling.LANCZOS)
 if f==0: palette=im.quantize(colors=64,dither=Image.Dither.NONE)
 im=im.quantize(palette=palette,dither=Image.Dither.NONE);frames.append(im)
frames[0].save(P/'header.gif',save_all=True,append_images=frames[1:],duration=160,loop=0,optimize=True)
frames[0].convert('RGB').save(P/'header-still.png')
labels=['LEARN','BUILD','TEST','REFLECT','IMPROVE'];frames=[]
for f in range(30):
 im=Image.new('RGB',(1200,75),'#0c1327');d=ImageDraw.Draw(im);font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',18)
 for i,label in enumerate(labels):
  x=49+i*230;active=f//6==i
  if active:d.rounded_rectangle((x-14,15,x+155,57),radius=20,fill='#294da0')
  d.text((x,25),label,font=font,fill='#eff6ff' if active else '#9aaccf')
  if i<4:d.text((x+176,25),'→',font=font,fill='#718aba')
 frames.append(im)
frames[0].save(P/'process.gif',save_all=True,append_images=frames[1:],duration=100,loop=0,optimize=True)
# Gradient-backed section dividers unify the entire profile without repeating the cover.
section_names=['philosophy','work','design','research','learning','principles','community','notebook','activity','connect']
for idx,name in enumerate(section_names):
 path=P/('section-'+name+'.svg');s=path.read_text();s=s.replace('<rect width="1200" height="115" rx="12" fill="#0c1327"/>','<defs><linearGradient id="g"><stop stop-color="#11203c"/><stop offset="1" stop-color="#1d2451"/></linearGradient></defs><rect width="1200" height="115" rx="12" fill="url(#g)"/><path d="M1030 0Q910 95 1200 110M1090 0Q940 73 1200 77M1150 0Q1010 65 1200 44" fill="none" stroke="#6288db" opacity=".45"/>');path.write_text(s)
print('Header motion:',(P/'header.gif').stat().st_size,'bytes; process motion:',(P/'process.gif').stat().st_size)
