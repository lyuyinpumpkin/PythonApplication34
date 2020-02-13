# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Users\\FESL14A835\\source\\repos\\PythonApplication34\\PythonApplication34\\restartProgram.py'],
             pathex=['C:\\Users\\FESL14A835\\source\\repos\\PythonApplication34\\PythonApplication34'],
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
          name='restartProgram',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\FESL14A835\\source\\repos\\PythonApplication34\\PythonApplication34\\restart_128px_1168699_easyicon.net.ico')
