from gpt_researcher.master.agent import GPTResearcher
import asyncio
from fastapi import FastAPI

async def run_agent(query, report_type):
    """Run the agent."""
    researcher = GPTResearcher(query=query, report_type=report_type)
    report = await researcher.run()
    return report

app = FastAPI()

@app.post('/report')
async def generate_report(query, report_type):
    return await run_agent(query, report_type)
