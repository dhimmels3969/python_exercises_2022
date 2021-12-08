class pythonExercises():
    def __init__(self):
        print("Welcome to the Python Exercise class...")

    def __del__(self):
        print("End of the Python Exercise class...")

    def parseDigits(self):
        print("============================================================================")
        print("==== Welcome to the Parse Number Exercise...                            ====")
        print("============================================================================")

        while True:
            u = input("\nEnter a number or ~~ to end: ")
            if u.lower() == "~~":
                break
            else:
                if u.isnumeric():
                    numberToParse = int(u)
                    print("%s will be parsed..." % numberToParse)
                    # results = self.processParseDigits(numberToParse)
                    results = self.buildList(numberToParse)
                else:
                    print("input is NOT numeric... please re-enter...")
                continue

        print(" \nThe End.")
        print("----------------------------------------------------------------")
        print("")

    def buildList(self, number):
        results_list = []
        results_list.append(0)
        for i in range(1, number):
            result = self.processParseDigits(i)
            results_list.append(result)
        print(results_list)
        for i in range(1, number):
            if i==results_list[i]:
                print("match found for item # %s" % i)
        return ""

    def processParseDigits(self, number):
        print("About to process %s" % number)
        digit_list = []
        results_list = []
        results_list.append(0)
        power = 0
        ceiling = 10 ** power
        while ceiling < number:
            power += 1
            ceiling = 10 ** power
        # print("power is %s" % power)
        x = list(range(power, 0, -1))
        for n in range(power - 1, -1, -1):
            divisor = 10 ** n
            digit = number // divisor
            if digit > 0:
                digit_list.append(digit)
            number = number % divisor
        # print(digit_list)
        sum_factorials = 0
        for i in digit_list:
            sum_factorials += self.fctrl(i)
        # print(sum_factorials)
        # sum up the factorials
        return sum_factorials

    def fctrl(self, n):
        k = 1
        for i in range(n):
            k = k * (i + 1)
        return k
