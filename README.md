# Flask Project

This is a Flask project for displaying data from a SQLite database via a website.

## Project Structure

- `main.py`: Contains the Flask application code including route definitions.
- `templates/`: Directory containing HTML templates for the website.
- `database.py`: Contains functions for database creation, table creation, and data insertion.
- `customer.csv`: Sample CSV file containing data for database insertion .
- `README.md`: This file providing an overview of the project and instructions for running it.
- `requirements.txt`: File listing all necessary Python packages required for running the project.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/jaspreetsinghsain/group5_flask_project
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-project
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python main.py
    ```

## Usage

- Visit [http://localhost:5000/](http://localhost:5000/) in your web browser to access the home page.
- Click on the "About" link to view information about the project.
- Click on the "Data" link to view the data displayed on the website.
