class MindMatchEngine:
    def __init__(self):
        self.providers = [
            {"id": "P1", "name": "Dr. Sarah Ahmed", "degree": "PhD Clinical Psych", "rate": 150, "match": 98},
            {"id": "P2", "name": "Dr. Rajesh Kumar", "degree": "MD Psychiatrist", "rate": 130, "match": 95}
        ]

    def get_calming_msg(self, text):
        # Bilingual Detection
        text_lower = text.lower()
        hinglish = ['hai', 'mein', 'kya', 'kaise', 'zyada', 'pareshan', 'kaam', 'masla']
        
        if any(word in text_lower for word in hinglish):
            return "Main samajh sakta hoon ke workload aur stress aapko pareshan kar raha hai. OMNI AI yahan hai. Gehra saans lein, hum mil kar behtar feel karenge. Kya main aapse assessment ke sawal pooch sakta hoon?"
        else:
            return "I can see that workload and stress are weighing on you. OMNI AI is here to support you. Take a deep breath. Shall we proceed with a clinical assessment?"

    def get_revenue_split(self, amount):
        # 20.5% Split (10.5% + 5% + 5%)
        cut = 0.205
        return {
            "net": amount * (1 - cut),
            "omni_fee": amount * cut,
            "breakdown": {"Clinician": "10.5%", "Platform": "5.0%", "Service": "5.0%"}
        }

    def match_logic(self, score):
        return self.providers[0] if score > 10 else self.providers[1]
