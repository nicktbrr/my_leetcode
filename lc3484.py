from typing import List

class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {}
        self.rows = rows

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        del (self.sheet[cell])

    def getValue(self, formula: str) -> int:
        temp = formula[1:].split('+')
        X = temp[0]
        Y = temp[1]
        x, y = None, None
        if not X.isdigit():
            x = self.sheet.get(X, 0)
        else:
            x = int(X)
        if not Y.isdigit():
            y = self.sheet.get(Y, 0)
        else:
            y = int(Y)
        return x + y

s = Spreadsheet(3)
print(s.getValue("=5+7"))
print(s.setCell("A1", 10))
print(s.getValue("=A1+6"))