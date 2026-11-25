import json, os, subprocess, sys
V = '/tmp/claude-0/-home-user-Bouw-marketing-/ae718e48-3374-5ea4-b0dc-c539d41ea878/scratchpad/vid'
OUTD = sys.argv[1]
os.makedirs(OUTD, exist_ok=True)
END = 3.2
NAMES = {'cumplimiento-es': 'BOUW-auditoria-BPM-hoy-vs-con-BOUW', 'excel-es': 'BOUW-automatizacion-cierre-de-mes-Excel',
         'compliance-en': 'BOUW-GMP-audit-today-vs-with-BOUW', 'excel-en': 'BOUW-month-end-close-automation-Excel'}
for k in sys.argv[2:]:
    d = f'{V}/build/{k}'
    c = json.load(open(f'{d}/cfg.json'))
    T = c['trim']; D = T + END
    vx, vy, vw, vh = c['box']
    inp = ['-i', f'{V}/in/{c["src"]}.mp4']
    img = lambda p: ['-loop', '1', '-framerate', '30', '-t', f'{D}', '-i', p]
    inp += img(f'{d}/bg.png') + img(f'{d}/mask.png')
    caps = sorted([f for f in os.listdir(d) if f.startswith('cap') and f.endswith('.png')])
    for f in caps:
        inp += img(f'{d}/{f}')
    inp += img(f'{d}/end.png') + img(f'{d}/bar.png')
    inp += ['-f', 'lavfi', '-t', f'{D}', '-i', 'anullsrc=r=48000:cl=stereo']
    n = len(caps)
    iend, ibar, iaud = 3 + n, 4 + n, 5 + n
    crop = f'crop={c["crop"][0]}:{c["crop"][1]}:{c["crop"][2]}:{c["crop"][3]},' if c['crop'] else ''
    fc = [f'[0:v]trim=0:{T},setpts=PTS-STARTPTS,fps=30,{crop}scale={vw}:{vh}:flags=lanczos,eq=contrast=1.04:saturation=1.05,'
          f'tpad=stop_mode=clone:stop_duration={END + 0.5},trim=0:{D},format=yuva420p[v]',
          '[2:v]format=gray[m]', '[v][m]alphamerge[vr]',
          '[1:v]format=rgba,split[bg][bgs]', f'[bg][vr]overlay={vx}:{vy}:shortest=1[c0]']
    for i, (a, b, *_rest) in enumerate(c['caps']):
        fa = 0 if a == 0 else 0.4
        fade_in = f'fade=t=in:st={a}:d=0.4:alpha=1,' if a > 0 else ''
        fc.append(f'[{3 + i}:v]format=rgba,{fade_in}fade=t=out:st={b - 0.35}:d=0.35:alpha=1[k{i}]')
        fc.append(f'[c{i}][k{i}]overlay=0:0[c{i + 1}]')
    fc.append(f'[{ibar}:v]format=rgba[bar]')
    fc.append(f"[c{n}][bar]overlay=x='72-936+936*min(t/{T}\\,1)':y=1219[cb]")
    fc.append('[bgs]crop=72:12:0:1214[sl]')
    fc.append('[cb][sl]overlay=0:1214[cc]')
    fc.append(f'[{iend}:v]format=rgba,fade=t=in:st={T - 0.15}:d=0.5:alpha=1[e]')
    fc.append('[cc][e]overlay=0:0,format=yuv420p[out]')
    out = f'{OUTD}/{NAMES[k]}-1080x1350.mp4'
    cmd = ['ffmpeg', '-v', 'error', '-y'] + inp + ['-filter_complex', ';'.join(fc), '-map', '[out]', '-map', f'{iaud}:a',
           '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-profile:v', 'high', '-r', '30', '-c:a', 'aac', '-b:a', '128k',
           '-t', f'{D}', '-movflags', '+faststart', out]
    subprocess.run(cmd, check=True)
    print('ok', out)
