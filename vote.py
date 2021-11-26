import pyrankvote
from typing import List
from pyrankvote import Candidate, Ballot

def create_ballots(candidates, rankings):
    preferences = [None] * len(candidates)
    for index, ranking in enumerate(rankings):
        candidate = candidates[index]
        preferences[ranking-1] = candidate

    return preferences

def get_result(candidate_names: List[str], voter_rankings_as_csv: List[str]):
    """
    Returns the winner of a vote using Instant Run-Off voting
    :param candidate_names: A list of strings, containing the candidates. E.g. ["Option A", "Option B", "Option C"]
    :param voter_rankings_as_csv: A list of CSVs, containing voter preferences. E.g. ["1,2,3", "2,3,1", "3,2,1"]
    :return:
    """
    candidates = [Candidate(name) for name in candidate_names]
    ranked_candidates = [create_ballots(candidates, map(int, ranking_str.split(","))) for ranking_str in voter_rankings_as_csv]
    ballots = [Ballot(ranked_candidates=ranked_candidate) for ranked_candidate in ranked_candidates]

    election_result = pyrankvote.instant_runoff_voting(candidates, ballots)
    winners = election_result.get_winners()
    return election_result

if __name__ == "__main__":
    candidates = ["Sunday, 7pm until 9pm (In Person)",
                  "Sunday, 7pm until 9pm (Zoom)",
                  "Alternating Tuesday/Wednesday 7pm until 9pm (In Person)",
                  "Alternating Tuesday/Wednesday 7pm until 9pm (Zoom)",
                  "Friday 6pm until 8pm (In Person)",
                  "Friday 6pm until 8pm (Zoom)",
                  "Saturday 11am until 1pm (In Person)",
                  "Saturday 11am until 1pm (Zoom)"
                  ]

    votes = ["8,7,1,2,6,5,3,4",
             "5,6,1,2,3,4,7,8",
             "5,6,1,2,7,8,3,4",
             "2,4,3,5,8,7,1,6",
             "3,4,5,2,6,1,8,7",
             "2,1,6,5,4,3,8,7",
             "2,1,7,8,6,5,3,4",
             "6,5,1,2,4,3,7,8",
             "3,4,1,2,6,5,7,8",
             "4,3,2,1,8,5,6,7",
             "2,1,4,3,8,7,5,6",
             "1,2,3,4,5,6,7,8",
            ]
    print(get_result(candidates, votes))