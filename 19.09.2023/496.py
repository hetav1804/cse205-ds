class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        self.x=[]

        for i in nums1:
            #print(i)
            if i in nums2:
                for j in range(len(nums2)):
                    if i == nums2[j]:
                        temp=i

                        if temp!=nums2[-1]:

                            for k in range(j,len(nums2)):
                                if temp<nums2[k]:
                                    temp=nums2[k]
                                    self.x.append(temp)
                                    #print(self.x)
                                    #print(temp)
                                    break
                                    
                            if temp==i:
                                temp=-1

                                self.x.append(temp)
                            
                        else:
                            temp=-1
                            self.x.append(temp)
        return self.x