# TXT Splitter GUI

TXT Splitter GUI 是一個 Windows 圖形介面工具，用於將 TXT 文字檔分割成多個檔案。

## 啟動程式

在 Windows PowerShell 進入專案資料夾後執行：

```powershell
.\run.bat
```

也可以使用已安裝的 Python 直接啟動：

```powershell
python .\txt_splitter_gui.py
```

在視窗中選取要分割的 TXT 檔案，依介面提示設定分割條件並執行。

## 建置 Windows 執行檔

若環境尚未安裝 PyInstaller，先在用於建置的 Python 環境執行：

```powershell
python -m pip install pyinstaller
```

接著執行建置腳本，完成後到 `dist/` 查看產物：

```powershell
.\build.bat
```

## 專案檔案

| 檔案 | 用途 |
| --- | --- |
| `txt_splitter_gui.py` | TXT 分割工具的 Python GUI 主程式 |
| `run.bat` | Windows 啟動腳本 |
| `build.bat` | Windows 建置腳本 |
| `txt_splitter_gui.spec` | PyInstaller 打包設定 |

`build/` 存放建置中間檔，`dist/` 存放打包產物。
