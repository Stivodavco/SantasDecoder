class Verifier:
    codes = {
        "maminka" : {
            "code": 135,
            "present": 4
        },
        "tatino": {
            "code": 7641,
            "present": 6
        },
        "darien": {
            "code": 3249,
            "present": 5
        },
        "baba": {
            "code": 2378814,
            "present": 9
        },
        "dedo": {
            "code": 3756,
            "present": 2
        },
        "maria": {
            "code": 4172,
            "present": 8
        },
        "martin": {
            "code": 454454,
            "present": 1
        },
        "mery": {
            "code": 910202127,
            "present": 7
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