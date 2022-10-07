import math


class Solution:
    def calculateEntropy(self, input) -> float:
        # return math.math.log(2, 5)
        # return math.log(2, 1)
        
        dict = {}
        for i in range(len(input)):
            if input[i] in dict:
                dict[input[i]] += 1
            else:
                dict[input[i]] = 1
        
        entropy = 0
        for key in dict:
            # P(xi) = dict[input[i]] / len(input)
            # entropy += - P(xi) * log2 (P(xi))
        
            prop = dict[key] / len(input)
            if prop == 1:
                return 0
            entropy -= prop * math.log(prop, 2)
        
        return entropy
    
    def calculateInfoGain(self, originalGroup, group1, group2) -> float:
        # H(L) - H(L1)*size(L1)/size(L) - H(L2)*size(L2)/size(L)
        
        return self.calculateEntropy(originalGroup) - self.calculateEntropy(group1) * len(group1) / len(originalGroup) - self.calculateEntropy(group2) * len (group2) / len(originalGroup)
            
    
    def calculateMaxInfoGain(self, petal_length, species) -> float:
        
        low = min(petal_length)
        high = max(petal_length)
        
        maxInfoGain = 0
        
        for mid in range(math.floor(low), math.ceil(high)):
            group1 = []
            group2 = []
            
            for i in range(len(petal_length)):
                length = petal_length [i]
                if length > mid:
                    group1.append(species[i])
                else:
                    group2.append(species[i])
            
            infoGain = self.calculateInfoGain(species, group1, group2)
            if infoGain > maxInfoGain:
                print("mid: ", mid)
                maxInfoGain = infoGain

        return maxInfoGain
            
                
            
if __name__ == "__main__":
    s = Solution()
    ans = s.calculateMaxInfoGain([1,2,3,4,5,6,7,8,9,10], 
                                 ["versicolor","versicolor","setosa","virginica","virginica","versicolor","versicolor","setosa","versicolor","versicolor"])
    
    print(ans)
    
    print(s.calculateMaxInfoGain([0.5,2.3,1.0,1.5],
                                 ["setosa","versicolor","setosa","versicolor"]))