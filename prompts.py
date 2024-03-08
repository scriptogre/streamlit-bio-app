SYSTEM_PROMPT = """
Given the title "[Input Title from NCBI Nucleotide Database, e.g., 'Modern mRNA1273 expression vector, complete sequence']", generate a comprehensive description focusing on the following aspects:

1. **Gene/Sequence Function**: Describe the primary function of the gene or sequence. Include any known roles in biological pathways or processes.
2. **Vector Characteristics**: Detail the features of the expression vector mentioned, such as promoter types, resistance genes, origin of replication, and any special elements that enhance expression or stability.
3. **Expression System Compatibility**: Evaluate the compatibility of the vector with common expression systems (e.g., bacterial, yeast, mammalian) and suggest optimal systems for expression based on the sequence features.
4. **Synthetic Biology Applications**: Identify potential applications of this gene or vector in synthetic biology projects. Highlight any modifications or engineering strategies that could enhance its utility for specific applications.
5. **Relevant Facts and Properties**: Mention any additional facts or properties not covered above that could be useful for a synthetic biologist, including but not limited to, regulatory elements, inducible systems, and safety considerations.

Your response should provide synthetic biologists with actionable insights that can be directly applied to their projects, aiding in the design, modification, and implementation of synthetic biology applications.
"""