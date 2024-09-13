# Job Data Scraper

This Python script retrieves job postings from the LinkedIn API using the RapidAPI platform and saves the resulting job data in both CSV and JSON formats.

## Prerequisites

- Python 3.x: Make sure you have Python 3 installed on your system.

### Required Libraries:

- `requests`: This library is used to make HTTP requests to the API.
- `csv`: For writing data to a CSV file.
- `json`: For writing data to a JSON file.

You can install the requests library via pip if not already installed:

```bash
pip install requests
```

## Usage

### API Key Setup:

1. To use this script, you need to set up an account with RapidAPI and subscribe to the LinkedIn Data Scraper API.
2. Replace the `x-rapidapi-key` in the headers section with your own RapidAPI key.

### Modify Company IDs:

- The `companyIds` in the payload must be replaced with the IDs of the companies whose job data you want to retrieve. You can modify these IDs in the script.

## Script Overview

The script performs the following tasks:

1. Setup the API request: It defines the API endpoint, request payload, and headers, including the API key.
2. Make the POST request: The script sends a POST request to the LinkedIn job data API.
3. Process the response:
   - If the request is successful (status_code 200), it retrieves the job data from the response.
   - It saves the job data in two formats: CSV and JSON.
4. Error Handling: If the request fails, it prints an error message with the response status code and the error details.

### CSV Output

- The CSV file includes the following fields: ID, Title, URL, Company, Location, Type, Post Date, and Benefits.
- It is saved in a file called `job_data.csv`.

### JSON Output

- The JSON output contains all the job data returned by the API and is saved in `job_data.json`.

## Example

Run the script as follows:

```bash
python job_scraper.py
```

### Response Example

If successful, you will see the following output:

```
Data saved to job_data.csv
Data saved to job_data.json
```

If the request fails, the output will look like this:

```
Failed to retrieve data: [Status Code], [Error Message]
```

## Recommendations and Improvements

### Pagination Support:

- Currently, the script only retrieves the first page of job data. Consider adding pagination to loop through all available pages of results.
- You can modify the payload to increment the page value and make multiple API calls until all jobs are retrieved.

Example:

```python
for page in range(1, total_pages + 1):
    payload["page"] = page
    # Repeat the API request logic
```

### Rate Limiting and Throttling:

- Be cautious of API rate limits imposed by RapidAPI. You might want to implement a delay between requests to avoid hitting the rate limit, especially when handling pagination.

Example:

```python
import time
time.sleep(1)  # 1 second delay between requests
```

### Enhanced Error Handling:

- Consider handling different types of errors (e.g., network issues, API key errors) separately to provide more descriptive error messages.
- Retry logic could be useful in case of temporary failures like network timeouts.

Example:

```python
try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
except requests.exceptions.Timeout:
    print("Request timed out. Please try again later.")
except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")
```

### Parameterize Inputs:

- Allow the user to pass companyIds, API key, and other parameters via command-line arguments or environment variables to make the script more flexible.

Example using argparse:

```python
import argparse

parser = argparse.ArgumentParser(description="Job Scraper Script")
parser.add_argument('--company-ids', nargs='+', help='List of Company IDs', required=True)
parser.add_argument('--api-key', help='Your RapidAPI Key', required=True)
args = parser.parse_args()
```

### Data Validation:

- Implement validation to ensure that the job data contains valid and non-empty values before saving it to the CSV or JSON files.

### Logging:

- Add logging to track the script's execution and make debugging easier. You can log the status of each API request and data processing step.

Example:

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Script started...")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
