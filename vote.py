import pyrankvote
from typing import List
from pyrankvote import Candidate, Ballot

def create_ballots(candidates, rankings):
    preferences = [None] * len(candidates)
    for index, ranking in enumerate(rankings):
        candidate = candidates[index]
        preferences[ranking-1] = candidate

    return preferences

def run():
    sunday_person = Candidate("Sunday, 7pm until 9pm (In Person)")
    sunday_zoom = Candidate("Sunday, 7pm until 9pm (Zoom)")
    tuesday_person = Candidate("Alternating Tuesday/Wednesday 7pm until 9pm (In Person)")
    tuesday_zoom = Candidate("Alternating Tuesday/Wednesday 7pm until 9pm (Zoom)")
    friday_person = Candidate("Friday 6pm until 8pm (In Person)")
    friday_zoom = Candidate("Friday 6pm until 8pm (Zoom)")
    saturday_person = Candidate("Saturday 11am until 1pm (In Person)")
    saturday_zoom = Candidate("Saturday 11am until 1pm (Zoom)")

    candidates = [sunday_person, sunday_zoom, tuesday_person,tuesday_zoom, friday_person, friday_zoom, saturday_person, saturday_zoom]

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

    ranked_candidates = [create_ballots(candidates, map(int, ranking_str.split(","))) for ranking_str in votes]
    ballots = [Ballot(ranked_candidates=ranked_candidate) for ranked_candidate in ranked_candidates]

    election_result = pyrankvote.instant_runoff_voting(candidates, ballots)
    winners = election_result.get_winners()
    print(election_result)

if __name__ == "__main__":
    run()