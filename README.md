# DocRAG

A Document Retrieval-Augmented Generation (RAG) system built with LangChain, LangGraph, and Streamlit. This project enables users to ingest documents from various sources (URLs, PDFs), process them into chunks, store them in a vector database, and perform intelligent retrieval and generation using AI models.

## Features

- **Document Ingestion**: Load documents from web URLs, PDF files, and directories
- **Text Processing**: Split documents into manageable chunks with configurable overlap
- **Vector Storage**: Store document embeddings using FAISS for efficient retrieval
- **Graph-Based Architecture**: Built with LangGraph for structured AI workflows
- **Streamlit Interface**: User-friendly web interface for interaction
- **OpenAI Integration**: Leverages OpenAI's models for generation and embeddings

## Installation

### Prerequisites
- Python 3.12 or higher
- uv package manager (recommended)

### Setup Steps

1. **Clone or navigate to the project directory**

2. **Initialize the project with uv**:
   ```bash
   uv init
   ```

3. **Create a virtual environment**:
   ```bash
   uv venv
   ```

4. **Activate the virtual environment**:
   ```bash
   source .venv/bin/activate
   ```

5. **Install dependencies**:
   ```bash
   uv add -r requirements.txt
   uv add ipykernel
   ```

6. **Set up environment variables**:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

### Running the Streamlit Application

```bash
streamlit run streamlit_app.py
```

This will start the web interface where you can:
- Upload documents
- Query the knowledge base
- View retrieved information

### Using the Document Processor

```python
from src.document_ingestion.document_processor import DocumentProcessor

# Initialize processor
processor = DocumentProcessor(chunk_size=500, chunk_overlap=50)

# Load documents from URL
docs = processor.load_from_url("https://example.com/document")

# Load documents from PDF directory
docs = processor.load_from_pdf_dir("path/to/pdf/directory")

# Process and split documents
chunks = processor.splitter.split_documents(docs)
```

## Project Structure

```
DocRAG/
├── data/
│   └── url.txt              # Sample URLs for document ingestion
├── src/
│   ├── __init__.py
│   ├── config/              # Configuration settings
│   ├── document_ingestion/  # Document loading and processing
│   │   └── document_processor.py
│   ├── graph_builder/       # LangGraph workflow construction
│   ├── nodes/               # Graph nodes for processing
│   ├── state/               # State management
│   └── vectorstore/         # Vector database operations
├── main.py                  # Main entry point
├── streamlit_app.py         # Streamlit web interface
├── pyproject.toml           # Project configuration
├── requirements.txt         # Python dependencies
├── README.md                # This file
└── Instructions.txt         # Setup instructions
```

## Dependencies

- **LangChain**: Framework for building LLM applications
- **LangGraph**: Library for creating graph-based AI workflows
- **FAISS**: Vector similarity search library
- **Streamlit**: Web app framework
- **OpenAI**: API client for OpenAI models
- **BeautifulSoup4**: HTML parsing for web content
- **Requests**: HTTP library for API calls
- **Pydantic**: Data validation and settings management

## Configuration

The system uses the following key configurations:
- Chunk size: 500 characters (configurable)
- Chunk overlap: 50 characters (configurable)
- Vector store: FAISS CPU version
- Embedding model: OpenAI embeddings (via LangChain)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
