RESEARCH_SUMMARY_PROMPT = """
You are an expert AI research analyst.

Analyze the provided research sources.

USER QUERY:
{query}

SEARCH RESULTS:
{results}

Return your analysis in the following format:

SUMMARY:
<concise summary>

KEY_FINDINGS:
- finding 1
- finding 2

TRENDS:
- trend 1
- trend 2

RISKS:
- risk 1
- risk 2
"""