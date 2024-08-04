from crewai import Agent, LLM
from src.config import HF_TOKEN, MODEL_NAME
from src.tools.stock_tools import (
    get_basic_stock_info,
    get_fundamental_analysis,
    get_stock_risk_assessment,
    get_technical_analysis,
    get_stock_news
)


# Initialize LLM
llm = LLM(
    model=MODEL_NAME,
    api_key=HF_TOKEN,
)

stock_researcher = Agent(
    llm=llm,
    role="Stock Researcher",
    goal="Identify the stock ticker and gather basic info about the company.",
    backstory="A junior stock researcher with a knack for gathering relevant company/stock info.",
    tools=[get_basic_stock_info],
    verbose=True,
    allow_delegation=False
)

financial_analyst = Agent(
    llm=llm,
    role="Financial Analyst",
    goal="Perform in-depth fundamental and technical analysis on the stock.",
    backstory="A seasoned financial analyst interpreting complex financial data.",
    tools=[get_fundamental_analysis, get_stock_risk_assessment, get_technical_analysis],
    verbose=True,
    allow_delegation=False
)

news_analyst = Agent(
    llm=llm,
    role="News Analyst",
    goal="Fetch recent news articles related to the stock.",
    backstory="A sharp news analyst who tracks stock news trends.",
    tools=[get_stock_news],
    verbose=True
)

report_writer = Agent(
    llm=llm,
    role='Financial Report Writer',
    goal='Synthesize all analysis into a cohesive, professional stock report.',
    backstory='An experienced financial writer capable of summarizing insights clearly.',
    tools=[],
    verbose=True,
    allow_delegation=False
)
