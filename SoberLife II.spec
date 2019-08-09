# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

assets = [
    ('Sober_Life_II/assets/*', 'assets'),
    ('Sober_Life_II/assets/*', 'Sober_Life_II/assets'),
    ('README.md', '.')
]

a = Analysis(['SoberLife II.py'],
             binaries=[],
             datas=assets,
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
          [],
          exclude_binaries=True,
          name='SoberLife II',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          icon='Sober_Life_II/assets/icon.ico'
          )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='SoberLife II')
