# BMI Pro 計算機 (Python Flask 版)

這是一個專業級的 BMI 計算器，使用 Python Flask 後端與 Tailwind CSS 前端。

## 🚀 快速開始

### 1. 克隆倉庫
```bash
git clone https://github.com/terrychuangagnt/bmi-calculator-python.git
cd bmi-calculator-python
```

### 2. 安裝依賴
建議使用虛擬環境：
```bash
pip install -r requirements.txt
```

### 3. 運行程式
```bash
python app.py
```

### 4. 訪問
打開瀏覽器訪問：`http://127.0.0.1:5000`

## 📈 功能特點
- **專業級 UI**：採用現代化雙欄布局，支援響應式設計。
- **計算歷史紀錄**：利用 Flask Session 實作，可追蹤最近 5 次的計算結果。
- **動態視覺回饋**：根據 BMI 分類（過輕/正常/過重/肥胖）自動切換配色。
- **強健的輸入驗證**：防止無效輸入導致的程式崩潰。

## ✅ 測試驗證報告
本項目已通過功能性與 UI 測試，驗證結果如下：

| 測試案例 | 輸入 (體重/身高) | 預期結果 | 實際結果 | 狀態 |
| :--- | :--- | :--- | :--- | :--- |
| 正常範圍 | 70kg / 175cm | 22.86 (Normal) | 22.86 (Normal) | ✅ 通過 |
| 肥胖範圍 | 90kg / 170cm | 31.14 (Obese) | 31.14 (Obese) | ✅ 通過 |
| 歷史記錄 | 連續計算兩次 | 記錄於右側面板 | 正確顯示兩筆紀錄 | ✅ 通過 |
| UI 布局 | 桌面/手機端 | 雙欄/單欄自適應 | 布局正確且美觀 | ✅ 通過 |

---
*Developed by Hermes Agent for terrychuangagnt*
