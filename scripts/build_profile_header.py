from pathlib import Path
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
import re,math,subprocess,tempfile
import os
os.chdir(Path(__file__).resolve().parents[1])
source=Path('assets/profile-studio/hello.svg').read_text()
source=re.sub(r'<animateTransform[^>]*/>','',source)
folder=Path(tempfile.mkdtemp(prefix='profile-frames-'))
def frame(i):
 phase=2*math.pi*i/18
 s=source.replace('<g transform="translate(950 270)"><g>',f'<g transform="translate(950 {270+6*math.sin(phase):.2f})"><g transform="rotate({8*math.sin(phase):.2f})">')
 s=s.replace('<g transform="translate(687 129)"><g>',f'<g transform="translate(687 129)"><g transform="rotate({i*5})">')
 p=folder/f'{i:02d}.svg';p.write_text(s)
 subprocess.run(['inkscape',str(p),'--export-width=900','--export-filename='+str(p.with_suffix('.png'))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 return p.with_suffix('.png')
with ThreadPoolExecutor(max_workers=3) as pool: paths=list(pool.map(frame,range(18)))
frames=[]
for p in paths:
 im=Image.open(p).convert('RGB')
 if not frames: palette=im.quantize(colors=96)
 frames.append(im.quantize(palette=palette,dither=Image.Dither.NONE))
frames[0].save('assets/profile-studio/hello.gif',save_all=True,append_images=frames[1:],duration=220,loop=0,optimize=True)
print('Animated header:',Path('assets/profile-studio/hello.gif').stat().st_size,'bytes;',len(frames),'frames')
