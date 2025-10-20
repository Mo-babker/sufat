# 💧 SUFAT — Su Faturası Takip Sistemi

## 📘 Overview
**SUFAT (Su Faturası Takip Sistemi)** is a Python-based application that calculates and analyzes **water consumption and billing** for different types of subscribers.  
It guides users interactively through data entry, computes detailed billing information based on Turkish water pricing tiers, stores results in a CSV file, and visualizes consumption and billing data using charts and tables.

---

## 👥 Authors
- **Emir Can Ertekin** (44-252)  
- **Mohamed Babker Ahmed** (19-39, 251-461)

---

## 🧠 Features
- Interactive console interface for user input  
- Supports multiple subscriber types:
  - 🏠 Konut (Residential)
  - 🏢 İş Yeri (Business)
  - 🏛️ Kamu Kuruluşu (Public Institution)
  - 🏨 Turistik Tesis (Touristic Facility)
- Calculates:
  - Water usage (ton)
  - Usage duration (days)
  - Monthly equivalent consumption
  - Water fee and wastewater fee
  - VAT (KDV) and total bill
- Saves all data to a `data.csv` file automatically
- Generates detailed tables and analytics using **pandas** and **tabulate**
- Creates visual charts using **matplotlib**:
  - Pie charts for subscriber distribution
  - Bar charts for total consumption and highest payers
- Computes statistics such as:
  - Highest water or wastewater fee
  - Percentages of subscribers in specific consumption tiers
  - Average daily usage per subscriber type
  - Total KDV and wastewater income

---

## ⚙️ Requirements

### 🧩 Python Libraries
Make sure you have the following installed:
```bash
pip install pandas numpy matplotlib tabulate
```

### 🐍 Python Version
Python **3.8 or later** is recommended.

---

## 🚀 How to Run

1. Clone or download the project files.
2. Open a terminal in the project folder.
3. Run:
   ```bash
   python SUFAT.py
   ```
4. Follow the on-screen instructions:
   - Enter number of subscribers.
   - Provide subscriber type, previous and current meter readings, and reading dates.
5. The program:
   - Calculates billing details for each subscriber.
   - Saves results into **`data.csv`**.
   - Optionally displays detailed tables and graphs.

---

## 📊 Output Example
After entering data, you’ll see:
```
Abone Tipi: Konut
Toplam Su Kullanımınız: 25 Ton
30 Günlük Su Tüketim Ücretiniz: 224.00 TL
Toplam Fatura Tutarınız: 270.72 TL
```
And optionally:
- CSV file: `data.csv`
- Console tables (tabulated)
- Graphs (pie and bar charts)

---

## 🧩 File Structure
```
SUFAT.py           → Main program file
data.csv           → Generated automatically; stores all subscriber data
README.md          → Project documentation
```

---

## 📈 Data Columns (CSV)
| Column | Description |
|--------|--------------|
| Abone Tipi | Type of subscriber |
| Önceki Sayaç Değeri | Previous meter value |
| Şimdiki Sayaç Değeri | Current meter value |
| Gün Sayısı | Days between readings |
| Başka Abone Var Mı? | Whether another subscriber exists |
| Su Tüketim Miktarı | Total water usage (ton) |
| Su Tüketim Ücreti | Water usage fee |
| Atık Su Ücreti | Wastewater fee |
| KDV Tutarı | VAT amount |
| Fatura Tutarı | Total bill |

---

## 🧮 Main Functions Summary
| Function | Purpose |
|-----------|----------|
| `dico()` | Prints a decorative line separator |
| `başlık(title)` | Displays a formatted title box |
| `count(column, value)` | Counts how many subscribers match a given type |
| `sor(prompt)` | Asks user for permission to display details |
| `max(column, desc)` | Finds and visualizes the subscriber with the highest fee |
| `toplam(column, desc, unit)` | Plots total values for each subscriber type |
| `tum(column, desc)` | Calculates total KDV or wastewater fees |

---

## 🧾 Notes
- All calculations follow real Turkish water billing models (including tiered pricing and KDV).  
- CSV data accumulates across runs — each new execution appends to the file.  
- Charts display only subscriber types that have been entered.

---

## 📜 License
This project is developed for **educational purposes** (Software Engineering coursework).  
Use and modification are allowed for learning and non-commercial purposes.
