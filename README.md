# Stock-Analyzer-Agents with CrewAI 💹🤖

A modular, multi-agent system built with **CrewAI**, **Hugging Face**, **Streamlit**, and **YFinance** to perform comprehensive stock analysis, including:

- **Basic Stock Info**: Name, Sector, Industry, Market Cap, etc.
- **Fundamental Analysis**: PE Ratio, Forward PE, etc.
- **Technical Analysis**: Moving Averages, Relative Strength Index (RSI), Moving Average Convergence/Divergence (MACD), etc.
- **Risk Assessment**: Volatility, Beta, Value at Risk (VaR), Drawdowns, Sharpe, Sortino, etc.
- **News Analysis**: Recent news articles and their potential impact.

---

## Table of Contents
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Installation \& Setup](#installation--setup)
- [Usage](#usage)
- [Customizing \& Extending](#customizing--extending)
- [Contributing](#contributing)
- [License](#license)
- [Additional Notes](#additional-notes)

---

## Features
- **Multi-Agent Workflow**: Agents specialized for different tasks (collecting data, fundamental/technical analysis, news, report writing).
- **Modular Code Structure**: Clear separation of agents, tasks, and tools for easy maintenance and extensibility.
- **Streamlit UI**: Simple web interface where users can enter queries, run analysis, and view results in their browser.
- **Extensible**: Swap in your own LLM or data source by editing config or tool functions.

---

## Repository Structure

    ├── .env                        # Environment file
    ├── requirements.txt            # Python/Project dependencies
    ├── README.md                   # Project documentation
    ├── src/                 
    │   ├── config.py               # Configuration (API keys/Tokens, model names, etc.)
    │   ├── agents/
    │   │   └── stock_agents.py     # Agent definitions (stock_researcher, financial_analyst, etc.)
    │   ├── tasks/
    │   │   └── stock_tasks.py      # Task definitions (collect_stock_info, perform_analysis, etc.)
    │   ├── tools/
    │   │   └── stock_tools.py      # Tool functions (get_basic_stock_info, get_fundamental_analysis, etc.)
    │   └── utils/
    │       └── financial_calculations.py  # Helper functions for calculations (beta, RSI, MACD, etc.)
    |
    └── main.py                     # Streamlit UI

**File Descriptions**:
- **`main.py`**: Runs the Streamlit app - your main user interface.
- **`src/config.py`**: Stores or loads configuration (API keys, model details, default environment variables, etc.).
- **`src/agents/`**: Contains agent definitions — each agent has a role (researcher, analyst, etc.).
- **`src/tasks/`**: Each task addresses a part of the workflow (gather info, analyze data, compile report).
- **`src/tools/`**: Contains the “tool” functions that agents can call (e.g., fetching stock data from Yahoo, running technical indicators).
- **`src/utils/`**: Helper modules for repeated calculations

---

## Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kenilp7/Stock-Analyzer-Agents.git
   cd Stock-Analyzer-Agents
2. **Create & Activate a Virtual Environment (Recommended)**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   # or
   .\.venv\Scripts\activate    # Windows
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Set Up Environment Variables**:
   - Edit .env file to add your own tokens (Hugging Face etc.) or API keys/Credentials (OpenAI etc.)
   ```bash
   HF_TOKEN=<YOUR_HUGGING_FACE_TOKEN>
   MODEL_NAME=<MODEL_LINK_HUGGING_FACE>
---

## Usage
1. **Run the Streamlit App**:
   ```bash
   streamlit run main.py
2. **Open** the URL that Streamlit shows (e.g., `http://localhost:8501`) in your browser.
3. **Enter** your query in the sidebar (e.g., `“Is Apple a safe long-term investment for a risk-averse person?”`) and click **Analyze**.
4. **Wait** for the agents to gather data, run analysis, fetch news, and compile a report.
5. **View** the final markdown report in the main panel. It should summarize fundamental, technical, and risk analyses, plus relevant news.

---

## Customizing & Extending
1. **Change the LLM**: In `src/config.py` or directly in `agents/stock_agents.py`, replace references to Hugging Face or a default model with your chosen LLM.
2. **Add New Tools**: Create additional functions in `src/tools/stock_tools.py` or a new file, then register them with your agents if you want them accessible.
3. **Add or Modify Tasks**: In `src/tasks/stock_tasks.py`, create tasks that chain different agents or tool calls (e.g., “compare multiple stocks” or “portfolio analysis”).
4. **Change the UI**: In `main.py`, rearrange or expand Streamlit inputs, add new sections for data visualization, etc.

---

## Contributing
Contributions are welcome! To contribute:
  1. **Fork** the repo and create a new branch.
  2. Make your changes or additions.
  3. **Test** (for e.g., `pytest`).
  4. **Submit** a PR describing your changes.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Additional Notes
- **Performance**: Complex analyses (especially with large LLM calls) can take time. Consider using caching or asynchronous tasks if needed.
- **Security**: Keep secrets out of source control. Use .env and .gitignore for API keys.
- **Scaling**: For production usage, you can deploy the Streamlit app via Docker or run it on cloud platforms (AWS, GCP, Azure).
- **Further Customization**: CrewAI is modular - you can define your own “manager_llm,” custom message parsing, or chain-of-thought prompts in your agents or tasks.

**Enjoy exploring and analyzing stocks with your AI Agents!** Feel free to open Issues or Pull Requests for feedback and improvements.