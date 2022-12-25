input_file  = 'python/d25/input.txt'
test_file = 'python/d25/test.txt'

def to_bal5(snafu_char):
    if snafu_char == "-":
        return -1
    elif snafu_char == "=":
        return -2
    else:
        return int(snafu_char)

def to_snafu_char(bal5):
    if bal5 == -1:
        return "-"
    elif bal5 == -2:
        return "="
    else:
        return str(bal5)

class Balanced5:
    digits = [0]

    def add_snafu_str(self,snafu_str):
        while len(snafu_str) > len(self.digits):
            self.digits.append(0)
        for i in range(len(snafu_str)):
            self.digits[i] += to_bal5(snafu_str[-i-1])

    def simplify(self):
        i = 0
        while True:
            q, r = self.digits[i]//5, self.digits[i]%5
            if r > 2:
                r = r-5
                q = q+1
            if q == 0 and i == len(self.digits) -1:
                return
            elif i == len(self.digits) -1:
                self.digits.append(0)
            self.digits[i] = r
            self.digits[i+1] += q
            i+=1

    def to_snafu_str(self):
        output = ""
        for x in self.digits:
            output = to_snafu_char(x) + output
        return output

def parse(filename):
    num = Balanced5()
    with open(filename) as file:
        for line in file:
            num.add_snafu_str(line.strip())
    return num

if __name__ == '__main__':
    num = parse(input_file)
    num.simplify()
    print(num.to_snafu_str())