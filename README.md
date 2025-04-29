# 📊 Raymond's Mutual Fund Analysis Tool

This is a simple, intuitive Python-based web app that helps users analyze and rank mutual funds using real-time data. Built with **Streamlit**, this tool allows you to enter a mutual fund ticker and retrieve:

- 📈 Historical price trends
- 💰 Latest closing price
- 📊 Estimated annual return
- ⚠️ Risk (volatility) metric

---

## 🔧 Features

- Text input for mutual fund tickers (e.g., `VFIAX`, `SWPPX`)
- Real-time data fetched using [Yahoo Finance](https://finance.yahoo.com/) via the `yfinance` API
- Calculations for:
  - Latest closing price
  - Annualized return
  - Volatility (standard deviation of returns)
- Interactive chart of historical price performance
- Clean, minimal interface powered by Streamlit

---

## 🧰 Tech Stack

- **Python 3.10+**
- [Streamlit](https://streamlit.io/)
- [YFinance](https://pypi.org/project/yfinance/)
- Pandas
- Matplotlib

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mutual-fund-analysis-tool.git
cd mutual-fund-analysis-tool
2. Create & Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
Activate it:

On Windows:

bash
Copy
Edit
.\\venv\\Scripts\\activate
On Mac/Linux:

bash
Copy
Edit
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you don’t have a requirements.txt file yet, you can install manually:

bash
Copy
Edit
pip install streamlit yfinance pandas matplotlib
4. Run the App
bash
Copy
Edit
streamlit run mutual_fund_analysis_tool.py
The app will launch in your browser at http://localhost:8501

🧹 Deactivating the Environment
When you're done, stop the app with Ctrl + C, then deactivate the virtual environment:

bash
Copy
Edit
deactivate
📄 Example Tickers to Try
VFIAX – Vanguard 500 Index Fund

SWPPX – Schwab S&P 500 Index Fund

FXAIX – Fidelity 500 Index Fund

📈 Future Improvements (Ideas)
Allow users to compare multiple funds side-by-side

Add Sharpe Ratio and expense ratio metrics

Implement caching for faster performance

Add fund category filters or search suggestions

👨‍💻 Author
Raymond Beaulieu
University of Arkansas | Finance Major
Built for Advanced Financial Modeling (Spring 2025)
