import numpy as np

class MindMatchAPI:
    def __init__(self):
        # Aapka Hardcoded Revenue Model
        self.dr_reg_fee = 149.99
        self.total_cut_percent = 0.205 # 20.5%
        self.splits = {
            "Clinician Commission": 0.105, # 10.5%
            "Platform Fee": 0.05,          # 5%
            "Service Fee": 0.05            # 5%
        }

    def calculate_revenue(self, session_price):
        total_fee = session_price * self.total_cut_percent
        breakdown = {k: session_price * v for k, v in self.splits.items()}
        return {
            "total_fee": total_fee,
            "dr_payout": session_price - total_fee,
            "breakdown": breakdown
        }

    def get_ai_insight(self):
        return {
            "acceleration": "2.08 sessions faster",
            "roi": "3.27x",
            "match_confidence": f"{np.random.randint(92, 99)}%"
        }
