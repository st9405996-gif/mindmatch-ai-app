class MindMatchEngine:
    def __init__(self):
        self.providers = [
            {"id": "P1", "name": "Dr. Sarah Ahmed", "degree": "PhD Clinical Psych", "rate": 150, "match": 98},
            {"id": "P2", "name": "Dr. Rajesh Kumar", "degree": "MD Psychiatrist", "rate": 130, "match": 95}
        ]

    def get_calming_msg(self, text):
        # Language Detection Logic (Simple keyword based)
        hinglish_keywords = ['hai', 'mein', 'kya', 'kaise', 'zyada', 'pareshan', 'ho', 'rha']
        is_hinglish = any(word in text.lower() for word in hinglish_keywords)

        if is_hinglish:
            return "Main samajh sakta hoon ke aap workload aur stress ki wajah se pareshan hain. OMNI AI aapke saath hai. Gehra saans lein. Kya hum behtar match ke liye assessment shuru karein?"
        else:
            return "I understand that you're feeling overwhelmed with your workload. OMNI AI is here for you. Take a deep breath. Shall we begin the assessment to find your ideal match?"

    def match_logic(self, score):
        return self.providers[0] if score > 10 else self.providers[1]
