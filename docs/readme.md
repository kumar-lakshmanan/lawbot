Legal Compass
Tagline: Navigate your legal options before taking the next step.
Description: Legal Compass helps individuals understand potential legal implications, applicable laws, rights, responsibilities, and available remedies based on their dispute or situation. It provides preliminary legal information to support informed decision-making before consulting a lawyer or approaching a court.

First:
Web Interface - Done using python Flask - app.py / render index.html with style.css and script.js
                 * Running on all addresses (0.0.0.0)
                   * Running on http://127.0.0.1:5000
                   * Running on http://192.168.1.25:5000

Second:
    CONSULT BUTTON ACTION - script.js
    basic step - get user input query and pass to "python core AI function" and wait for its response . once response received display them as table.

Third:
    python core AI function

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



i have ai based web application. it has RAG db with BNS and IPC indian laws loaded. and if you pass any query or any legal situation to it.
it checks and list down the law applicable and list down the penalty and fine details. etc. actually, it was done for education purpose and kind of POC showing how to load custom rules and document to the rag db and make AI provide details for the user question with given db context.

we need to display this project in school expo about ACADEMIC EXPO 2026 - SUSTAINABLE DEVELOPMENT GOALS.

for this we need to make this tool heading relavent to SUSTAINABLE DEVELOPMENT GOALS. also need to give a speech about the tool relavent to SUSTAINABLE DEVELOPMENT GOALS. with help of this AI web app.

suggest a good name relavent to this topic. along with the AI web app we have.

now in AI web app ... we can load custom rules. like we loaded our custom school rules and allowing users to use this tool as kiosk for school to understand the school code of conduct and rules for students. they can provide any scenairo and AI analyse the scenario and list down internal school law and penalty and fine and punishment details. 
this is the sample output
| Law | CIS Student Conduct & Discipline Rules |
| Section | CIS‑S002 |
| Case category | School Discipline |
| Case subcategory | Repeated Damage to Property |
| Nature of dispute | Property damage / misconduct |
| Civil or Criminal | Civil |
| Cognizable or Non Cognizable | Non Cognizable |
| Bailable or Non Bailable | Uncertain |
| Maximum punishment | Suspension of 3 school days |
| Fine amount | 500 ₹ |
| Court type | Not applicable |
| Appropriate court | Not applicable |
| Important observations | Ravi has damaged the book for the fifth time, report suggests enforcing suspension. |
| Case description | Ravi repeatedly tore pages of Satish’s math book, fifth incident, subject to CIS‑S002 penalties. 


making use of these info. 
need to setup a good name for this ai tool should be relavent to the main topic.
optionally, if you suggest some pdf or data about main topic , we can also load into rag db (but output is rigged to give in above table format only).

additionally need to give 10min speech about this tool and it also should be relavent to main topic.





