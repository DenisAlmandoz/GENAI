# Section 2 Lab - Data Preparation

## What you will practice
- Chunking strategy selection.
- Noise removal for RAG quality.
- Python package selection for extraction.
- Delta Lake and Unity Catalog ingestion planning.
- Retrieval evaluation and re-ranking.

## Exercises
1. Clean `data/raw/policies/policy_manual.md` with `filter_extraneous_lines()`.
2. Chunk the cleaned text with both `paragraph_chunks()` and `markdown_heading_chunks()`.
3. Decide which strategy better preserves meaning for policy retrieval.
4. Use `recommend_extractor()` to choose packages for pdf, html, docx, pptx, and json.
5. Write the sequence to load chunks into Delta tables in Unity Catalog.
6. Use `reranking_note()` to explain why re-ranking helps after the initial retrieval stage.
7. Create three example prompt/response pairs for extraction or summarization practice.

## Check yourself
- Did you remove noisy lines that could pollute embeddings?
- Did your chunk size preserve headings with their detail?
- Did you describe how metadata should be stored with chunks?
