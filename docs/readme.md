Legal Compass
Tagline: Navigate your legal options before taking the next step.
Description: Legal Compass helps individuals understand potential legal implications, applicable laws, rights, responsibilities, and available remedies based on their dispute or situation. It provides preliminary legal information to support informed decision-making before consulting a lawyer or approaching a court.

                User Query
                     |
                     V
          +-------------------+
          | GPT OSS 20B       |
          | (Ollama)          |
          +-------------------+
                     ^
                     |
          +-------------------+
          | Vector Database   |
          | (ChromaDB)        |
          +-------------------+
                     ^
                     |
          +-------------------+
          | Law Documents     |
          |   IPC/BNS         |
          |   CPC             |
          |   CrPC/BNSS       |
          |   Evidence Act    |
          |   TN State Acts   |
          +-------------------+

Python
Ollama
GPT-OSS:20b

LangChain
ChromaDB

Sentence Transformers
(all-MiniLM-L6-v2)

pip install langchain
pip install chromadb
pip install sentence-transformers
pip install gradio
pip install pypdf
pip install pandas

pip install -U langchain
pip install -U langchain-community
pip install -U langchain-huggingface
pip install -U chromadb
pip install -U pypdf
pip install -U langchain-text-splitters

pip install langchain
pip install langchain-community
pip install langchain-text-splitters
pip install langchain-huggingface
pip install chromadb
pip install pypdf

Documents RAGd
Bharatiya Nyaya Sanhita (BNS)
Bharatiya Nagarik Suraksha Sanhita (BNSS)

Documents yet to be RAGd
Bharatiya Sakshya Adhiniyam (BSA)
Code of Civil Procedure
Consumer Protection Act
Tamil Nadu Property Acts
Tamil Nadu Rent Control Act
Motor Vehicle Act
Negotiable Instruments Act

More Details can be fetched
"additional case detail"
    party_1_name: parties involved - if not mentioned, say not mentioned  
    party_1_role: [Complainant/Plaintiff/Victim/Bank/Government/etc]  (if it is dispute or issue between two person, victim , accused or any list of people involed. can be mentioend as party1 - state or bank or person1 , party2 - government or bank or person2 etc
    party_2_name: if not mentioned, say not mentioned
    party_2_role: [Accused/Defendant/Respondent/etc]
    other_parties: if not mentioned, say not mentioned
    Complainant
    Plaintiff
    Defendant
    Accused
    Victim
    Respondent
    Petitioner
    Appellant
    Witness
    Investigating Officer
    Government Authority
    Bank / Financial Institution
    Company / Employer
