# Calculates the winner of an election using instant run-off voting

## Example usage
```bash
pip install -r requirements.txt
python app.py
```

## Data format
Data must be passed through as two related lists of values:
1. A list of strings containing the Candidates that can be voted for.
2. A list of CSVs containing the Preferences (by number) of each Voter. 
The position of the Preference in the CSV corresponds to the Candidate at the same position in the list of Candidates.

## Assumptions
1. The number of Preferences for each vote corresponds to the number of Candidates. 
2. The Preference for each Candidate is unique for each Voter.

## Usage
[Microsoft Forms](https://forms.office.com/) can output the values of single questions in a suitable format for use by this script.

## Dependencies
[pyrankvote](https://pypi.org/project/pyrankvote/)