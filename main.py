import streamlit as st
from datetime import datetime
from crewai import Crew, Process
from src.agents.stock_agents import (
    stock_researcher,
    financial_analyst,
    news_analyst,
    report_writer,
    llm
)
from src.tasks.stock_tasks import (
    collect_stock_info,
    perform_analysis,
    analyze_stock_news,
    generate_stock_report
)

st.set_page_config(page_title="Advanced Stock Analysis Dashboard", layout="wide")

def create_crew():
    """Instantiate the Crew object with agents and tasks."""
    return Crew(
        agents=[stock_researcher, financial_analyst, news_analyst, report_writer],
        tasks=[
            collect_stock_info,
            perform_analysis,
            analyze_stock_news,
            generate_stock_report
        ],
        process=Process.sequential,
        manager_llm=llm
    )

def main():
    st.title("Welcome to Stock Analysis Dashboard")

    st.sidebar.header("Stock Analysis Query")
    query = st.sidebar.text_area(
        "Enter your stock analysis question",
        value="Is Apple a safe long-term bet for a risk-averse individual?",
        height=100
    )
    
    analyze_button = st.sidebar.button("Analyze") 
    
    if analyze_button:
        st.info(f"Starting analysis for query: {query}.\nThis may take a few moments...")
        
        crew = create_crew()
        default_date = datetime.now().date()
        
        # Kick off the workflow
        result = crew.kickoff(inputs={"query": query, "default_date": str(default_date)})
        
        st.success("Analysis complete!")
        
        # Display the final report
        st.markdown("## Full Analysis Report")
        st.markdown(result)

    st.markdown("---")
    st.markdown("Made by Kenil Patel")

if __name__ == "__main__":
    main()
