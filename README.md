# Running Flask App with Virtual Environment (venv)

This README.md file provides instructions on how to run a Flask app with a virtual environment named venv.

## Requirements

Ensure you have the following installed on your system:

- [Python](https://www.python.org/) - Python programming language
- [pip](https://pip.pypa.io/en/stable/) - Python package installer

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Nyx1on/Snapify-backend-2.git
    ```

2. Navigate to the project directory:

    ```bash
    cd <project-directory>
    ```

3. Create a virtual environment named `venv`:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:
    
        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:
    
        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

No additional configuration is required. However, you may adjust settings in your Flask app according to your needs.

## Usage

To start the Flask app, run the following command:

```bash
python app.py
