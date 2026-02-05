class MindMatchEngine:
    def __init__(self):
        self.providers = [
            {"id": "P1", "name": "Dr. Sarah Ahmed", "degree": "PhD Clinical Psych", "rate": 150, "match": 98},
            {"id": "P2", "name": "Dr. Rajesh Kumar", "degree": "MD Psychiatrist", "rate": 130, "match": 95}
        ]

    def get_calming_msg(self, text):
        return "Main samajh sakta hoon ke aap mushkil waqt se guzar rahe hain. OMNI AI aapke saath hai. Gehra saans lein. Kya hum assessment shuru karein?"

    def get_revenue_split(self, amount):
        cut = 0.205
        return {
            "net": amount * (1 - cut),
            "omni_fee": amount * cut,
            "breakdown": {"Clinician (10.5%)": amount*0.105, "Platform (5%)": amount*0.05, "Service (5%)": amount*0.05}
        }

    def match_logic(self, score):
        return self.providers[0] if score > 10 else self.providers[1]
