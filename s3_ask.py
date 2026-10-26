import requests
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="legal_db",
    embedding_function=embedding
)

def ask_ollama(prompt):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"gpt-oss:20b-cloud",
            "prompt":prompt,
            "stream":False
        }
    )
    print(response.json())
    return response.json()["response"]


def legal_query(user_question):

    docs = db.similarity_search(
        user_question,
        k=5
    )

    context = "\n\n".join(
        d.page_content for d in docs
    )

    prompt = f"""
You are an Indian legal education assistant.

Using ONLY provided context.

Context:
{context}

Question:
{user_question}

Provide the response as two parts only, no other extra information. split the two parts with custom splitter : <<SPLITTER>>
user will split the output into two parts using the with custom splitter - <<SPLITTER>>

First part, this should be a clear mark-down table string
    in this part provide the below required details from the user question,provide it as a table as a name/value pair.
    derive the value from the user question by analysing the legal details of it use the context provided.
    and make sure, value should be in one line short and brief. 
    dont provide any other details or information beyond the requested list of information.
    always use | Field | Value | and next row |-------|-------| on start of the table.
    
    Requesting below list of information in MD table structure.
    
    1. Law : (Mention the law name user query falls)
    2. Section : (Mention the law section number) 
    3. Case category : (Mention the case category user query falls) 
    4. Case subcategory : (Mention the case subcategory user query falls) 
    5. Nature of dispute : (Mention the type of dispute) 
    6. Civil or Criminal : (Mention whether its criminal or civil)
    7. Cognizable or Non Cognizable :  (Mention whether its Cognizable or Non Cognizable)
    8. Bailable or Non Bailable : (Mention whether its Bailable or Non Bailable)
    9. Maximum punishment :  (Mention the maximum punishment for the case law)
    11. Fine amount : (Mention the fine amount if any applicable for the case law)
    12. Court type :  (Mention the court type the case falls)
    13. Appropriate court : (mention which ever applicable -> Judicial Magistrate, Sessions Court,District Court,Family Court,Consumer Court,Labour Court,High Court,Supreme Court)
    14. Important observations : (share the important observation from the user query about the case)
    15. Case description : (mention the case description here)
    
    If uncertain in any field, say uncertain or not mentioned.
    
    This part of string should be MD Table only. String will be rendered as MD table. should not include any other information. 

Second part, a simple string:
     combine above listed 15 items as a complete string of description.
     make this string as natural speaking tone. will deliver it as audio sound. 
     so use punctuations for fluent and clear tone.   

"""

    return ask_ollama(prompt)



if __name__ == "__main__" :

    qry = """
        Person A borrowed money from Person B and later he issued a cheque. And cheque bounced due to insufficient funds.        
           """
    response = legal_query(qry)
    part1, part2 = response.split("<<SPLITTER>>")
    print(part1)
    print(part2)