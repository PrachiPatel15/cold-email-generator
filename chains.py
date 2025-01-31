import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {page_data}
            ### INSTRUCTION:
            The given text is from the linkedIn job posting.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]
    
    def write_mail(self, role, experience, skills, description):
        prompt_email = PromptTemplate.from_template(
            """
                You are an expert email writer specializing in cold outreach for job applications. Write a complete, natural-sounding cold email for a {role} position. The candidate's relevant skills are: {skills}.

                Follow these guidelines to craft the email:

                1. Create a clear subject line that mentions the specific role
                2. Address the recipient professionally (assume "Hiring Manager" if no name provided)
                3. Write a compelling opening paragraph (2-3 sentences) that:
                - Shows genuine interest in the company/role
                - Demonstrates research/knowledge about the company
                - Explains why you're reaching out

                4. Write a strong second paragraph (3-4 sentences) that:
                - Highlights 2-3 most relevant skills from: {skills}
                - Includes a specific achievement or relevant project
                - Connects your experience to the role's requirements

                5. Write a brief closing paragraph that:
                - References the attached resume and any other relevant documents
                - Expresses enthusiasm for discussing further
                - Includes a specific call to action
                - Thanks the recipient

                6. Add a professional signature block that includes:
                - Your name
                - Phone number placeholder
                - Professional email placeholder
                - Optional LinkedIn profile reference

                Format the email as a complete message with clear spacing between paragraphs. Don't use placeholders like [Company] - instead, write the email in a way that works without requiring substitution.

                Example structure:

                Subject: Experienced Data Scientist Excited to Contribute to Your Team

                Dear Hiring Manager,

                [Complete opening paragraph]

                [Complete body paragraph]

                [Complete closing paragraph with resume reference]

                Best regards,
                [Full signature block]

                Remember:
                - Keep the total length between 150-200 words
                - Make it sound natural and conversational, not formulaic
                - Focus on value proposition and relevant skills
                - Be confident but not arrogant
                - Maintain professional tone throughout
                - Use proper email formatting with spaces between paragraphs
                - Include a natural reference to attached materials
                - Add LinkedIn profile reference in signature if appropriate

                Please write the complete email now, following all these guidelines and making the resume reference sound natural and professional.
            """
        )
        
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"role": str(role), "experience": experience, "skills": skills, "description": description})
        return res.content

    
if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))