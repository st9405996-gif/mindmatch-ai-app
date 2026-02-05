class MindMatchEngine:
    def __init__(self):
        self.providers = [
            {"id": "P1", "name": "Dr. Sarah Ahmed", "degree": "PhD Clinical Psych", "license": "NY-9920", "rate": 150, "match": 98},
            {"id": "P2", "name": "Dr. Rajesh Kumar", "degree": "MD Psychiatrist", "license": "CA-1102", "rate": 130, "match": 95}
        ]

    def get_revenue_breakdown(self, amount):
        total_cut = amount * 0.205
        return {
            "gross": amount,
            "net_to_provider": amount - total_cut,
            "omni_cut": total_cut,
            "audit": {
                "Clinician Network (10.5%)": amount * 0.105,
                "Platform Ops (5%)": amount * 0.05,
                "Clinical Service (5%)": amount * 0.05
            }
        }

    def match_ai(self, score):
        return self.providers[0] if score > 10 else self.providers[1]
