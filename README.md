# GenAI App - AI Code Reviewer

## Project Overview
The **GenAI App - AI Code Reviewer** is a Python application developed to allow users to submit their Python code for review. The app utilizes the OpenAI/GoogleAI API to analyze the code for potential bugs, errors, and areas of improvement. Additionally, it provides suggestions for fixes and the corrected code snippets, making the review process faster and more efficient.

## Objective
The primary objective of this project is to provide a seamless and user-friendly way for developers to receive feedback on their code, helping them identify and fix errors more effectively. The AI-powered code reviewer enhances productivity and improves code quality by automating the review process.

## Key Features
- **User-Friendly Interface**: Built using Streamlit, the app offers a clean and intuitive user interface.
- **Code Submission**: Users can easily paste their Python code for review.
- **Bug Detection**: The AI model analyzes the submitted code for bugs and errors.
- **Suggestions for Fixes**: The AI provides suggestions for improvements and corrected code snippets.
- **Past Code History**: Users can view the history of their past code submissions.

## Project Structure
- **Left Sidebar**: Displays a personalized bio section, with information about the developer, including internship details, supervisor, and the company name (Innomatics Research Labs).
- **Main Section**: Contains an input area for pasting Python code, and AI integration for code review and suggestions.

## Technologies Used
- **Streamlit**: Used to build the web interface for the app.
- **Google/ OpenAI Generative AI API**: Utilized for analyzing the Python code and providing feedback and fixes.
- **Python**: The main programming language for the application.
- **HTML/CSS**: Used for styling the user interface.

## Installation Instructions

### Prerequisites
To run this application locally, you need:
- Python 3.7+
- Streamlit
- Google AI API (or OpenAI API) access key

### Steps to Set Up the Application

1. Clone the repository to your local machine:
   ```bash
      git clone https://github.com/your-username/genai-app-ai-code-reviewer.git
   ```
2. Navigate to the project directory:
   ```bash
      cd genai-app-ai-code-reviewer
   ```
3. Create a virtual environment:
   ```bash
      python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
        .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
        source venv/bin/activate
     ```
5. Install the required dependencies:
   ```bash
      pip install -r requirements.txt
   ```
6. Obtain a Google API key (or OpenAI API key) for code review functionality. Follow the documentation provided by Google or OpenAI to get your API key.
7. Update the application code with your API key:
     - In the code, locate the line that configures the API key and add your key.
        ```bash
           genai.configure(api_key="YOUR_API_KEY_HERE")
        ```
8. Run the Streamlit app:
   ```bash
      streamlit run app.py
   ```
9. Open your web browser and navigate to ** http://localhost:8501 ** to access the app.

### How to Use
1. **Submit Code for Review**: Paste your Python code into the input box in the main section.
2. **Get Review and Suggestions**: Click the **Review Code** button, and the AI will analyze your code, identify potential issues, and provide suggestions for fixes.
3. **View Past Submissions**: Use the "View Past History" button to see previously submitted code.

## Example Video

## Future Improvements
- Allow users to upload Python files for review.
- Enable a more detailed history feature, where users can filter by date or issues found.
- Provide a downloadable report of the code review with suggestions for fixes.

## License
This project is licensed under the MIT License - see the **LICENSE file** for details.

## Acknowledgments
This project is part of an internship at **Innomatics Research Labs**, supervised by **Kanav Bansal**.
Special thanks to **Google/ OpenAI** for providing the generative AI APIs used in this project.

## Contact 
for any question or contributions, feel free to reach out to: 
- **Email:** p91035gmail.com
- **Linkedin:** Parmod's LinkedIn
