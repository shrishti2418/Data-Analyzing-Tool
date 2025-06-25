# CSV Data Analyzing Tool


The CSV Data Analyzing Tool is a versatile utility that allows you to analyze and gain insights from any CSV file effortlessly. Powered by LangChain, Python, the Pandas library, OpenAI API, and Streamlit for the user interface, this tool is designed to make data exploration and answering questions related to CSV data files a breeze.

## Features

- **Effortless Data Exploration**: Easily upload and explore any CSV file, regardless of its size or complexity.

- **Question and Answer**: Ask questions related to your data, and the tool will provide insightful answers.

- **Natural Language Understanding**: Leverages LangChain and OpenAI API to understand your queries in natural language.

- **Data Manipulation**: Use Pandas for data manipulation and transformation to prepare your data for analysis.

- **Interactive User Interface**: The Streamlit-based interface offers a user-friendly experience for both beginners and experts.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Pandas library](https://pandas.pydata.org/)
- [OpenAI API key](https://beta.openai.com/signup/)

### Installation

1. Clone this repository to your local machine.

```shell
git clone https://github.com/Shrishti2418/Data-Analyzing-Tool.git
```

2. Install the required Python packages.

```shell
pip install -r requirements.txt
```

3. Create a `.env` file in the project directory and add your OpenAI API key.

```shell
OPENAI_API_KEY=your_api_key
```

4. Run the tool.

```shell
streamlit run app.py
```

## Usage

1. Launch the CSV Data Analyzing Tool by running `app.py` using Streamlit.
2. Upload your CSV file for analysis.
3. Use the natural language interface to ask questions related to your data.
4. The tool will utilize LangChain, Pandas, and the OpenAI API to provide answers and insights.
5. Explore your data and gain valuable information from it.

