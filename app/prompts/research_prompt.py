RESEARCH_SUMMARY_PROMPT = """
You are an expert AI research analyst.

Your task is to analyze search results and generate a research summary.

USER QUERY:
{query}

SEARCH RESULTS:
{results}

Generate:
1. A concise summary
2. Key findings
3. Important trends
4. Risks or limitations

Return clean structured text.
"""