python -c "f=open('file.html','r',encoding='utf-8');t=f.read();f=open('rfile.html','w',encoding='utf-8');f.write(t.replace('<math>','<code>').replace('</math>', '</code>'))"
pandoc rfile.html --to markdown-bracketed_spans+hard_line_breaks -o out.md --wrap=none

python -c "import re;f=open('out.md','r',encoding='utf-8');t=f.read();f=open('out.md','w',encoding='utf-8'); t=t.replace('`', ' $ ').replace('\\mathrm','\\rm').replace('---', chr(8212)).replace('</span>', '**');t=re.sub(r'<span .*?>', '**', t); t=re.sub(r'\\overline\\rm{(.*?)}', r'\\rm{\\overline{''\\1}}', t); t=re.sub(r'\\overline\\rm (.)', r'\\rm{\\overline ''\\1}', t);f.write(t)"
rm rfile.html