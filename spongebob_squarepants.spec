# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['spongebob_squarepants.py'],
             pathex=['C:\\Users\\shine\\OneDrive\\바탕 화면\\SUN\\KPU\\2학년 2학기\\2DGP_git\\2DGP_Term_Project'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='spongebob_squarepants',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
