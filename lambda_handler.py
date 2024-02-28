from gpt_researcher.master.agent import GPTResearcher
import asyncio

async def run_agent(query, report_type):
    """Run the agent."""
    # run agent
    researcher = GPTResearcher(query=query, report_type=report_type)
    report = await researcher.run()
    return report


async def async_handler(event, context):
    # Put your asynchronous code here

    query = "Tell me more about Marvel Cinematic Universe."
    report_type='research_report'
    report = await run_agent(query, report_type)

    return {'statusCode': 200, 'body': report }

# Point to this function as a handler in the Lambda configuration
def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    # DynamoDB resource defined above is attached to this loop:
    #   if you use asyncio.run instead
    #   you will encounter "Event loop closed" exception
    return loop.run_until_complete(async_handler(event, context))