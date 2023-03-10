<h1>Analytics Framework</h1>

<p>This project provides a framework for performing analytics tasks with local files in formats like CSV or Excel. It includes functions for importing data from local files into pandas dataframes, as well as for cleaning, transforming, and analyzing that data.</p>

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg?logo=python)](https://www.python.org/)


<h2>Installation</h2>

<p>To use this project, you first need to create a virtual environment and install the required packages. You can do this by following these steps:</p>

<ol>
  <li>Clone the repository to your local machine.</li>
  <li>Navigate to the repository root directory.</li>
  <li>Create a virtual environment by running:</li>
</ol>

<code>python -m venv analytics_env</code>

<p>Activate the virtual environment by running:</p>

<code>source analytics_env/bin/activate</code>

<p>Install the required packages by running:</p>

<code>pip install -r requirements.txt</code>

<h2>Usage</h2>

<h3>Importing local files</h3>

<p>To import a local CSV or Excel file into a pandas dataframe, you can use the import_local_file_to_df() function from the local_files_management package. This function takes as input the path to the file you want to import and returns a pandas dataframe containing the file's contents.</p>

<p>Here's an example of how to use this function:</p>

<code>
python
from local_files_management import import_local_file_to_df

df = import_local_file_to_df('/path/to/my_local_file.csv')
</code>

<h3>Running analytics tasks</h3>

<p>To perform analytics tasks on the data in a pandas dataframe, you can use any of the functions provided in the analytics package. These functions include data cleaning, transformation, aggregation, and visualization functions.</p>

<p>Here's an example of how to use one of these functions:</p>

<code>
python
from analytics import plot_histogram

plot_histogram(df, 'column_name')
</code>

<h3>Running the main program</h3>

<p>To run the main program, which is located in the main.py file at the root of the repository, you can simply run:</p>

<code>python main.py</code>

<p>This will run the program and execute any analytics tasks that you have defined in the main function.</p>

<h2>Testing</h2>

<p>To run the unit tests for this project, you can use the unittest package. The test files are located in the tests directory, and you can run them using the following command:</p>

<code>python -m unittest discover tests</code>

<h2>Contributing</h2>

<p>If you would like to contribute to this project, please submit a pull request with your changes. Make sure to follow the same code style and formatting as the rest of the project, and to add tests for any new functions or features you add.</p>
