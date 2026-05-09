# UAE AI STUDENT PROJECTS
## Production-Ready Projects for Each AI Technique
### Complete Implementation Prompts & Architectures

**Target Audience**: Computer Science & Engineering Students in UAE  
**Focus Areas**: Healthcare, Legal Tech, Agriculture, Smart Cities  
**Skill Level**: Intermediate to Advanced  
**Last Updated**: May 2026

---

## TABLE OF CONTENTS

1. [Project 1: UAE Labor Law Assistant](#project-1-simple-rag) - **Simple RAG**
2. [Project 2: Medical Research Intelligence System](#project-2-agentic-rag) - **Agentic RAG**
3. [Project 3: UAE University Enrollment Assistant](#project-3-ai-agent) - **AI Agent**
4. [Project 4: Clinical Diagnosis Support System](#project-4-multi-agent) - **Multi-Agent**
5. [Project 5: Arabic Legal Document Analyzer](#project-5-fine-tuning) - **Fine-Tuning**
6. [Project 6: Prescription Verification System](#project-6-rag-human-in-loop) - **RAG + Human-in-Loop**
7. [Project 7: Real-Time Farm Advisory Bot](#project-7-rag-streaming) - **RAG + Streaming**
8. [Project 8: Smart Campus Operations Agent](#project-8-agent-with-tools) - **Agent with Tools**
9. [Project 9: Integrated Healthcare Platform](#project-9-combination-1) - **Combination Strategy**
10. [Project 10: Legal Contract Automation Suite](#project-10-combination-2) - **Advanced Combination**

---

## PROJECT 1: UAE LABOR LAW ASSISTANT
**Technique**: Simple RAG  
**Domain**: Legal Tech  
**Difficulty**: ⭐⭐☆☆☆ (Intermediate)

### Problem Statement
UAE labor laws are complex and frequently updated. Workers and small business owners need quick, accurate answers to common questions about employment rights, visa regulations, and workplace disputes without hiring expensive lawyers.

### Why This Project?
- **Real Impact**: Helps thousands of workers understand their rights
- **UAE Relevance**: Based on UAE Federal Law No. 33 of 2021
- **Educational Value**: Teaches RAG fundamentals with legal documents
- **Portfolio Piece**: Shows ability to work with complex, structured documents

### Architecture Diagram
```
┌─────────────────────────────────────────────────────┐
│                   USER INTERFACE                    │
│            (Streamlit Web Application)              │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│              QUERY PROCESSING                       │
│  ├─ Language Detection (Arabic/English)             │
│  ├─ Query Classification (visa/salary/termination)  │
│  └─ Query Expansion (add legal synonyms)            │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│           RETRIEVAL PIPELINE                        │
│  ├─ Vector Search (Pinecone)                        │
│  │  └─ Embedding: text-embedding-3-large            │
│  ├─ Metadata Filtering (by law section)             │
│  └─ Re-Ranking (top 3 most relevant articles)       │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│         CONTEXT CONSTRUCTION                        │
│  ├─ Include: Relevant law articles                  │
│  ├─ Include: Article numbers for citation           │
│  └─ Include: Effective dates                        │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│            LLM GENERATION                           │
│  Model: GPT-4o-mini (cost-effective)                │
│  Temperature: 0.1 (factual accuracy)                │
│  Output: Answer + Legal Citations                   │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│         POST-PROCESSING                             │
│  ├─ Format citations                                │
│  ├─ Add disclaimer                                  │
│  └─ Suggest related questions                       │
└─────────────────────────────────────────────────────┘
```

### Technology Stack
- **Frontend**: Streamlit (Python)
- **Vector DB**: Pinecone (free tier: 100K vectors)
- **Embeddings**: OpenAI text-embedding-3-large
- **LLM**: GPT-4o-mini
- **Document Processing**: PyPDF2, LangChain
- **Deployment**: Streamlit Cloud (free)

### Dataset
- UAE Federal Law No. 33 of 2021 (Labor Law)
- UAE Cabinet Resolution No. 1 of 2022 (Implementation Regulations)
- Ministry of Human Resources guides (Arabic + English)
- ~500 pages of legal documents

### Implementation Prompt

```markdown
# PROMPT FOR AI ASSISTANT

You are an expert AI engineer building a Simple RAG system for UAE Labor Law. 
Implement the following production-ready system:

## PROJECT REQUIREMENTS

### 1. Document Ingestion Pipeline

Create a Python script `ingest_documents.py` that:

**Input**: PDF files of UAE Labor Law (provided in `/data/raw/`)
- UAE_Labor_Law_2021_EN.pdf
- UAE_Labor_Law_2021_AR.pdf
- Implementation_Regulations_2022_EN.pdf

**Processing Steps**:
1. Extract text from PDFs using PyPDF2
2. Split into chunks:
   - Chunk size: 500 tokens
   - Overlap: 50 tokens
   - Split on: Article boundaries (preserve legal structure)
   - Use RecursiveCharacterTextSplitter with custom separators

3. Extract metadata for each chunk:
   ```python
   metadata = {
       "source": "UAE Labor Law 2021",
       "article_number": "Article 15",
       "chapter": "Chapter 2: Employment Contract",
       "language": "en",
       "effective_date": "2022-02-02",
       "document_type": "federal_law"
   }
   ```

4. Generate embeddings using OpenAI text-embedding-3-large

5. Store in Pinecone:
   - Index name: "uae-labor-law"
   - Dimension: 3072
   - Metric: cosine similarity
   - Namespace: separate by language (en/ar)

**Output**: Confirmation that X chunks successfully ingested

**Code Structure**:
```python
# File: src/ingestion/document_processor.py

from typing import List, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
import PyPDF2
import re

class LegalDocumentProcessor:
    """
    Process UAE legal documents for RAG ingestion
    """
    
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\nArticle ",  # Legal article boundary
                "\nChapter ",  # Chapter boundary
                "\n\n",       # Paragraph
                "\n",         # Line
                ". ",         # Sentence
                " "           # Word
            ]
        )
    
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text preserving structure"""
        # Implementation here
        pass
    
    def extract_article_metadata(self, text: str) -> Dict:
        """
        Extract article number, chapter, section using regex
        
        Example patterns:
        - "Article 15" or "المادة 15"
        - "Chapter 2: Employment Contract"
        """
        # Implementation here
        pass
    
    def chunk_document(self, document: str) -> List[Dict]:
        """
        Chunk document while preserving legal structure
        
        Returns:
            List of dicts with 'text' and 'metadata'
        """
        # Implementation here
        pass
```

### 2. Retrieval Pipeline

Create `src/retrieval/labor_law_retriever.py`:

**Functionality**:
- Accept user query in English or Arabic
- Detect language automatically
- Search appropriate namespace in Pinecone
- Retrieve top 10 candidates
- Re-rank to top 3 using cross-encoder
- Return structured results with citations

**Key Features**:
```python
class LaborLawRetriever:
    """
    Retrieval system for UAE Labor Law
    """
    
    def __init__(self, pinecone_index, embedding_model):
        self.index = pinecone_index
        self.embedder = embedding_model
        self.reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-12-v2')
    
    def retrieve(
        self, 
        query: str, 
        filters: Dict = None,
        top_k: int = 3
    ) -> List[Dict]:
        """
        Retrieve relevant law articles
        
        Args:
            query: User's legal question
            filters: Optional metadata filters (e.g., {"chapter": "Employment Contract"})
            top_k: Number of final results
            
        Returns:
            List of dicts with:
            - article_text
            - article_number
            - relevance_score
            - metadata
        """
        # Step 1: Embed query
        query_vector = self.embedder.encode(query)
        
        # Step 2: Vector search (get top 10)
        results = self.index.query(
            vector=query_vector.tolist(),
            top_k=10,
            include_metadata=True,
            filter=filters
        )
        
        # Step 3: Re-rank with cross-encoder
        pairs = [[query, r['metadata']['text']] for r in results['matches']]
        scores = self.reranker.predict(pairs)
        
        # Step 4: Sort and return top-k
        ranked_results = sorted(
            zip(results['matches'], scores),
            key=lambda x: x[1],
            reverse=True
        )[:top_k]
        
        # Step 5: Format output
        return self._format_results(ranked_results)
    
    def _format_results(self, ranked_results):
        """Format for LLM consumption"""
        # Implementation
        pass
```

### 3. RAG Query Pipeline

Create `src/core/labor_law_rag.py`:

**System Prompt**:
```python
SYSTEM_PROMPT = """You are a UAE Labor Law expert assistant. Your role is to provide accurate, helpful information about UAE Federal Law No. 33 of 2021.

CRITICAL RULES:
1. ONLY use information from the provided law articles below
2. Always cite the specific Article number when making a claim
3. If the answer is not in the provided context, say "This information is not covered in the articles provided. Please consult the full law or a legal professional."
4. Never make up article numbers or legal provisions
5. If the question involves complex legal interpretation, recommend consulting a lawyer
6. Provide answers in the same language as the question (Arabic or English)

FORMAT YOUR RESPONSE:
- Start with a direct answer
- Support with specific article citations: [Article X]
- Include relevant quotes from the law
- End with a disclaimer if appropriate

DISCLAIMER (include when relevant):
"This information is for educational purposes only and does not constitute legal advice. For specific legal matters, please consult a qualified lawyer or the UAE Ministry of Human Resources and Emiratisation."
"""

def answer_query(query: str, retrieved_articles: List[Dict]) -> str:
    """
    Generate answer using RAG
    """
    # Construct context from retrieved articles
    context = "\n\n".join([
        f"[Article {article['article_number']}]\n{article['text']}"
        for article in retrieved_articles
    ])
    
    # Build user prompt
    user_prompt = f"""Based on the following UAE Labor Law articles, answer this question:

Question: {query}

Relevant Law Articles:
{context}

Provide a clear, accurate answer with article citations."""
    
    # Call LLM
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.1,
        max_tokens=800
    )
    
    return response.choices[0].message.content
```

### 4. Streamlit Web Interface

Create `app.py`:

**Features**:
- Bilingual interface (Arabic/English toggle)
- Example questions for common scenarios
- Citation display with expandable law articles
- Copy answer button
- Feedback mechanism (thumbs up/down)

**UI Components**:
```python
import streamlit as st

st.set_page_config(
    page_title="UAE Labor Law Assistant",
    page_icon="⚖️",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("⚖️ UAE Labor Law Assistant")
    language = st.selectbox("Language", ["English", "العربية"])
    
    st.markdown("### Example Questions")
    examples = [
        "What is the notice period for resignation?",
        "Am I entitled to end-of-service gratuity?",
        "How many days of annual leave do I get?",
        "What are the rules for working hours?",
        "Can my employer terminate me during probation?"
    ]
    
    for example in examples:
        if st.button(example):
            st.session_state.query = example

# Main interface
st.header("Ask a Question About UAE Labor Law")

query = st.text_input(
    "Enter your question:",
    value=st.session_state.get('query', ''),
    placeholder="e.g., What is the minimum notice period for resignation?"
)

if st.button("Get Answer", type="primary"):
    with st.spinner("Searching UAE Labor Law..."):
        # Retrieve relevant articles
        articles = retriever.retrieve(query, top_k=3)
        
        # Generate answer
        answer = rag_pipeline.answer_query(query, articles)
        
        # Display answer
        st.markdown("### Answer")
        st.markdown(answer)
        
        # Display sources
        with st.expander("📚 View Legal Citations"):
            for article in articles:
                st.markdown(f"**{article['article_number']}**")
                st.markdown(article['text'])
                st.divider()
        
        # Feedback
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👍 Helpful"):
                log_feedback(query, answer, positive=True)
        with col2:
            if st.button("👎 Not Helpful"):
                log_feedback(query, answer, positive=False)

# Disclaimer
st.info("⚠️ This is an educational tool. For legal advice, consult a qualified lawyer.")
```

### 5. Evaluation Suite

Create `tests/evaluation/test_rag_quality.py`:

**Golden Dataset** (create 50 Q&A pairs):
```json
{
  "questions": [
    {
      "question": "What is the maximum probation period?",
      "ground_truth_article": "Article 11",
      "ground_truth_answer": "The probation period shall not exceed six months.",
      "category": "employment_contract"
    },
    {
      "question": "How is end-of-service gratuity calculated?",
      "ground_truth_article": "Article 51",
      "ground_truth_answer": "21 days' wage for each of the first five years of service and 30 days' wage for each additional year.",
      "category": "termination"
    }
    // ... 48 more
  ]
}
```

**Metrics to Measure**:
1. **Faithfulness**: Are citations accurate? (target: >95%)
2. **Answer Relevancy**: Does it answer the question? (target: >90%)
3. **Context Precision**: Were the right articles retrieved? (target: >85%)
4. **Latency**: Response time (target: <3s)

**Evaluation Code**:
```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision

def run_evaluation(golden_dataset_path: str):
    """
    Run RAGAS evaluation on the system
    """
    # Load golden dataset
    dataset = load_golden_dataset(golden_dataset_path)
    
    # Generate predictions
    predictions = []
    for item in dataset:
        articles = retriever.retrieve(item['question'])
        answer = rag_pipeline.answer_query(item['question'], articles)
        
        predictions.append({
            'question': item['question'],
            'answer': answer,
            'contexts': [a['text'] for a in articles],
            'ground_truth': item['ground_truth_answer']
        })
    
    # Evaluate
    results = evaluate(
        predictions,
        metrics=[faithfulness, answer_relevancy, context_precision]
    )
    
    return results
```

### 6. Deployment Configuration

**Docker Setup** (`Dockerfile`):
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501"]
```

**Environment Variables** (`.env.example`):
```bash
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENVIRONMENT=us-east-1
PINECONE_INDEX_NAME=uae-labor-law
```

**Deployment Steps**:
1. Test locally: `streamlit run app.py`
2. Build Docker image: `docker build -t labor-law-assistant .`
3. Deploy to Streamlit Cloud (free tier)
4. Configure secrets in Streamlit dashboard

### DELIVERABLES

Please provide:

1. **Complete codebase** with folder structure:
   ```
   labor-law-assistant/
   ├── src/
   │   ├── ingestion/
   │   ├── retrieval/
   │   └── core/
   ├── tests/
   ├── data/
   ├── app.py
   ├── requirements.txt
   └── README.md
   ```

2. **README.md** with:
   - Project description
   - Setup instructions
   - API keys needed
   - How to run locally
   - How to deploy
   - Example screenshots

3. **Evaluation Report**:
   - RAGAS scores on 50 test questions
   - Latency benchmarks
   - Error analysis (what types of questions fail?)

4. **Documentation**:
   - Architecture diagram (Mermaid)
   - API documentation
   - Data pipeline flowchart

5. **Demo Video** (3 minutes):
   - Show document ingestion
   - Ask 5 example questions
   - Show citation mechanism
   - Explain evaluation results

### SUCCESS CRITERIA

- [ ] Retrieves correct articles for >85% of questions
- [ ] Generates accurate answers with proper citations
- [ ] Responds in <3 seconds
- [ ] Handles both Arabic and English queries
- [ ] Includes proper legal disclaimers
- [ ] Deployed and accessible via public URL
- [ ] Costs <$10/month to operate (free tier)

Build this system using best practices for production RAG systems. Focus on:
- Accurate retrieval
- Proper citation
- User experience
- Evaluation rigor
```

---

## PROJECT 2: MEDICAL RESEARCH INTELLIGENCE SYSTEM
**Technique**: Agentic RAG  
**Domain**: Healthcare  
**Difficulty**: ⭐⭐⭐⭐☆ (Advanced)

### Problem Statement
Medical students and researchers in UAE need to stay updated with the latest research on diseases, treatments, and drugs. Current approaches (manual PubMed searches) are time-consuming and often miss relevant papers across multiple sources.

### Why This Project?
- **Healthcare Impact**: Helps medical professionals make evidence-based decisions
- **UAE Relevance**: Supports research at institutions like MBRU, UAEU Medical School
- **Technical Challenge**: Multi-source retrieval, query refinement, self-correction
- **Career Value**: Demonstrates advanced AI agent capabilities

### Architecture Diagram
```
┌─────────────────────────────────────────────────────┐
│           USER QUERY                                │
│  "Latest treatments for Type 2 Diabetes in UAE"    │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│       QUERY ANALYSIS AGENT                          │
│  ├─ Identify medical entities (Disease, Drug)       │
│  ├─ Determine search strategy                       │
│  └─ Generate multiple search queries                │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│       MULTI-SOURCE RETRIEVAL                        │
│  ├─ PubMed API (research papers)                    │
│  ├─ Internal RAG (hospital protocols)               │
│  ├─ Web Search (clinical trials)                    │
│  └─ Drug Database API                               │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│       SELF-EVALUATION AGENT                         │
│  "Is this information sufficient?"                  │
│  ├─ Check: Coverage of key aspects                  │
│  ├─ Check: Recency of sources                       │
│  └─ Decision: Continue or refine search             │
└─────────────────┬───────────────────────────────────┘
                  │
       ┌──────────┴──────────┐
       │                     │
     [YES]                 [NO]
       │                     │
       │                     v
       │           ┌──────────────────┐
       │           │ QUERY REFINEMENT │
       │           │  Agent           │
       │           └────────┬─────────┘
       │                    │
       │                    └─────────┐
       │                              │
       v                              v
┌─────────────────────────────────────────────────────┐
│       SYNTHESIS AGENT                               │
│  ├─ Combine information from all sources            │
│  ├─ Resolve conflicts                               │
│  ├─ Generate evidence summary                       │
│  └─ Cite all sources                                │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│       STRUCTURED OUTPUT                             │
│  ├─ Executive Summary                               │
│  ├─ Key Findings (with evidence levels)             │
│  ├─ Treatment Options (ranked)                      │
│  ├─ Drug Information                                │
│  ├─ Clinical Trial Updates                          │
│  └─ References (APA format)                         │
└─────────────────────────────────────────────────────┘
```

### Implementation Prompt

```markdown
# PROMPT FOR AI ASSISTANT

Build an Agentic RAG system for medical research intelligence. This system must intelligently search multiple sources, evaluate its own results, and iteratively refine queries until comprehensive information is gathered.

## PROJECT REQUIREMENTS

### 1. Medical Query Router Agent

Create `src/agents/query_router.py`:

**Functionality**:
- Analyze medical queries using NER (Named Entity Recognition)
- Classify query intent: literature_review, drug_info, treatment_options, etc.
- Determine which sources to query
- Generate optimized search queries for each source

**Implementation**:
```python
from typing import Dict, List
from pydantic import BaseModel
import openai

class QueryPlan(BaseModel):
    """Structured plan for information gathering"""
    medical_entities: List[Dict]  # {type: "disease/drug/procedure", name: "..."}
    query_intent: str  # "literature_review", "drug_information", etc.
    sources_to_query: List[str]  # ["pubmed", "internal_rag", "web_search"]
    optimized_queries: Dict[str, str]  # {source: optimized_query}
    expected_info_types: List[str]  # ["efficacy", "side_effects", "dosage"]

class MedicalQueryRouter:
    """
    Analyzes medical queries and plans information retrieval
    """
    
    def __init__(self):
        self.client = openai.OpenAI()
    
    def analyze_and_plan(self, user_query: str) -> QueryPlan:
        """
        Create a retrieval plan for medical query
        """
        
        system_prompt = """You are a medical information retrieval specialist.
        
Analyze the user's medical query and create a comprehensive search plan.

Extract:
1. Medical entities (diseases, drugs, procedures, symptoms)
2. Query intent (What type of information is needed?)
3. Which sources to search:
   - pubmed: For peer-reviewed research papers
   - internal_rag: For hospital protocols/guidelines
   - web_search: For clinical trials, news, FDA updates
   - drug_db: For detailed drug information
4. Optimized search queries for each source
5. Expected information types to gather

Return a structured JSON plan."""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Query: {user_query}\n\nCreate retrieval plan:"}
            ],
            response_format={"type": "json_object"},
            temperature=0.1
        )
        
        plan_data = json.loads(response.choices[0].message.content)
        return QueryPlan(**plan_data)
```

### 2. Multi-Source Retrieval System

Create `src/retrieval/multi_source.py`:

**Sources**:
1. **PubMed** (via Bio.Entrez API)
2. **Internal RAG** (hospital protocols)
3. **Web Search** (clinical trials via ClinicalTrials.gov API)
4. **DrugBank API** (drug information)

**Implementation**:
```python
from Bio import Entrez
import requests

class MultiSourceRetriever:
    """
    Retrieves medical information from multiple sources
    """
    
    def __init__(self):
        # Configure email for PubMed API
        Entrez.email = "your_email@university.ae"
        
        # Internal RAG setup
        self.internal_rag = InternalRAGPipeline()
        
        # API keys
        self.drugbank_api_key = os.getenv("DRUGBANK_API_KEY")
    
    def search_pubmed(
        self,
        query: str,
        max_results: int = 10,
        recent_only: bool = True
    ) -> List[Dict]:
        """
        Search PubMed for research papers
        """
        # Build search term
        if recent_only:
            # Only papers from last 5 years
            query += " AND (\"2019\"[Date - Publication] : \"3000\"[Date - Publication])"
        
        # Search
        handle = Entrez.esearch(
            db="pubmed",
            term=query,
            retmax=max_results,
            sort="relevance"
        )
        record = Entrez.read(handle)
        handle.close()
        
        # Fetch details
        id_list = record["IdList"]
        if not id_list:
            return []
        
        handle = Entrez.efetch(
            db="pubmed",
            id=id_list,
            rettype="medline",
            retmode="text"
        )
        
        papers = self._parse_pubmed_results(handle.read())
        handle.close()
        
        return papers
    
    def search_clinical_trials(self, condition: str) -> List[Dict]:
        """
        Search ClinicalTrials.gov for active trials
        """
        url = "https://clinicaltrials.gov/api/query/study_fields"
        params = {
            "expr": condition,
            "fields": "NCTId,BriefTitle,OverallStatus,Phase,Condition,InterventionName",
            "fmt": "json",
            "max_rnk": 10
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        return self._format_trial_results(data)
    
    def search_drug_database(self, drug_name: str) -> Dict:
        """
        Get detailed drug information from DrugBank
        """
        # DrugBank API call
        # Returns: indications, dosage, interactions, contraindications
        pass
    
    def search_internal_protocols(self, query: str) -> List[Dict]:
        """
        Search hospital's internal knowledge base
        """
        return self.internal_rag.query(query, top_k=5)
```

### 3. Self-Evaluation Agent

Create `src/agents/evaluator.py`:

**Purpose**: Determine if retrieved information is sufficient

```python
class InformationEvaluator:
    """
    Evaluates completeness of retrieved information
    """
    
    def __init__(self):
        self.client = openai.OpenAI()
    
    def evaluate_completeness(
        self,
        original_query: str,
        expected_info_types: List[str],
        retrieved_info: Dict[str, List]
    ) -> Dict:
        """
        Evaluate if we have sufficient information
        
        Returns:
            {
                "is_sufficient": bool,
                "missing_aspects": List[str],
                "confidence": float,
                "suggestions_for_refinement": str
            }
        """
        
        # Summarize what was retrieved
        summary = self._summarize_retrieved(retrieved_info)
        
        evaluation_prompt = f"""You are evaluating the completeness of medical research results.

Original Query: {original_query}

Expected Information Types: {expected_info_types}

Retrieved Information Summary:
{summary}

Evaluate:
1. Is this information sufficient to answer the query comprehensively?
2. What key aspects are missing (if any)?
3. How confident are you in the completeness? (0-1)
4. If insufficient, how should we refine the search?

Return JSON:
{{
  "is_sufficient": true/false,
  "missing_aspects": ["aspect1", "aspect2"],
  "confidence": 0.85,
  "suggestions_for_refinement": "Search for more recent papers on X"
}}"""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": evaluation_prompt}],
            response_format={"type": "json_object"},
            temperature=0.1
        )
        
        return json.loads(response.choices[0].message.content)
```

### 4. Iterative Refinement Loop

Create `src/agents/research_agent.py`:

**Main orchestration logic**:

```python
class MedicalResearchAgent:
    """
    Orchestrates the agentic RAG workflow
    """
    
    def __init__(self):
        self.query_router = MedicalQueryRouter()
        self.retriever = MultiSourceRetriever()
        self.evaluator = InformationEvaluator()
        self.max_iterations = 3
    
    def research(self, user_query: str) -> Dict:
        """
        Execute iterative research process
        """
        trajectory = []
        all_retrieved_info = {
            "pubmed": [],
            "clinical_trials": [],
            "drug_info": {},
            "internal_protocols": []
        }
        
        # Step 1: Initial planning
        plan = self.query_router.analyze_and_plan(user_query)
        print(f"Query Plan: {plan.query_intent}")
        print(f"Will search: {plan.sources_to_query}")
        
        # Iterative search loop
        for iteration in range(self.max_iterations):
            print(f"\n=== Iteration {iteration + 1} ===")
            
            # Step 2: Execute searches
            for source in plan.sources_to_query:
                query = plan.optimized_queries.get(source, user_query)
                
                if source == "pubmed":
                    results = self.retriever.search_pubmed(query)
                    all_retrieved_info["pubmed"].extend(results)
                
                elif source == "clinical_trials":
                    condition = plan.medical_entities[0]['name']
                    results = self.retriever.search_clinical_trials(condition)
                    all_retrieved_info["clinical_trials"].extend(results)
                
                elif source == "drug_db" and plan.medical_entities:
                    drug_entities = [e for e in plan.medical_entities if e['type'] == 'drug']
                    for drug in drug_entities:
                        drug_info = self.retriever.search_drug_database(drug['name'])
                        all_retrieved_info["drug_info"][drug['name']] = drug_info
                
                elif source == "internal_rag":
                    results = self.retriever.search_internal_protocols(query)
                    all_retrieved_info["internal_protocols"].extend(results)
            
            # Step 3: Evaluate completeness
            evaluation = self.evaluator.evaluate_completeness(
                original_query=user_query,
                expected_info_types=plan.expected_info_types,
                retrieved_info=all_retrieved_info
            )
            
            trajectory.append({
                'iteration': iteration,
                'sources_queried': plan.sources_to_query,
                'num_results': sum(len(v) for v in all_retrieved_info.values() if isinstance(v, list)),
                'evaluation': evaluation
            })
            
            # Step 4: Check if sufficient
            if evaluation['is_sufficient'] or iteration == self.max_iterations - 1:
                print(f"Research complete after {iteration + 1} iterations")
                break
            
            # Step 5: Refine query for next iteration
            print(f"Missing: {evaluation['missing_aspects']}")
            print(f"Refinement: {evaluation['suggestions_for_refinement']}")
            
            # Update plan based on suggestions
            plan = self._refine_plan(plan, evaluation)
        
        # Step 6: Synthesize final answer
        final_report = self.synthesize_report(
            user_query=user_query,
            retrieved_info=all_retrieved_info,
            trajectory=trajectory
        )
        
        return final_report
    
    def synthesize_report(
        self,
        user_query: str,
        retrieved_info: Dict,
        trajectory: List
    ) -> Dict:
        """
        Generate comprehensive research report
        """
        # Prepare context from all sources
        context = self._format_all_sources(retrieved_info)
        
        synthesis_prompt = f"""You are a medical research synthesizer. Create a comprehensive, evidence-based report.

Original Query: {user_query}

Information Retrieved:
{context}

Generate a structured report with:

1. **Executive Summary** (2-3 sentences)
2. **Key Findings** (bullet points with evidence levels: A, B, C)
3. **Treatment Options** (if applicable, ranked by evidence)
4. **Drug Information** (if applicable)
5. **Ongoing Clinical Trials** (if applicable)
6. **Recommendations**
7. **References** (APA format, numbered)

Use medical terminology appropriately but explain complex terms.
Cite sources inline as [1], [2], etc.
Note any conflicts in the evidence.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": synthesis_prompt}],
            temperature=0.2,
            max_tokens=2000
        )
        
        report = response.choices[0].message.content
        
        return {
            "report": report,
            "sources": retrieved_info,
            "iterations": len(trajectory),
            "trajectory": trajectory
        }
```

### 5. Streamlit Interface

Create `app.py`:

```python
import streamlit as st

st.set_page_config(
    page_title="Medical Research Intelligence",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Medical Research Intelligence System")
st.markdown("*Agentic RAG for Evidence-Based Medicine*")

# Sidebar
with st.sidebar:
    st.header("Settings")
    
    max_iterations = st.slider("Max Search Iterations", 1, 5, 3)
    recent_only = st.checkbox("Recent papers only (5 years)", value=True)
    
    st.markdown("### Example Queries")
    examples = [
        "Latest treatments for Type 2 Diabetes",
        "Efficacy of Metformin in pediatric patients",
        "COVID-19 treatment protocols in ICU",
        "Drug interactions with Warfarin",
        "Clinical trials for Alzheimer's disease"
    ]
    
    for ex in examples:
        if st.button(ex, key=ex):
            st.session_state.query = ex

# Main query input
query = st.text_area(
    "Enter your medical research question:",
    value=st.session_state.get('query', ''),
    height=100,
    placeholder="e.g., What are the latest evidence-based treatments for hypertension in diabetic patients?"
)

if st.button("🔍 Research", type="primary"):
    if not query:
        st.warning("Please enter a question")
    else:
        # Initialize agent
        agent = MedicalResearchAgent()
        
        # Progress tracking
        progress_container = st.container()
        
        with progress_container:
            st.info("🤖 Agent Status: Planning search strategy...")
            
            # Execute research (with progress updates)
            with st.spinner("Conducting research..."):
                result = agent.research(query)
        
        # Display results
        st.success(f"✅ Research Complete ({result['iterations']} iterations)")
        
        # Main report
        st.markdown("## Research Report")
        st.markdown(result['report'])
        
        # Show trajectory
        with st.expander("🔄 View Research Process"):
            for step in result['trajectory']:
                st.markdown(f"**Iteration {step['iteration'] + 1}**")
                st.json(step['evaluation'])
        
        # Show sources
        with st.expander("📚 View All Sources"):
            tabs = st.tabs(["PubMed", "Clinical Trials", "Protocols", "Drug Info"])
            
            with tabs[0]:
                for paper in result['sources']['pubmed']:
                    st.markdown(f"**{paper['title']}**")
                    st.caption(f"{paper['authors']} ({paper['year']})")
                    st.markdown(paper['abstract'][:300] + "...")
                    st.divider()
            
            with tabs[1]:
                for trial in result['sources']['clinical_trials']:
                    st.markdown(f"**{trial['title']}**")
                    st.caption(f"Status: {trial['status']} | Phase: {trial['phase']}")
                    st.divider()
            
            # ... similar for other tabs

# Warning
st.warning("⚠️ This system is for educational purposes. All medical decisions should be made by qualified healthcare professionals.")
```

### 6. Evaluation Framework

Create `tests/evaluation/test_agentic_rag.py`:

**Metrics**:
1. **Iteration Efficiency**: Average iterations needed (target: <3)
2. **Source Diversity**: Uses multiple sources (target: >2 avg)
3. **Completeness**: Covers all aspects of query (manual eval)
4. **Evidence Quality**: Cites recent, peer-reviewed sources
5. **Latency**: Total time including iterations (target: <30s)

```python
def evaluate_research_quality(test_queries: List[Dict]):
    """
    Test queries should have:
    {
        "query": "...",
        "expected_sources": ["pubmed", "clinical_trials"],
        "expected_aspects": ["efficacy", "safety", "dosage"],
        "ground_truth_key_findings": ["finding1", "finding2"]
    }
    """
    
    agent = MedicalResearchAgent()
    results = []
    
    for test_case in test_queries:
        result = agent.research(test_case['query'])
        
        # Evaluate
        evaluation = {
            'query': test_case['query'],
            'iterations_used': result['iterations'],
            'sources_used': len([k for k, v in result['sources'].items() if v]),
            'all_aspects_covered': check_aspects_covered(
                result['report'],
                test_case['expected_aspects']
            ),
            'cited_recent_papers': count_recent_citations(result['sources']['pubmed']),
            'total_time': result.get('elapsed_time', 0)
        }
        
        results.append(evaluation)
    
    # Aggregate statistics
    avg_iterations = np.mean([r['iterations_used'] for r in results])
    avg_sources = np.mean([r['sources_used'] for r in results])
    completeness_rate = np.mean([r['all_aspects_covered'] for r in results])
    
    print(f"Average Iterations: {avg_iterations:.1f}")
    print(f"Average Sources Used: {avg_sources:.1f}")
    print(f"Completeness Rate: {completeness_rate:.1%}")
    
    return results
```

### DELIVERABLES

1. **Complete System** with:
   - Query router agent
   - Multi-source retrieval (PubMed, trials, internal docs)
   - Self-evaluation agent
   - Iterative refinement loop
   - Report synthesizer

2. **Web Interface** showing:
   - Real-time agent status
   - Iteration tracking
   - Source citations
   - Interactive report

3. **Evaluation Report**:
   - Test on 20 medical queries
   - Measure iteration efficiency
   - Assess information completeness
   - Compare to simple RAG baseline

4. **Documentation**:
   - Architecture diagram
   - Agent decision flow
   - API integration guides

### SUCCESS CRITERIA

- [ ] Retrieves from 3+ sources per query
- [ ] Self-corrects when information is incomplete
- [ ] Completes research in <3 iterations on average
- [ ] Generates comprehensive reports with proper citations
- [ ] Handles complex medical queries
- [ ] Total latency <30 seconds
- [ ] Cost <$0.50 per research query

Focus on the **agentic behavior**: show decision-making, iterative refinement, and multi-source intelligence gathering.
```

---

## PROJECT 3: UAE UNIVERSITY ENROLLMENT ASSISTANT
**Technique**: AI Agent  
**Domain**: Education Technology  
**Difficulty**: ⭐⭐⭐☆☆ (Intermediate-Advanced)

### Problem Statement
Students applying to UAE universities face complex enrollment processes involving checking admission requirements, calculating GPA conversions, verifying document requirements, and tracking application status across multiple systems.

### Why This Project?
- **Student Impact**: Simplifies enrollment for thousands of applicants
- **UAE Context**: Handles specific requirements for UAE/GCC nationals vs internationals
- **Learning Value**: Demonstrates tool use, state management, multi-step workflows
- **Real-World Complexity**: Deals with actual university systems and requirements

### Architecture Diagram
```
┌─────────────────────────────────────────────────────┐
│            STUDENT REQUEST                          │
│  "Help me apply to UAEU Computer Science"          │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│         PLANNING AGENT (ReAct)                      │
│  Thought: "Need to check admission requirements"    │
│  Action: search_requirements                        │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│           TOOL: Requirements Checker                │
│  Input: {university: "UAEU", program: "CS"}         │
│  Output: {min_gpa: 3.0, required_tests: [...]}      │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│         OBSERVATION                                 │
│  "Minimum GPA is 3.0, requires EmSAT or SAT"        │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│         NEXT ACTION                                 │
│  Thought: "Student mentioned their GPA is 3.2"      │
│  Action: calculate_eligibility                      │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│           TOOL: Eligibility Calculator              │
│  Input: {student_gpa: 3.2, requirements: {...}}     │
│  Output: {eligible: true, missing: ["EmSAT"]}       │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│         NEXT ACTION                                 │
│  Thought: "Student is eligible but needs EmSAT"     │
│  Action: check_emsat_dates                          │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│           TOOL: EmSAT Schedule API                  │
│  Output: {next_test: "2026-06-15", ...}             │
└─────────────────┬───────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────┐
│         FINAL RESPONSE                              │
│  "You're eligible! Here's your action plan..."      │
│  ├─ Step 1: Register for EmSAT by June 1           │
│  ├─ Step 2: Gather documents (list provided)        │
│  └─ Step 3: Submit application by July 15           │
└─────────────────────────────────────────────────────┘
```

### Implementation Prompt

```markdown
# PROMPT FOR AI ASSISTANT

Build an AI Agent system for UAE university enrollment assistance. The agent must use tools to check requirements, calculate eligibility, verify documents, and guide students through the application process.

## PROJECT REQUIREMENTS

### 1. Tool Definitions

Create the following tools in `src/tools/`:

#### Tool 1: University Requirements Checker
**File**: `src/tools/requirements_tool.py`

```python
class UniversityRequirementsTool:
    """
    Fetches admission requirements for UAE universities
    """
    
    def get_definition(self) -> Dict:
        """OpenAI function definition"""
        return {
            "type": "function",
            "function": {
                "name": "check_admission_requirements",
                "description": "Get admission requirements for a specific university program in UAE",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "university": {
                            "type": "string",
                            "enum": ["UAEU", "AUS", "AUD", "ZU", "HCT", "MBRU"],
                            "description": "University code"
                        },
                        "program": {
                            "type": "string",
                            "description": "Program name (e.g., 'Computer Science', 'Medicine')"
                        },
                        "student_nationality": {
                            "type": "string",
                            "enum": ["uae_national", "gcc_national", "international"],
                            "description": "Student nationality category"
                        }
                    },
                    "required": ["university", "program", "student_nationality"]
                }
            }
        }
    
    def execute(
        self,
        university: str,
        program: str,
        student_nationality: str
    ) -> Dict:
        """
        Query university requirements database
        """
        # In production, this would call a real API or database
        # For now, use a static knowledge base
        
        requirements_db = {
            "UAEU": {
                "Computer Science": {
                    "uae_national": {
                        "min_high_school_gpa": 3.0,
                        "required_tests": ["EmSAT English", "EmSAT Math"],
                        "min_emsat_scores": {"english": 1100, "math": 900},
                        "required_documents": [
                            "High school certificate",
                            "Emirates ID",
                            "Family book",
                            "EmSAT results"
                        ],
                        "application_fee": 0,  # Free for nationals
                        "application_deadline": "2026-07-15"
                    },
                    "international": {
                        "min_high_school_gpa": 3.5,
                        "required_tests": ["SAT or EmSAT", "IELTS or TOEFL"],
                        "min_sat_score": 1200,
                        "min_ielts_score": 6.0,
                        "required_documents": [
                            "High school certificate (attested)",
                            "Passport copy",
                            "Residence permit",
                            "SAT/IELTS results",
                            "No objection certificate"
                        ],
                        "application_fee": 1000,  # AED
                        "application_deadline": "2026-06-30"
                    }
                }
            }
            # Add more universities and programs
        }
        
        try:
            reqs = requirements_db[university][program][student_nationality]
            return {
                "success": True,
                "university": university,
                "program": program,
                "requirements": reqs
            }
        except KeyError:
            return {
                "success": False,
                "error": f"Requirements not found for {university} {program} ({student_nationality})"
            }
```

#### Tool 2: Eligibility Calculator
**File**: `src/tools/eligibility_tool.py`

```python
class EligibilityCalculatorTool:
    """
    Calculates student eligibility based on their profile
    """
    
    def get_definition(self) -> Dict:
        return {
            "type": "function",
            "function": {
                "name": "calculate_eligibility",
                "description": "Calculate if student meets admission requirements",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "student_gpa": {
                            "type": "number",
                            "description": "Student's high school GPA (0-4 scale)"
                        },
                        "test_scores": {
                            "type": "object",
                            "description": "Student's test scores (EmSAT, SAT, IELTS, etc.)"
                        },
                        "requirements": {
                            "type": "object",
                            "description": "Program requirements from requirements tool"
                        }
                    },
                    "required": ["student_gpa", "requirements"]
                }
            }
        }
    
    def execute(
        self,
        student_gpa: float,
        test_scores: Dict,
        requirements: Dict
    ) -> Dict:
        """
        Check eligibility
        """
        eligible = True
        missing_requirements = []
        met_requirements = []
        
        # Check GPA
        min_gpa = requirements.get('min_high_school_gpa', 0)
        if student_gpa >= min_gpa:
            met_requirements.append(f"GPA requirement ({min_gpa})")
        else:
            eligible = False
            missing_requirements.append(
                f"GPA: Need {min_gpa}, have {student_gpa}"
            )
        
        # Check test scores
        required_tests = requirements.get('required_tests', [])
        for test in required_tests:
            test_name = test.split()[0].lower()  # Extract test type
            
            if test_name in test_scores:
                min_score_key = f"min_{test_name}_score"
                if min_score_key in requirements:
                    min_score = requirements[min_score_key]
                    student_score = test_scores[test_name]
                    
                    if student_score >= min_score:
                        met_requirements.append(f"{test} ({student_score})")
                    else:
                        eligible = False
                        missing_requirements.append(
                            f"{test}: Need {min_score}, have {student_score}"
                        )
            else:
                missing_requirements.append(f"{test} - Not taken yet")
                eligible = False
        
        return {
            "eligible": eligible,
            "met_requirements": met_requirements,
            "missing_requirements": missing_requirements,
            "overall_score": len(met_requirements) / (len(met_requirements) + len(missing_requirements))
        }
```

#### Tool 3: Test Schedule Checker
**File**: `src/tools/test_schedule_tool.py`

```python
class TestScheduleTool:
    """
    Check upcoming EmSAT and other test dates
    """
    
    def get_definition(self) -> Dict:
        return {
            "type": "function",
            "function": {
                "name": "get_test_schedule",
                "description": "Get upcoming test dates for EmSAT, SAT, IELTS in UAE",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_type": {
                            "type": "string",
                            "enum": ["emsat", "sat", "ielts", "toefl"],
                            "description": "Type of test"
                        },
                        "emirate": {
                            "type": "string",
                            "enum": ["Abu Dhabi", "Dubai", "Sharjah", "Ajman", "UAQ", "RAK", "Fujairah"],
                            "description": "Test location emirate"
                        }
                    },
                    "required": ["test_type"]
                }
            }
        }
    
    def execute(self, test_type: str, emirate: str = None) -> Dict:
        """
        Fetch test schedule (mock data)
        """
        schedules = {
            "emsat": [
                {
                    "date": "2026-06-15",
                    "registration_deadline": "2026-06-01",
                    "locations": ["Abu Dhabi", "Dubai", "Sharjah"],
                    "subjects": ["English", "Math", "Physics", "Chemistry"],
                    "fee": 0
                },
                {
                    "date": "2026-08-20",
                    "registration_deadline": "2026-08-05",
                    "locations": ["All Emirates"],
                    "subjects": ["English", "Math", "Physics", "Chemistry", "Biology"],
                    "fee": 0
                }
            ],
            "sat": [
                {
                    "date": "2026-06-05",
                    "registration_deadline": "2026-05-06",
                    "locations": ["AUS", "AUD", "GEMS Schools"],
                    "fee": 300
                }
            ]
        }
        
        return {
            "test_type": test_type,
            "upcoming_dates": schedules.get(test_type, []),
            "filtered_emirate": emirate
        }
```

#### Tool 4: Document Checklist Generator
**File**: `src/tools/document_tool.py`

```python
class DocumentChecklistTool:
    """
    Generate personalized document checklist
    """
    
    def get_definition(self) -> Dict:
        return {
            "type": "function",
            "function": {
                "name": "generate_document_checklist",
                "description": "Create a personalized checklist of required documents",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "requirements": {
                            "type": "object",
                            "description": "Program requirements"
                        },
                        "student_profile": {
                            "type": "object",
                            "description": "Student information (nationality, education system, etc.)"
                        }
                    },
                    "required": ["requirements"]
                }
            }
        }
    
    def execute(self, requirements: Dict, student_profile: Dict = None) -> Dict:
        """
        Generate checklist with specific instructions
        """
        required_docs = requirements.get('required_documents', [])
        
        checklist = []
        for doc in required_docs:
            item = {
                "document": doc,
                "instructions": self._get_doc_instructions(doc, student_profile),
                "attestation_required": self._needs_attestation(doc, student_profile)
            }
            checklist.append(item)
        
        return {
            "total_documents": len(checklist),
            "checklist": checklist,
            "estimated_processing_time": "2-4 weeks"
        }
    
    def _get_doc_instructions(self, doc: str, profile: Dict) -> str:
        """
        Get specific instructions for each document
        """
        instructions_map = {
            "High school certificate": "Original certificate with transcript. If not in English/Arabic, certified translation required.",
            "Emirates ID": "Valid Emirates ID copy (front and back)",
            "Passport copy": "Passport copy with minimum 6 months validity",
            "EmSAT results": "Official EmSAT results from MOE portal",
            # ... more
        }
        return instructions_map.get(doc, "Provide original or certified copy")
    
    def _needs_attestation(self, doc: str, profile: Dict) -> bool:
        """
        Determine if document needs MOFA attestation
        """
        if profile and profile.get('education_country') != 'UAE':
            if 'certificate' in doc.lower():
                return True
        return False
```

### 2. ReAct Agent Implementation

Create `src/agents/enrollment_agent.py`:

```python
from typing import List, Dict
import openai
import json

class EnrollmentAgent:
    """
    AI Agent for university enrollment assistance
    """
    
    def __init__(self):
        self.client = openai.OpenAI()
        self.tools = {}
        self.conversation_history = []
        self.max_iterations = 10
        
        # Register tools
        self._register_tools()
    
    def _register_tools(self):
        """
        Register all available tools
        """
        from src.tools.requirements_tool import UniversityRequirementsTool
        from src.tools.eligibility_tool import EligibilityCalculatorTool
        from src.tools.test_schedule_tool import TestScheduleTool
        from src.tools.document_tool import DocumentChecklistTool
        
        self.tools = {
            "check_admission_requirements": UniversityRequirementsTool(),
            "calculate_eligibility": EligibilityCalculatorTool(),
            "get_test_schedule": TestScheduleTool(),
            "generate_document_checklist": DocumentChecklistTool()
        }
    
    def help_student(self, student_request: str) -> Dict:
        """
        Main entry point for student assistance
        """
        # Initialize conversation
        system_prompt = """You are an expert UAE university enrollment advisor.

Your role:
- Help students understand admission requirements
- Calculate their eligibility
- Provide step-by-step enrollment guidance
- Answer questions about tests, documents, deadlines

Available tools:
- check_admission_requirements: Get program requirements
- calculate_eligibility: Check if student qualifies
- get_test_schedule: Find upcoming test dates
- generate_document_checklist: Create personalized document list

Process:
1. Understand what the student needs
2. Use tools to gather necessary information
3. Provide clear, actionable guidance
4. When complete, respond with "ENROLLMENT_PLAN_COMPLETE: <summary>"

Be friendly, clear, and encouraging. UAE higher education is accessible!"""

        self.conversation_history = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": student_request}
        ]
        
        trajectory = []
        
        # Agent loop
        for iteration in range(self.max_iterations):
            print(f"\n=== Agent Iteration {iteration + 1} ===")
            
            # Get agent response
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=self.conversation_history,
                tools=self._get_tool_definitions(),
                tool_choice="auto",
                temperature=0.2
            )
            
            message = response.choices[0].message
            self.conversation_history.append(message)
            
            # Check if using tools
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    tool_name = tool_call.function.name
                    tool_args = json.loads(tool_call.function.arguments)
                    
                    print(f"🔧 Using tool: {tool_name}")
                    print(f"   Arguments: {tool_args}")
                    
                    # Execute tool
                    result = self._execute_tool(tool_name, tool_args)
                    
                    print(f"   Result: {result}")
                    
                    # Add result to conversation
                    self.conversation_history.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": tool_name,
                        "content": json.dumps(result)
                    })
                    
                    trajectory.append({
                        'iteration': iteration,
                        'action': tool_name,
                        'input': tool_args,
                        'output': result
                    })
            
            # Check if complete
            elif message.content and "ENROLLMENT_PLAN_COMPLETE" in message.content:
                print(f"\n✅ {message.content}")
                
                return {
                    'success': True,
                    'final_guidance': message.content,
                    'iterations': iteration + 1,
                    'trajectory': trajectory,
                    'conversation': self.conversation_history
                }
            
            # Continue reasoning
            else:
                print(f"💭 Thinking: {message.content}")
        
        # Max iterations reached
        return {
            'success': False,
            'error': 'Could not complete enrollment plan',
            'iterations': self.max_iterations,
            'trajectory': trajectory
        }
    
    def _get_tool_definitions(self) -> List[Dict]:
        """Get OpenAI tool definitions"""
        return [tool.get_definition() for tool in self.tools.values()]
    
    def _execute_tool(self, tool_name: str, arguments: Dict) -> Dict:
        """Execute a tool"""
        if tool_name not in self.tools:
            return {"error": f"Tool {tool_name} not found"}
        
        try:
            return self.tools[tool_name].execute(**arguments)
        except Exception as e:
            return {"error": str(e)}
```

### 3. Streamlit Chat Interface

Create `app.py`:

```python
import streamlit as st
from src.agents.enrollment_agent import EnrollmentAgent

st.set_page_config(
    page_title="UAE University Enrollment Assistant",
    page_icon="🎓",
    layout="wide"
)

# Initialize agent
if 'agent' not in st.session_state:
    st.session_state.agent = EnrollmentAgent()

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Header
st.title("🎓 UAE University Enrollment Assistant")
st.caption("AI-powered guidance for UAE higher education")

# Sidebar
with st.sidebar:
    st.header("Quick Start")
    
    examples = [
        "I want to study Computer Science at UAEU",
        "Am I eligible for AUS Engineering with 3.4 GPA?",
        "When is the next EmSAT test?",
        "What documents do I need for university application?",
        "I'm an international student, help me apply to AUD"
    ]
    
    st.markdown("### Example Questions")
    for ex in examples:
        if st.button(ex, key=ex):
            st.session_state.messages.append({
                "role": "user",
                "content": ex
            })
            st.rerun()
    
    if st.button("🔄 Clear Conversation"):
        st.session_state.messages = []
        st.session_state.agent = EnrollmentAgent()
        st.rerun()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about UAE university enrollment..."):
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            result = st.session_state.agent.help_student(prompt)
        
        # Display response
        if result['success']:
            response = result['final_guidance'].replace("ENROLLMENT_PLAN_COMPLETE: ", "")
            st.markdown(response)
            
            # Show agent actions
            with st.expander("🔍 View Agent Actions"):
                for step in result['trajectory']:
                    st.json(step)
        else:
            st.error("I apologize, I couldn't complete the enrollment plan. Please try rephrasing your question.")
    
    # Add assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": result.get('final_guidance', 'Error occurred')
    })
```

### 4. Evaluation

Create `tests/test_agent_scenarios.py`:

```python
def test_enrollment_scenarios():
    """
    Test common enrollment scenarios
    """
    agent = EnrollmentAgent()
    
    test_cases = [
        {
            "scenario": "UAE national applying to UAEU CS",
            "request": "I'm an Emirati student with 3.2 GPA. I want to study Computer Science at UAEU. What do I need?",
            "expected_actions": [
                "check_admission_requirements",
                "calculate_eligibility",
                "get_test_schedule",
                "generate_document_checklist"
            ],
            "expected_outcome": "Complete enrollment plan with steps"
        },
        {
            "scenario": "International student eligibility check",
            "request": "I'm an international student with SAT 1300, IELTS 7.0, GPA 3.6. Can I get into AUS Engineering?",
            "expected_actions": [
                "check_admission_requirements",
                "calculate_eligibility"
            ],
            "expected_outcome": "Eligibility confirmation"
        },
        # Add more test cases
    ]
    
    results = []
    for test in test_cases:
        print(f"\n Testing: {test['scenario']}")
        result = agent.help_student(test['request'])
        
        # Check if expected actions were used
        actions_used = [step['action'] for step in result['trajectory']]
        all_actions_present = all(
            action in actions_used 
            for action in test['expected_actions']
        )
        
        results.append({
            'scenario': test['scenario'],
            'success': result['success'],
            'used_correct_tools': all_actions_present,
            'iterations': result['iterations']
        })
    
    return results
```

### DELIVERABLES

1. **Agent System** with:
   - 4+ functional tools
   - ReAct reasoning loop
   - State management
   - Error handling

2. **Web Interface**:
   - Chat-based interaction
   - Real-time agent status
   - Action visualization
   - Example scenarios

3. **Testing Suite**:
   - 10+ test scenarios
   - Tool accuracy validation
   - End-to-end workflow tests

4. **Documentation**:
   - Tool definitions
   - Agent decision logic
   - Deployment guide

### SUCCESS CRITERIA

- [ ] Successfully completes 8/10 enrollment scenarios
- [ ] Uses appropriate tools for each scenario
- [ ] Provides complete, actionable guidance
- [ ] Handles edge cases (missing info, eligibility failures)
- [ ] Completes tasks in <7 tool calls on average
- [ ] Response time <15 seconds total
- [ ] User-friendly chat interface

Build this as a production-ready system that could actually help real students navigate UAE university enrollment.
```

---

*[Note: Due to length constraints, I'll create the remaining projects in a more condensed format. The full document would continue with Projects 4-10 following the same detailed structure. Would you like me to continue with the complete implementation of all 10 projects, or would you prefer the condensed version now?]*

Let me know if you'd like me to:
1. Continue with full detail for all 10 projects (will be very long)
2. Provide condensed versions of the remaining projects
3. Focus on specific projects you're most interested in

Should I proceed with the complete document including all 10 projects?
