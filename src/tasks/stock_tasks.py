from crewai import Task
from src.agents.stock_agents import (
    stock_researcher,
    financial_analyst,
    news_analyst,
    report_writer
)

# 1. Collect stock info
collect_stock_info = Task(
    description='''
    1. Extract the ticker from the user query (or identify it if missing).
    2. Provide only basic stock info at this stage.
    ''',
    expected_output="A summary of the stock's key metrics.",
    agent=stock_researcher,
    dependencies=[],
    context=[]
)

# 2. Perform analysis
perform_analysis = Task(
    description='''
    Conduct a thorough analysis (fundamental, risk, technical) based on the user's query.
    ''',
    expected_output="Detailed financial and technical analysis.",
    agent=financial_analyst,
    dependencies=[collect_stock_info],
    context=[collect_stock_info]
)

# 3. Analyze stock news
analyze_stock_news = Task(
    description='''
    Fetch recent news related to the stock and assess its potential impact.
    ''',
    expected_output="Summary of recent news articles.",
    agent=news_analyst,
    dependencies=[collect_stock_info],
    context=[collect_stock_info]
)

# 4. Generate comprehensive report
generate_stock_report = Task(
    description='''
    Synthesize all collected info and analyses into a cohesive stock report.
    ''',
    expected_output="A comprehensive stock report in markdown format.",
    agent=report_writer,
    dependencies=[collect_stock_info],
    context=[collect_stock_info, perform_analysis, analyze_stock_news]
)
