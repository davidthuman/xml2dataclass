from dataclasses import dataclass
@dataclass
class VoteTally:

    yeas: str
    nays: str

@dataclass
class Vote:

    vote_number: str
    vote_date: str
    issue: str
    question: str
    result: str
    vote_tally: VoteTally
    title: str

@dataclass
class Votes:

    votes: list[Vote]

@dataclass
class VoteSummary:

    congress: str
    session: str
    congress_year: str
    votes: Votes

