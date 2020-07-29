# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [('encCP', '.'), ('encDA', '.'), ('encPD', '.'), ('mlpCP', '.'), ('mlpDA', '.'), ('mlpPD', '.'), ('/opt/anaconda3/lib/python3.7/site-packages/dask/dask.yaml', './dask'), ('/opt/anaconda3/lib/python3.7/site-packages/distributed/distributed.yaml', './distributed'),('icon.ico','.')]


a = Analysis(['FlightDelayPredictor.py'],
             pathex=['/Users/kingwong/Desktop/NewGUI'],
             binaries=[('/System/Library/Frameworks/Tk.framework/Tk', 'tk'), ('/System/Library/Frameworks/Tcl.framework/Tcl', 'tcl')],
             datas=added_files,
             hiddenimports=["pickle","scikit-learn", "sklearn.neural_network", "sklearn.ensemble", "sklearn.neighbors._typedefs", "sklearn.utils._cython_blas", "sklearn.neighbors._quad_tree", "sklearn.tree._utils", "dask_ml", "dask_ml.wrappers"],
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
          name='FlightDelayPredictor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True, icon = 'icon.ico')
