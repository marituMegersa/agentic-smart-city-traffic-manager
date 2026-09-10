class HybridRetriever:
    def retrieve(self, query: str, top_k: int = 5):
        return [
            {"id": "doc_1", "score": 0.95, "content": f"Relevant context for '{query}'"},
            {"id": "doc_2", "score": 0.88, "content": "Evidence citation metadata"}
        ]
