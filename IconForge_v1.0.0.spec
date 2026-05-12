# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['IconForge_v1.0.0_venv_cuda_py311_np2.py'],
    pathex=[],
    binaries=[],
    datas=[('IconForge.ico', '.'), ('IconForge_logo.png', '.'), ('IconForge_text.png', '.'), ('IconForge.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='IconForge_v1.0.0',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['IconForge.ico'],
)
