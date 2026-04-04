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
