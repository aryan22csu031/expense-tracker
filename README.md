# Bachat Buddy

Bachat Buddy is a simple and intuitive expense tracker that helps you analyze your spending habits. The project features a web interface where users can upload a CSV file containing their expense data. The data is then processed and analyzed using Streamlit, with Flask serving as the backend.

## Features

- **Upload CSV File**: The home page features an HTML form that allows users to upload a CSV file containing their expense data.
- **Data Analysis**: The uploaded CSV file is sent to a Streamlit application (`dashboard.py`) for analysis.
- **Visualization**: The analyzed data is displayed to the user through an interactive dashboard.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask
- Streamlit
- Pandas

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/aryan22csu031/expense-tracker.git
    cd expense-tracker
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Flask server:**

    ```bash
    python app.py
    ```

2. **Run the Streamlit dashboard:**

    ```bash
    streamlit run dashboard.py
    ```

3. **Open your web browser and go to:**

    ```
    http://localhost:5000
    ```

### Project Structure

- `app.py`: The main Flask application file that handles the file upload and serves the home page.
- `dashboard.py`: The Streamlit application that performs the data analysis and visualization.
- `templates/`: Contains the HTML templates for the Flask application.
- `static/`: Contains static files such as CSS and JavaScript (if any).
- `requirements.txt`: List of Python packages required to run the project.

### Usage

1. **Upload CSV File**: On the home page, use the provided form to upload your CSV file containing expense data.
2. **View Analysis**: Once the file is uploaded, the data will be sent to the Streamlit app for analysis. You will be redirected to a page displaying an interactive dashboard with various visualizations of your spending habits.

### Example CSV Format

Ensure your CSV file follows a format similar to this:

| Date       | Category | Description       | Amount |
|------------|----------|-------------------|--------|
| 2023-01-01 | Food     | Grocery shopping  | 50.75  |
| 2023-01-02 | Travel   | Bus ticket        | 2.50   |
| 2023-01-03 | Utilities| Electricity bill  | 30.00  |

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Contact

If you have any questions or suggestions, feel free to contact the project maintainer at [your-email@example.com].

---

**Happy tracking with Bachat Buddy!**
