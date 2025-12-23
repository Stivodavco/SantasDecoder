class Verifier:
    codes = {
        "maminka" : {
            "code": 12345,
            "present": 541
        },
        "tatino": {
            "code": 12345,
            "present": 541
        },
        "darien": {
            "code": 12345,
            "present": 541
        },
        "baba": {
            "code": 12345,
            "present": 541
        },
        "dedo": {
            "code": 12345,
            "present": 541
        },
        "maria": {
            "code": 12345,
            "present": 541
        },
        "martin": {
            "code": 12345,
            "present": 541
        },
        "mery": {
            "code": 12345,
            "present": 541
        },
        "maros": {
            "code": 12345,
            "present": 541
        },
    }

    def verify(self, person, code):
        found_person = self.codes.get(person)
        print(found_person.get("code"))
        if found_person and found_person.get("code") == code:
            return True, found_person.get("present")
        else:
            return False, None