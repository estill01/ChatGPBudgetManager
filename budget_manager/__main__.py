from gpbudget_manager.trackers import BudgetTracker
from gbbudget_manager.cost_calculator import CostCalculator
import datetime

# TODO .. make this better
initial_budget = 50 - 10  # Total budget - server cost
# Initialize the CostCalculator with pricing information 
# TODO FIX - this implementation sucks
pricing = {
    "gpt_3_5_turbo": (0.002, 0.002),
}
cost_calculator = CostCalculator(pricing=pricing)

# TODO FIX - this implementation sucks
models = {
    "gpt_3_5_turbo": "gpt-3.5-turbo"
}

# Create a BudgetManager instance
budget_manager = BudgetManager(
    initial_budget=initial_budget,
    budget_cycle_duration=datetime.timedelta(days=30),
    auto_allocation=0.0,
)


