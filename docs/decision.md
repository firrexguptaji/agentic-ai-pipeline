## [2026-04-04] Use Monorepo for Microservices

### Context

Need to organize multiple services (API, Agent, RAG) while keeping development simple.

### Decision

Use a single repository with service-based folder structure.

### Reasoning

* Faster development
* Easier dependency sharing
* Simpler setup for MVP

### Tradeoffs

* Less isolation between services
* May need splitting later

### Future Considerations

Can split into multiple repos once system scales.

## [2026-04-04] Use Monorepo for Microservices

### Context

Need to organize multiple services (API, Agent, RAG) while keeping development simple.

### Decision

Use a single repository with service-based folder structure.

### Reasoning

* Faster development
* Easier dependency sharing
* Simpler setup for MVP

### Tradeoffs

* Less isolation between services
* May need splitting later

### Future Considerations

Can split into multiple repos once system scales.

## [2026-04-04] Select Gemini 2.5 Flash Model

### Context

Multiple Gemini models available via API.

### Decision

Use gemini-2.5-flash as default model.

### Reasoning

* Stable and supported
* Good balance of speed and quality
* Suitable for agent workflows

### Tradeoffs

* Slightly lower reasoning ability than Pro models

### Future Considerations

Upgrade to Gemini Pro for complex reasoning tasks.

## [2026-04-04] Use Environment-Based Configuration

### Context

Need flexible service configuration (e.g., service URLs).

### Decision

Use environment variables with a shared config module.

### Reasoning

* Simple and scalable
* Works across environments (local, docker, cloud)
* Avoids hardcoding values

### Tradeoffs

* Requires env management

### Future Considerations

May adopt config service for large-scale system.


## [2026-04-04] Increase Service Timeout for LLM Calls

### Context

LLM responses may take several seconds depending on complexity.

### Decision

Set API Gateway timeout to 10–15 seconds for agent calls.

### Reasoning

* Avoid premature request failures
* LLM latency is variable

### Tradeoffs

* Slightly longer wait time for failures

### Future Considerations

Implement async processing or streaming responses.
## [2026-04-04] Use Gemini Embedding API for Vector Generation

### Context

Need to generate embeddings for text to support RAG (Retrieval-Augmented Generation) and semantic search.

### Decision

Use Google Gemini embedding model (`gemini-embedding-001`) within the Agent Service.

### Reasoning

* Already using Gemini ecosystem (no additional provider needed)
* Simple integration with existing API setup
* Good quality embeddings for general-purpose use
* Reduces system complexity (single provider)

### Tradeoffs

* External dependency on Gemini API
* Limited control compared to local embedding models

## [2026-04-04] Centralized Configuration Management

### Context

Configuration values (API keys, service URLs, vector size) were initially scattered across services, leading to duplication and harder maintainability.

### Decision

Centralize all configuration using a shared `settings.py` module under `shared/config/`, backed by environment variables (`.env`).

### Reasoning

* Avoid hardcoded values across services
* Ensure consistency between microservices
* Simplify updates and environment management
* Enable scalability without modifying multiple files

### Tradeoffs

* Requires proper import structure across services
* Initial setup complexity (module path issues, environment loading)

### Future Considerations

* Add validation for required environment variables
* Support multiple environments (dev, staging, prod)
* Integrate secrets management for production (e.g., vault, cloud secrets)


### Future Considerations

* Evaluate local embedding models for cost/performance optimization
* Add batching for large-scale embedding generation
* Move embedding to dedicated microservice if scaling requires

## [2026-04-04] Adopt Qdrant for Vector Database

### Context

Need a vector database to store and retrieve embeddings for semantic search and RAG pipeline.

### Decision

Use Qdrant as the vector database and integrate it via a dedicated `VectorDB` service within the Agent Service.

### Reasoning

* Native support for vector similarity search
* Lightweight and easy to integrate with Python services
* Suitable for microservice-based architecture
* Supports cosine similarity for semantic retrieval

### Tradeoffs

* External service dependency (Docker/container required)
* Strict schema requirement (vector dimension must match embeddings)
* Collection must be recreated if schema changes

### Future Considerations

* Add filtering and metadata-based search
* Optimize search with indexing strategies
* Introduce distributed setup for scaling
* Abstract DB layer to support alternative providers if needed

