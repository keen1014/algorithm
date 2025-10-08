def solution(new_id):
    answer = ''
    def u1(new_id):
        for i in range(len(new_id)):
            if new_id[i].isupper():
                new_id=new_id.replace(new_id[i], new_id[i].lower())
        return new_id
    def u2(new_id):
        for i in range(len(new_id)):
            if not (new_id[i].islower() or new_id[i].isdigit() or new_id[i]=='-' or new_id[i]=='_' or new_id[i]=='-' or new_id[i]=='.'):
                new_id=new_id.replace(new_id[i], '!')
        new_id=new_id.replace('!', '')
        return new_id
    def u3(new_id):
        while '..' in new_id:
            new_id=new_id.replace('..','.')
        return new_id
    def u4(new_id):
        if new_id[0]=='.':
            new_id=new_id[1:]
        if new_id and new_id[-1]=='.':
            new_id=new_id[0:-1]
        return new_id
    def u5(new_id):
        if new_id=='':
            new_id+='a'
        return new_id
    def u6(new_id):
        if 16<=len(new_id):
            new_id=new_id[:15]
            new_id=u4(new_id)
        return new_id
    def u7(new_id):
        while len(new_id)<3:
            new_id=u5(new_id)
            new_id+=new_id[-1]
        return new_id
    new_id=u1(new_id)
    new_id=u2(new_id)
    new_id=u3(new_id)
    new_id=u4(new_id)
    new_id=u5(new_id)
    new_id=u6(new_id)
    new_id=u7(new_id)
    
    answer=new_id
    return answer