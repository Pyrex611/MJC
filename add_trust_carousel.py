# Run in the MJC & Co repo root:  python add_trust_carousel.py
# Inserts the dual trust carousel into index.html (after the stats strip in #about). Nothing else changes.
import re,sys
snip=open('trust-carousel-snippet.html',encoding='utf-8').read() if len(sys.argv)<2 else open(sys.argv[1],encoding='utf-8').read()
css=re.search(r'<style>(.*?)</style>',snip,re.S).group(1)
markup=snip.split('-->',1)[1].split('<script>',1)[0].strip()
js=re.search(r'<script>(.*?)</script>',snip,re.S).group(1)
s=open('index.html',encoding='utf-8').read()
assert 'trustCar' not in s,'already applied'
s=s.replace('</style>',css+'</style>',1)
anchor='<div class="stat-cell"><div class="n">ISA</div>'
i=s.index(anchor); j=s.index('</section>',i)
s=s[:j]+'<div class="wrap" style="margin-top:72px">\n'+markup+'\n    </div>\n  '+s[j:]
k=s.rindex('</script>'); s=s[:k]+js+'\n'+s[k:]
open('index.html','w',encoding='utf-8').write(s); print('done')
