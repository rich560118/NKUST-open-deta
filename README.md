# NKUST 校務數據公開

這個專案以靜態 HTML 呈現國立高雄科技大學校務資料視覺化，主要頁面為 `education_dynamic_chart.html`。`index.html` 作為入口頁，會導向主要儀表板。

## 檔案用途

- `index.html`：網站入口。
- `education_dynamic_chart.html`：ECharts 儀表板主檔，內含視覺樣式、圖表邏輯與預設資料。
- `extract_docx.py`、`read_docx*.py`、`read_all.py`、`read_tables.py`：Word 資料萃取輔助腳本。
- `requirements.txt`：Python 輔助腳本所需套件。

## 執行方式

靜態網頁可直接開啟：

```text
index.html
```

若要執行 Word 萃取腳本，先安裝 Python 依賴：

```bash
pip install -r requirements.txt
```

再依需求執行，例如：

```bash
python extract_docx.py "統計數據-專任(案)教師數_修正.docx"
```

## 維護注意

- `Pages.html`、`Pages_files/`、`temp.html` 是本機匯出或暫存檔，不屬於正式網站內容。
- 更新 `education_dynamic_chart.html` 內的資料時，請確認年份陣列與各資料序列長度一致。
- GitHub Pages 若使用根目錄部署，請以 `index.html` 作為入口。
