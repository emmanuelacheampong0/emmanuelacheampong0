"""Generate original terminal-style artwork and interest labels for the profile."""
from pathlib import Path
from html import escape
from PIL import Image,ImageDraw,ImageFont
import math
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'assets/profile-terminal';OUT.mkdir(parents=True,exist_ok=True)
BG='#0d1117';FG='#e6edf3';BLUE='#58b9ff';GRAY='#98a6b6';LINE='#263240'
def txt(x,y,s,size=20,color=FG,weight=400,extra=''):
 return f'<text x="{x}" y="{y}" font-family="DejaVu Sans Mono, monospace" font-size="{size}" font-weight="{weight}" fill="{color}" {extra}>{escape(s)}</text>'
def save(name,w,h,b,title):
 (OUT/(name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{escape(title)}</title><rect width="{w}" height="{h}" rx="8" fill="{BG}"/>'+b+'</svg>')
sections=[('philosophy','01','Build to understand.','CURIOSITY → EXPERIMENT → SOMETHING USEFUL'),('work','02','Selected builds','PLAY / EXPLORE / READ THE CODE'),('design','03','Design with a point of view','VISUAL STORYTELLING / PRODUCT / CULTURE'),('research','04','Questions in progress','AI / PRODUCT / HUMAN-CENTERED TECHNOLOGY'),('learning','05','Always learning. Always building.','FOUNDATIONS TODAY. BETTER SYSTEMS TOMORROW.'),('principles','06','How I approach the work','CURIOSITY / CLARITY / CARE'),('community','07','Built with people','COMMUNITY / COLLABORATION / LEADERSHIP'),('notebook','08','Free Read Code','OPEN THE SOURCE. FOLLOW THE QUESTION.'),('activity','09','The public lab, in motion','PUBLIC CONTRIBUTIONS / DATED SNAPSHOT'),('connect','10','Let’s build something useful','SOFTWARE / PRODUCT / DESIGN / RESEARCH')]
for name,num,title,sub in sections:
 b=f'<rect x="0" y="0" width="5" height="145" fill="{BLUE}"/>'+txt(30,35,num+' / '+sub,12,GRAY)+txt(29,98,title,39,FG,700)+f'<path d="M30 119H1170" stroke="{LINE}"/>'
 save('section-'+name,1200,145,b,title)
# Segmented labels echo the supplied reference while describing Emmanuel's interests.
badges=[('software','BUILDING','SOFTWARE ENGINEERING','#238636',660),('ai','EXPLORING','AI / MACHINE LEARNING','#0969da',670),('product','PRODUCT','MANAGEMENT + DESIGN','#bd561d',650),('design','CREATIVE','UI/UX + VISUAL DESIGN','#8957e5',670),('scholars','ELON','ODYSSEY + RENAISSANCE SCHOLAR','#b52b3b',840)]
for name,left,right,color,w in badges:
 split=200 if name!='scholars' else 145
 b=f'<rect width="{split}" height="58" fill="#343c47"/><rect x="{split}" width="{w-split}" height="58" fill="{color}"/>'+txt(split/2,37,left,19,FG,400,'text-anchor="middle" letter-spacing="1"')+txt(split+(w-split)/2,37,right,20,'#ffffff',700,'text-anchor="middle" letter-spacing=".7"')
 save('badge-'+name,w,58,b,left+': '+right)
for name,label in [('play','PLAY GAME ↗'),('explore','EXPLORE ↗'),('research','READ RESEARCH ↗'),('prototype','TRY PROTOTYPE ↗'),('linkedin','LINKEDIN ↗'),('email','SAY HELLO ↗'),('github','FOLLOW ON GITHUB ↗'),('portfolio','OPEN INTERACTIVE PORTFOLIO ↗')]:
 b=f'<rect x="1" y="1" width="318" height="56" rx="6" fill="#132336" stroke="#397faf"/>'+txt(160,36,label,15,BLUE,700,'text-anchor="middle"')
 save(name,320,58,b,label)
for name,num,title,subtitle,tokens,color in [('roshambo','01','ROSHAMBO','Small game. Big learning.',['R','P','S'],'#53d391'),('neddle','02','NEDDLE','Five letters. One more try.',list('BUILD'),'#58b9ff'),('budget','03','QUESTION THE AI','Evidence. Limits. Reflection.',['?','→','!'],'#e4af71'),('compound','04','HOW SURE IS IT?','Uncertainty in drug discovery.',['C','—','N'],'#bf9bff')]:
 b=txt(27,35,num+' / OPEN LAB',12,GRAY)+txt(25,101,title,42,FG,700)+txt(28,143,subtitle,19,color)
 for i,ch in enumerate(tokens):
  x=35+i*(530/len(tokens));w=490/len(tokens)
  b+=f'<rect x="{x}" y="185" width="{w}" height="91" rx="5" fill="#152536" stroke="{color}"/>'+txt(x+w/2,247,ch,43,color,700,'text-anchor="middle"')
 b+=txt(29,316,'CODE / CURIOSITY / HUMAN CONTEXT',11,GRAY)
 save(name,600,345,b,title+'. '+subtitle)
b=''
for i,(a,m,sub) in enumerate([('ENGINEERING','Python · HTML · Git','Functions, tests, modularity'),('PRODUCT','Discovery · metrics','Needs, priorities, experiments'),('DESIGN','Figma · UI/UX','Flows, hierarchy, accessibility'),('RESEARCH','Questions · methods','Literature, evidence, evaluation'),('CREATIVE','Adobe Creative Cloud','Visual storytelling and identity'),('DEVELOPMENT','VS Code · GitHub','Build, debug and document')]):
 x=30+i%3*400;y=20+i//3*150;b+=txt(x,y+25,a,12,BLUE,700)+txt(x,y+65,m,20,FG,700)+txt(x,y+102,sub,12,GRAY)
b+='<path d="M1120 195l-25 21-15-12-7 6 16 15-16 15 7 6 15-12 25 21 12-5v-51zm0 17v26l-16-13z" fill="#007ACC"/>'
save('toolkit',1200,330,b,'Engineering, product, design, research, creative and development tools in use or being learned.')
b=txt(36,55,'> Building with curiosity.',35,FG,700)+txt(36,110,'> Building with people in mind.',35,BLUE,700)+txt(39,162,'THANKS FOR VISITING / EMMANUEL SEFAH ACHEAMPONG',12,GRAY)
save('footer',1200,195,b,'Building with curiosity. Building with people in mind. Thanks for visiting.')
# Original code-drawn moving field and typing line, rendered as a GitHub-safe GIF.
fontroot='/usr/share/fonts/truetype/dejavu/'
fonts={k:ImageFont.truetype(fontroot+f,size) for k,f,size in [('name','DejaVuSansMono-Bold.ttf',67),('tag','DejaVuSansMono.ttf',12),('line','DejaVuSansMono.ttf',19),('small','DejaVuSansMono.ttf',14)]}
frames=[];phrase='I’m building what I learned two minutes ago.'
for i in range(26):
 im=Image.new('RGB',(1000,410),BG);d=ImageDraw.Draw(im)
 for row in range(15):
  points=[]
  for x in range(620,1010,6):
   y=92+row*13+18*math.sin(x/85+i*.14+row*.16);points.append((x,y))
  d.line(points,fill=(25+row,55+row*2,82+row*3),width=1)
 d.rounded_rectangle((20,18,980,392),radius=10,outline=LINE,width=1)
 for j,c in enumerate(['#f17f79','#eabf64','#68c99a']):d.ellipse((40+j*18,35,47+j*18,42),fill=c)
 d.text((108,32),'EMMANUEL / LEARNING IN PUBLIC',font=fonts['tag'],fill=GRAY)
 d.text((40,81),'EMMANUEL',font=fonts['name'],fill=FG)
 d.text((40,157),'ACHEAMPONG',font=fonts['name'],fill=BLUE)
 d.text((44,257),'Computer Science @ Elon University',font=fonts['line'],fill=FG)
 d.text((44,289),'Design enthusiast · Builder · Product thinker',font=fonts['small'],fill=GRAY)
 shown=phrase[:min(len(phrase),i*4)]
 d.text((44,346),'> '+shown+(' ▌' if i%4<2 else ''),font=fonts['line'],fill='#70d69b')
 if i==0:palette=im.quantize(colors=64)
 frames.append(im.quantize(palette=palette,dither=Image.Dither.NONE))
frames[0].save(OUT/'hello.gif',save_all=True,append_images=frames[1:],duration=[130]*25+[1800],loop=0,optimize=True)
frames[-1].convert('RGB').save(OUT/'hello-preview.png')
print('Created',len(list(OUT.iterdir())),'assets; GIF', (OUT/'hello.gif').stat().st_size,'bytes')
