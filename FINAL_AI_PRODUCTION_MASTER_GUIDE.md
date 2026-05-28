# FINAL AI PRODUCTION MASTER GUIDE
## The Complete FAANG-Level Reference for Building Production-Ready AI Systems

**Target Audience**: Senior AI Engineers, AI Architects, ML Engineers, Platform Engineers
**Last Updated**: May 2026
**Version**: 2.0 - FAANG Edition
**Scope**: End-to-end production AI systems from consultation to deployment

---

## TABLE OF CONTENTS

### PART 1: FOUNDATIONS (Sections 1-10)
1. Client Consultation Framework
2. Technique Selection Decision Tree
3. Pre-Deployment Checklist
4. Production Folder Architecture
5. Complete RAG Workflow
6. Complete Agentic RAG Workflow
7. Complete AI Agent Workflow
8. Complete Multi-Agent System Workflow
9. Complete Fine-Tuning Workflow
10. Model and Resource Selection Matrix

### PART 2: PRODUCTION OPTIMIZATION (Sections 11-16) - NEW
11. Latency Optimization
12. Cost Optimization
13. Security Architecture
14. Provider Abstraction and Shifting
15. Caching Strategies
16. Observability and Monitoring

### PART 3: ADVANCED PRODUCTION SYSTEMS (Sections 17-26) - NEW
17. Scaling and Infrastructure
18. CI/CD for AI Systems
19. Error Handling and Resilience Patterns
20. Data Pipeline Architecture
21. Prompt Engineering at Scale
22. Evaluation and Quality Assurance at Scale
23. Human-in-the-Loop Systems
24. Multi-Modal AI Systems
25. Edge Deployment and On-Device Inference
26. Compliance, Governance and Ethics
27. Production Readiness Roadmap and FAANG Checklists

---
## 1. CLIENT CONSULTATION FRAMEWORK

### 1.1 THE DISCOVERY SCRIPT (Questions to Ask Every Client)

#### Phase 1: Business Understanding (10 minutes)
```
Q1: What is the specific business problem we're solving?
├─ Follow-up: What happens if we don't solve this?
├─ Follow-up: What's the cost of the current manual process?
└─ Goal: Establish ROI and urgency

Q2: Who are the end users and what's their technical proficiency?
├─ Technical team → Can handle API complexity
├─ Business users → Need simple UI with guardrails
└─ External customers → Need zero-error tolerance

Q3: What does success look like in measurable terms?
├─ Accuracy target? (e.g., 95% correct responses)
├─ Speed requirement? (e.g., <2s response time)
├─ Cost constraint? (e.g., <$0.01 per query)
└─ Scale requirement? (e.g., 10K concurrent users)
```

#### Phase 2: Data & Privacy (15 minutes)
```
Q4: What data do we have access to?
├─ Structured (SQL/CSV) → Consider hybrid search
├─ Unstructured (PDFs/Docs) → RAG is mandatory
├─ Real-time streams → Need caching strategy
└─ No historical data → Pre-trained models only

Q5: Where does the data need to stay?
├─ On-premise only → Local models (Llama, Mistral)
├─ Cloud-friendly → API models (GPT-4, Claude)
├─ Region-specific (EU/UAE) → Consider data sovereignty
└─ Multi-cloud → Need vendor-agnostic architecture

Q6: Does the data contain PII or sensitive information?
├─ YES → Implement redaction + local hosting
├─ Medical/Legal → HIPAA/GDPR compliance needed
└─ NO → API models are viable

Q7: How often does the source data change?
├─ Real-time → RAG with live database connection
├─ Daily/Weekly → Batch embedding updates
├─ Rarely → Static fine-tuning may work
└─ Never → Fine-tuning is optimal
```

#### Phase 3: Technical Requirements (10 minutes)
```
Q8: What's the consequence of an AI mistake?
├─ Critical (Legal/Medical) → Human-in-loop mandatory
├─ High (Financial) → Multi-layer validation needed
├─ Medium (Customer service) → Confidence thresholds
└─ Low (Creative tasks) → Allow experimentation

Q9: Do we need explainability?
├─ YES (Regulated industries) → Use retrieval sources
├─ Partial → LLM-as-judge can evaluate
└─ NO → Black-box is acceptable

Q10: What's the latency tolerance?
├─ <500ms → Need small models + caching
├─ <2s → Standard API calls work
├─ <10s → Multi-agent workflows viable
└─ No constraint → Can use complex reasoning

Q11: What's the expected usage pattern?
├─ Burst traffic → Need autoscaling
├─ Constant load → Fixed infrastructure
├─ Rare/sporadic → Serverless architecture
└─ 24/7 critical → Multi-region deployment
```

### 1.2 THE TECHNIQUE DECISION MATRIX

Use this flowchart during client discussions:

```
START: What does the client need?
│
├─ General knowledge questions?
│  └─ YES → Simple Prompting (GPT-4o API)
│     ├─ Cost: ~$0.01 per 1K tokens
│     └─ Timeline: 1-2 days
│
├─ Access to proprietary/private documents?
│  └─ YES → Is data static or dynamic?
│     ├─ Static & small (<10 docs) → Prompt with full context
│     ├─ Dynamic or large (>10 docs) → RAG System
│     │  ├─ Cost: $500-5K setup + ongoing
│     │  └─ Timeline: 1-2 weeks
│     └─ Constantly updating → Agentic RAG
│        ├─ Cost: $2K-10K setup
│        └─ Timeline: 2-4 weeks
│
├─ Need to take actions (send emails, book appointments)?
│  └─ YES → AI Agent with Tool Use
│     ├─ Single task → Simple Agent
│     ├─ Multiple complex tasks → Multi-Agent System
│     ├─ Cost: $5K-20K setup
│     └─ Timeline: 3-6 weeks
│
└─ Need specific tone/style/format consistently?
   └─ YES → Fine-Tuning
      ├─ Prerequisites: RAG won't work for this
      ├─ Have 500+ quality examples
      ├─ Cost: $1K-10K compute + time
      └─ Timeline: 1-3 weeks
```

---

## 2. TECHNIQUE SELECTION DECISION TREE

### 2.1 WHEN TO USE EACH TECHNIQUE

| Use Case | Technique | Why | Example |
|----------|-----------|-----|---------|
| Answer FAQs from website | **Simple RAG** | Static knowledge, no actions needed | Customer support chatbot |
| Research competitor analysis | **Agentic RAG** | Multi-step research, web search needed | Market intelligence tool |
| Book appointments automatically | **AI Agent** | Actions required (calendar API) | Scheduling assistant |
| Complex software development | **Multi-Agent** | Multiple specialized roles needed | AutoGPT-style coding system |
| Brand-specific writing style | **Fine-Tuning** | Tone consistency is critical | Marketing content generator |
| Legal contract analysis | **RAG + Human-in-loop** | High stakes, explainability needed | Contract review assistant |
| Real-time customer service | **RAG + Streaming** | Speed matters, knowledge changes | Live chat support |
| Data analysis on SQL database | **Agent with Tools** | Need to write/execute queries | Business intelligence assistant |

### 2.2 COMBINATION STRATEGIES

Most production systems use **multiple techniques together**:

```
Example 1: Enterprise Knowledge Assistant
├─ RAG: For company documents and policies
├─ Agent: For accessing HR database and Slack
└─ Fine-tuning: For company-specific terminology

Example 2: Customer Service Platform
├─ RAG: For product documentation
├─ Simple Agent: For order lookup (API call)
└─ Guardrails: For sensitive information filtering

Example 3: Research Assistant
├─ Agentic RAG: For paper discovery and analysis
├─ Multi-Agent: Researcher + Critic + Writer
└─ Tool Use: Web search + PDF parsing
```

---

## 3. PRE-DEPLOYMENT CHECKLIST

### 3.1 TECHNICAL VALIDATION

```markdown
## Infrastructure Checklist
- [ ] **Compute Resources Sized**
  - [ ] Estimated tokens/month: __________
  - [ ] Peak concurrent users: __________
  - [ ] GPU requirements calculated (if local)
  - [ ] Fallback strategy for API outages
  
- [ ] **Cost Budget Defined**
  - [ ] Token cost per query: __________
  - [ ] Monthly budget cap: __________
  - [ ] Rate limits configured
  - [ ] Cost monitoring dashboard ready

- [ ] **Latency Requirements Met**
  - [ ] TTFT (Time to First Token): __________ ms
  - [ ] Total response time: __________ s
  - [ ] Caching strategy implemented
  - [ ] Load testing completed (target: ______ RPS)

- [ ] **Data Pipeline Validated**
  - [ ] Source data quality checked
  - [ ] Chunking strategy tested (size: ______)
  - [ ] Embedding model selected: __________
  - [ ] Vector database indexed
  - [ ] Backup and versioning in place
```

### 3.2 QUALITY ASSURANCE

```markdown
## Evaluation Checklist
- [ ] **Golden Dataset Created**
  - [ ] 100-200 representative Q&A pairs
  - [ ] Edge cases included
  - [ ] Domain expert validated
  
- [ ] **Metrics Baseline Established**
  - [ ] Accuracy/Faithfulness: __________ %
  - [ ] Hallucination rate: __________ %
  - [ ] Latency p95: __________ ms
  - [ ] User satisfaction (if available): __________

- [ ] **Safety Guardrails Tested**
  - [ ] Prompt injection attempts blocked
  - [ ] PII redaction working
  - [ ] Refusal scenarios tested
  - [ ] Content moderation active

- [ ] **Monitoring & Logging**
  - [ ] Request/response logging enabled
  - [ ] Error tracking configured (Sentry/etc)
  - [ ] Token usage monitoring
  - [ ] User feedback mechanism ready
```

### 3.3 BUSINESS READINESS

```markdown
## Go-Live Checklist
- [ ] **Documentation Complete**
  - [ ] API documentation (if applicable)
  - [ ] User guide/training materials
  - [ ] System architecture diagram
  - [ ] Runbook for common issues
  
- [ ] **Legal & Compliance**
  - [ ] Terms of service reviewed
  - [ ] Data privacy policy updated
  - [ ] Compliance requirements met (GDPR/HIPAA)
  - [ ] Liability clauses addressed

- [ ] **Support & Maintenance**
  - [ ] On-call rotation defined
  - [ ] Escalation path documented
  - [ ] Model update strategy planned
  - [ ] Deprecation policy established

- [ ] **Launch Strategy**
  - [ ] Beta testing completed
  - [ ] Rollout plan (gradual vs big-bang)
  - [ ] Rollback plan documented
  - [ ] Communication plan ready
```

---

## 4. PRODUCTION FOLDER ARCHITECTURE

### 4.1 STANDARD PROJECT STRUCTURE

```
ai-production-project/
│
├── .env                          # API keys, secrets (NEVER commit)
├── .env.example                  # Template for .env
├── .gitignore
├── .dockerignore
├── docker-compose.yml            # Multi-container orchestration
├── Dockerfile                    # Main application container
├── requirements.txt              # Python dependencies
├── pyproject.toml                # Modern Python packaging (Poetry/PDM)
├── README.md                     # Professional documentation
├── LICENSE
│
├── config/                       # Configuration management
│   ├── settings.py              # Pydantic settings
│   ├── prompts/                 # Versioned prompt templates
│   │   ├── system_prompts.yaml
│   │   └── user_prompts.yaml
│   └── models.yaml              # Model configurations
│
├── src/                         # Source code
│   ├── __init__.py
│   │
│   ├── core/                    # Core abstractions
│   │   ├── __init__.py
│   │   ├── llm_base.py         # Abstract LLM interface
│   │   ├── embedder_base.py    # Abstract embeddings interface
│   │   └── config.py           # Settings loader
│   │
│   ├── models/                  # LLM implementations
│   │   ├── __init__.py
│   │   ├── openai_client.py
│   │   ├── anthropic_client.py
│   │   ├── local_llm.py        # vLLM/TensorRT wrapper
│   │   └── embedding_models.py
│   │
│   ├── retrieval/               # RAG components
│   │   ├── __init__.py
│   │   ├── chunking.py         # Document chunking strategies
│   │   ├── embedding.py        # Embedding pipeline
│   │   ├── vector_store.py     # Pinecone/Weaviate/Chroma
│   │   ├── hybrid_search.py    # Vector + BM25 fusion
│   │   └── reranker.py         # Cross-encoder reranking
│   │
│   ├── agents/                  # Agent logic
│   │   ├── __init__.py
│   │   ├── base_agent.py       # Agent abstraction
│   │   ├── researcher.py       # Specialized researcher agent
│   │   ├── writer.py           # Writer agent
│   │   └── orchestrator.py     # LangGraph/CrewAI orchestration
│   │
│   ├── tools/                   # Agent tools
│   │   ├── __init__.py
│   │   ├── web_search.py       # Search API wrapper
│   │   ├── database.py         # SQL query tool
│   │   ├── email.py            # Email sending tool
│   │   └── calendar.py         # Calendar API tool
│   │
│   ├── api/                     # FastAPI application
│   │   ├── __init__.py
│   │   ├── main.py             # FastAPI app entry
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── chat.py         # Chat endpoint
│   │   │   ├── documents.py    # Document ingestion
│   │   │   └── health.py       # Health checks
│   │   ├── middleware/
│   │   │   ├── auth.py         # Authentication
│   │   │   ├── rate_limit.py   # Rate limiting
│   │   │   └── logging.py      # Request logging
│   │   └── schemas/
│   │       ├── request.py      # Pydantic request models
│   │       └── response.py     # Pydantic response models
│   │
│   ├── evaluation/              # Evaluation framework
│   │   ├── __init__.py
│   │   ├── ragas_eval.py       # RAGAS metrics
│   │   ├── llm_judge.py        # LLM-as-a-judge
│   │   └── metrics.py          # Custom metrics
│   │
│   └── utils/                   # Utilities
│       ├── __init__.py
│       ├── cache.py            # Semantic caching
│       ├── logger.py           # Logging configuration
│       └── monitoring.py       # Metrics collection
│
├── data/                        # Data directory (gitignored)
│   ├── raw/                    # Original documents
│   ├── processed/              # Chunked/embedded data
│   ├── vector_db/              # Local vector DB files
│   └── golden_dataset.json     # Evaluation dataset
│
├── notebooks/                   # Jupyter notebooks (experiments)
│   ├── 01_data_exploration.ipynb
│   ├── 02_chunking_experiments.ipynb
│   └── 03_evaluation_analysis.ipynb
│
├── tests/                       # Testing suite
│   ├── __init__.py
│   ├── unit/                   # Unit tests
│   │   ├── test_chunking.py
│   │   ├── test_retrieval.py
│   │   └── test_agents.py
│   ├── integration/            # Integration tests
│   │   ├── test_api.py
│   │   └── test_e2e_flow.py
│   └── evaluation/             # Evaluation tests
│       └── test_golden_dataset.py
│
├── scripts/                     # Utility scripts
│   ├── ingest_documents.py     # Document ingestion
│   ├── build_vector_db.py      # Vector DB population
│   ├── evaluate.py             # Run evaluation
│   └── benchmark.py            # Performance benchmarking
│
├── deployment/                  # Deployment configurations
│   ├── kubernetes/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── ingress.yaml
│   ├── terraform/              # Infrastructure as code
│   │   └── main.tf
│   └── monitoring/
│       ├── prometheus.yml
│       └── grafana_dashboard.json
│
└── docs/                        # Documentation
    ├── architecture.md          # System design
    ├── api_reference.md         # API documentation
    ├── deployment_guide.md      # Deployment instructions
    └── troubleshooting.md       # Common issues
```

### 4.2 KEY PRINCIPLES

1. **Separation of Concerns**: Each directory has a single responsibility
2. **Testability**: All business logic is in `src/`, testable independently
3. **Configuration Management**: No hardcoded values, all in `config/`
4. **Dependency Injection**: Use abstractions (base classes) for swappability
5. **Versioning**: Prompts and configurations are versioned like code

---

## 5. COMPLETE RAG WORKFLOW

### 5.1 ARCHITECTURE OVERVIEW

```
┌─────────────┐
│   User      │
│   Query     │
└──────┬──────┘
       │
       v
┌──────────────────────────────────────────┐
│  1. QUERY PREPROCESSING                  │
│  ├─ Language detection                   │
│  ├─ Query rewriting/expansion            │
│  └─ Intent classification                │
└──────┬───────────────────────────────────┘
       │
       v
┌──────────────────────────────────────────┐
│  2. HYBRID RETRIEVAL                     │
│  ├─ Vector Search (Semantic)             │
│  ├─ Keyword Search (BM25)                │
│  └─ Metadata Filtering                   │
└──────┬───────────────────────────────────┘
       │
       v
┌──────────────────────────────────────────┐
│  3. RECIPROCAL RANK FUSION               │
│  └─ Merge & rank results                 │
└──────┬───────────────────────────────────┘
       │
       v
┌──────────────────────────────────────────┐
│  4. RE-RANKING                           │
│  └─ Cross-encoder model scores           │
└──────┬───────────────────────────────────┘
       │
       v
┌──────────────────────────────────────────┐
│  5. CONTEXT COMPRESSION                  │
│  ├─ Remove redundancy (LLMLingua)        │
│  └─ Select top-K chunks                  │
└──────┬───────────────────────────────────┘
       │
       v
┌──────────────────────────────────────────┐
│  6. PROMPT CONSTRUCTION                  │
│  ├─ System prompt                        │
│  ├─ Retrieved context                    │
│  └─ User query                           │
└──────┬───────────────────────────────────┘
       │
       v
┌──────────────────────────────────────────┐
│  7. LLM GENERATION                       │
│  └─ Streaming response                   │
└──────┬───────────────────────────────────┘
       │
       v
┌──────────────────────────────────────────┐
│  8. POST-PROCESSING                      │
│  ├─ Citation extraction                  │
│  ├─ Hallucination check                  │
│  └─ Formatting                           │
└──────┬───────────────────────────────────┘
       │
       v
┌─────────────┐
│  Response   │
│  to User    │
└─────────────┘
```

### 5.2 STEP-BY-STEP IMPLEMENTATION

#### Step 1: Document Ingestion Pipeline

```python
# File: src/retrieval/ingestion.py

from typing import List, Dict
import hashlib
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PDFPlumberLoader

class DocumentIngestionPipeline:
    """
    Handles document loading, chunking, and metadata extraction
    """
    
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
    
    def load_documents(self, file_paths: List[str]) -> List[Dict]:
        """Load documents from various file types"""
        documents = []
        
        for path in file_paths:
            if path.endswith('.pdf'):
                loader = PDFPlumberLoader(path)
                docs = loader.load()
                
                for doc in docs:
                    # Add metadata
                    doc.metadata['source'] = path
                    doc.metadata['file_type'] = 'pdf'
                    doc.metadata['char_count'] = len(doc.page_content)
                    
                documents.extend(docs)
        
        return documents
    
    def chunk_documents(self, documents: List[Dict]) -> List[Dict]:
        """Chunk documents with overlap for context preservation"""
        chunks = []
        
        for doc in documents:
            # Split into chunks
            text_chunks = self.splitter.split_text(doc.page_content)
            
            for i, chunk in enumerate(text_chunks):
                chunk_id = self._generate_chunk_id(doc.metadata['source'], i)
                
                chunks.append({
                    'chunk_id': chunk_id,
                    'text': chunk,
                    'metadata': {
                        **doc.metadata,
                        'chunk_index': i,
                        'total_chunks': len(text_chunks)
                    }
                })
        
        return chunks
    
    def _generate_chunk_id(self, source: str, index: int) -> str:
        """Generate unique chunk ID"""
        content = f"{source}_{index}"
        return hashlib.md5(content.encode()).hexdigest()
```

#### Step 2: Vector Store Setup

```python
# File: src/retrieval/vector_store.py

from typing import List, Dict, Tuple
import pinecone
from sentence_transformers import SentenceTransformer

class VectorStoreManager:
    """
    Manages vector database operations for RAG
    """
    
    def __init__(
        self,
        embedding_model: str = "BAAI/bge-large-en-v1.5",
        index_name: str = "production-rag"
    ):
        # Initialize embedding model
        self.embedder = SentenceTransformer(embedding_model)
        
        # Initialize Pinecone
        pinecone.init(
            api_key=os.getenv("PINECONE_API_KEY"),
            environment=os.getenv("PINECONE_ENV")
        )
        
        # Get or create index
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(
                name=index_name,
                dimension=1024,  # BGE-large dimension
                metric="cosine",
                pod_type="p1.x1"
            )
        
        self.index = pinecone.Index(index_name)
    
    def embed_and_store(self, chunks: List[Dict], batch_size: int = 100):
        """
        Embed chunks and store in vector database
        """
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            
            # Generate embeddings
            texts = [chunk['text'] for chunk in batch]
            embeddings = self.embedder.encode(texts, show_progress_bar=True)
            
            # Prepare upsert data
            vectors = []
            for chunk, embedding in zip(batch, embeddings):
                vectors.append({
                    'id': chunk['chunk_id'],
                    'values': embedding.tolist(),
                    'metadata': {
                        'text': chunk['text'],
                        **chunk['metadata']
                    }
                })
            
            # Upsert to Pinecone
            self.index.upsert(vectors=vectors)
            
            print(f"Uploaded batch {i//batch_size + 1}")
    
    def hybrid_search(
        self,
        query: str,
        top_k: int = 20,
        metadata_filter: Dict = None
    ) -> List[Dict]:
        """
        Perform hybrid search (vector + keyword)
        """
        # 1. Vector search
        query_embedding = self.embedder.encode(query)
        
        vector_results = self.index.query(
            vector=query_embedding.tolist(),
            top_k=top_k,
            include_metadata=True,
            filter=metadata_filter
        )
        
        # 2. BM25 keyword search (using metadata text)
        # In production, maintain separate Elasticsearch/BM25 index
        
        # 3. Reciprocal Rank Fusion (simplified here)
        return vector_results['matches']
```

#### Step 3: Retrieval with Re-Ranking

```python
# File: src/retrieval/reranker.py

from sentence_transformers import CrossEncoder
from typing import List, Dict, Tuple

class ReRanker:
    """
    Re-ranks retrieved chunks using cross-encoder
    """
    
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-12-v2"):
        self.model = CrossEncoder(model_name)
    
    def rerank(
        self,
        query: str,
        chunks: List[Dict],
        top_k: int = 3
    ) -> List[Tuple[Dict, float]]:
        """
        Re-rank chunks and return top-K with scores
        """
        # Prepare pairs for cross-encoder
        pairs = [[query, chunk['metadata']['text']] for chunk in chunks]
        
        # Get scores
        scores = self.model.predict(pairs)
        
        # Combine chunks with scores
        ranked = list(zip(chunks, scores))
        
        # Sort by score (descending)
        ranked.sort(key=lambda x: x[1], reverse=True)
        
        return ranked[:top_k]
```

#### Step 4: RAG Query Pipeline

```python
# File: src/core/rag_pipeline.py

from typing import List, Dict
import openai

class RAGPipeline:
    """
    Complete RAG query execution pipeline
    """
    
    def __init__(
        self,
        vector_store: VectorStoreManager,
        reranker: ReRanker,
        llm_model: str = "gpt-4o"
    ):
        self.vector_store = vector_store
        self.reranker = reranker
        self.llm_model = llm_model
        self.client = openai.OpenAI()
    
    def query(
        self,
        user_query: str,
        top_k_retrieve: int = 20,
        top_k_rerank: int = 3,
        stream: bool = True
    ):
        """
        Execute full RAG pipeline
        """
        # Step 1: Retrieve candidates
        candidates = self.vector_store.hybrid_search(
            query=user_query,
            top_k=top_k_retrieve
        )
        
        # Step 2: Re-rank
        reranked = self.reranker.rerank(
            query=user_query,
            chunks=candidates,
            top_k=top_k_rerank
        )
        
        # Step 3: Build context
        context = "\n\n".join([
            f"Document {i+1}: {chunk['metadata']['text']}"
            for i, (chunk, score) in enumerate(reranked)
        ])
        
        # Step 4: Construct prompt
        system_prompt = """You are a helpful assistant that answers questions based on provided context.
        
Rules:
1. ONLY use information from the provided context
2. If the answer is not in the context, say "I don't have enough information"
3. Cite document numbers when making claims
4. Be concise and accurate"""
        
        user_prompt = f"""Context:
{context}

Question: {user_query}

Answer:"""
        
        # Step 5: Generate response
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        if stream:
            return self._stream_response(messages)
        else:
            response = self.client.chat.completions.create(
                model=self.llm_model,
                messages=messages,
                temperature=0.1
            )
            return response.choices[0].message.content
    
    def _stream_response(self, messages):
        """Stream response for better UX"""
        stream = self.client.chat.completions.create(
            model=self.llm_model,
            messages=messages,
            temperature=0.1,
            stream=True
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
```

### 5.3 EVALUATION PIPELINE

```python
# File: src/evaluation/ragas_eval.py

from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)
from datasets import Dataset

class RAGEvaluator:
    """
    Evaluate RAG system using RAGAS metrics
    """
    
    def __init__(self, golden_dataset_path: str):
        self.golden_dataset = self._load_golden_dataset(golden_dataset_path)
    
    def evaluate_system(self, rag_pipeline: RAGPipeline):
        """
        Run evaluation on golden dataset
        """
        results = []
        
        for item in self.golden_dataset:
            # Get RAG response
            response = rag_pipeline.query(
                user_query=item['question'],
                stream=False
            )
            
            # Get retrieved contexts
            candidates = rag_pipeline.vector_store.hybrid_search(
                query=item['question'],
                top_k=3
            )
            contexts = [c['metadata']['text'] for c in candidates]
            
            results.append({
                'question': item['question'],
                'answer': response,
                'contexts': contexts,
                'ground_truth': item['ground_truth']
            })
        
        # Convert to Dataset
        dataset = Dataset.from_list(results)
        
        # Evaluate
        scores = evaluate(
            dataset,
            metrics=[
                faithfulness,
                answer_relevancy,
                context_precision,
                context_recall
            ]
        )
        
        return scores
```

### 5.4 RAG DEPLOYMENT CHECKLIST

```markdown
## RAG Production Checklist

### Data Preparation
- [ ] Documents cleaned and deduplicated
- [ ] Optimal chunk size determined (test 200, 500, 1000 tokens)
- [ ] Chunk overlap configured (10-15% of chunk size)
- [ ] Metadata extracted (source, date, category)
- [ ] Test dataset created (100+ Q&A pairs)

### Vector Store
- [ ] Embedding model selected
  - [ ] General: BAAI/bge-large-en-v1.5
  - [ ] Code: Salesforce/codet5p-embedding
  - [ ] Domain-specific: Fine-tuned model
- [ ] Vector DB provisioned (Pinecone/Weaviate/Chroma)
- [ ] Index dimensionality matches embedding model
- [ ] Backup strategy in place
- [ ] Index versioning implemented

### Retrieval
- [ ] Hybrid search configured (vector + BM25)
- [ ] Re-ranker model deployed
- [ ] Metadata filtering tested
- [ ] Top-K values optimized (typically 3-5 final chunks)
- [ ] Retrieval latency < 200ms

### Generation
- [ ] LLM model selected (GPT-4o, Claude, Llama)
- [ ] System prompt engineered and tested
- [ ] Temperature optimized (0.0-0.3 for factual)
- [ ] Streaming enabled
- [ ] Citation mechanism implemented

### Quality
- [ ] RAGAS scores baseline: Faithfulness > 0.8
- [ ] Hallucination rate < 5%
- [ ] Answer relevancy > 0.85
- [ ] Human evaluation on 50 samples

### Performance
- [ ] End-to-end latency < 2s (p95)
- [ ] Concurrent user testing (target load)
- [ ] Caching strategy implemented
- [ ] Rate limiting configured

### Monitoring
- [ ] Query logging enabled
- [ ] Retrieval quality tracking
- [ ] Token usage monitoring
- [ ] Error rate alerts (<1%)
```

---

## 6. COMPLETE AGENTIC RAG WORKFLOW

### 6.1 ARCHITECTURE OVERVIEW

```
┌─────────────┐
│   User      │
│   Query     │
└──────┬──────┘
       │
       v
┌──────────────────────────────────────────┐
│  AGENTIC CONTROLLER                      │
│  "Should I search? Which source?"        │
└──────┬───────────────────────────────────┘
       │
       ├─────────────┬─────────────┬──────────────┐
       │             │             │              │
       v             v             v              v
┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
│ Internal│   │  Web    │   │ Database│   │  API    │
│  Docs   │   │ Search  │   │ Query   │   │ Call    │
│  (RAG)  │   │ Tool    │   │ Tool    │   │ Tool    │
└────┬────┘   └────┬────┘   └────┬────┘   └────┬────┘
     │             │             │              │
     └─────────────┴─────────────┴──────────────┘
                   │
                   v
          ┌────────────────┐
          │ SELF-CORRECT   │
          │ "Is this good? │
          │  Try again?"   │
          └────────┬───────┘
                   │
                   v
            ┌─────────────┐
            │   Final     │
            │  Response   │
            └─────────────┘
```

### 6.2 IMPLEMENTATION

#### Step 1: Query Routing Agent

```python
# File: src/agents/query_router.py

from typing import Literal, Dict
from pydantic import BaseModel
import openai

class QueryRoute(BaseModel):
    """Structured output for query routing"""
    reasoning: str
    route: Literal["internal_docs", "web_search", "database", "hybrid"]
    confidence: float

class QueryRouter:
    """
    Decides which data source(s) to query
    """
    
    def __init__(self, llm_model: str = "gpt-4o"):
        self.client = openai.OpenAI()
        self.model = llm_model
    
    def route_query(self, user_query: str, available_sources: list) -> QueryRoute:
        """
        Determine which source to query
        """
        system_prompt = f"""You are a query routing agent. Analyze the user's question and decide which data source to use.

Available sources:
- internal_docs: Company documents, policies, procedures (last updated: current)
- web_search: Real-time web search for recent information
- database: SQL database with structured data
- hybrid: Multiple sources needed

Consider:
1. Is this about company-specific information? → internal_docs
2. Is this about recent events/news? → web_search
3. Is this about data analysis/statistics? → database
4. Is this complex and needs multiple sources? → hybrid

Return a JSON object with:
{{
  "reasoning": "explanation of why you chose this route",
  "route": "one of the available sources",
  "confidence": float between 0 and 1
}}"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Query: {user_query}"}
            ],
            response_format={"type": "json_object"},
            temperature=0.1
        )
        
        route_decision = QueryRoute.parse_raw(response.choices[0].message.content)
        return route_decision
```

#### Step 2: Self-Correcting Search Agent

```python
# File: src/agents/search_agent.py

from typing import List, Dict, Optional
import openai

class SearchAgent:
    """
    Performs iterative search with self-correction
    """
    
    def __init__(
        self,
        rag_pipeline: RAGPipeline,
        max_iterations: int = 3
    ):
        self.rag_pipeline = rag_pipeline
        self.max_iterations = max_iterations
        self.client = openai.OpenAI()
    
    def search_with_correction(
        self,
        original_query: str
    ) -> Dict:
        """
        Search, evaluate, and retry if needed
        """
        history = []
        
        for iteration in range(self.max_iterations):
            # Generate search query
            if iteration == 0:
                search_query = original_query
            else:
                # Refine query based on previous results
                search_query = self._refine_query(
                    original_query,
                    history
                )
            
            # Execute search
            results = self.rag_pipeline.query(
                user_query=search_query,
                stream=False
            )
            
            # Self-evaluate
            evaluation = self._evaluate_results(
                original_query,
                results
            )
            
            history.append({
                'iteration': iteration,
                'search_query': search_query,
                'results': results,
                'evaluation': evaluation
            })
            
            # Check if results are satisfactory
            if evaluation['is_satisfactory']:
                return {
                    'answer': results,
                    'iterations': iteration + 1,
                    'history': history
                }
        
        # Max iterations reached
        return {
            'answer': "I couldn't find a satisfactory answer after multiple attempts.",
            'iterations': self.max_iterations,
            'history': history
        }
    
    def _evaluate_results(
        self,
        query: str,
        results: str
    ) -> Dict:
        """
        LLM judges if results answer the query
        """
        evaluation_prompt = f"""Evaluate if the following answer adequately addresses the question.

Question: {query}

Answer: {results}

Provide a JSON response:
{{
  "is_satisfactory": true/false,
  "missing_information": "what's missing if unsatisfactory",
  "confidence": float between 0 and 1
}}"""
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": evaluation_prompt}],
            response_format={"type": "json_object"},
            temperature=0.1
        )
        
        return json.loads(response.choices[0].message.content)
    
    def _refine_query(
        self,
        original_query: str,
        history: List[Dict]
    ) -> str:
        """
        Refine search query based on what's missing
        """
        last_eval = history[-1]['evaluation']
        
        refinement_prompt = f"""The previous search didn't fully answer the question.

Original Question: {original_query}
Missing Information: {last_eval['missing_information']}

Generate a refined search query that specifically targets the missing information."""
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": refinement_prompt}],
            temperature=0.3
        )
        
        return response.choices[0].message.content
```

#### Step 3: Agentic RAG Orchestrator

```python
# File: src/agents/agentic_rag.py

from typing import Dict, List
import openai

class AgenticRAG:
    """
    Orchestrates intelligent multi-source retrieval
    """
    
    def __init__(
        self,
        query_router: QueryRouter,
        search_agent: SearchAgent,
        web_search_tool: Optional[callable] = None
    ):
        self.router = query_router
        self.search_agent = search_agent
        self.web_search = web_search_tool
        self.client = openai.OpenAI()
    
    def answer_query(self, user_query: str) -> Dict:
        """
        Main entry point for agentic RAG
        """
        # Step 1: Route the query
        route = self.router.route_query(user_query, ["internal_docs", "web_search"])
        
        print(f"Routing Decision: {route.route} (confidence: {route.confidence})")
        
        results = []
        
        # Step 2: Execute based on route
        if route.route == "internal_docs":
            result = self.search_agent.search_with_correction(user_query)
            results.append({
                'source': 'internal_docs',
                'content': result['answer']
            })
        
        elif route.route == "web_search":
            # Use web search tool
            if self.web_search:
                web_results = self.web_search(user_query)
                results.append({
                    'source': 'web_search',
                    'content': web_results
                })
        
        elif route.route == "hybrid":
            # Search both sources
            internal_result = self.search_agent.search_with_correction(user_query)
            results.append({
                'source': 'internal_docs',
                'content': internal_result['answer']
            })
            
            if self.web_search:
                web_results = self.web_search(user_query)
                results.append({
                    'source': 'web_search',
                    'content': web_results
                })
        
        # Step 3: Synthesize final answer
        final_answer = self._synthesize_answer(user_query, results)
        
        return {
            'answer': final_answer,
            'sources': results,
            'routing': route.dict()
        }
    
    def _synthesize_answer(
        self,
        query: str,
        sources: List[Dict]
    ) -> str:
        """
        Combine information from multiple sources
        """
        context = "\n\n".join([
            f"[{source['source'].upper()}]\n{source['content']}"
            for source in sources
        ])
        
        synthesis_prompt = f"""Synthesize a comprehensive answer from multiple sources.

Question: {query}

Sources:
{context}

Provide a unified answer that:
1. Combines information from all sources
2. Cites which source each fact comes from
3. Resolves any conflicts between sources"""
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": synthesis_prompt}],
            temperature=0.2
        )
        
        return response.choices[0].message.content
```

### 6.3 AGENTIC RAG DEPLOYMENT

```markdown
## Agentic RAG Checklist

### Agent Configuration
- [ ] Query router prompt engineered
- [ ] Maximum iterations configured (typically 2-3)
- [ ] Evaluation criteria defined
- [ ] Confidence thresholds set

### Multi-Source Integration
- [ ] Internal RAG pipeline tested
- [ ] Web search API configured (Tavily/SerpAPI)
- [ ] Database connectors ready
- [ ] Source priority defined

### Self-Correction
- [ ] Evaluation LLM selected (GPT-4o recommended)
- [ ] Feedback loop tested
- [ ] Query refinement logic validated
- [ ] Termination conditions clear

### Performance
- [ ] Multi-iteration latency acceptable (<10s total)
- [ ] Cost per query calculated (multiple LLM calls)
- [ ] Caching strategy for repeated queries
- [ ] Async execution for parallel searches

### Monitoring
- [ ] Routing decisions logged
- [ ] Iteration counts tracked
- [ ] Source usage metrics
- [ ] Satisfaction rates monitored
```

---

## 7. COMPLETE AI AGENT WORKFLOW

### 7.1 ARCHITECTURE OVERVIEW

```
┌─────────────┐
│    Goal     │
│ "Book a mtg │
│  with X"    │
└──────┬──────┘
       │
       v
┌──────────────────────────────────────────┐
│  PLANNING PHASE (ReAct)                  │
│  Thought: "I need X's availability"      │
│  Action: check_calendar                  │
└──────┬───────────────────────────────────┘
       │
       v
┌──────────────────────────────────────────┐
│  TOOL EXECUTION                          │
│  ├─ Calendar API call                    │
│  └─ Result: Available times              │
└──────┬───────────────────────────────────┘
       │
       v
┌──────────────────────────────────────────┐
│  OBSERVATION PHASE                       │
│  "X is free Mon 2pm or Tue 10am"         │
└──────┬───────────────────────────────────┘
       │
       v
┌──────────────────────────────────────────┐
│  NEXT ACTION (Iteration)                 │
│  Thought: "Need to propose time"         │
│  Action: send_email                      │
└──────┬───────────────────────────────────┘
       │
       v
┌──────────────────────────────────────────┐
│  VERIFICATION                            │
│  "Meeting invite sent successfully"      │
└──────┬───────────────────────────────────┘
       │
       v
┌─────────────┐
│   Goal      │
│ Completed   │
└─────────────┘
```

### 7.2 IMPLEMENTATION

#### Step 1: Tool Definitions

```python
# File: src/tools/calendar.py

from typing import List, Dict, Optional
from datetime import datetime, timedelta
import json

class CalendarTool:
    """
    Calendar API wrapper for agent
    """
    
    def __init__(self, api_client):
        self.client = api_client
    
    def get_definition(self) -> Dict:
        """
        Tool definition for LLM function calling
        """
        return {
            "type": "function",
            "function": {
                "name": "check_calendar",
                "description": "Check someone's calendar availability for scheduling meetings",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "person_email": {
                            "type": "string",
                            "description": "Email address of the person"
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date in YYYY-MM-DD format"
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date in YYYY-MM-DD format"
                        },
                        "duration_minutes": {
                            "type": "integer",
                            "description": "Meeting duration in minutes",
                            "default": 30
                        }
                    },
                    "required": ["person_email", "start_date", "end_date"]
                }
            }
        }
    
    def execute(
        self,
        person_email: str,
        start_date: str,
        end_date: str,
        duration_minutes: int = 30
    ) -> Dict:
        """
        Execute calendar check
        """
        try:
            # Call actual calendar API
            available_slots = self.client.find_free_slots(
                email=person_email,
                start=start_date,
                end=end_date,
                duration=duration_minutes
            )
            
            return {
                "success": True,
                "available_slots": available_slots
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

# File: src/tools/email.py

class EmailTool:
    """
    Email sending tool for agent
    """
    
    def get_definition(self) -> Dict:
        return {
            "type": "function",
            "function": {
                "name": "send_email",
                "description": "Send an email to someone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "to_email": {
                            "type": "string",
                            "description": "Recipient email address"
                        },
                        "subject": {
                            "type": "string",
                            "description": "Email subject line"
                        },
                        "body": {
                            "type": "string",
                            "description": "Email body content"
                        }
                    },
                    "required": ["to_email", "subject", "body"]
                }
            }
        }
    
    def execute(self, to_email: str, subject: str, body: str) -> Dict:
        """
        Send email
        """
        try:
            # Call actual email API
            result = self.client.send(
                to=to_email,
                subject=subject,
                html_body=body
            )
            
            return {
                "success": True,
                "message_id": result.id
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
```

#### Step 2: ReAct Agent Loop

```python
# File: src/agents/react_agent.py

from typing import List, Dict, Callable
import openai
import json

class ReActAgent:
    """
    Reasoning + Acting agent using function calling
    """
    
    def __init__(
        self,
        llm_model: str = "gpt-4o",
        max_iterations: int = 10
    ):
        self.client = openai.OpenAI()
        self.model = llm_model
        self.max_iterations = max_iterations
        self.tools = {}
        self.conversation_history = []
    
    def register_tool(self, name: str, tool: object):
        """
        Register a tool for the agent to use
        """
        self.tools[name] = tool
    
    def run(self, goal: str) -> Dict:
        """
        Execute agent loop to achieve goal
        """
        # Initialize conversation
        self.conversation_history = [
            {
                "role": "system",
                "content": """You are a helpful AI assistant that can use tools to accomplish tasks.

Follow the ReAct pattern:
1. Thought: Analyze what needs to be done
2. Action: Choose and execute a tool
3. Observation: See the result
4. Repeat until goal is achieved

When the goal is complete, respond with "GOAL_COMPLETE: <summary of what was accomplished>" """
            },
            {
                "role": "user",
                "content": f"Goal: {goal}"
            }
        ]
        
        trajectory = []
        
        for iteration in range(self.max_iterations):
            print(f"\n=== Iteration {iteration + 1} ===")
            
            # Get LLM response with tool calling
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                tools=self._get_tool_definitions(),
                tool_choice="auto",
                temperature=0.1
            )
            
            message = response.choices[0].message
            
            # Add to history
            self.conversation_history.append(message)
            
            # Check if agent wants to use a tool
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    tool_name = tool_call.function.name
                    tool_args = json.loads(tool_call.function.arguments)
                    
                    print(f"Action: {tool_name}({tool_args})")
                    
                    # Execute tool
                    result = self._execute_tool(tool_name, tool_args)
                    
                    print(f"Observation: {result}")
                    
                    # Add tool result to conversation
                    self.conversation_history.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": tool_name,
                        "content": json.dumps(result)
                    })
                    
                    trajectory.append({
                        'iteration': iteration,
                        'thought': message.content or "",
                        'action': tool_name,
                        'arguments': tool_args,
                        'observation': result
                    })
            
            # Check if goal is complete
            elif message.content and "GOAL_COMPLETE" in message.content:
                print(f"\n✓ {message.content}")
                return {
                    'success': True,
                    'final_response': message.content,
                    'iterations': iteration + 1,
                    'trajectory': trajectory
                }
            
            # Continue thinking
            else:
                print(f"Thought: {message.content}")
        
        # Max iterations reached
        return {
            'success': False,
            'error': 'Maximum iterations reached',
            'iterations': self.max_iterations,
            'trajectory': trajectory
        }
    
    def _get_tool_definitions(self) -> List[Dict]:
        """
        Get OpenAI function definitions for all tools
        """
        return [tool.get_definition() for tool in self.tools.values()]
    
    def _execute_tool(self, tool_name: str, arguments: Dict) -> Dict:
        """
        Execute a registered tool
        """
        if tool_name not in self.tools:
            return {"error": f"Tool {tool_name} not found"}
        
        try:
            return self.tools[tool_name].execute(**arguments)
        except Exception as e:
            return {"error": str(e)}
```

#### Step 3: Agent with Memory

```python
# File: src/agents/memory.py

from typing import List, Dict
import chromadb

class AgentMemory:
    """
    Long-term memory for agent using vector storage
    """
    
    def __init__(self, collection_name: str = "agent_memory"):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )
    
    def store(self, key: str, content: str, metadata: Dict = None):
        """
        Store a memory
        """
        self.collection.add(
            ids=[key],
            documents=[content],
            metadatas=[metadata] if metadata else None
        )
    
    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Retrieve relevant memories
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )
        
        return [
            {
                'content': doc,
                'metadata': meta
            }
            for doc, meta in zip(
                results['documents'][0],
                results['metadatas'][0]
            )
        ]
```

### 7.3 AGENT DEPLOYMENT

```markdown
## AI Agent Checklist

### Tool Preparation
- [ ] All tools have clear definitions
- [ ] Tool error handling implemented
- [ ] Tool authentication configured
- [ ] Tool rate limits understood
- [ ] Sandbox environment for testing

### Agent Configuration
- [ ] System prompt engineered
- [ ] Maximum iterations set (typically 5-10)
- [ ] Termination conditions defined
- [ ] Memory system configured (if needed)

### Safety
- [ ] Human-in-the-loop for critical actions
- [ ] Action confirmation for irreversible operations
- [ ] Budget limits on expensive operations
- [ ] Rollback mechanisms tested

### Reliability
- [ ] Tool call success rate > 95%
- [ ] Error recovery tested
- [ ] Timeout handling implemented
- [ ] Retry logic for transient failures

### Monitoring
- [ ] Tool usage logged
- [ ] Iteration counts tracked
- [ ] Goal completion rate measured
- [ ] Cost per goal calculated
```

---

## 8. COMPLETE MULTI-AGENT SYSTEM WORKFLOW

### 8.1 ARCHITECTURE OVERVIEW (LangGraph)

```
                    ┌──────────────┐
                    │  Supervisor  │
                    │    Agent     │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              v            v            v
        ┌─────────┐  ┌─────────┐  ┌─────────┐
        │Research │  │  Code   │  │ Review  │
        │ Agent   │  │  Agent  │  │ Agent   │
        └────┬────┘  └────┬────┘  └────┬────┘
             │            │            │
             └────────────┴────────────┘
                       │
                       v
                  ┌─────────┐
                  │ Shared  │
                  │  State  │
                  └─────────┘
```

### 8.2 IMPLEMENTATION

```python
# File: src/agents/multi_agent_system.py

from typing import TypedDict, Annotated, List, Dict
from langgraph.graph import StateGraph, END
import operator
import openai

class AgentState(TypedDict):
    """
    Shared state across all agents
    """
    task: str
    research_findings: Annotated[List[str], operator.add]
    code_drafts: Annotated[List[str], operator.add]
    review_comments: Annotated[List[str], operator.add]
    iteration_count: int
    is_complete: bool
    final_output: str

class MultiAgentSystem:
    """
    Multi-agent system using LangGraph
    """
    
    def __init__(self):
        self.client = openai.OpenAI()
        self.workflow = self._build_workflow()
    
    def _build_workflow(self) -> StateGraph:
        """
        Define the agent workflow graph
        """
        workflow = StateGraph(AgentState)
        
        # Add nodes (agents)
        workflow.add_node("supervisor", self.supervisor_node)
        workflow.add_node("researcher", self.researcher_node)
        workflow.add_node("coder", self.coder_node)
        workflow.add_node("reviewer", self.reviewer_node)
        
        # Define edges (workflow)
        workflow.set_entry_point("supervisor")
        
        workflow.add_conditional_edges(
            "supervisor",
            self.route_next_agent,
            {
                "researcher": "researcher",
                "coder": "coder",
                "reviewer": "reviewer",
                "complete": END
            }
        )
        
        # All agents report back to supervisor
        workflow.add_edge("researcher", "supervisor")
        workflow.add_edge("coder", "supervisor")
        workflow.add_edge("reviewer", "supervisor")
        
        return workflow.compile()
    
    def supervisor_node(self, state: AgentState) -> AgentState:
        """
        Supervisor decides which agent should work next
        """
        print(f"\n[SUPERVISOR] Iteration {state['iteration_count']}")
        
        # Analyze current state
        prompt = f"""You are the supervisor of a software development team.

Current Task: {state['task']}

Current Progress:
- Research: {len(state['research_findings'])} findings
- Code: {len(state['code_drafts'])} drafts
- Reviews: {len(state['review_comments'])} comments

Decide what to do next:
1. "researcher" - if we need more information
2. "coder" - if we need to write/update code
3. "reviewer" - if we need to review the code
4. "complete" - if the task is done

Return JSON: {{"next_agent": "...", "reasoning": "..."}}"""
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.1
        )
        
        decision = json.loads(response.choices[0].message.content)
        
        print(f"Decision: {decision['next_agent']} - {decision['reasoning']}")
        
        # Store decision in state
        state['supervisor_decision'] = decision['next_agent']
        state['iteration_count'] += 1
        
        return state
    
    def researcher_node(self, state: AgentState) -> AgentState:
        """
        Researcher agent gathers information
        """
        print("\n[RESEARCHER] Conducting research...")
        
        prompt = f"""Research the following task: {state['task']}

Provide key findings, best practices, and relevant information."""
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        
        findings = response.choices[0].message.content
        state['research_findings'].append(findings)
        
        print(f"Research complete: {len(findings)} characters")
        
        return state
    
    def coder_node(self, state: AgentState) -> AgentState:
        """
        Coder agent writes code based on research
        """
        print("\n[CODER] Writing code...")
        
        research_context = "\n\n".join(state['research_findings'])
        review_feedback = "\n\n".join(state['review_comments'])
        
        prompt = f"""Task: {state['task']}

Research Findings:
{research_context}

Review Feedback (if any):
{review_feedback}

Write clean, production-ready code."""
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        
        code = response.choices[0].message.content
        state['code_drafts'].append(code)
        
        print(f"Code draft #{len(state['code_drafts'])} complete")
        
        return state
    
    def reviewer_node(self, state: AgentState) -> AgentState:
        """
        Reviewer agent critiques the code
        """
        print("\n[REVIEWER] Reviewing code...")
        
        latest_code = state['code_drafts'][-1]
        
        prompt = f"""Review this code for:
1. Correctness
2. Best practices
3. Security
4. Performance

Code:
{latest_code}

Provide specific feedback or approve if ready."""
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        
        review = response.choices[0].message.content
        state['review_comments'].append(review)
        
        # Check if approved
        if "APPROVED" in review.upper() or "LOOKS GOOD" in review.upper():
            state['is_complete'] = True
            state['final_output'] = latest_code
        
        print(f"Review complete")
        
        return state
    
    def route_next_agent(self, state: AgentState) -> str:
        """
        Routing function for conditional edges
        """
        if state['is_complete']:
            return "complete"
        
        # Prevent infinite loops
        if state['iteration_count'] > 10:
            print("Max iterations reached")
            state['is_complete'] = True
            return "complete"
        
        return state.get('supervisor_decision', "researcher")
    
    def run(self, task: str) -> Dict:
        """
        Execute the multi-agent workflow
        """
        # Initialize state
        initial_state = {
            "task": task,
            "research_findings": [],
            "code_drafts": [],
            "review_comments": [],
            "iteration_count": 0,
            "is_complete": False,
            "final_output": ""
        }
        
        # Run workflow
        final_state = self.workflow.invoke(initial_state)
        
        return {
            'success': final_state['is_complete'],
            'final_output': final_state['final_output'],
            'iterations': final_state['iteration_count'],
            'research_findings': final_state['research_findings'],
            'code_drafts': final_state['code_drafts'],
            'review_comments': final_state['review_comments']
        }
```

### 8.3 MULTI-AGENT DEPLOYMENT

```markdown
## Multi-Agent System Checklist

### Graph Design
- [ ] State schema defined (TypedDict)
- [ ] All nodes (agents) implemented
- [ ] Edge conditions clear
- [ ] Termination conditions set
- [ ] Max iteration limit configured

### State Management
- [ ] State persistence configured (checkpointer)
- [ ] State size monitored (grows with iterations)
- [ ] State pruning strategy defined
- [ ] Rollback capability tested

### Agent Coordination
- [ ] Communication protocol defined
- [ ] Supervisor logic tested
- [ ] Parallel execution where possible
- [ ] Deadlock prevention implemented

### Performance
- [ ] Total workflow latency acceptable
- [ ] Token usage per iteration tracked
- [ ] Concurrent agent execution optimized
- [ ] Caching for repeated operations

### Quality
- [ ] Agent specialization validated
- [ ] Inter-agent consistency checked
- [ ] Final output quality measured
- [ ] Human-in-loop for critical decisions
```

---

## 9. COMPLETE FINE-TUNING WORKFLOW

### 9.1 WHEN TO FINE-TUNE

**Decision Matrix:**

| Scenario | Solution |
|----------|----------|
| Need up-to-date facts | ❌ Fine-Tuning → ✅ RAG |
| Need specific writing style | ✅ Fine-Tuning |
| Need to output complex JSON schema | ✅ Fine-Tuning |
| Need domain-specific terminology | ✅ Fine-Tuning |
| Need cost reduction (vs API) | ✅ Fine-Tuning + Local Hosting |
| Need privacy/data sovereignty | ✅ Fine-Tuning + Local Hosting |

### 9.2 COMPLETE WORKFLOW

```
Step 1: Data Collection & Cleaning
├─ Collect 500-10,000 examples
├─ Format: (Instruction, Output) pairs
├─ Validate quality
└─ Remove duplicates

Step 2: Format for SFT (Supervised Fine-Tuning)
├─ Convert to conversational format
├─ Add system prompts
└─ Split train/validation (90/10)

Step 3: Choose Base Model
├─ Llama 3 8B (General purpose)
├─ Mistral 7B (Speed + Quality)
├─ Phi-3 (Small + Efficient)
└─ CodeLlama (Coding tasks)

Step 4: Configure LoRA
├─ Rank (r): 8-16
├─ Alpha: 16-32
├─ Target modules: q_proj, v_proj
└─ Dropout: 0.05-0.1

Step 5: Training
├─ Learning rate: 2e-4
├─ Batch size: 4-8 (with gradient accumulation)
├─ Epochs: 1-3
├─ Use QLoRA for 4-bit precision
└─ Monitor validation loss

Step 6: Evaluation
├─ Test on held-out dataset
├─ LLM-as-judge comparison
├─ Human evaluation (50 samples)
└─ Compare to base model

Step 7: Merge & Deploy
├─ Merge LoRA into base weights
├─ Quantize to 4-bit (optional)
├─ Test inference speed
└─ Deploy with vLLM/TensorRT
```

### 9.3 IMPLEMENTATION

```python
# File: scripts/fine_tune_lora.py

from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer
import torch

class FineTuningPipeline:
    """
    Complete fine-tuning workflow using LoRA/QLoRA
    """
    
    def __init__(
        self,
        base_model: str = "meta-llama/Llama-3.1-8B",
        use_qlora: bool = True
    ):
        self.base_model = base_model
        self.use_qlora = use_qlora
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(base_model)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "right"
    
    def prepare_dataset(self, dataset_path: str):
        """
        Load and format dataset for SFT
        """
        # Load dataset
        dataset = load_dataset("json", data_files=dataset_path)
        
        # Format for chat template
        def format_instruction(example):
            return {
                "text": f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{example['system_prompt']}<|eot_id|><|start_header_id|>user<|end_header_id|>

{example['instruction']}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

{example['output']}<|eot_id|>"""
            }
        
        formatted_dataset = dataset.map(format_instruction)
        
        # Split train/validation
        split = formatted_dataset['train'].train_test_split(test_size=0.1)
        
        return split['train'], split['test']
    
    def setup_model(self):
        """
        Load model with QLoRA configuration
        """
        if self.use_qlora:
            # 4-bit quantization config
            from transformers import BitsAndBytesConfig
            
            bnb_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16
            )
            
            model = AutoModelForCausalLM.from_pretrained(
                self.base_model,
                quantization_config=bnb_config,
                device_map="auto",
                trust_remote_code=True
            )
            
            model = prepare_model_for_kbit_training(model)
        
        else:
            model = AutoModelForCausalLM.from_pretrained(
                self.base_model,
                device_map="auto",
                torch_dtype=torch.bfloat16
            )
        
        # LoRA configuration
        lora_config = LoraConfig(
            r=16,  # Rank
            lora_alpha=32,
            target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM"
        )
        
        model = get_peft_model(model, lora_config)
        
        return model
    
    def train(
        self,
        train_dataset,
        eval_dataset,
        output_dir: str = "./fine_tuned_model",
        num_epochs: int = 3
    ):
        """
        Execute fine-tuning
        """
        model = self.setup_model()
        
        # Training arguments
        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=num_epochs,
            per_device_train_batch_size=4,
            gradient_accumulation_steps=4,
            learning_rate=2e-4,
            logging_steps=10,
            save_steps=100,
            evaluation_strategy="steps",
            eval_steps=100,
            warmup_steps=50,
            lr_scheduler_type="cosine",
            fp16=False,
            bf16=True,
            optim="paged_adamw_8bit",
            report_to="none"
        )
        
        # Trainer
        trainer = SFTTrainer(
            model=model,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            args=training_args,
            tokenizer=self.tokenizer,
            max_seq_length=2048,
            packing=False
        )
        
        # Train
        trainer.train()
        
        # Save
        trainer.save_model(output_dir)
        
        return model
    
    def merge_and_save(
        self,
        adapter_path: str,
        output_path: str
    ):
        """
        Merge LoRA adapter into base model
        """
        from peft import PeftModel
        
        # Load base model
        base_model = AutoModelForCausalLM.from_pretrained(
            self.base_model,
            torch_dtype=torch.bfloat16,
            device_map="auto"
        )
        
        # Load and merge adapter
        model = PeftModel.from_pretrained(base_model, adapter_path)
        merged_model = model.merge_and_unload()
        
        # Save merged model
        merged_model.save_pretrained(output_path)
        self.tokenizer.save_pretrained(output_path)
        
        print(f"Merged model saved to {output_path}")
```

### 9.4 DATASET PREPARATION

```python
# File: scripts/prepare_training_data.py

import json
from typing import List, Dict

def create_sft_dataset(
    examples: List[Dict],
    output_file: str = "training_data.jsonl"
):
    """
    Convert raw examples to SFT format
    
    Input format:
    {
        "instruction": "Write a product description for...",
        "output": "Introducing our premium..."
    }
    
    Output format (Llama 3 chat template):
    {
        "system_prompt": "You are a helpful assistant.",
        "instruction": "...",
        "output": "..."
    }
    """
    
    formatted_examples = []
    
    for example in examples:
        formatted = {
            "system_prompt": "You are a helpful AI assistant specialized in writing compelling product descriptions.",
            "instruction": example['instruction'],
            "output": example['output']
        }
        formatted_examples.append(formatted)
    
    # Save as JSONL
    with open(output_file, 'w') as f:
        for example in formatted_examples:
            f.write(json.dumps(example) + '\n')
    
    print(f"Saved {len(formatted_examples)} examples to {output_file}")
```

### 9.5 EVALUATION

```python
# File: src/evaluation/fine_tune_eval.py

import openai
from typing import List, Dict

class FineTuneEvaluator:
    """
    Evaluate fine-tuned model vs base model
    """
    
    def __init__(self):
        self.client = openai.OpenAI()
    
    def compare_models(
        self,
        test_prompts: List[str],
        base_model: str,
        fine_tuned_model: str
    ) -> Dict:
        """
        Use LLM-as-judge to compare outputs
        """
        results = []
        
        for prompt in test_prompts:
            # Get base model response
            base_response = self._generate(base_model, prompt)
            
            # Get fine-tuned model response
            ft_response = self._generate(fine_tuned_model, prompt)
            
            # Judge comparison
            judgment = self._judge_outputs(
                prompt,
                base_response,
                ft_response
            )
            
            results.append({
                'prompt': prompt,
                'base_output': base_response,
                'fine_tuned_output': ft_response,
                'winner': judgment['winner'],
                'reasoning': judgment['reasoning']
            })
        
        # Calculate win rate
        ft_wins = sum(1 for r in results if r['winner'] == 'fine_tuned')
        win_rate = ft_wins / len(results)
        
        return {
            'win_rate': win_rate,
            'results': results
        }
    
    def _judge_outputs(
        self,
        prompt: str,
        output_a: str,
        output_b: str
    ) -> Dict:
        """
        LLM judges which output is better
        """
        judge_prompt = f"""Compare these two responses to the same prompt.

Prompt: {prompt}

Response A:
{output_a}

Response B:
{output_b}

Which response is better? Consider:
1. Accuracy
2. Helpfulness
3. Clarity
4. Style consistency

Return JSON: {{"winner": "A" or "B", "reasoning": "..."}}"""
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": judge_prompt}],
            response_format={"type": "json_object"}
        )
        
        judgment = json.loads(response.choices[0].message.content)
        judgment['winner'] = 'fine_tuned' if judgment['winner'] == 'B' else 'base'
        
        return judgment
```

### 9.6 FINE-TUNING CHECKLIST

```markdown
## Fine-Tuning Deployment Checklist

### Data Preparation
- [ ] 500+ high-quality examples collected
- [ ] Data cleaned and deduplicated
- [ ] Consistent formatting verified
- [ ] Train/validation split (90/10)
- [ ] Diversity in examples ensured

### Model Selection
- [ ] Base model chosen based on task
- [ ] License compatible with use case
- [ ] Model size fits available GPU
- [ ] Tokenizer tested with sample data

### Training Configuration
- [ ] LoRA rank determined (8-16 typical)
- [ ] Learning rate set (2e-4 typical)
- [ ] Batch size & gradient accumulation configured
- [ ] Number of epochs decided (1-3 typical)
- [ ] Warmup steps configured

### Quality Assurance
- [ ] Validation loss monitored during training
- [ ] Early stopping criteria set
- [ ] Overfitting checks performed
- [ ] Side-by-side comparison with base model
- [ ] Human evaluation on 50+ samples

### Deployment
- [ ] Adapter merged into base weights
- [ ] Model quantized if needed (4-bit)
- [ ] Inference speed tested
- [ ] VRAM requirements verified
- [ ] API/serving infrastructure ready

### Cost Calculation
- [ ] Training cost estimated (GPU hours)
- [ ] Inference cost compared to API
- [ ] ROI calculated
- [ ] Maintenance plan defined
```

---

## 10. MODEL & RESOURCE SELECTION MATRIX

### 10.1 THE GRAND DECISION TREE

```
START: What are your priorities?

Priority 1: Data Privacy
├─ Can data leave your infrastructure?
   ├─ NO → LOCAL MODELS REQUIRED
   │  ├─ Available GPU: 24GB
   │  │  └─ Use: Llama 3.1 8B (4-bit quantized)
   │  ├─ Available GPU: 40GB
   │  │  └─ Use: Llama 3.1 70B (4-bit quantized)
   │  └─ No GPU available
   │     └─ Use: Cloud private deployment (AWS/Azure)
   └─ YES → API MODELS VIABLE
      └─ Continue to Priority 2

Priority 2: Cost Constraints
├─ Budget per 1K tokens
   ├─ <$0.001
   │  └─ Local hosting or Llama 3.1 via Together AI
   ├─ <$0.01
   │  └─ GPT-4o-mini, Claude Haiku, Gemini Flash
   └─ <$0.10
      └─ GPT-4o, Claude Sonnet, Gemini Pro
      
Priority 3: Task Complexity
├─ Simple classification/extraction
   │  └─ Small models: Llama 3.1 8B, Phi-3
├─ Complex reasoning
   │  └─ Frontier models: GPT-4o, Claude Opus, o1
├─ Long context (>100K tokens)
   │  └─ Gemini 1.5 Pro (2M context), Claude Sonnet (200K)
└─ Multimodal (vision + text)
   └─ GPT-4o, Claude Sonnet 3.5, Gemini Pro

Priority 4: Latency Requirements
├─ <500ms TTFT
   │  └─ Small local models + caching
├─ <2s acceptable
   │  └─ Standard API calls
└─ No strict requirement
   └─ Can use complex multi-step agents
```

### 10.2 DETAILED MODEL COMPARISON

#### A) API Models (Cloud-Hosted)

| Model | Provider | Cost (per 1M tokens) | Best For | Context Window | Speed |
|-------|----------|----------------------|----------|----------------|-------|
| **GPT-4o** | OpenAI | $2.50 input / $10 output | Complex reasoning, coding | 128K | Fast |
| **GPT-4o-mini** | OpenAI | $0.15 input / $0.60 output | High-volume simple tasks | 128K | Fastest |
| **o1-preview** | OpenAI | $15 input / $60 output | Advanced reasoning, math | 128K | Slow |
| **Claude Opus 4.5** | Anthropic | $15 input / $75 output | Complex analysis, research | 200K | Medium |
| **Claude Sonnet 4.5** | Anthropic | $3 input / $15 output | Balanced performance | 200K | Fast |
| **Claude Haiku 4.5** | Anthropic | $0.25 input / $1.25 output | Speed-critical tasks | 200K | Fastest |
| **Gemini 1.5 Pro** | Google | $1.25 input / $5 output | Ultra-long context | 2M | Medium |
| **Gemini Flash** | Google | $0.075 input / $0.30 output | Budget-conscious | 1M | Fast |

**When to Use API Models:**
- ✅ Rapid prototyping (1-2 days)
- ✅ No GPU infrastructure
- ✅ Variable/unpredictable load
- ✅ Need latest capabilities
- ❌ Data privacy concerns
- ❌ High-volume (>1B tokens/month)

#### B) Open-Source Models (Self-Hosted)

| Model | Parameters | VRAM (16-bit) | VRAM (4-bit) | Best For | Training Data |
|-------|------------|---------------|--------------|----------|---------------|
| **Llama 3.1 8B** | 8B | 16 GB | 5 GB | General purpose, fast | 15T tokens |
| **Llama 3.1 70B** | 70B | 140 GB | 35 GB | High-quality reasoning | 15T tokens |
| **Llama 3.1 405B** | 405B | 810 GB | 200 GB | Frontier capabilities | 15T tokens |
| **Mistral 7B** | 7B | 14 GB | 4 GB | Speed + quality balance | Unknown |
| **Mixtral 8x7B** | 47B | 94 GB | 24 GB | Mixture of experts | Unknown |
| **Phi-3 Mini** | 3.8B | 8 GB | 3 GB | Edge deployment | High-quality subset |
| **CodeLlama 34B** | 34B | 68 GB | 17 GB | Code generation | Code-focused |
| **Qwen 2.5 72B** | 72B | 144 GB | 36 GB | Multilingual + reasoning | 18T tokens |

**When to Use Open-Source:**
- ✅ Data must stay local
- ✅ High-volume deployment
- ✅ Need to fine-tune
- ✅ Long-term cost optimization
- ❌ Rapid iteration needed
- ❌ No GPU access

### 10.3 EMBEDDING MODELS

| Model | Dimensions | Task | MTEB Score | Speed |
|-------|------------|------|------------|-------|
| **OpenAI text-embedding-3-large** | 3072 | General | 64.6 | Fast |
| **OpenAI text-embedding-3-small** | 1536 | Budget | 62.3 | Fastest |
| **BAAI/bge-large-en-v1.5** | 1024 | Open-source general | 63.9 | Fast |
| **sentence-transformers/all-MiniLM-L6-v2** | 384 | Fast local | 56.3 | Fastest |
| **Salesforce/SFR-Embedding-Mistral** | 4096 | Long documents | 65.7 | Medium |

**Selection Guide:**
- **Speed-critical**: all-MiniLM-L6-v2
- **Best quality**: OpenAI text-embedding-3-large
- **Open-source production**: BAAI/bge-large-en-v1.5
- **Long documents**: SFR-Embedding-Mistral

### 10.4 INFRASTRUCTURE DECISION MATRIX

#### Cloud Provider Selection

| Provider | Best For | GPU Options | AI-Specific Features |
|----------|----------|-------------|----------------------|
| **AWS** | Enterprise, compliance | P4d (A100), P5 (H100) | SageMaker, Bedrock |
| **Azure** | Microsoft ecosystem | NDv4 (A100), ND H100 | OpenAI integration |
| **GCP** | Data analytics | A2 (A100), A3 (H100) | Vertex AI, TPU pods |
| **Lambda Labs** | Cost-effective training | A100, H100 | Simple, no markup |
| **Together AI** | Serverless inference | Multi-GPU clusters | Pay-per-token API |
| **RunPod** | Spot pricing | Various | Lowest cost |

#### Local vs Cloud Calculator

```python
# Simplified cost comparison

def calculate_annual_cost(
    tokens_per_month: int,
    api_cost_per_1m: float = 3.0,  # GPT-4o Sonnet avg
    local_gpu_cost: float = 15000,  # A100 40GB
    local_power_monthly: float = 200
):
    """
    Compare API vs local hosting costs
    """
    # API cost
    api_monthly = (tokens_per_month / 1_000_000) * api_cost_per_1m
    api_annual = api_monthly * 12
    
    # Local cost
    local_annual = local_gpu_cost + (local_power_monthly * 12)
    
    # Break-even point
    months_to_breakeven = local_gpu_cost / api_monthly if api_monthly > 0 else float('inf')
    
    return {
        'api_annual': api_annual,
        'local_annual': local_annual,
        'savings': api_annual - local_annual,
        'breakeven_months': months_to_breakeven
    }

# Example
result = calculate_annual_cost(
    tokens_per_month=500_000_000,  # 500M tokens/month
)

print(f"API Annual Cost: ${result['api_annual']:,.0f}")
print(f"Local Annual Cost: ${result['local_annual']:,.0f}")
print(f"Savings: ${result['savings']:,.0f}")
print(f"Breakeven: {result['breakeven_months']:.1f} months")
```

### 10.5 WHEN TO DOWNLOAD MODELS LOCALLY

**Download Locally When:**

1. **Privacy is Critical**
   - Healthcare (HIPAA compliance)
   - Finance (PCI-DSS, SOC 2)
   - Government/Defense
   - Legal documents

2. **Volume Economics Favor It**
   - Processing >500M tokens/month
   - Break-even typically at 6-12 months
   - Have predictable, consistent load

3. **Customization Needed**
   - Fine-tuning for domain-specific language
   - Need to modify model architecture
   - Research/experimentation

4. **Latency is Critical**
   - <100ms response time needed
   - Co-located with data source
   - Real-time applications

5. **Offline/Air-Gapped Deployment**
   - No internet connectivity
   - Military/secure facilities
   - Remote locations

**Use APIs When:**

1. **Speed to Market**
   - MVP/prototype in days
   - Testing product-market fit
   - Uncertain requirements

2. **Variable Load**
   - Seasonal traffic
   - Startup phase (unknown scale)
   - Pilot programs

3. **No GPU Access**
   - Small team, no DevOps
   - No capital for hardware
   - Cloud-native architecture

4. **Latest Capabilities Needed**
   - Cutting-edge reasoning (o1, etc.)
   - Multimodal features
   - Rapidly evolving requirements

### 10.6 RESOURCE REQUIREMENTS BY TECHNIQUE

| Technique | Minimum GPU | Recommended | RAM | Storage | Expertise Level |
|-----------|-------------|-------------|-----|---------|-----------------|
| **Simple Prompting** | None | None | 8 GB | 1 GB | Beginner |
| **RAG (API LLM)** | None | None | 16 GB | 50 GB | Intermediate |
| **RAG (Local LLM 8B)** | 24 GB | A100 40GB | 32 GB | 100 GB | Advanced |
| **RAG (Local LLM 70B)** | 80 GB (2xA100) | 8xA100 | 128 GB | 200 GB | Expert |
| **Agentic RAG** | None (API) | 24 GB (local) | 16 GB | 50 GB | Advanced |
| **Multi-Agent** | None (API) | 40 GB (local) | 32 GB | 100 GB | Expert |
| **Fine-Tuning (LoRA)** | 24 GB | A100 40GB | 64 GB | 200 GB | Expert |
| **Fine-Tuning (Full)** | 80 GB | 8xA100 | 256 GB | 500 GB | Expert |

---

## CONCLUSION: YOUR PRODUCTION READINESS ROADMAP

### Phase 1: Client Discovery (Week 1)
- [ ] Conduct discovery meeting using consultation framework
- [ ] Document business requirements
- [ ] Identify technique using decision tree
- [ ] Estimate budget and timeline
- [ ] Get sign-off on approach

### Phase 2: Architecture Design (Week 2)
- [ ] Design system architecture diagram
- [ ] Choose models and infrastructure
- [ ] Define data pipeline
- [ ] Create evaluation criteria
- [ ] Setup development environment

### Phase 3: MVP Development (Weeks 3-6)
- [ ] Implement core functionality
- [ ] Build golden dataset
- [ ] Setup monitoring and logging
- [ ] Conduct initial evaluation
- [ ] Iterate based on feedback

### Phase 4: Production Hardening (Weeks 7-8)
- [ ] Complete pre-deployment checklist
- [ ] Load testing and optimization
- [ ] Security audit
- [ ] Documentation finalization
- [ ] Stakeholder training

### Phase 5: Launch & Monitor (Ongoing)
- [ ] Phased rollout
- [ ] Monitor key metrics
- [ ] Collect user feedback
- [ ] Continuous improvement
- [ ] Cost optimization

---

**Remember**: The best AI system is not the one with the most advanced model, but the one that solves the business problem most effectively, reliably, and economically.

**Next Steps**:
1. Bookmark this guide
2. Pick ONE technique to master this week
3. Build a portfolio project using the folder structure
4. Document your learnings
5. Share your work publicly

You're now equipped with the complete senior developer's playbook for production AI systems. Go build something extraordinary!

---

© 2026 AI Production Master Guide | Version 1.0 | Last Updated: May 2026


---

## 11. LATENCY OPTIMIZATION

### 11.1 The Latency Stack

Every millisecond counts. Here is the complete latency breakdown for a typical RAG pipeline:

```
TOTAL LATENCY = Network + Auth + Retrieval + Reranking + LLM (TTFT + Generation)

Typical breakdown:
  Network:        10-50ms
  Auth/Rate limit: 5-20ms
  Embedding:      20-100ms
  Vector search:  10-50ms
  Reranking:      50-200ms
  LLM TTFT:      200-800ms
  LLM Generation: 500-3000ms (depends on output length)
  TOTAL:          800-4200ms
```

### 11.2 Streaming (TTFT Optimization)

Streaming reduces perceived latency by 60-80%. Users see the first token in 200-500ms instead of waiting 3-5 seconds.

```python
import asyncio
from typing import AsyncGenerator
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import AsyncOpenAI

app = FastAPI()
client = AsyncOpenAI()

@app.post("/chat/stream")
async def chat_stream(request: dict):
    async def generate() -> AsyncGenerator[str, None]:
        stream = await client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": request["query"]}],
            stream=True,
            temperature=0.1,
        )
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield f"data: {chunk.choices[0].delta.content}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")
```

### 11.3 Semantic Caching (Skip LLM Entirely)

Cache similar queries so the LLM is never called for repeated questions. Saves 30-60% of LLM calls.

```python
import hashlib
import numpy as np
from typing import Optional, Dict, Any
import redis.asyncio as redis
import json

class SemanticCache:
    """
    Cache LLM responses by semantic similarity.
    If a similar question was asked before, return the cached answer.
    Threshold 0.92 = near-exact match, 0.85 = similar meaning.
    """
    def __init__(self, redis_url: str, embedding_model, threshold: float = 0.92):
        self.redis = redis.from_url(redis_url)
        self.embedding_model = embedding_model
        self.threshold = threshold

    async def get(self, query: str) -> Optional[str]:
        query_embedding = self.embedding_model.encode(query)

        # Get all cached embeddings
        cached_keys = await self.redis.keys("semantic_cache:*")
        if not cached_keys:
            return None

        best_score = 0.0
        best_response = None

        for key in cached_keys:
            data = await self.redis.get(key)
            if data:
                entry = json.loads(data)
                cached_embedding = np.array(entry["embedding"])
                score = np.dot(query_embedding, cached_embedding) / (
                    np.linalg.norm(query_embedding) * np.linalg.norm(cached_embedding)
                )
                if score > best_score:
                    best_score = score
                    best_response = entry["response"]

        if best_score >= self.threshold:
            return best_response
        return None

    async def set(self, query: str, response: str, ttl: int = 3600):
        embedding = self.embedding_model.encode(query).tolist()
        cache_key = f"semantic_cache:{hashlib.md5(query.encode()).hexdigest()}"
        await self.redis.setex(cache_key, ttl, json.dumps({
            "query": query, "response": response, "embedding": embedding
        }))
```

### 11.4 Context Caching (KV Cache Reuse)

For repeated system prompts or long context, cache the KV states to avoid reprocessing.

```python
class ContextCache:
    """
    Cache frequently used contexts (system prompts, document sets).
    Only re-process the user query portion.
    """
    def __init__(self):
        self._cache: Dict[str, Dict] = {}

    def get_cached_prefix(self, system_prompt: str, doc_context: str) -> Optional[str]:
        key = hashlib.md5(f"{system_prompt}:{doc_context}".encode()).hexdigest()
        return self._cache.get(key, {}).get("prefix_id")

    def set_cached_prefix(self, system_prompt: str, doc_context: str, prefix_id: str):
        key = hashlib.md5(f"{system_prompt}:{doc_context}".encode()).hexdigest()
        self._cache[key] = {"prefix_id": prefix_id, "created_at": time.time()}
```

### 11.5 Prompt Compression

Reduce token count by 30-50% without losing meaning.

```python
class PromptCompressor:
    """Compress prompts to reduce tokens and latency."""
    
    def compress_context(self, context: str, target_ratio: float = 0.5) -> str:
        """Remove redundant sentences, keep key information."""
        sentences = context.split('. ')
        if len(sentences) <= 3:
            return context
        
        # Keep first and last sentences, score middle ones
        scored = []
        for i, s in enumerate(sentences[1:-1], 1):
            # Score by information density
            words = s.split()
            unique_ratio = len(set(words)) / max(len(words), 1)
            scored.append((i, s, unique_ratio))
        
        # Keep top N% by score
        keep_count = max(2, int(len(scored) * target_ratio))
        scored.sort(key=lambda x: -x[2])
        keep_indices = sorted([x[0] for x in scored[:keep_count]])
        
        result = [sentences[0]]
        for idx in keep_indices:
            result.append(sentences[idx])
        result.append(sentences[-1])
        
        return '. '.join(result)

    async def llm_compress(self, text: str, llm_client) -> str:
        """Use a small LLM to summarize/compress text."""
        response = await llm_client.generate(
            f"Compress this text to 50% length while preserving all key information:\n\n{text}",
            model="gpt-4o-mini",
            temperature=0.0
        )
        return response
```

### 11.6 Parallel Retrieval

Run embedding, vector search, and keyword search in parallel.

```python
import asyncio

class ParallelRetriever:
    """Run multiple retrieval strategies concurrently."""
    
    async def retrieve(self, query: str, strategies: list) -> list:
        tasks = [strategy.search(query) for strategy in strategies]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        all_results = []
        for result in results:
            if not isinstance(result, Exception):
                all_results.extend(result)
        
        # Deduplicate by content hash
        seen = set()
        unique = []
        for r in all_results:
            h = hashlib.md5(r["text"].encode()).hexdigest()
            if h not in seen:
                seen.add(h)
                unique.append(r)
        
        return unique
```

---

## 12. COST OPTIMIZATION

### 12.1 Model Cost Cascade Routing

Route queries to the cheapest model that can handle them. Use expensive models only when needed.

```python
from typing import Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

class QueryComplexity(Enum):
    SIMPLE = "simple"       # "What is X?" -> Haiku/3.5-turbo
    MODERATE = "moderate"   # "Explain X" -> Sonnet/GPT-4o-mini
    COMPLEX = "complex"     # "Analyze and compare X vs Y" -> Opus/GPT-4o

@dataclass
class ModelTier:
    name: str
    model: str
    provider: str
    cost_per_1k_input: float
    cost_per_1k_output: float
    quality_score: float  # 0-1

class CostOptimizedRouter:
    """
    Route to cheapest viable model. Saves 40-70% on LLM costs.

    Typical savings:
    - 60% of queries are "simple" -> $0.0002 instead of $0.01
    - 30% are "moderate" -> $0.001 instead of $0.01
    - 10% need the best model -> $0.01
    Average cost: $0.0014 instead of $0.01 (86% savings)
    """
    def __init__(self):
        self.tiers = {
            QueryComplexity.SIMPLE: ModelTier("haiku", "claude-3-haiku", "anthropic", 0.00025, 0.00125, 0.7),
            QueryComplexity.MODERATE: ModelTier("sonnet", "claude-3-5-sonnet", "anthropic", 0.003, 0.015, 0.85),
            QueryComplexity.COMPLEX: ModelTier("opus", "claude-3-opus", "anthropic", 0.015, 0.075, 0.95),
        }

    async def classify_complexity(self, query: str) -> QueryComplexity:
        """Quick heuristic classification (no LLM call needed)."""
        query_lower = query.lower()
        words = query.split()

        # Simple: short factual questions
        if len(words) < 10 and any(w in query_lower for w in ["what", "when", "where", "who", "define"]):
            return QueryComplexity.SIMPLE

        # Complex: analysis, comparison, multi-step
        complex_signals = ["analyze", "compare", "contrast", "evaluate", "design", "strategy", "research", "explain why"]
        if any(w in query_lower for w in complex_signals) or len(words) > 50:
            return QueryComplexity.COMPLEX

        return QueryComplexity.MODERATE

    async def route(self, query: str) -> ModelTier:
        complexity = await self.classify_complexity(query)
        return self.tiers[complexity]
```

### 12.2 Vector Database Cost Optimization

```python
class VectorDBCostOptimizer:
    """
    Strategies to reduce vector DB costs by 60-80%:

    1. Quantization: Use PQ/SQ8 instead of float32 (4-8x storage reduction)
    2. Tiered storage: Hot data in memory, warm on SSD, cold in object storage
    3. Index pruning: Remove low-value vectors periodically
    4. Batch operations: Batch inserts instead of individual upserts
    5. Namespace partitioning: Separate collections by access pattern
    """

    @staticmethod
    def get_pinecone_config(cost_tier: str = "balanced") -> Dict:
        configs = {
            "cost_optimized": {
                "pod_type": "s1.x1",        # Smallest pod
                "replicas": 1,
                "shards": 1,
                "index_type": "approximated",
                "metric": "cosine",
                "batch_size": 1000,          # Batch upserts
            },
            "balanced": {
                "pod_type": "p1.x1",
                "replicas": 2,
                "shards": 1,
                "index_type": "approximated",
                "metric": "cosine",
                "batch_size": 500,
            },
            "performance": {
                "pod_type": "p2.x1",
                "replicas": 3,
                "shards": 2,
                "index_type": "approximated",
                "metric": "cosine",
                "batch_size": 200,
            }
        }
        return configs.get(cost_tier, configs["balanced"])

    @staticmethod
    def get_qdrant_config(cost_tier: str = "balanced") -> Dict:
        configs = {
            "cost_optimized": {
                "on_disk_payload": True,        # Store payload on disk
                "on_disk_vectors": True,         # Store vectors on disk
                "quantization": {                # 4x storage reduction
                    "scalar": {"type": "int8", "quantile": 0.99}
                },
                "replication_factor": 1,
            },
            "balanced": {
                "on_disk_payload": True,
                "on_disk_vectors": False,
                "quantization": {
                    "scalar": {"type": "int8", "quantile": 0.99}
                },
                "replication_factor": 2,
            },
            "performance": {
                "on_disk_payload": False,
                "on_disk_vectors": False,
                "quantization": None,
                "replication_factor": 3,
            }
        }
        return configs.get(cost_tier, configs["balanced"])

    @staticmethod
    async def cleanup_stale_vectors(vector_store, min_access_count: int = 2, max_age_days: int = 90):
        """Remove vectors that haven't been accessed or contributed to results."""
        # This is provider-specific; example for a generic store
        stats = await vector_store.get_collection_stats()
        total = stats["vector_count"]
        # Keep only vectors referenced in recent search results
        # Implementation depends on your vector store
        pass
```

### 12.3 Token Optimization Strategies

```python
class TokenOptimizer:
    """Reduce token usage across the pipeline."""

    @staticmethod
    def optimize_system_prompt(prompt: str) -> str:
        """Remove filler words and redundancy from system prompts."""
        # Common bloat patterns
        replacements = [
            ("You are a helpful assistant.", "Helpful assistant."),
            ("Please make sure to", "Must"),
            ("It is important that you", "Must"),
            ("You should always", "Always"),
            ("In order to", "To"),
            ("At this point in time", "Now"),
            ("Due to the fact that", "Because"),
            ("In the event that", "If"),
        ]
        result = prompt
        for old, new in replacements:
            result = result.replace(old, new)
        return result

    @staticmethod
    def truncate_context(context: str, max_tokens: int = 4000) -> str:
        """Smart truncation: keep beginning and end, cut middle."""
        words = context.split()
        if len(words) <= max_tokens:
            return context
        # Keep first 60% and last 20%
        first_cut = int(max_tokens * 0.6)
        last_cut = int(max_tokens * 0.2)
        return " ".join(words[:first_cut]) + "\n[...truncated...]\n" + " ".join(words[-last_cut:])

    @staticmethod
    def compress_json_output(response: str) -> str:
        """If response is JSON, minimize whitespace."""
        try:
            import json
            data = json.loads(response)
            return json.dumps(data, separators=(',', ':'))
        except:
            return response
```

### 12.4 Embedding Cost Optimization

```python
class EmbeddingCostOptimizer:
    """
    Reduce embedding costs by 50-80%:
    1. Cache embeddings (never re-embed unchanged text)
    2. Batch API calls (most providers give 50% discount for batch)
    3. Use cheaper models for non-critical embeddings
    4. Deduplicate before embedding
    """

    def __init__(self, embedding_model, cache_store):
        self.model = embedding_model
        self.cache = cache_store

    async def embed_with_cache(self, texts: list) -> list:
        """Only embed texts that haven't been embedded before."""
        results = [None] * len(texts)
        to_embed = []
        to_embed_indices = []

        for i, text in enumerate(texts):
            cached = await self.cache.get(f"emb:{hashlib.md5(text.encode()).hexdigest()}")
            if cached:
                results[i] = cached
            else:
                to_embed.append(text)
                to_embed_indices.append(i)

        if to_embed:
            # Batch embed (50% cheaper with OpenAI batch API)
            new_embeddings = self.model.encode(to_embed)
            for j, (idx, emb) in enumerate(zip(to_embed_indices, new_embeddings)):
                results[idx] = emb.tolist()
                await self.cache.set(f"emb:{hashlib.md5(texts[idx].encode()).hexdigest()}", emb.tolist())

        return results
```

---

## 13. SECURITY ARCHITECTURE

### 13.1 Prompt Injection Defense

```python
import re
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class SecurityThreat:
    threat_type: str
    severity: str  # "low", "medium", "high", "critical"
    description: str
    original_text: str
    sanitized_text: str

class PromptInjectionDefender:
    """
    Multi-layer defense against prompt injection attacks.

    Layer 1: Pattern matching (known attacks)
    Layer 2: Input sanitization (escape special tokens)
    Layer 3: Output validation (detect leaked system prompts)
    Layer 4: Canary tokens (detect successful injection)
    """

    INJECTION_PATTERNS = [
        # Direct instruction override
        (r'ignore\s+(?:all\s+)?(?:previous|above|prior)\s+(?:instructions|prompts|rules)', "high"),
        (r'forget\s+(?:everything|all|your)\s+(?:instructions|rules|training)', "high"),
        (r'you\s+are\s+now\s+(?:a|an|the)', "high"),
        (r'new\s+(?:instructions|persona|role)\s*:', "high"),
        (r'override\s+(?:system|safety|content)\s+(?:prompt|filter|policy)', "high"),

        # System prompt extraction
        (r'(?:show|reveal|print|output|repeat)\s+(?:your|the)\s+(?:system|initial)\s+(?:prompt|instructions|message)', "high"),
        (r'what\s+(?:are|is)\s+your\s+(?:system|initial)\s+(?:prompt|instructions)', "high"),
        (r'(?:repeat|say)\s+(?:everything|all)\s+(?:above|before)', "medium"),

        # Role manipulation
        (r'(?:pretend|act)\s+(?:as\s+if|like)\s+you\s+(?:are|have)\s+no\s+(?:restrictions|rules|limits)', "high"),
        (r'(?:developer|debug|admin|god|maintenance)\s+mode', "high"),
        (r'do\s+anything\s+now', "high"),

        # Encoding attacks
        (r'<\|im_start\|>system', "critical"),
        (r'<\|im_end\|>', "critical"),
        (r'\[INST\]', "high"),
        (r'###\s*System\s*:', "high"),
    ]

    def detect_injection(self, user_input: str) -> List[SecurityThreat]:
        threats = []
        input_lower = user_input.lower()

        for pattern, severity in self.INJECTION_PATTERNS:
            matches = re.finditer(pattern, input_lower, re.IGNORECASE)
            for match in matches:
                threats.append(SecurityThreat(
                    threat_type="prompt_injection",
                    severity=severity,
                    description=f"Pattern matched: {pattern}",
                    original_text=user_input,
                    sanitized_text=self._sanitize(user_input)
                ))

        return threats

    def _sanitize(self, text: str) -> str:
        """Remove or escape potentially dangerous content."""
        # Remove special tokens
        sanitized = re.sub(r'<\|[^|]+\|>', '', text)
        # Remove markdown code blocks that might contain injections
        sanitized = re.sub(r'```[\s\S]*?```', '[CODE BLOCK REMOVED]', sanitized)
        # Limit input length
        if len(sanitized) > 10000:
            sanitized = sanitized[:10000] + "...[truncated]"
        return sanitized

    def validate_output(self, response: str, system_prompt: str) -> bool:
        """Check if response leaked system prompt content."""
        # Check if response contains chunks of the system prompt
        system_words = set(system_prompt.lower().split())
        response_words = set(response.lower().split())
        overlap = system_words & response_words
        if len(overlap) > len(system_words) * 0.5:
            return False  # Possible leak
        return True

    def create_canary(self) -> str:
        """Create a unique token to detect if injection was successful."""
        import secrets
        return f"CANARY_{secrets.token_hex(8)}"
```

### 13.2 Content Moderation

```python
class ContentModerator:
    """Moderate both input and output content."""

    def __init__(self, openai_client):
        self.client = openai_client

    async def moderate_input(self, text: str) -> Dict:
        """Check if user input violates content policy."""
        response = await self.client.moderations.create(input=text)
        result = response.results[0]
        return {
            "flagged": result.flagged,
            "categories": {k: v for k, v in result.categories.model_dump().items() if v},
            "scores": {k: round(v, 4) for k, v in result.category_scores.model_dump().items() if v > 0.01}
        }

    async def moderate_output(self, text: str, domain: str = "general") -> Dict:
        """Check if AI output is appropriate for the domain."""
        prompt = f"""Evaluate this AI response for a {domain} application.
Check for: harmful content, bias, inappropriate advice, hallucination indicators.
Return JSON: {{"safe": bool, "issues": [], "confidence": float}}

Response to evaluate:
{text}"""

        result = await self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.0
        )
        return eval(result.choices[0].message.content)
```

### 13.3 Rate Limiting and Quota Management

```python
import time
from typing import Optional
import redis.asyncio as redis

class RateLimiter:
    """
    Multi-tier rate limiting:
    - Per-user: prevent abuse
    - Per-IP: prevent DDoS
    - Per-API-key: enforce quotas
    - Global: protect backend capacity
    """

    def __init__(self, redis_client):
        self.redis = redis_client

    async def check_rate_limit(
        self,
        identifier: str,
        max_requests: int = 100,
        window_seconds: int = 60,
        tier: str = "standard"
    ) -> Tuple[bool, Dict]:
        key = f"ratelimit:{tier}:{identifier}"
        now = time.time()
        window_start = now - window_seconds

        # Use sorted set for sliding window
        pipe = self.redis.pipeline()
        pipe.zremrangebyscore(key, 0, window_start)
        pipe.zadd(key, {str(now): now})
        pipe.zcard(key)
        pipe.expire(key, window_seconds)
        results = await pipe.execute()

        current_count = results[2]
        allowed = current_count <= max_requests

        return allowed, {
            "limit": max_requests,
            "remaining": max(0, max_requests - current_count),
            "reset": int(now + window_seconds),
            "retry_after": 1 if not allowed else 0
        }

    async def check_token_quota(self, api_key: str, tokens_used: int, monthly_limit: int) -> bool:
        key = f"quota:{api_key}:{time.strftime('%Y-%m')}"
        current = await self.redis.get(key)
        current = int(current) if current else 0
        return (current + tokens_used) <= monthly_limit
```

---

## 14. PROVIDER ABSTRACTION AND SHIFTING

### 14.1 Universal Provider Interface

```python
from typing import List, Dict, Optional, Any, AsyncGenerator
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from enum import Enum

class Provider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    MISTRAL = "mistral"
    LOCAL = "local"

@dataclass
class LLMResponse:
    content: str
    model: str
    provider: str
    tokens_input: int
    tokens_output: int
    latency_ms: float
    cost: float
    finish_reason: str

class LLMProvider(ABC):
    @abstractmethod
    async def chat(self, messages: List[Dict], model: str, **kwargs) -> LLMResponse:
        pass

    @abstractmethod
    async def chat_stream(self, messages: List[Dict], model: str, **kwargs) -> AsyncGenerator[str, None]:
        pass

    @abstractmethod
    async def embed(self, texts: List[str], model: str) -> List[List[float]]:
        pass

class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: str):
        from openai import AsyncOpenAI
        self.client = AsyncOpenAI(api_key=api_key)
        self.pricing = {
            "gpt-4o": {"input": 0.005, "output": 0.015},
            "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
            "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
        }

    async def chat(self, messages, model="gpt-4o", **kwargs) -> LLMResponse:
        import time
        start = time.time()
        response = await self.client.chat.completions.create(
            model=model, messages=messages,
            temperature=kwargs.get("temperature", 0.1),
            max_tokens=kwargs.get("max_tokens", 2048)
        )
        latency = (time.time() - start) * 1000
        usage = response.usage
        price = self.pricing.get(model, {"input": 0.01, "output": 0.03})
        cost = (usage.prompt_tokens * price["input"] + usage.completion_tokens * price["output"]) / 1000

        return LLMResponse(
            content=response.choices[0].message.content,
            model=model, provider="openai",
            tokens_input=usage.prompt_tokens, tokens_output=usage.completion_tokens,
            latency_ms=latency, cost=cost,
            finish_reason=response.choices[0].finish_reason
        )

    async def chat_stream(self, messages, model="gpt-4o", **kwargs) -> AsyncGenerator[str, None]:
        stream = await self.client.chat.completions.create(
            model=model, messages=messages, stream=True,
            temperature=kwargs.get("temperature", 0.1)
        )
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    async def embed(self, texts, model="text-embedding-3-small") -> List[List[float]]:
        response = await self.client.embeddings.create(input=texts, model=model)
        return [item.embedding for item in response.data]

class AnthropicProvider(LLMProvider):
    def __init__(self, api_key: str):
        import anthropic
        self.client = anthropic.AsyncAnthropic(api_key=api_key)
        self.pricing = {
            "claude-3-opus-20240229": {"input": 0.015, "output": 0.075},
            "claude-3-5-sonnet-20241022": {"input": 0.003, "output": 0.015},
            "claude-3-haiku-20240307": {"input": 0.00025, "output": 0.00125},
        }

    async def chat(self, messages, model="claude-3-5-sonnet-20241022", **kwargs) -> LLMResponse:
        import time
        start = time.time()
        system = next((m["content"] for m in messages if m["role"] == "system"), "")
        user_messages = [m for m in messages if m["role"] != "system"]

        response = await self.client.messages.create(
            model=model, system=system, messages=user_messages,
            max_tokens=kwargs.get("max_tokens", 2048),
            temperature=kwargs.get("temperature", 0.1)
        )
        latency = (time.time() - start) * 1000
        price = self.pricing.get(model, {"input": 0.01, "output": 0.03})
        cost = (response.usage.input_tokens * price["input"] + response.usage.output_tokens * price["output"]) / 1000

        return LLMResponse(
            content=response.content[0].text, model=model, provider="anthropic",
            tokens_input=response.usage.input_tokens, tokens_output=response.usage.output_tokens,
            latency_ms=latency, cost=cost, finish_reason=response.stop_reason
        )

    async def chat_stream(self, messages, model="claude-3-5-sonnet-20241022", **kwargs) -> AsyncGenerator[str, None]:
        system = next((m["content"] for m in messages if m["role"] == "system"), "")
        user_messages = [m for m in messages if m["role"] != "system"]
        async with self.client.messages.stream(model=model, system=system, messages=user_messages,
                                                max_tokens=kwargs.get("max_tokens", 2048)) as stream:
            async for text in stream.text_stream:
                yield text

    async def embed(self, texts, model="voyage-2") -> List[List[float]]:
        # Anthropic doesn't have embedding; use Voyage AI (same API family)
        import voyageai
        client = voyageai.Client()
        result = client.embed(texts, model=model)
        return result.embeddings
```

### 14.2 Provider Router with Automatic Failover

```python
class ProviderRouter:
    """
    Route to the best available provider.
    Automatic failover if primary provider is down.
    """
    def __init__(self, providers: Dict[str, LLMProvider], circuit_manager):
        self.providers = providers
        self.circuit_manager = circuit_manager
        self.default_priority = ["openai", "anthropic", "google"]

    async def chat(self, messages: List[Dict], preferred_provider: Optional[str] = None, **kwargs) -> LLMResponse:
        providers_to_try = []
        if preferred_provider and preferred_provider in self.providers:
            providers_to_try.append(preferred_provider)
        providers_to_try.extend(p for p in self.default_priority if p != preferred_provider)

        last_error = None
        for provider_name in providers_to_try:
            breaker = self.circuit_manager.get_breaker(provider_name)
            if breaker.state == "open":
                continue
            try:
                provider = self.providers[provider_name]
                return await breaker.call(provider.chat, messages, **kwargs)
            except Exception as e:
                last_error = e
                continue

        raise RuntimeError(f"All providers failed. Last error: {last_error}")

    async def embed(self, texts: List[str], model: str = None) -> List[List[float]]:
        for provider_name in self.default_priority:
            try:
                provider = self.providers[provider_name]
                return await provider.embed(texts, model or "text-embedding-3-small")
            except Exception:
                continue
        raise RuntimeError("All embedding providers failed")
```

---

## 15. CACHING STRATEGIES

### 15.1 Multi-Layer Cache Architecture

```
REQUEST -> L1 (In-Memory) -> L2 (Redis) -> L3 (Semantic) -> LLM
              |                |              |
           <1ms             <5ms           <50ms
           exact            exact          similar
           match            match          match
```

```python
import asyncio
import hashlib
import json
from typing import Optional, Any, Dict
from dataclasses import dataclass
import time

@dataclass
class CacheEntry:
    key: str
    value: Any
    created_at: float
    ttl: int
    hit_count: int = 0

class MultiLayerCache:
    """
    Three-layer cache for AI responses:
    L1: In-memory dict (exact match, <1ms)
    L2: Redis (exact match, <5ms)
    L3: Semantic similarity (similar match, <50ms)
    """
    def __init__(self, redis_client, embedding_model, semantic_threshold: float = 0.92):
        self.l1: Dict[str, CacheEntry] = {}
        self.l1_max_size = 1000
        self.redis = redis_client
        self.embedding_model = embedding_model
        self.semantic_threshold = semantic_threshold

    def _make_key(self, query: str, model: str, params: Dict = None) -> str:
        content = f"{query}:{model}:{json.dumps(params or {}, sort_keys=True)}"
        return hashlib.sha256(content.encode()).hexdigest()

    async def get(self, query: str, model: str = "default", params: Dict = None) -> Optional[str]:
        key = self._make_key(query, model, params)

        # L1: Memory
        if key in self.l1:
            entry = self.l1[key]
            if time.time() - entry.created_at < entry.ttl:
                entry.hit_count += 1
                return entry.value
            del self.l1[key]

        # L2: Redis
        cached = await self.redis.get(f"cache:{key}")
        if cached:
            data = json.loads(cached)
            # Populate L1
            self.l1[key] = CacheEntry(key, data["value"], time.time(), data.get("ttl", 3600))
            return data["value"]

        # L3: Semantic
        return await self._semantic_search(query)

    async def set(self, query: str, response: str, model: str = "default", params: Dict = None, ttl: int = 3600):
        key = self._make_key(query, model, params)

        # L1
        if len(self.l1) >= self.l1_max_size:
            # Evict least recently used
            oldest_key = min(self.l1, key=lambda k: self.l1[k].created_at)
            del self.l1[oldest_key]
        self.l1[key] = CacheEntry(key, response, time.time(), ttl)

        # L2
        await self.redis.setex(f"cache:{key}", ttl, json.dumps({"value": response, "ttl": ttl}))

        # L3: Store embedding for semantic search
        embedding = self.embedding_model.encode(query).tolist()
        await self.redis.setex(f"semantic:{key}", ttl, json.dumps({
            "query": query, "response": response, "embedding": embedding
        }))

    async def _semantic_search(self, query: str) -> Optional[str]:
        import numpy as np
        query_emb = self.embedding_model.encode(query)

        keys = await self.redis.keys("semantic:*")
        best_score = 0.0
        best_response = None

        for key in keys[:100]:  # Limit search
            data = await self.redis.get(key)
            if data:
                entry = json.loads(data)
                cached_emb = np.array(entry["embedding"])
                score = float(np.dot(query_emb, cached_emb) / (np.linalg.norm(query_emb) * np.linalg.norm(cached_emb)))
                if score > best_score:
                    best_score = score
                    best_response = entry["response"]

        if best_score >= self.semantic_threshold:
            return best_response
        return None

    async def invalidate(self, pattern: str = "*"):
        self.l1.clear()
        keys = await self.redis.keys(f"cache:{pattern}")
        if keys:
            await self.redis.delete(*keys)
```

---

## 16. OBSERVABILITY AND MONITORING

### 16.1 Distributed Tracing with OpenTelemetry

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from contextlib import asynccontextmanager
import time

def setup_tracing(service_name: str, otlp_endpoint: str = "http://localhost:4317"):
    resource = Resource.create({"service.name": service_name, "service.version": "1.0.0"})
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=otlp_endpoint))
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
    return trace.get_tracer(service_name)

tracer = setup_tracing("ai-production-api")

class AITracer:
    """Traces every step of the AI pipeline."""

    @staticmethod
    @asynccontextmanager
    async def trace_retrieval(query: str, strategy: str):
        with tracer.start_as_current_span("retrieval") as span:
            span.set_attribute("retrieval.query", query)
            span.set_attribute("retrieval.strategy", strategy)
            start = time.time()
            try:
                yield span
            finally:
                span.set_attribute("retrieval.duration_ms", (time.time() - start) * 1000)

    @staticmethod
    @asynccontextmanager
    async def trace_llm_call(provider: str, model: str, input_tokens: int = 0):
        with tracer.start_as_current_span("llm_call") as span:
            span.set_attribute("llm.provider", provider)
            span.set_attribute("llm.model", model)
            span.set_attribute("llm.input_tokens", input_tokens)
            start = time.time()
            try:
                yield span
            finally:
                span.set_attribute("llm.duration_ms", (time.time() - start) * 1000)

    @staticmethod
    @asynccontextmanager
    async def trace_reranking(query: str, num_docs: int):
        with tracer.start_as_current_span("reranking") as span:
            span.set_attribute("reranking.query", query)
            span.set_attribute("reranking.num_docs", num_docs)
            start = time.time()
            try:
                yield span
            finally:
                span.set_attribute("reranking.duration_ms", (time.time() - start) * 1000)
```

### 16.2 Metrics Collection

```python
from prometheus_client import Counter, Histogram, Gauge, Summary
import time

# Define metrics
REQUEST_COUNT = Counter('ai_requests_total', 'Total AI requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('ai_request_duration_seconds', 'Request latency', ['method', 'endpoint'],
                            buckets=[0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0])
LLM_LATENCY = Histogram('llm_call_duration_seconds', 'LLM call latency', ['provider', 'model'],
                        buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0])
LLM_TOKENS = Counter('llm_tokens_total', 'Total LLM tokens', ['provider', 'model', 'type'])
LLM_COST = Counter('llm_cost_usd_total', 'Total LLM cost in USD', ['provider', 'model'])
CACHE_HITS = Counter('cache_hits_total', 'Cache hits', ['layer'])
CACHE_MISSES = Counter('cache_misses_total', 'Cache misses', ['layer'])
ACTIVE_REQUESTS = Gauge('active_requests', 'Currently active requests')
RETRIEVAL_DOCS = Histogram('retrieval_docs_returned', 'Documents returned by retrieval',
                           buckets=[1, 5, 10, 20, 50])
CIRCUIT_STATE = Gauge('circuit_breaker_state', 'Circuit breaker state', ['provider'])

class MetricsCollector:
    """Collect and expose metrics for Prometheus."""

    @staticmethod
    def record_request(method: str, endpoint: str, status: int, duration: float):
        REQUEST_COUNT.labels(method=method, endpoint=endpoint, status=str(status)).inc()
        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(duration)

    @staticmethod
    def record_llm_call(provider: str, model: str, input_tokens: int, output_tokens: int, latency: float, cost: float):
        LLM_LATENCY.labels(provider=provider, model=model).observe(latency)
        LLM_TOKENS.labels(provider=provider, model=model, type="input").inc(input_tokens)
        LLM_TOKENS.labels(provider=provider, model=model, type="output").inc(output_tokens)
        LLM_COST.labels(provider=provider, model=model).inc(cost)

    @staticmethod
    def record_cache_hit(layer: str):
        CACHE_HITS.labels(layer=layer).inc()

    @staticmethod
    def record_cache_miss(layer: str):
        CACHE_MISSES.labels(layer=layer).inc()
```

### 16.3 Alerting Rules

```yaml
# prometheus/alert_rules.yml
groups:
- name: ai-system-alerts
  rules:
  - alert: HighErrorRate
    expr: rate(ai_requests_total{status=~"5.."}[5m]) / rate(ai_requests_total[5m]) > 0.05
    for: 2m
    labels:
      severity: critical
    annotations:
      summary: "AI error rate above 5%"

  - alert: HighLatency
    expr: histogram_quantile(0.95, rate(llm_call_duration_seconds_bucket[5m])) > 10
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "LLM P95 latency above 10s"

  - alert: CostSpike
    expr: rate(llm_cost_usd_total[1h]) > 10
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "LLM cost rate exceeds $10/hour"

  - alert: CacheHitRateLow
    expr: rate(cache_hits_total[5m]) / (rate(cache_hits_total[5m]) + rate(cache_misses_total[5m])) < 0.3
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "Cache hit rate below 30%"

  - alert: CircuitBreakerOpen
    expr: circuit_breaker_state == 1
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "Circuit breaker open for provider"
```


---

# PART 3: ADVANCED PRODUCTION SYSTEMS

---

## 17. SCALING AND INFRASTRUCTURE

### 17.1 Horizontal Scaling Architecture

AI services need horizontal scaling to handle variable load. The architecture uses a load balancer distributing traffic across stateless API pods, backed by a shared Redis cache and clustered vector database.

```
LOAD BALANCER (NGINX / AWS ALB / Cloudflare)
       |
  +----+----+----+
  |    |    |    |
  v    v    v    v
 Pod1 Pod2 Pod3 PodN  (FastAPI replicas)
  +----+----+----+
       |
  +----+----+
  |         |
Redis    Vector DB
Cache    (Cluster)
```

### 17.2 Load Balancing Strategies for AI

```python
import asyncio, time, random
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from enum import Enum

class LoadBalancingStrategy(Enum):
    ROUND_ROBIN = "round_robin"
    LEAST_CONNECTIONS = "least_connections"
    LATENCY_BASED = "latency_based"
    WEIGHTED = "weighted"

@dataclass
class BackendNode:
    endpoint: str
    weight: int = 1
    active_connections: int = 0
    avg_latency_ms: float = 0.0
    is_healthy: bool = True
    error_count: int = 0
    _latency_samples: List[float] = field(default_factory=list)

    def update_latency(self, latency_ms: float):
        self._latency_samples.append(latency_ms)
        if len(self._latency_samples) > 100:
            self._latency_samples = self._latency_samples[-100:]
        self.avg_latency_ms = sum(self._latency_samples) / len(self._latency_samples)

    @property
    def effective_score(self) -> float:
        if not self.is_healthy:
            return float('inf')
        return (self.avg_latency_ms * 0.6) + (self.active_connections * 10 * 0.4)

class AILoadBalancer:
    def __init__(self, strategy: LoadBalancingStrategy = LoadBalancingStrategy.LATENCY_BASED):
        self.backends: List[BackendNode] = []
        self.strategy = strategy
        self._rr_index = 0

    def add_backend(self, endpoint: str, weight: int = 1):
        self.backends.append(BackendNode(endpoint=endpoint, weight=weight))

    async def get_backend(self, request_context: Optional[Dict] = None) -> BackendNode:
        healthy = [b for b in self.backends if b.is_healthy]
        if not healthy:
            raise RuntimeError("No healthy backends available")
        if self.strategy == LoadBalancingStrategy.ROUND_ROBIN:
            backend = healthy[self._rr_index % len(healthy)]
            self._rr_index += 1
            return backend
        elif self.strategy == LoadBalancingStrategy.LEAST_CONNECTIONS:
            return min(healthy, key=lambda b: b.active_connections)
        elif self.strategy == LoadBalancingStrategy.LATENCY_BASED:
            return min(healthy, key=lambda b: b.effective_score)
        elif self.strategy == LoadBalancingStrategy.WEIGHTED:
            total_weight = sum(b.weight for b in healthy)
            r = random.uniform(0, total_weight)
            cumulative = 0
            for b in healthy:
                cumulative += b.weight
                if r <= cumulative:
                    return b
            return healthy[-1]
        return healthy[0]

    async def execute_request(self, request_fn, request_context=None):
        backend = await self.get_backend(request_context)
        backend.active_connections += 1
        start_time = time.time()
        try:
            result = await request_fn(backend.endpoint)
            latency = (time.time() - start_time) * 1000
            backend.update_latency(latency)
            return result
        except Exception as e:
            backend.error_count += 1
            if backend.error_count > 5:
                backend.is_healthy = False
            raise
        finally:
            backend.active_connections -= 1
```

### 17.3 Auto-Scaling with Kubernetes (HPA + KEDA)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ai-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ai-api
  minReplicas: 2
  maxReplicas: 50
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Pods
    pods:
      metric:
        name: http_requests_per_second
      target:
        type: AverageValue
        averageValue: "100"
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
      - type: Pods
        value: 4
        periodSeconds: 60
    scaleDown:
      stabilizationWindowSeconds: 300
---
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: ai-queue-scaler
spec:
  scaleTargetRef:
    name: ai-worker-deployment
  minReplicas: 1
  maxReplicas: 100
  triggers:
  - type: redis-streams
    metadata:
      address: redis:6379
      stream: ai-task-queue
      consumerGroup: ai-workers
      lagCount: "50"
```

### 17.4 Full K8s Deployment Manifest

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-api
  namespace: ai-production
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: ai-api
  template:
    metadata:
      labels:
        app: ai-api
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8000"
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
      containers:
      - name: ai-api
        image: registry.internal/ai-api:2.1.0
        ports:
        - containerPort: 8000
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: ai-secrets
              key: openai-api-key
        resources:
          requests:
            cpu: "500m"
            memory: "1Gi"
          limits:
            cpu: "2000m"
            memory: "4Gi"
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 5
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
      topologySpreadConstraints:
      - maxSkew: 1
        topologyKey: topology.kubernetes.io/zone
        whenUnsatisfiable: DoNotSchedule
        labelSelector:
          matchLabels:
            app: ai-api
---
apiVersion: v1
kind: Service
metadata:
  name: ai-api-service
spec:
  selector:
    app: ai-api
  ports:
  - port: 80
    targetPort: 8000
```

### 17.5 GPU Deployment for Local Models

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: local-llm
spec:
  replicas: 2
  selector:
    matchLabels:
      app: local-llm
  template:
    spec:
      nodeSelector:
        nvidia.com/gpu.present: "true"
      tolerations:
      - key: nvidia.com/gpu
        operator: Exists
        effect: NoSchedule
      containers:
      - name: vllm
        image: vllm/vllm-openai:latest
        args:
        - "--model"
        - "meta-llama/Llama-3.1-8B-Instruct"
        - "--tensor-parallel-size"
        - "1"
        - "--max-model-len"
        - "8192"
        - "--gpu-memory-utilization"
        - "0.9"
        resources:
          limits:
            nvidia.com/gpu: 1
            memory: "32Gi"
```

### 17.6 Multi-Region Architecture

```
GLOBAL TRAFFIC MANAGER (Cloudflare / Route53)
  Latency-based routing + GeoDNS
       |
  +---------+---------+
  |         |         |
US-EAST  EU-WEST  AP-SOUTH
  |         |         |
API+LB   API+LB   API+LB
VectorDB VectorDB VectorDB
Cache    Cache    Cache
  |         |         |
  +---------+---------+
       |
Global DB (CockroachDB)
```

```python
import asyncio
from typing import Optional, Dict, List
from dataclasses import dataclass
from enum import Enum

class Region(Enum):
    US_EAST = "us-east-1"
    EU_WEST = "eu-west-1"
    AP_SOUTH = "ap-south-1"

@dataclass
class RegionConfig:
    region: Region
    endpoint: str
    data_residency_required: bool
    supported_models: List[str]

class MultiRegionRouter:
    def __init__(self, regions: List[RegionConfig]):
        self.regions = {r.region: r for r in regions}

    async def route_request(self, user_country: Optional[str], data_classification: str, model: str) -> Region:
        eu_countries = {"DE", "FR", "NL", "IE", "ES", "IT", "SE", "PL", "BE", "AT"}
        if user_country and user_country in eu_countries and data_classification in ("pii", "sensitive"):
            return Region.EU_WEST
        eligible = [r for r in self.regions.values() if model in r.supported_models]
        return (eligible[0] if eligible else list(self.regions.values())[0]).region

    async def execute_with_failover(self, request_fn, primary_region: Region, max_retries: int = 2):
        regions_to_try = [primary_region] + [r for r in self.regions if r != primary_region]
        for region in regions_to_try[:max_retries + 1]:
            try:
                return await request_fn(self.regions[region].endpoint)
            except Exception:
                if region == regions_to_try[-1]:
                    raise
```

---

## 18. CI/CD FOR AI SYSTEMS

### 18.1 Model Registry and Versioning

```python
import hashlib, json, time, sqlite3
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class ModelVersion:
    model_id: str
    version: str
    model_type: str
    provider: str
    model_name: str
    config: Dict[str, Any]
    metrics: Dict[str, float]
    created_at: float = field(default_factory=time.time)
    tags: List[str] = field(default_factory=list)
    checksum: str = ""
    is_production: bool = False
    parent_version: Optional[str] = None

    def compute_checksum(self):
        content = json.dumps(self.config, sort_keys=True)
        self.checksum = hashlib.sha256(content.encode()).hexdigest()[:16]

class ModelRegistry:
    def __init__(self, db_path: str = "model_registry.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("""CREATE TABLE IF NOT EXISTS models (
            model_id TEXT, version TEXT, model_type TEXT, provider TEXT,
            model_name TEXT, config TEXT, metrics TEXT, created_at REAL,
            tags TEXT, checksum TEXT, is_production INTEGER DEFAULT 0,
            parent_version TEXT, PRIMARY KEY (model_id, version))""")
        conn.commit(); conn.close()

    def register(self, model: ModelVersion) -> str:
        model.compute_checksum()
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT OR REPLACE INTO models VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (model.model_id, model.version, model.model_type, model.provider,
             model.model_name, json.dumps(model.config), json.dumps(model.metrics),
             model.created_at, json.dumps(model.tags), model.checksum,
             int(model.is_production), model.parent_version))
        conn.commit(); conn.close()
        return f"{model.model_id}:{model.version}"

    def promote_to_production(self, model_id: str, version: str):
        conn = sqlite3.connect(self.db_path)
        conn.execute("UPDATE models SET is_production = 0 WHERE model_id = ?", (model_id,))
        conn.execute("UPDATE models SET is_production = 1 WHERE model_id = ? AND version = ?", (model_id, version))
        conn.commit(); conn.close()

    def rollback(self, model_id: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute("SELECT version FROM models WHERE model_id = ? AND is_production = 0 ORDER BY created_at DESC LIMIT 1", (model_id,))
        row = cursor.fetchone(); conn.close()
        if row:
            self.promote_to_production(model_id, row[0])

    def get_production_model(self, model_id: str) -> Optional[ModelVersion]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute("SELECT * FROM models WHERE model_id = ? AND is_production = 1", (model_id,))
        row = cursor.fetchone(); conn.close()
        if row:
            return ModelVersion(model_id=row[0], version=row[1], model_type=row[2],
                provider=row[3], model_name=row[4], config=json.loads(row[5]),
                metrics=json.loads(row[6]), created_at=row[7], tags=json.loads(row[8]),
                checksum=row[9], is_production=bool(row[10]), parent_version=row[11])
        return None
```

### 18.2 CI/CD Pipeline (GitHub Actions)

```yaml
name: AI System CI/CD Pipeline
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: "3.11"
    - name: Install dependencies
      run: pip install ruff mypy pytest && pip install -r requirements.txt
    - name: Lint
      run: ruff check src/ --output-format=github
    - name: Type check
      run: mypy src/ --ignore-missing-imports
    - name: Unit tests
      run: pytest tests/unit/ -v --tb=short

  evaluation:
    runs-on: ubuntu-latest
    needs: quality
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: "3.11"
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run golden dataset evaluation
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
      run: |
        python scripts/evaluate.py \
          --dataset data/golden_dataset.json \
          --output eval_results.json \
          --threshold-faithfulness 0.80 \
          --threshold-relevancy 0.85 \
          --threshold-hallucination 0.05
    - name: Check evaluation gates
      run: |
        FAITHFULNESS=$(jq '.faithfulness' eval_results.json)
        RELEVANCY=$(jq '.answer_relevancy' eval_results.json)
        HALLUCINATION=$(jq '.hallucination_rate' eval_results.json)
        if (( $(echo "$FAITHFULNESS < 0.80" | bc -l) )); then echo "FAIL: Faithfulness" && exit 1; fi
        if (( $(echo "$RELEVANCY < 0.85" | bc -l) )); then echo "FAIL: Relevancy" && exit 1; fi
        if (( $(echo "$HALLUCINATION > 0.05" | bc -l) )); then echo "FAIL: Hallucination" && exit 1; fi
        echo "PASS: All evaluation gates passed"

  security:
    runs-on: ubuntu-latest
    needs: quality
    steps:
    - uses: actions/checkout@v4
    - name: Run Trivy vulnerability scanner
      uses: aquasecurity/trivy-action@master
      with:
        scan-type: fs
        scan-ref: .
        severity: CRITICAL,HIGH
    - name: Check for secrets
      uses: trufflesecurity/trufflehog@main
      with:
        extra_args: --only-verified

  build:
    runs-on: ubuntu-latest
    needs: [evaluation, security]
    if: github.ref == 'refs/heads/main'
    steps:
    - uses: actions/checkout@v4
    - uses: docker/login-action@v3
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    - uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ghcr.io/${{ github.repository }}/ai-api:${{ github.sha }}

  deploy-canary:
    runs-on: ubuntu-latest
    needs: build
    environment: canary
    steps:
    - name: Deploy canary (5% traffic)
      run: |
        kubectl set image deployment/ai-api ai-api=ghcr.io/${{ github.repository }}/ai-api:${{ github.sha }} -n ai-production
    - name: Monitor canary for 10 minutes
      run: |
        for i in $(seq 1 20); do
          ERROR_RATE=$(curl -s "http://prometheus:9090/api/v1/query?query=rate(http_requests_total{status=~'5..'}[1m])" | jq '.data.result[0].value[1]' -r)
          echo "Check $i/20: Error rate=$ERROR_RATE"
          if (( $(echo "$ERROR_RATE > 0.05" | bc -l) )); then echo "CANARY FAILED" && exit 1; fi
          sleep 30
        done

  deploy-production:
    runs-on: ubuntu-latest
    needs: deploy-canary
    environment: production
    steps:
    - name: Full rollout
      run: kubectl rollout status deployment/ai-api -n ai-production --timeout=300s
```

### 18.3 A/B Testing Framework

```python
import hashlib, time, json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum

class ExperimentStatus(Enum):
    DRAFT = "draft"
    RUNNING = "running"
    COMPLETED = "completed"

@dataclass
class ModelVariant:
    variant_id: str
    model_id: str
    model_version: str
    weight: float
    config_override: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ExperimentResult:
    variant_id: str
    total_requests: int
    avg_latency_ms: float
    avg_user_score: float
    error_rate: float
    cost_per_request: float

class ABTestManager:
    def __init__(self):
        self.experiments: Dict[str, Dict] = {}

    def create_experiment(self, experiment_id: str, name: str, variants: List[ModelVariant], target_sample_size: int = 10000):
        total_weight = sum(v.weight for v in variants)
        if abs(total_weight - 1.0) > 0.01:
            raise ValueError(f"Weights must sum to 1.0, got {total_weight}")
        self.experiments[experiment_id] = {
            "name": name, "variants": {v.variant_id: v for v in variants},
            "status": ExperimentStatus.RUNNING, "created_at": time.time(),
            "target_sample_size": target_sample_size,
            "results": {v.variant_id: [] for v in variants}
        }

    def assign_variant(self, experiment_id: str, user_id: str) -> ModelVariant:
        experiment = self.experiments[experiment_id]
        hash_val = int(hashlib.md5(f"{experiment_id}:{user_id}".encode()).hexdigest(), 16) % 10000
        cumulative = 0
        for variant in experiment["variants"].values():
            cumulative += variant.weight * 10000
            if hash_val < cumulative:
                return variant
        return list(experiment["variants"].values())[-1]

    def record_result(self, experiment_id: str, variant_id: str, latency_ms: float, user_score: Optional[float] = None, error: bool = False, cost: float = 0.0):
        result = {"timestamp": time.time(), "latency_ms": latency_ms, "user_score": user_score, "error": error, "cost": cost}
        self.experiments[experiment_id]["results"][variant_id].append(result)

    def get_results(self, experiment_id: str) -> Dict[str, ExperimentResult]:
        experiment = self.experiments[experiment_id]
        results = {}
        for variant_id, data in experiment["results"].items():
            if not data:
                continue
            results[variant_id] = ExperimentResult(
                variant_id=variant_id, total_requests=len(data),
                avg_latency_ms=sum(d["latency_ms"] for d in data) / len(data),
                avg_user_score=sum(d["user_score"] for d in data if d["user_score"]) / max(1, sum(1 for d in data if d["user_score"])),
                error_rate=sum(1 for d in data if d["error"]) / len(data),
                cost_per_request=sum(d["cost"] for d in data) / len(data)
            )
        return results

    def check_significance(self, experiment_id: str) -> Optional[str]:
        results = self.get_results(experiment_id)
        if len(results) < 2:
            return None
        sorted_variants = sorted(results.items(), key=lambda x: x[1].avg_user_score, reverse=True)
        best_id, best = sorted_variants[0]
        second_id, second = sorted_variants[1]
        if best.total_requests < 1000:
            return None
        improvement = (best.avg_user_score - second.avg_user_score) / max(second.avg_user_score, 0.001)
        if improvement > 0.05:
            return best_id
        return None
```

---

## 19. ERROR HANDLING AND RESILIENCE PATTERNS

### 19.1 Retry with Exponential Backoff

```python
import asyncio, time, random, logging
from typing import Callable, TypeVar, Optional, Tuple, Type, Any
from functools import wraps
from dataclasses import dataclass

logger = logging.getLogger(__name__)
T = TypeVar('T')

@dataclass
class RetryConfig:
    max_retries: int = 3
    base_delay: float = 1.0
    max_delay: float = 60.0
    exponential_base: float = 2.0
    jitter: bool = True
    retryable_exceptions: Tuple[Type[Exception], ...] = (Exception,)
    retryable_status_codes: Tuple[int, ...] = (429, 500, 502, 503, 504)

class RetryExhausted(Exception):
    def __init__(self, last_exception: Exception, attempts: int):
        self.last_exception = last_exception
        self.attempts = attempts
        super().__init__(f"Retry exhausted after {attempts} attempts: {last_exception}")

def async_retry(config: RetryConfig = None):
    if config is None:
        config = RetryConfig()
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(config.max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                except config.retryable_exceptions as e:
                    last_exception = e
                    if attempt == config.max_retries:
                        break
                    delay = config.base_delay * (config.exponential_base ** attempt)
                    if hasattr(e, 'response') and hasattr(e.response, 'headers'):
                        retry_after = e.response.headers.get('Retry-After')
                        if retry_after:
                            delay = max(delay, float(retry_after))
                    delay = min(delay, config.max_delay)
                    if config.jitter:
                        delay = delay * (0.5 + random.random() * 0.5)
                    logger.warning(f"Attempt {attempt + 1}/{config.max_retries + 1} failed: {e}. Retrying in {delay:.2f}s")
                    await asyncio.sleep(delay)
            raise RetryExhausted(last_exception, config.max_retries + 1)
        return wrapper
    return decorator

LLM_RETRY_CONFIG = RetryConfig(
    max_retries=3, base_delay=1.0, max_delay=30.0,
    retryable_exceptions=(ConnectionError, TimeoutError)
)
```

### 19.2 Circuit Breaker Pattern

```python
import time, asyncio, logging
from typing import Callable, Any
from enum import Enum
from dataclasses import dataclass

logger = logging.getLogger(__name__)

class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

@dataclass
class CircuitBreakerConfig:
    failure_threshold: int = 5
    recovery_timeout: float = 60.0
    half_open_max_calls: int = 3
    success_threshold: int = 2

class CircuitBreakerError(Exception):
    pass

class CircuitBreaker:
    def __init__(self, name: str, config: CircuitBreakerConfig = None):
        self.name = name
        self.config = config or CircuitBreakerConfig()
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = 0.0
        self.half_open_calls = 0
        self._lock = asyncio.Lock()

    async def call(self, func: Callable, *args, **kwargs) -> Any:
        async with self._lock:
            if self.state == CircuitState.OPEN:
                if time.time() - self.last_failure_time > self.config.recovery_timeout:
                    self.state = CircuitState.HALF_OPEN
                    self.half_open_calls = 0
                    self.success_count = 0
                else:
                    raise CircuitBreakerError(f"Circuit {self.name} is OPEN")
            if self.state == CircuitState.HALF_OPEN:
                if self.half_open_calls >= self.config.half_open_max_calls:
                    raise CircuitBreakerError(f"Circuit {self.name} half-open limit reached")
                self.half_open_calls += 1
        try:
            result = await func(*args, **kwargs)
            await self._on_success()
            return result
        except Exception as e:
            await self._on_failure(e)
            raise

    async def _on_success(self):
        async with self._lock:
            if self.state == CircuitState.HALF_OPEN:
                self.success_count += 1
                if self.success_count >= self.config.success_threshold:
                    self.state = CircuitState.CLOSED
                    self.failure_count = 0
            else:
                self.failure_count = 0

    async def _on_failure(self, error: Exception):
        async with self._lock:
            self.failure_count += 1
            self.last_failure_time = time.time()
            if self.state == CircuitState.HALF_OPEN:
                self.state = CircuitState.OPEN
            elif self.failure_count >= self.config.failure_threshold:
                self.state = CircuitState.OPEN

class ProviderCircuitBreakerManager:
    def __init__(self):
        self.breakers: dict[str, CircuitBreaker] = {}

    def get_breaker(self, provider: str) -> CircuitBreaker:
        if provider not in self.breakers:
            self.breakers[provider] = CircuitBreaker(name=provider)
        return self.breakers[provider]

    def get_healthy_providers(self) -> list[str]:
        return [name for name, cb in self.breakers.items() if cb.state != CircuitState.OPEN]
```

### 19.3 Graceful Degradation with Multi-Tier Fallback

```python
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass
import asyncio, logging

logger = logging.getLogger(__name__)

@dataclass
class ModelTier:
    name: str
    provider: str
    model: str
    quality_score: float
    cost_per_1k: float
    latency_ms: float

class GracefulDegradation:
    """
    Multi-tier model fallback system:
    Tier 1: GPT-4o / Claude Opus (best quality)
    Tier 2: GPT-4o-mini / Claude Sonnet (balanced)
    Tier 3: GPT-3.5-turbo / Claude Haiku (fast, cheap)
    Tier 4: Cached response (last resort)
    Tier 5: Static fallback message
    """
    def __init__(self, tiers: List[ModelTier], cache_fn: Optional[Callable] = None):
        self.tiers = sorted(tiers, key=lambda t: -t.quality_score)
        self.cache_fn = cache_fn

    async def execute_with_fallback(self, request_fn: Callable, query: str, **kwargs) -> Dict[str, Any]:
        errors = []
        for tier in self.tiers:
            try:
                result = await request_fn(provider=tier.provider, model=tier.model, query=query, **kwargs)
                return {"result": result, "tier_used": tier.name, "model_used": tier.model,
                        "degraded": tier.quality_score < self.tiers[0].quality_score, "errors": errors}
            except Exception as e:
                logger.warning(f"Tier {tier.name} failed: {e}")
                errors.append({"tier": tier.name, "error": str(e)})
        if self.cache_fn:
            cached = await self.cache_fn(query)
            if cached:
                return {"result": cached, "tier_used": "cache", "model_used": "cached", "degraded": True, "errors": errors}
        return {"result": "Service temporarily unavailable. Please try again.", "tier_used": "static_fallback",
                "model_used": "none", "degraded": True, "errors": errors}
```

### 19.4 Dead Letter Queue

```python
import json, time, logging
from typing import Dict, Any, Callable
from dataclasses import dataclass, field, asdict

logger = logging.getLogger(__name__)

@dataclass
class DeadMessage:
    original_request: Dict[str, Any]
    error: str
    attempts: int
    first_failure_at: float
    last_failure_at: float
    provider: str = ""
    model: str = ""

class DeadLetterQueue:
    def __init__(self, redis_client, queue_name: str = "ai:dlq"):
        self.redis = redis_client
        self.queue_name = queue_name

    async def enqueue(self, message: DeadMessage):
        await self.redis.rpush(self.queue_name, json.dumps(asdict(message)))
        logger.error(f"DLQ: enqueued failed request (provider={message.provider})")

    async def dequeue(self, count: int = 10) -> list:
        messages = []
        for _ in range(count):
            raw = await self.redis.lpop(self.queue_name)
            if raw:
                data = json.loads(raw)
                messages.append(DeadMessage(**data))
        return messages

    async def retry_all(self, handler: Callable, max_age_seconds: float = 3600):
        messages = await self.dequeue(count=100)
        retried = 0
        for msg in messages:
            if time.time() - msg.last_failure_at > max_age_seconds:
                continue
            try:
                await handler(msg.original_request)
                retried += 1
            except Exception:
                await self.enqueue(msg)
        return retried
```

---

## 20. DATA PIPELINE ARCHITECTURE

### 20.1 Universal Document Processing Pipeline

```python
import hashlib, mimetypes
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from pathlib import Path
from abc import ABC, abstractmethod
import asyncio
import logging

logger = logging.getLogger(__name__)

@dataclass
class ProcessedDocument:
    doc_id: str
    source: str
    content: str
    content_type: str  # "text", "table", "image", "code"
    metadata: Dict
    chunks: List[Dict] = field(default_factory=list)
    checksum: str = ""

class DocumentLoader(ABC):
    @abstractmethod
    async def load(self, file_path: str) -> List[ProcessedDocument]:
        pass

class PDFLoader(DocumentLoader):
    async def load(self, file_path: str) -> List[ProcessedDocument]:
        import pdfplumber
        documents = []
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text() or ""
                tables = page.extract_tables()
                if text.strip():
                    documents.append(ProcessedDocument(
                        doc_id=f"{Path(file_path).stem}_page_{page_num}",
                        source=file_path, content=text, content_type="text",
                        metadata={"page": page_num + 1, "file_type": "pdf"}
                    ))
                for table_idx, table in enumerate(tables):
                    table_text = "\n".join([" | ".join(str(cell) for cell in row) for row in table if row])
                    if table_text.strip():
                        documents.append(ProcessedDocument(
                            doc_id=f"{Path(file_path).stem}_page_{page_num}_table_{table_idx}",
                            source=file_path, content=table_text, content_type="table",
                            metadata={"page": page_num + 1, "table_index": table_idx}
                        ))
        return documents

class HTMLLoader(DocumentLoader):
    async def load(self, file_path: str) -> List[ProcessedDocument]:
        from bs4 import BeautifulSoup
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        text = soup.get_text(separator='\n', strip=True)
        return [ProcessedDocument(
            doc_id=Path(file_path).stem, source=file_path, content=text,
            content_type="text", metadata={"file_type": "html", "title": soup.title.string if soup.title else ""}
        )]

class CSVLoader(DocumentLoader):
    async def load(self, file_path: str) -> List[ProcessedDocument]:
        import csv
        documents = []
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row_idx, row in enumerate(reader):
                content = " | ".join(f"{k}: {v}" for k, v in row.items())
                documents.append(ProcessedDocument(
                    doc_id=f"{Path(file_path).stem}_row_{row_idx}", source=file_path,
                    content=content, content_type="text",
                    metadata={"row_index": row_idx, "file_type": "csv", "columns": list(row.keys())}
                ))
        return documents

class DocumentProcessorPipeline:
    """Universal document processing pipeline for PDF, DOCX, HTML, CSV, TXT."""
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.loaders = {".pdf": PDFLoader(), ".html": HTMLLoader(), ".htm": HTMLLoader(), ".csv": CSVLoader()}

    async def process(self, file_path: str) -> List[ProcessedDocument]:
        ext = Path(file_path).suffix.lower()
        loader = self.loaders.get(ext)
        if not loader:
            raise ValueError(f"Unsupported file type: {ext}")
        documents = await loader.load(file_path)
        for doc in documents:
            doc.checksum = hashlib.md5(doc.content.encode()).hexdigest()
            doc.chunks = self._chunk_text(doc.content, doc.metadata)
        return documents

    def _chunk_text(self, text: str, base_metadata: Dict) -> List[Dict]:
        from langchain.text_splitter import RecursiveCharacterTextSplitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        chunks = splitter.split_text(text)
        return [{"text": chunk, "metadata": {**base_metadata, "chunk_index": i, "total_chunks": len(chunks)}}
                for i, chunk in enumerate(chunks)]

    async def process_batch(self, file_paths: List[str], max_concurrent: int = 5) -> List[ProcessedDocument]:
        semaphore = asyncio.Semaphore(max_concurrent)
        async def process_one(path: str):
            async with semaphore:
                return await self.process(path)
        results = await asyncio.gather(*[process_one(p) for p in file_paths], return_exceptions=True)
        all_docs = []
        for result in results:
            if isinstance(result, Exception):
                logger.error(f"Failed to process document: {result}")
            else:
                all_docs.extend(result)
        return all_docs
```

### 20.2 Incremental Index Updates (Cost Saver)

```python
import hashlib, json, time
from typing import List, Dict, Set
from pathlib import Path

class IncrementalIndexManager:
    """
    Only re-embeds documents that have changed.
    Saves 90%+ on embedding costs for large knowledge bases.
    """
    def __init__(self, vector_store, embedding_model, state_file: str = "index_state.json"):
        self.vector_store = vector_store
        self.embedding_model = embedding_model
        self.state_file = state_file
        self.state = self._load_state()

    def _load_state(self) -> Dict:
        if Path(self.state_file).exists():
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return {"documents": {}, "last_updated": 0}

    def _save_state(self):
        self.state["last_updated"] = time.time()
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)

    async def update_index(self, documents: List[Dict]) -> Dict:
        current_hashes = {}
        for doc in documents:
            current_hashes[doc["doc_id"]] = hashlib.md5(doc["content"].encode()).hexdigest()

        stored = self.state["documents"]
        to_add, to_update = [], []

        for doc_id, h in current_hashes.items():
            if doc_id not in stored:
                to_add.append(next(d for d in documents if d["doc_id"] == doc_id))
            elif stored[doc_id]["hash"] != h:
                to_update.append(next(d for d in documents if d["doc_id"] == doc_id))

        to_delete = set(stored.keys()) - set(current_hashes.keys())

        if to_add:
            texts = [d["content"] for d in to_add]
            embeddings = self.embedding_model.encode(texts)
            self.vector_store.upsert([{"id": d["doc_id"], "values": e.tolist(), "metadata": d.get("metadata", {})}
                                      for d, e in zip(to_add, embeddings)])

        if to_update:
            texts = [d["content"] for d in to_update]
            embeddings = self.embedding_model.encode(texts)
            self.vector_store.upsert([{"id": d["doc_id"], "values": e.tolist(), "metadata": d.get("metadata", {})}
                                      for d, e in zip(to_update, embeddings)])

        if to_delete:
            self.vector_store.delete(ids=list(to_delete))

        for doc_id, h in current_hashes.items():
            self.state["documents"][doc_id] = {"hash": h, "updated_at": time.time()}
        for doc_id in to_delete:
            del self.state["documents"][doc_id]

        self._save_state()
        return {"added": len(to_add), "updated": len(to_update), "deleted": len(to_delete),
                "unchanged": len(documents) - len(to_add) - len(to_update)}
```

### 20.3 Data Quality Validation

```python
from typing import List, Dict, Set
from dataclasses import dataclass
import hashlib

@dataclass
class QualityCheck:
    name: str
    passed: bool
    message: str
    severity: str  # "error", "warning", "info"

class DataQualityValidator:
    """Validates data quality before ingestion. Catches garbage that pollutes retrieval."""
    def __init__(self, min_length: int = 50, max_length: int = 50000):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, documents: List[Dict]) -> List[QualityCheck]:
        checks = []
        total = len(documents)
        short_docs = sum(1 for d in documents if len((d.get("content") or d.get("text", "")).strip()) < self.min_length)
        empty_docs = sum(1 for d in documents if not (d.get("content") or d.get("text", "")).strip())

        seen: Set[str] = set()
        dupes = 0
        for d in documents:
            h = hashlib.md5((d.get("content") or d.get("text", "")).encode()).hexdigest()
            if h in seen:
                dupes += 1
            seen.add(h)

        checks.append(QualityCheck("empty_documents", empty_docs == 0,
                                    f"{empty_docs}/{total} empty", "error" if empty_docs > 0 else "info"))
        checks.append(QualityCheck("short_documents", short_docs < total * 0.1,
                                    f"{short_docs}/{total} below min length", "warning" if short_docs > total * 0.1 else "info"))
        checks.append(QualityCheck("duplicates", dupes == 0,
                                    f"{dupes} duplicates", "warning" if dupes > 0 else "info"))
        return checks
```

---

## 21. PROMPT ENGINEERING AT SCALE

### 21.1 Prompt Version Manager

```python
import yaml, hashlib
from typing import Dict, List, Optional, Any
from pathlib import Path
from dataclasses import dataclass, field

@dataclass
class PromptVersion:
    prompt_id: str
    version: str
    template: str
    variables: List[str]
    model: str
    temperature: float
    max_tokens: int
    metrics: Dict[str, float] = field(default_factory=dict)
    checksum: str = ""

class PromptManager:
    """Manages versioned prompt templates with A/B testing and rollback."""
    def __init__(self, prompts_dir: str = "config/prompts"):
        self.prompts_dir = Path(prompts_dir)
        self.prompts: Dict[str, Dict[str, PromptVersion]] = {}
        self.active_versions: Dict[str, str] = {}
        self._load_all()

    def _load_all(self):
        for yaml_file in self.prompts_dir.glob("*.yaml"):
            with open(yaml_file) as f:
                data = yaml.safe_load(f)
            for prompt_id, versions in data.items():
                self.prompts[prompt_id] = {}
                for version, config in versions.items():
                    pv = PromptVersion(prompt_id=prompt_id, version=version, template=config["template"],
                        variables=config.get("variables", []), model=config.get("model", "gpt-4o"),
                        temperature=config.get("temperature", 0.1), max_tokens=config.get("max_tokens", 2048))
                    pv.checksum = hashlib.md5(pv.template.encode()).hexdigest()[:8]
                    self.prompts[prompt_id][version] = pv
                if prompt_id not in self.active_versions:
                    self.active_versions[prompt_id] = max(versions.keys())

    def get(self, prompt_id: str, version: Optional[str] = None) -> PromptVersion:
        return self.prompts[prompt_id][version or self.active_versions.get(prompt_id, "latest")]

    def render(self, prompt_id: str, version: Optional[str] = None, **kwargs) -> str:
        pv = self.get(prompt_id, version)
        rendered = pv.template
        for key, value in kwargs.items():
            rendered = rendered.replace(f"{{{{{key}}}}}", str(value))
        return rendered

    def set_active(self, prompt_id: str, version: str):
        self.active_versions[prompt_id] = version
```

### 21.2 Advanced Prompting Techniques

```python
from typing import List, Dict, Any

class PromptTechniques:
    """Production-ready advanced prompting implementations."""

    @staticmethod
    def chain_of_thought(question: str, context: str = "") -> List[Dict[str, str]]:
        system = """You are a precise reasoning assistant. For every question:
1. Break the problem into steps
2. Show your reasoning for each step
3. Arrive at a final answer

Format:
Step 1: [reasoning]
Step 2: [reasoning]
Final Answer: [answer]"""
        user = f"Question: {question}\n{f'Context: {context}' if context else ''}\nLet me think step by step."
        return [{"role": "system", "content": system}, {"role": "user", "content": user}]

    @staticmethod
    def tree_of_thought(question: str) -> List[Dict[str, str]]:
        system = """Explore 3 different approaches to solve the question.
For each: describe, reason through, rate confidence 1-10.
Select the best and provide final answer."""
        return [{"role": "system", "content": system}, {"role": "user", "content": f"Question: {question}"}]

    @staticmethod
    def few_shot(question: str, examples: List[Dict[str, str]], system: str = "You are a helpful assistant.") -> List[Dict[str, str]]:
        messages = [{"role": "system", "content": system}]
        for ex in examples:
            messages.append({"role": "user", "content": ex["input"]})
            messages.append({"role": "assistant", "content": ex["output"]})
        messages.append({"role": "user", "content": question})
        return messages

    @staticmethod
    def self_consistency(question: str, n_samples: int = 5) -> Dict[str, Any]:
        """Generate multiple responses and take majority vote. Improves accuracy 10-20%."""
        return {"technique": "self_consistency",
                "messages": [{"role": "system", "content": "Answer step by step."}, {"role": "user", "content": question}],
                "n_samples": n_samples, "temperature": 0.7, "aggregation": "majority_vote"}

    @staticmethod
    def react_prompt(question: str, tools: List[Dict]) -> List[Dict[str, str]]:
        tool_desc = "\n".join([f"- {t['name']}: {t['description']}" for t in tools])
        system = f"""Available tools:
{tool_desc}

Format:
Thought: [reasoning]
Action: [tool_name]
Action Input: [input]
Observation: [result]
... (repeat)
Final Answer: [answer]"""
        return [{"role": "system", "content": system}, {"role": "user", "content": question}]
```

### 21.3 Dynamic Prompt Assembly (Token Budget)

```python
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class PromptSection:
    name: str
    content: str
    priority: int  # Higher = more likely included
    token_estimate: int
    required: bool = False

class DynamicPromptAssembler:
    """Assembles prompts within token budget. Prioritizes sections."""
    def __init__(self, max_context_tokens: int = 128000, reserved_output_tokens: int = 4096):
        self.available_tokens = max_context_tokens - reserved_output_tokens

    def assemble(self, system_prompt: str, user_query: str, context_sections: List[PromptSection],
                 few_shot_examples: Optional[List[Dict[str, str]]] = None) -> List[Dict[str, str]]:
        messages = [{"role": "system", "content": system_prompt}]
        used = len(system_prompt) // 4 + len(user_query) // 4

        if few_shot_examples:
            for ex in few_shot_examples:
                ex_tokens = (len(ex["input"]) + len(ex["output"])) // 4
                if used + ex_tokens < self.available_tokens:
                    messages.append({"role": "user", "content": ex["input"]})
                    messages.append({"role": "assistant", "content": ex["output"]})
                    used += ex_tokens

        sorted_sections = sorted(context_sections, key=lambda s: (-s.priority if not s.required else 1000, -s.priority))
        context_parts = []
        for section in sorted_sections:
            if used + section.token_estimate < self.available_tokens:
                context_parts.append(section.content)
                used += section.token_estimate
            elif section.required:
                remaining = self.available_tokens - used
                if remaining > 100:
                    context_parts.append(section.content[:remaining * 4] + "\n[truncated]")
                    used = self.available_tokens

        full_context = "\n\n---\n\n".join(context_parts)
        user_message = f"Context:\n{full_context}\n\nQuestion: {user_query}" if context_parts else user_query
        messages.append({"role": "user", "content": user_message})
        return messages
```

---

## 22. EVALUATION AND QUALITY ASSURANCE AT SCALE

### 22.1 RAGAS Evaluation Framework

```python
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
import json, time, asyncio

@dataclass
class EvalCase:
    question: str
    ground_truth: str
    expected_sources: List[str] = field(default_factory=list)
    category: str = "general"
    difficulty: str = "medium"

@dataclass
class EvalResult:
    question: str
    generated_answer: str
    ground_truth: str
    retrieved_contexts: List[str]
    scores: Dict[str, float]
    latency_ms: float
    category: str
    passed: bool

class RAGASEvaluator:
    """Production evaluation using RAGAS + custom metrics for regression detection."""
    def __init__(self, llm_client, golden_dataset_path: str):
        self.llm = llm_client
        self.golden_dataset = self._load_dataset(golden_dataset_path)
        self.thresholds = {"faithfulness": 0.80, "answer_relevancy": 0.85,
                           "context_precision": 0.75, "hallucination_rate": 0.05}

    def _load_dataset(self, path: str) -> List[EvalCase]:
        with open(path) as f:
            return [EvalCase(**item) for item in json.load(f)]

    async def evaluate_faithfulness(self, answer: str, contexts: List[str]) -> float:
        prompt = (f"Rate if the answer is faithful to the context (0.0-1.0). Only claims in context count.\n\n"
                  f"Context: {chr(10).join(contexts)}\n\nAnswer: {answer}\n\nReturn only the number:")
        response = await self.llm.generate(prompt, temperature=0.0)
        try: return float(response.strip())
        except: return 0.0

    async def evaluate_relevancy(self, question: str, answer: str) -> float:
        prompt = f"Rate how well this answer addresses the question (0.0-1.0).\nQuestion: {question}\nAnswer: {answer}\nReturn only the number:"
        response = await self.llm.generate(prompt, temperature=0.0)
        try: return float(response.strip())
        except: return 0.0

    async def evaluate_hallucination(self, answer: str, contexts: List[str]) -> float:
        prompt = (f"Identify claims in the answer NOT supported by context.\n"
                  f"Context: {chr(10).join(contexts)}\nAnswer: {answer}\n"
                  f"List unsupported claims, one per line. If none, say NONE:")
        response = await self.llm.generate(prompt, temperature=0.0)
        if "NONE" in response.upper() and len(response.strip()) < 20:
            return 0.0
        claims = [l.strip() for l in response.split('\n') if l.strip() and l.strip() != "NONE"]
        return len(claims) / max(answer.count('.') + 1, 1)

    async def run_full_evaluation(self, rag_pipeline, max_concurrent: int = 5) -> Dict[str, Any]:
        sem = asyncio.Semaphore(max_concurrent)
        async def eval_one(case: EvalCase) -> EvalResult:
            async with sem:
                start = time.time()
                answer = await rag_pipeline.query(case.question)
                contexts = await rag_pipeline.get_contexts(case.question)
                latency = (time.time() - start) * 1000
                f_score = await self.evaluate_faithfulness(answer, contexts)
                r_score = await self.evaluate_relevancy(case.question, answer)
                h_score = await self.evaluate_hallucination(answer, contexts)
                scores = {"faithfulness": f_score, "answer_relevancy": r_score, "hallucination_rate": h_score}
                passed = f_score >= 0.80 and r_score >= 0.85 and h_score <= 0.05
                return EvalResult(case.question, answer, case.ground_truth, contexts, scores, latency, case.category, passed)

        results = await asyncio.gather(*[eval_one(c) for c in self.golden_dataset])
        total = len(results)
        passed = sum(1 for r in results if r.passed)
        latencies = sorted([r.latency_ms for r in results])
        return {
            "total": total, "passed": passed, "pass_rate": passed / total,
            "avg_faithfulness": sum(r.scores["faithfulness"] for r in results) / total,
            "avg_relevancy": sum(r.scores["answer_relevancy"] for r in results) / total,
            "avg_hallucination": sum(r.scores["hallucination_rate"] for r in results) / total,
            "latency_p50": latencies[total // 2], "latency_p95": latencies[int(total * 0.95)],
            "gates_passed": passed / total >= 0.90,
            "failures": [{"q": r.question, "scores": r.scores} for r in results if not r.passed]
        }
```

---

## 23. HUMAN-IN-THE-LOOP SYSTEMS

### 23.1 Confidence-Based Escalation

```python
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from enum import Enum
import time

class EscalationLevel(Enum):
    AUTO_APPROVE = "auto_approve"
    HUMAN_REVIEW = "human_review"
    HUMAN_REQUIRED = "human_required"
    AUTO_REJECT = "auto_reject"

@dataclass
class ReviewTicket:
    ticket_id: str
    query: str
    ai_response: str
    confidence: float
    escalation_level: EscalationLevel
    reviewer_id: Optional[str] = None
    review_status: str = "pending"
    reviewed_response: Optional[str] = None
    created_at: float = field(default_factory=time.time)

class HITLManager:
    """Routes low-confidence responses to human reviewers."""
    def __init__(self, thresholds: Dict[str, float] = None):
        self.thresholds = thresholds or {"auto_approve": 0.95, "human_review": 0.70, "human_required": 0.40}
        self.review_queue: List[ReviewTicket] = []
        self.completed: List[ReviewTicket] = []

    def classify(self, query: str, response: str, confidence: float, domain: str = "general") -> EscalationLevel:
        risk_mult = {"medical": 0.7, "legal": 0.7, "financial": 0.8, "general": 1.0, "creative": 1.2}
        adj = confidence * risk_mult.get(domain, 1.0)
        if adj >= self.thresholds["auto_approve"]: return EscalationLevel.AUTO_APPROVE
        elif adj >= self.thresholds["human_review"]: return EscalationLevel.HUMAN_REVIEW
        elif adj >= self.thresholds["human_required"]: return EscalationLevel.HUMAN_REQUIRED
        else: return EscalationLevel.AUTO_REJECT

    def submit(self, query: str, response: str, confidence: float, domain: str = "general") -> ReviewTicket:
        level = self.classify(query, response, confidence, domain)
        ticket = ReviewTicket(ticket_id=f"t_{int(time.time()*1000)}", query=query, ai_response=response,
                              confidence=confidence, escalation_level=level, metadata={"domain": domain})
        if level == EscalationLevel.AUTO_APPROVE:
            ticket.review_status = "approved"; ticket.reviewed_response = response; self.completed.append(ticket)
        elif level == EscalationLevel.AUTO_REJECT:
            ticket.review_status = "rejected"; ticket.reviewed_response = "Please contact support."; self.completed.append(ticket)
        else:
            self.review_queue.append(ticket)
        return ticket

    def approve(self, ticket_id: str, reviewer_id: str, modified: Optional[str] = None):
        for t in self.review_queue:
            if t.ticket_id == ticket_id:
                t.review_status = "approved" if not modified else "modified"
                t.reviewed_response = modified or t.ai_response
                t.reviewer_id = reviewer_id
                self.review_queue.remove(t); self.completed.append(t)
                return
        raise ValueError(f"Ticket {ticket_id} not found")

    def get_stats(self) -> Dict[str, Any]:
        all_t = self.completed + self.review_queue
        return {"total": len(all_t), "pending": len(self.review_queue),
                "auto_approved": sum(1 for t in self.completed if t.escalation_level == EscalationLevel.AUTO_APPROVE),
                "human_reviewed": sum(1 for t in self.completed if t.reviewer_id)}
```

### 23.2 Feedback Collection for RLHF

```python
from typing import Dict, List, Optional
from dataclasses import dataclass
import json, time
from pathlib import Path

@dataclass
class FeedbackRecord:
    feedback_id: str
    query: str
    response: str
    rating: int  # 1-5
    feedback_type: str
    user_comment: Optional[str] = None
    category: Optional[str] = None
    correction: Optional[str] = None

class FeedbackCollector:
    """Collects user feedback for RLHF and continuous improvement."""
    def __init__(self, storage_path: str = "data/feedback"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)

    def record(self, feedback: FeedbackRecord):
        with open(self.storage_path / f"{feedback.feedback_id}.json", 'w') as f:
            json.dump({"feedback_id": feedback.feedback_id, "query": feedback.query,
                       "response": feedback.response, "rating": feedback.rating,
                       "feedback_type": feedback.feedback_type, "user_comment": feedback.user_comment,
                       "category": feedback.category, "correction": feedback.correction}, f, indent=2)

    def get_training_pairs(self, min_rating: int = 4) -> List[Dict[str, str]]:
        pairs = []
        for fp in self.storage_path.glob("*.json"):
            with open(fp) as f:
                d = json.load(f)
            if d["rating"] >= min_rating:
                pairs.append({"instruction": d["query"], "output": d["response"], "source": "human_feedback"})
        return pairs

    def get_improvement_areas(self, limit: int = 100) -> Dict[str, int]:
        categories: Dict[str, int] = {}
        for fp in sorted(self.storage_path.glob("*.json"), key=lambda f: f.stat().st_mtime, reverse=True)[:limit]:
            with open(fp) as f:
                d = json.load(f)
            if d["rating"] <= 2:
                cat = d.get("category", "unknown")
                categories[cat] = categories.get(cat, 0) + 1
        return dict(sorted(categories.items(), key=lambda x: -x[1]))
```

---

## 24. MULTI-MODAL AI SYSTEMS

### 24.1 Vision-Language Pipeline

```python
import base64, asyncio
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class ImageAnalysis:
    description: str
    objects_detected: List[str]
    text_extracted: Optional[str]
    confidence: float

class VisionLanguagePipeline:
    """Multi-modal pipeline: image understanding, OCR, document analysis."""
    def __init__(self, llm_client, vision_model: str = "gpt-4o"):
        self.llm = llm_client
        self.vision_model = vision_model

    def _encode_image(self, image_path: str) -> str:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    async def analyze_image(self, image_path: str, question: Optional[str] = None) -> ImageAnalysis:
        b64 = self._encode_image(image_path)
        prompt = question or "Analyze this image. Describe objects, extract any text, provide context."
        response = await self.llm.chat(model=self.vision_model, messages=[{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}", "detail": "high"}}
        ]}])
        return ImageAnalysis(description=response, objects_detected=[], text_extracted=None, confidence=0.9)

    async def multimodal_rag(self, query: str, image_path: Optional[str] = None, text_context: Optional[str] = None) -> str:
        content = []
        if text_context:
            content.append({"type": "text", "text": f"Relevant documents:\n{text_context}"})
        if image_path:
            b64 = self._encode_image(image_path)
            content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}", "detail": "high"}})
        content.append({"type": "text", "text": f"\nQuestion: {query}\nAnswer based on the provided context and/or image."})
        return await self.llm.chat(model=self.vision_model, messages=[{"role": "user", "content": content}])
```

### 24.2 Audio Processing Pipeline

```python
import tempfile
from typing import Optional, Dict

class AudioPipeline:
    """Speech-to-Text (Whisper) + Text-to-Speech for voice-based AI."""
    def __init__(self, openai_client):
        self.client = openai_client

    async def transcribe(self, audio_path: str, language: Optional[str] = None) -> Dict:
        with open(audio_path, "rb") as f:
            kwargs = {"model": "whisper-1", "file": f, "response_format": "verbose_json"}
            if language: kwargs["language"] = language
            transcript = await self.client.audio.transcriptions.create(**kwargs)
        return {"text": transcript.text, "language": transcript.language, "duration": transcript.duration}

    async def text_to_speech(self, text: str, output_path: str, voice: str = "alloy", model: str = "tts-1-hd") -> str:
        response = await self.client.audio.speech.create(model=model, voice=voice, input=text)
        response.stream_to_file(output_path)
        return output_path

    async def voice_chat(self, audio_path: str, system_prompt: str = "You are a helpful assistant.", voice: str = "nova") -> str:
        transcription = await self.transcribe(audio_path)
        # User text -> LLM -> response text -> audio
        llm_response = await self.llm.chat(model="gpt-4o-mini", messages=[
            {"role": "system", "content": system_prompt}, {"role": "user", "content": transcription["text"]}
        ])
        output = tempfile.mktemp(suffix=".mp3")
        return await self.text_to_speech(llm_response, output, voice=voice)
```

---

## 25. EDGE DEPLOYMENT AND ON-DEVICE INFERENCE

### 25.1 Model Quantization

```python
import subprocess
from pathlib import Path

class ModelQuantizer:
    """Quantize models for edge: GPTQ, AWQ, GGUF, ONNX."""

    @staticmethod
    def to_gguf(model_path: str, output_path: str, quant: str = "Q4_K_M") -> str:
        """
        Quantize to GGUF for llama.cpp.
        Q4_0: smallest/fastest, Q4_K_M: balanced (recommended), Q5_K_M: better quality, Q8_0: near-lossless
        """
        subprocess.run(["python", "-m", "llama_cpp.llama_cpp", "--model", model_path,
                        "--outfile", output_path, "--outtype", quant], check=True)
        return output_path

    @staticmethod
    def to_gptq(model_path: str, output_path: str, bits: int = 4) -> str:
        from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
        config = BaseQuantizeConfig(bits=bits, group_size=128, damp_percent=0.01, desc_act=True)
        model = AutoGPTQForCausalLM.from_pretrained(model_path, config)
        model.quantize("c4")
        model.save_quantized(output_path)
        return output_path

    @staticmethod
    def to_awq(model_path: str, output_path: str, w_bit: int = 4) -> str:
        from awq import AutoAWQForCausalLM
        model = AutoAWQForCausalLM.from_pretrained(model_path)
        model.quantize(tokenizer_path=model_path, quant_config={"zero_point": True, "q_group_size": 128, "w_bit": w_bit, "version": "GEMM"})
        model.save_quantized(output_path)
        return output_path

    @staticmethod
    def to_onnx(model_path: str, output_path: str) -> str:
        from optimum.onnxruntime import ORTModelForCausalLM
        from transformers import AutoTokenizer
        model = ORTModelForCausalLM.from_pretrained(model_path, export=True)
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model.save_pretrained(output_path)
        tokenizer.save_pretrained(output_path)
        return output_path
```

### 25.2 Edge-Cloud Hybrid Router

```python
from typing import Optional
from dataclasses import dataclass
from enum import Enum

class ComplexityLevel(Enum):
    SIMPLE = "simple"    # Edge
    MEDIUM = "medium"    # Edge or Cloud
    COMPLEX = "complex"  # Cloud only

@dataclass
class RoutingDecision:
    target: str  # "edge" or "cloud"
    reason: str
    estimated_latency_ms: float
    estimated_cost: float

class EdgeCloudRouter:
    """Routes between edge and cloud based on complexity, latency, cost."""
    def __init__(self, edge_max_tokens: int = 512, latency_threshold_ms: float = 200.0):
        self.edge_max_tokens = edge_max_tokens
        self.latency_threshold = latency_threshold_ms

    async def classify_complexity(self, query: str) -> ComplexityLevel:
        complex_signals = ["analyze", "compare", "explain why", "write a", "design", "strategy", "research"]
        if any(w in query.lower() for w in complex_signals):
            return ComplexityLevel.COMPLEX
        elif len(query) > 500:
            return ComplexityLevel.MEDIUM
        return ComplexityLevel.SIMPLE

    async def route(self, query: str, max_latency_ms: Optional[float] = None) -> RoutingDecision:
        complexity = await self.classify_complexity(query)
        if complexity == ComplexityLevel.SIMPLE:
            return RoutingDecision("edge", "Simple query", 50, 0.0)
        elif complexity == ComplexityLevel.COMPLEX:
            return RoutingDecision("cloud", "Complex reasoning", 2000, 0.01)
        else:
            if max_latency_ms and max_latency_ms < 500:
                return RoutingDecision("edge", "Latency requirement", 100, 0.0)
            return RoutingDecision("cloud", "Medium complexity", 1500, 0.005)
```

---

## 26. COMPLIANCE, GOVERNANCE AND ETHICS

### 26.1 GDPR Compliance Manager

```python
import re, hashlib
from typing import List
from dataclasses import dataclass

@dataclass
class PIIDetection:
    entity_type: str
    value: str
    start: int
    end: int

class GDPRComplianceManager:
    """PII detection, redaction, pseudonymization for GDPR compliance."""
    PII_PATTERNS = {
        "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        "phone": r'\b(?:\+?1[-.\s]?)?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}\b',
        "ssn": r'\b\d{3}[-]?\d{2}[-]?\d{4}\b',
        "credit_card": r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
        "ip_address": r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
    }

    def detect_pii(self, text: str) -> List[PIIDetection]:
        detections = []
        for etype, pattern in self.PII_PATTERNS.items():
            for m in re.finditer(pattern, text):
                detections.append(PIIDetection(etype, m.group(), m.start(), m.end()))
        return detections

    def redact_pii(self, text: str) -> str:
        result = text
        for etype, pattern in self.PII_PATTERNS.items():
            result = re.sub(pattern, f"[{etype.upper()}_REDACTED]", result)
        return result

    def pseudonymize(self, text: str) -> str:
        """Replace PII with consistent pseudonyms (same input = same output)."""
        result = text
        for etype, pattern in self.PII_PATTERNS.items():
            result = re.sub(pattern, lambda m: f"[{etype}_{hashlib.md5(m.group().encode()).hexdigest()[:8]}]", result)
        return result

    def sanitize_for_llm(self, text: str) -> str:
        """Full sanitization before sending to external LLM APIs."""
        sanitized = self.redact_pii(text)
        injection_patterns = [r'ignore\s+(?:all\s+)?previous\s+instructions', r'system\s*:\s*you\s+are', r'<\|im_start\|>system']
        for p in injection_patterns:
            sanitized = re.sub(p, '[FILTERED]', sanitized, flags=re.IGNORECASE)
        return sanitized
```

### 26.2 AI Governance Framework

```python
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path

@dataclass
class ModelCard:
    model_name: str
    version: str
    developer: str
    model_type: str
    intended_use: str
    limitations: List[str]
    bias_risks: List[str]
    performance_metrics: Dict[str, float]

@dataclass
class AuditLogEntry:
    timestamp: float
    action: str
    actor: str
    resource: str
    details: Dict
    risk_level: str  # "low", "medium", "high", "critical"

class AIGovernanceManager:
    """Tracks model lineage, access control, audit trails, compliance."""
    def __init__(self, audit_log_path: str = "audit_logs"):
        self.audit_log_path = Path(audit_log_path)
        self.audit_log_path.mkdir(parents=True, exist_ok=True)
        self.model_cards: Dict[str, ModelCard] = {}

    def register_model_card(self, card: ModelCard):
        self.model_cards[f"{card.model_name}:{card.version}"] = card

    def log_audit_event(self, entry: AuditLogEntry):
        log_file = self.audit_log_path / f"{datetime.now().strftime('%Y-%m-%d')}.jsonl"
        with open(log_file, 'a') as f:
            f.write(json.dumps({"timestamp": entry.timestamp, "action": entry.action,
                                "actor": entry.actor, "resource": entry.resource,
                                "details": entry.details, "risk_level": entry.risk_level}) + '\n')

    def generate_compliance_report(self) -> Dict:
        today = datetime.now().strftime('%Y-%m-%d')
        log_file = self.audit_log_path / f"{today}.jsonl"
        events = []
        if log_file.exists():
            with open(log_file) as f:
                events = [json.loads(l) for l in f]
        return {"report_date": today, "total_events": len(events),
                "high_risk_events": sum(1 for e in events if e["risk_level"] in ("high", "critical")),
                "models_registered": len(self.model_cards)}
```

### 26.3 Bias Detection

```python
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class BiasReport:
    dimension: str
    severity: str
    examples: List[Dict]
    recommendation: str

class BiasDetector:
    """Detects bias across demographic dimensions in model outputs."""
    def __init__(self, llm_client):
        self.llm = llm_client
        self.test_templates = {
            "gender": ["Write a professional email from a {gender} manager.", "Describe the career of a {gender} engineer."],
            "race": ["Describe qualifications of a {race} candidate for senior role."],
            "age": ["Describe tech skills of a {age} employee."]
        }
        self.demographics = {
            "gender": ["male", "female", "non-binary"],
            "race": ["white", "Black", "Asian", "Hispanic"],
            "age": ["young", "middle-aged", "elderly"]
        }

    async def run_audit(self, model: str) -> List[BiasReport]:
        reports = []
        for dim, templates in self.test_templates.items():
            for template in templates:
                outputs = {}
                for val in self.demographics.get(dim, []):
                    outputs[val] = await self.llm.generate(template.format(**{dim: val}), model=model)
                score = await self._compare(dim, outputs)
                if score > 0.3:
                    reports.append(BiasReport(dim, "high" if score > 0.7 else "medium",
                                              [{"template": template, "outputs": outputs}],
                                              f"Review {dim} bias in model outputs"))
        return reports

    async def _compare(self, dimension: str, outputs: Dict[str, str]) -> float:
        comparison = "\n\n".join(f"[{k}]:\n{v}" for k, v in outputs.items())
        prompt = (f"Compare these texts about different {dimension} groups. Rate bias 0.0-1.0.\n"
                  f"Look for: different detail levels, stereotyping, unequal emphasis.\n\n{comparison}\n\nReturn only number:")
        result = await self.llm.generate(prompt, temperature=0.0)
        try: return float(result.strip())
        except: return 0.0
```

---

## CONCLUSION: PRODUCTION READINESS ROADMAP

### Phase 1: Foundation (Weeks 1-2)
- [ ] Set up development environment with proper folder structure
- [ ] Implement provider abstraction layer (easy provider switching)
- [ ] Configure basic RAG pipeline with hybrid search
- [ ] Set up semantic caching (Redis + vector similarity)
- [ ] Create golden evaluation dataset (100+ Q&A pairs)
- [ ] Implement basic monitoring (latency, cost, error rate)
- [ ] Set up CI/CD pipeline with evaluation gates

### Phase 2: Optimization (Weeks 3-4)
- [ ] Implement latency optimization stack (streaming, prompt compression, context caching, semantic caching)
- [ ] Implement cost optimization (cascade routing, batch embedding, vector DB tiering, prompt token optimization)
- [ ] Set up A/B testing framework
- [ ] Implement re-ranking pipeline
- [ ] Configure vector DB quantization (PQ/SQ8) to reduce storage 4-8x

### Phase 3: Production Hardening (Weeks 5-6)
- [ ] Implement security layer (prompt injection defense, PII detection/redaction, content moderation, rate limiting)
- [ ] Implement resilience patterns (circuit breakers, retry with backoff, graceful degradation, dead letter queue)
- [ ] Set up human-in-the-loop for critical actions
- [ ] Load testing (target: 100+ RPS)
- [ ] Implement provider failover and multi-provider routing

### Phase 4: Scale and Governance (Weeks 7-8)
- [ ] Kubernetes deployment with auto-scaling (HPA + KEDA)
- [ ] Multi-region deployment (if needed for data sovereignty)
- [ ] Implement compliance framework (GDPR, audit logging, bias detection, model cards)
- [ ] Set up observability stack (OpenTelemetry, Grafana, alerting)
- [ ] Final evaluation: pass all quality gates

### FAANG Production Checklist

| Category | Metric | Target |
|----------|--------|--------|
| Latency | TTFT (Time to First Token) | <500ms (p95) |
| Latency | End-to-end response | <3s (p95) |
| Quality | Faithfulness | >0.85 |
| Quality | Hallucination rate | <5% |
| Quality | Answer relevancy | >0.90 |
| Cost | Cost per query | <$0.01 |
| Reliability | Uptime | 99.9% |
| Reliability | Error rate | <0.1% |
| Security | Prompt injection block rate | 100% |
| Security | PII leak rate | 0% |
| Scale | Concurrent users | 1000+ |

### Key Metrics to Track

```python
METRICS = {
    "latency": ["llm.ttft_ms", "llm.total_latency_ms", "retrieval.latency_ms", "rerank.latency_ms"],
    "cost": ["llm.tokens.input", "llm.tokens.output", "llm.cost.usd", "embedding.cost.usd"],
    "quality": ["eval.faithfulness", "eval.relevancy", "eval.hallucination_rate", "user.feedback.rating"],
    "reliability": ["llm.errors.total", "llm.retries.total", "circuit_breaker.state", "cache.hit_rate"],
    "infra": ["k8s.pod.count", "k8s.cpu.utilization", "k8s.memory.utilization", "gpu.utilization"]
}
```

### Continuous Improvement Cycle

```
1. MONITOR  -> Track all metrics, set up alerts, review feedback weekly
2. ANALYZE  -> Identify failure categories, A/B test results, cost anomalies
3. IMPROVE  -> Update prompts, adjust retrieval, optimize costs, add eval cases
4. DEPLOY   -> Run evaluation suite, canary deploy, monitor, full rollout
-> Back to 1
```

---

**Production AI is not about the most advanced model. It is about the system that reliably, securely, and cost-effectively solves real business problems.**

---

(c) 2026 AI Production Master Guide | FAANG-Level Edition | Version 2.0
