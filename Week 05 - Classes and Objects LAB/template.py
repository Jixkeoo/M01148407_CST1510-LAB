"""
RECORD CHECK  -  my version
===========================

Name  :   Leon Beaupere
Lane  :   Cyber 
Date  :   24/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

class Record:
    count = 0
    def __init__(self, label, value, limit):
        """store the record's label, value and limit"""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT, WARNONG or OK based on value and limit"""
        percent = self.value / self.limit * 100
        if percent >= 100:
            return("OVER LIMIT")
        elif percent >= 90:
            return("WARNING")
        else:
            return("OK")

def load_records(path):
    """Read label, value, limit lines from a file and return a list of record"""
    records = []
    with open(path) as f:
        for i in f:
            label, value, limit = i.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return(records)

records = load_records("records.txt")

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f" Label   : {record.label:>11}")
    print(f" Value   : {record.value:11.2f}")
    print(f" Limit   : {record.limit:11.2f}")
    print(f" Status  : {record.status():>11}")

    print("=" * 34)


