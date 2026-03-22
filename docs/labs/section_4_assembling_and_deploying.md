# Section 4 Lab - Assembling and Deploying Applications

## What you will practice
- Coding simple chains.
- Packaging pyfunc models.
- Vector Search and deployment sequencing.
- Unity Catalog registration and endpoint planning.

## Exercises
1. Run `rag_preprocess()` on `data/raw/architecture_notes.md`.
2. Sketch a simple chain: input -> preprocess -> retrieve -> generate -> post-process.
3. Use `deployment_sequence()` to write the deployment runbook.
4. For a basic RAG app, list the required elements:
   - model flavor
   - embedding model
   - retriever
   - dependencies
   - input example
   - model signature
5. Explain when `ai_query()` is better than online endpoint serving.

## Check yourself
- Did you include Unity Catalog in both data and model governance steps?
- Did you separate batch inference workloads from real-time serving?
- Did you identify endpoint access controls?
