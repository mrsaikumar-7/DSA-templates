class SegmentTree:
    def __init__(self,nums):
        self.n = len(nums)
        self.seg = [0]*4*self.n
        self.buildTree(nums,0,0,self.n-1)
    def buildTree(self,nums,ind,low,high):
        if low==high:
            self.seg[ind] = nums[low]
            return 
        mid = (low+high)//2
        self.buildTree(nums,2*ind+1,low,mid)
        self.buildTree(nums,2*ind+2,mid+1,high)
        self.seg[ind] = self.seg[2*ind+1] + self.seg[2*ind+2]
    
    def sumQuery(self,ind,low,high,l,r):
        #case 1 : No overlap
        # [low , high, l, r] or [l,r , low, high]
        if high<l or r<low:
            return 0
        #case 2: Complete overlap
        # [l, low, high, r]
        elif low>=l and high<= r:
            return self.seg[ind]
        #case 3: Partial overlap
        else:
            mid = (low+high)//2
            leftAns = self.sumQuery(2*ind+1,low,mid,l,r)
            rightAns = self.sumQuery(2*ind+2,mid+1,high,l,r)
            return leftAns+rightAns
    
    def update(self,ind,low,high,i,val):
        if low==high:
            self.seg[ind] = val
            return 
        mid = (low+high)//2
        if i<= mid:
            self.update(2*ind+1,low,mid,i,val)
        else:
            self.update(2*ind+2,mid+1,high,i,val)
        self.seg[ind] = self.seg[2*ind+1] + self.seg[2*ind+2]
            


class NumArray:

    def __init__(self, nums):
       self.segTree = SegmentTree(nums)
    def update(self, index: int, val: int) -> None:
        self.segTree.update(0,0,self.segTree.n-1,index,val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segTree.sumQuery(0,0,self.segTree.n-1,left,right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)