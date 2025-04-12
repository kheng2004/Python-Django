def countSymmetricIntegers(low, high):
        count = 0
        for i in range(low, high+1):
            s = str(i)
            length = len(s)
            if(length %2 == 0 and length > 1):
                  half = length // 2
                  first_half = s[: half]
                  last_half = s[half:]
                  sum_f = sum(int(c) for c in first_half  )
                  sum_l = sum(int(c) for c in last_half)
                  if (sum_f == sum_l):
                        count += 1
        return count
print(countSymmetricIntegers(1, 100))