class Solution:
    def convert(self, s: str, numRows: int) -> str:
        batch=numRows-2+numRows
        if batch==0:
            return s
        length=len(s)
        if length%batch==0:
            batch_no=length//batch
        else:
            batch_no=length//batch+1
        res=""
        for idx in range(numRows):
            if idx==0 or idx==numRows-1:
                for i in range(batch_no):
                    try:
                        res+=s[idx+i*batch]
                    except:
                        break                
            else:
                for i in range(batch_no):
                    try:
                        res+=s[i*batch+idx]
                        res+=s[(i+1)*batch-idx]
                    except:
                        break
        return res
