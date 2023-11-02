class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # t[i] = name,time,amount,city

        seen = {}
        invalid = set()
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            time, amount = int(time), int(amount)

            if name not in seen:
                seen[name] = []

                if amount > 1000:
                    invalid.add(i)
            
            past = seen[name]
            
            for t0 in seen[name]:
                time0, city0, amount0, index0, s = t0
                if t0 == t:
                    continue

                if amount > 1000:
                    invalid.add(i)

                if city0 != city and abs(time0-time) <= 60:
                    invalid.add(i)
                    invalid.add(index0)
                

            seen[name].append((time, city, amount, i, t))
        return [transactions[i] for i in invalid]