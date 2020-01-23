class Group:
    def __init__(self,preferences):
        self.preference_dictonary = {
            "cover":{
                "0": int(preferences[0]),
                "1": int(preferences[1])
            },
            "paper": {
                "00": int(preferences[2]),
                "01": int(preferences[3]),
                "10": int(preferences[4]),
                "11": int(preferences[5])
            },
            "font": {
                "00": int(preferences[6]),
                "01": int(preferences[7]),
                "10": int(preferences[8]),
                "11": int(preferences[9]) 
            }
        }
        self.preferred_price = int(preferences[10])