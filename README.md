### Steps for Setting Up and Running the Application

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Create a Virtual Environment (Optional)**  
   ```bash
   python -m venv venv
   ```

   - Activate the virtual environment:  
     - **Windows:**  
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux:**  
       ```bash
       source venv/bin/activate
       ```

3. **Install Requirements**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the `.env` File**  
   - Copy `.env.example` to `.env`:  
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and replace placeholder values with your API key and other details:
     ```plaintext
     HUGGINGFACEHUB_API_TOKEN=your-actual-api-key
     ```

5. **Run the Application**  
   ```bash
   streamlit run LangchainHuggingFaceChatbot.py
   ```

