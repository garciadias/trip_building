# Trip Building Data Analysis

## Running the code

## Prerequisites

- Python 3.9.17
- Poetry 1.5.1

## Installation

1. Clone the repository
2. Run `poetry install` to install the dependencies
3. Run `poetry shell` to activate the virtual environment
4. Run tasks using `poetry run task <task_name>`
5. Run `poetry run task --list` to see the available tasks

To run all the tasks, use the following command:

```bash
poetry run task run_all

```

The individual tasks are:

1. data_profiling
    - This task will generate a data profiling report for the dataset, both for the full data and the cut of the data that contains only failed trips. The report will be saved in the `reports` folder and will be open in your default browser once the task is finished.
2. create_date_analysis
    - This task will generate plots to analyze the distribution of the creation date of the trips.
3. preferred_date_analysis
    - This task will generate plots to analyze the distribution of the preferred dates of the trips.
4. preferred_experience_analysis
    - This task will generate plots to analyze the distribution of the preferred experience of the trips.

The data profiles can be accessed at the following links:
📈 [Exploratory view of the full dataset](https://garciadias.github.io/projects/reporting_trip_request_extract_report.html)
📉 [Exploratory view of the errors](https://garciadias.github.io/projects/reporting_trip_request_extract_failed_report.html)

The full data analysis with my findings and recommendations can be found [here](https://www.notion.so/Byway-data-analysis-39c7574d5fa241d4a1afec24023ff2d3?pvs=21).

### Code Observations:

- The data is not evenly distributed across the months, with a significant number of trips being created in March.
- The data is not published here to respect the privacy of the users and the company. A file should be added at `data/raw/reporting-trip-request-extract.csv` with the data to run the analysis.
- I don't use Jupyter Notebooks on this analysis. Instead, I use the `# %%` tag on vscode to separate the code into cells. This way, I can run the code in a similar way to Jupyter Notebooks and still have the benefits of using a code editor. At the end of
my analysis, I could convert the code into a Jupyter Notebook if needed. In this case I preferred to refactor the code to make it more readable and to add comments to explain the code. The file `trip_building/exploration/quick_exploration.py` is an example of how I would use this approach to run quick and dirty analysis before structuring the code into a more readable and production-ready format.

# Summary of the analysis

## Code Task: Data Analysis and Recommendations Report

### Data Analysis Overview

This analysis delves into various aspects of trip planning data, identifying key patterns, trends, and anomalies. The initial exploration focuses on data types, missing values, and constant variables, setting the stage for a deeper investigation into travel preferences and potential areas for improvement in the trip-building process.

### Initial Exploration Insights

The primary step involved identifying data types and formats crucial for effective processing and visualization. Key observations include:

- Missing values in `creationdate` and `tripbuildtimeseconds` point to failures in trip creation, while `failtimeseconds` are absent in successful cases.
- The discovery of constant values, such as `jotform_onewaytrip` being NaN across the board, suggests some data fields may be irrelevant for further analysis due to uniformity or lack of variability.

## Patterns and Trends

### Time Patterns

- An unexpected preference for trip starts in March, especially on Mondays, suggests a potential default bias in website field selections.
- Trip requests peaked on Sundays between 16:00 and 22:00, highlighting specific times when users are most engaged in trip planning.

### Location Patterns

- `London` emerged as the most common starting city, followed by `Paris`, `Manchester`, `Birmingham`, `Newcastle`, and `Edinburgh`.
- `Highlands & Islands` was the top destination choice, with preferences varying significantly based on the user's starting city.

## Experience Preferences

A diverse range of experience preferences was noted, with specific interests varying by destination region and city of origin. For instance, trips to the `Highlands & Islands` were associated with nature and relaxation, while Northern Italy attracted visitors from Paris with different preferences.

## Further Data Considerations

To enhance the analysis, additional data points such as confirmed bookings, trip costs, and comparisons with independently planned trips would offer more comprehensive insights. A more evenly distributed data collection period could also provide a balanced view of travel patterns.

## Summary of Findings

The analysis revealed several key insights, including specific time and location patterns in trip planning, as well as varied experience preferences among travellers. Notably, the data suggests a significant influence of default website options on user choices, indicating areas for potential improvement in user interface design.

## Recommendations for Business Intelligence

### Addressing Observed Errors

The analysis identified a 2.6% error rate in trip planning, primarily due to `norouteserrorcount`. A detailed examination of failed trips, especially to Yorkshire, highlighted the need for more robust route planning and error messaging within the trip builder tool.

## Improving the Trip Builder

Suggestions for enhancing the trip builder include:

- Refining the user interface to avoid default bias in date and location selections.
- Implementing more intuitive error messaging and alternative suggestions for users facing planning failures.

### Key Metrics for Performance Monitoring

Proposed metrics for ongoing performance evaluation encompass:

- Analysis of trip origin and destination trends.
- Composition of travel groups and their preferred activities.
- Monitoring and addressing error rates in trip planning.

## Enhancing Decision-Making

The insights derived from this analysis can inform strategic decisions in product development and technological enhancements, focusing on:

- User interface improvements to facilitate more personalized and successful trip planning.
- Data-driven adjustments to address common errors and enhance user satisfaction.

## Conclusion

This report underscores the value of detailed data analysis in identifying user preferences, uncovering system inefficiencies, and guiding strategic improvements. By addressing the identified issues and leveraging the insights gained, the company can enhance the trip-building experience, ultimately leading to higher user satisfaction and conversion rates.
