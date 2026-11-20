#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Instalador del parche de traducción al español (España) de Super Robot Wars V (Steam).
Uso:
    python instalar_parche.py "D:\\Juegos\\Super Robot Wars V"            # instalar
    python instalar_parche.py "D:\\Juegos\\Super Robot Wars V" --restaurar # volver al original
Antes de tocar nada hace copia de cada fichero en <juego>/_backup_traduccion_es/.
Si algún fichero no coincide con el original de Steam, lo salta y te lo dice."""
import os,sys,json,hashlib,shutil,subprocess,tempfile
AQUI=os.path.dirname(os.path.abspath(__file__))
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(1<<22),b''): h.update(c)
    return h.hexdigest()
def get_zstd():
    try:
        import zstandard; return zstandard
    except ImportError:
        print('Instalando el módulo "zstandard" (pip)...')
        try: subprocess.check_call([sys.executable,'-m','pip','install','--user','zstandard'])
        except Exception: pass
        try:
            import zstandard; return zstandard
        except ImportError: return None
def aplicar(zs,orig_path,patch_path,out_path):
    patch=open(patch_path,'rb').read()
    if orig_path is None:
        data=zs.ZstdDecompressor().decompress(patch,max_output_size=1<<31) if zs else None
    else:
        o=open(orig_path,'rb').read()
        d=zs.ZstdDecompressor(dict_data=zs.ZstdCompressionDict(o,dict_type=zs.DICT_TYPE_RAWCONTENT),max_window_size=2**31)
        data=d.decompress(patch,max_output_size=max(len(o)*2,1<<28))
    with open(out_path,'wb') as f: f.write(data)
def main():
    args=[a for a in sys.argv[1:] if not a.startswith('--')]
    juego=args[0] if args else input('Carpeta del juego (donde está SRWV.EXE): ').strip().strip('"')
    if not os.path.exists(os.path.join(juego,'SRWV.EXE')):
        sys.exit('No encuentro SRWV.EXE en esa carpeta.')
    bk=os.path.join(juego,'_backup_traduccion_es')
    man=json.load(open(os.path.join(AQUI,'manifest.json'),encoding='utf8'))['files']
    if '--restaurar' in sys.argv:
        n=0
        for e in man:
            b=os.path.join(bk,e['path'])
            if os.path.exists(b): shutil.copy2(b,os.path.join(juego,e['path'])); n+=1
        print('Restaurados %d ficheros desde %s'%(n,bk)); return
    zs=get_zstd()
    if zs is None: sys.exit('Hace falta el módulo Python "zstandard" (pip install zstandard).')
    ok=ya=salt=0
    for e in man:
        dst=os.path.join(juego,e['path'])
        if not os.path.exists(dst): print('  (no existe, se omite) '+e['path']); salt+=1; continue
        s=sha(dst)
        if s==e['new_sha256']: print('  ya traducido  '+e['path']); ya+=1; continue
        if not e.get('full') and s!=e['orig_sha256']:
            print('  !! NO COINCIDE con el original de Steam, se omite: '+e['path']); salt+=1; continue
        b=os.path.join(bk,e['path'])
        if not os.path.exists(b):
            os.makedirs(os.path.dirname(b),exist_ok=True); shutil.copy2(dst,b)
        tmp=dst+'.tmp_es'
        try:
            aplicar(zs,None if e.get('full') else b,os.path.join(AQUI,'patches',e['patch']),tmp)
            if sha(tmp)!=e['new_sha256']: raise ValueError('verificación fallida')
            os.replace(tmp,dst); ok+=1; print('  OK            '+e['path'])
        except Exception as ex:
            print('  !! ERROR en %s: %s'%(e['path'],ex)); salt+=1
            if os.path.exists(tmp): os.remove(tmp)
    print('\nAplicados: %d · ya estaban: %d · omitidos/errores: %d'%(ok,ya,salt))
    print('Copia de seguridad en: '+bk)
if __name__=='__main__': main()
