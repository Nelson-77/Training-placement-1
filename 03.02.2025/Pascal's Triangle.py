class Solution(object):
    def generate(self, numRows):
        answer_list = []
        for i in range(1,numRows+1):
            #calling the generate_single_row method to get the elements in particular Row
            result = self.generate_single_row(i)
            answer_list.append(result)
        return answer_list


    def generate_single_row(self,row):
        temp_list = []
        ans = 1
        # Every Row anyway it will start from 1
        temp_list.append(1)

        for col in range(1,row):
            ans = ans * (row - col)
            ans = ans // col
            temp_list.append(ans)
        return temp_list


        
