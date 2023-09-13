from votekit.elections import STV, fractional_transfer
from votekit import PlackettLuce, CambridgeSampler, AlternatingCrossover
from utils import BradleyTerry
import random


ballot_generators = {
    "bt": BradleyTerry,
    "pl": PlackettLuce,
    "cs": CambridgeSampler,
    "ac": AlternatingCrossover,
}

candidates = {
    "Republicans": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10"],
    "Democrats": ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"],
}

direchlets = [
    {"W": {"C": 0.5, "W": 1}, "C": {"W": 1, "C": 0.5}},
    {"W": {"C": 1, "W": 1}, "C": {"W": 1, "C": 1}},
    {"W": {"C": 2, "W": 1}, "C": {"W": 1, "C": 2}},
]


def simulate_ensembles(
    ensemble: list,
    election: str,
    cohesion: dict,
    num_reps: int,
    num_dems: int,
    seats: int,
    num_ballots: int = 1000,
    num_elections: int = 50,
    low_turnout: bool = False,
    alternate_slate: callable = None,
):
    """
    Runs simulation of RCV elections of an ensemble of plans
    """
    ensemble_results = {}
    for plan_num, plan in enumerate(ensemble):
        plan_results = []
        # find data for a given election
        zone_shares = plan[election]
        for idx, share in enumerate(zone_shares):
            zone_data = {}
            zone_data["zone"] = idx
            zone_data["voter_share"] = share
            # build hyperparams base on share and other toggles
            blocs = {"W": share, "C": 1 - share}
            if low_turnout:
                blocs = {"W": (1 / 3), "C": (2 / 3)}
            # pick direchlets values
            alphas = random.choice(direchlets)
            cand_slate = {
                "W": candidates["Republicans"][:num_reps],
                "C": candidates["Democrats"][:num_dems],
            }
            crossover_rates = {"W": {"C": 0.4}, "C": {"W": 0.5}}
            # loop through number of simulated RCV elections
            for _ in range(num_elections):
                for model_name, model in ballot_generators.items():
                    print(model_name)
                    if model_name in ['cs', 'ac']:
                        generator = model.from_params(
                            slate_to_candidates=cand_slate,
                            bloc_voter_prop=blocs,
                            cohesion=cohesion,
                            alphas=alphas,
                            bloc_crossover_rate=crossover_rates,
                        )
                    else:
                        generator = model.from_params(
                            slate_to_candidates=cand_slate,
                            bloc_voter_prop=blocs,
                            cohesion=cohesion,
                            alphas=alphas,
                        )

                    ballots = generator.generate_profile(num_ballots)
                    results = STV(
                        ballots,
                        transfer=fractional_transfer,
                        seats=seats,
                        ballot_ties=False,
                    ).run_election()
                    num_winners = count_winners(results.get_all_winners(), "Republicans")

                    if model_name not in zone_data:
                        zone_data[model_name] = []
                    zone_data[model_name].append(num_winners)

            plan_results.append(zone_data)

        ensemble_results[plan_num] = plan_results

    return ensemble_results


def count_winners(elected: list[set], party: str) -> int:
    """
    Counts number of elected candidates from the inputted party.
    """
    winner_count = 0
    for winner_set in elected:
        for cand in winner_set:
            if cand in candidates[party]:
                winner_count += 1

    return winner_count


def slate_by_share(vote_share: float) -> dict:
    pass
