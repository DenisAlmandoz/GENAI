# RAG Architecture Notes

## Retrieval
Use structure-aware chunking for markdown manuals and policy documents so each heading remains attached to its detail.
Evaluate retrieval with hit rate, MRR, and qualitative review of missing evidence.
Re-ranking can improve top-k precision when vector search returns loosely related passages.

## Deployment
Write chunked text and metadata into Delta Lake tables in Unity Catalog before creating embeddings and a Mosaic AI Vector Search index.
Package the chain with MLflow pyfunc when you need custom pre-processing and post-processing around a model call.

## Monitoring
Use inference tables, Agent Monitoring, and endpoint metrics to track latency, groundedness, token usage, and business success.
